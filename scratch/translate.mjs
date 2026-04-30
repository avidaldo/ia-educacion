import fs from 'fs';
import path from 'path';
import { translate } from 'google-translate-api-x';

const DOCS_DIR = path.resolve('../docs');
const I18N_EN_DIR = path.resolve('../i18n/en/docusaurus-plugin-content-docs/current');
const I18N_IT_DIR = path.resolve('../i18n/it/docusaurus-plugin-content-docs/current');

// Ensure dirs exist
fs.mkdirSync(I18N_EN_DIR, { recursive: true });
fs.mkdirSync(I18N_IT_DIR, { recursive: true });

async function processFile(filePath, destDir, targetLang) {
    const content = fs.readFileSync(filePath, 'utf-8');
    const lines = content.split('\n');
    let inCodeBlock = false;
    let inFrontmatter = false;
    
    let translatedLines = [];
    
    // Batch translation to avoid too many requests
    // We will translate chunk by chunk
    let textToTranslate = [];
    let mappings = []; // index in translatedLines

    for (let i = 0; i < lines.length; i++) {
        let line = lines[i];
        
        if (i === 0 && line.trim() === '---') {
            inFrontmatter = true;
            translatedLines.push(line);
            continue;
        }
        if (inFrontmatter && line.trim() === '---') {
            inFrontmatter = false;
            translatedLines.push(line);
            continue;
        }
        if (inFrontmatter) {
            // translate title, ignore slug
            if (line.startsWith('title:')) {
                textToTranslate.push(line.replace('title:', '').trim());
                mappings.push({ index: i, type: 'title' });
                translatedLines.push(line); // placeholder
            } else if (line.startsWith('sidebar_position:')) {
                translatedLines.push(line);
            } else {
                translatedLines.push(line);
            }
            continue;
        }

        if (line.trim().startsWith('```')) {
            inCodeBlock = !inCodeBlock;
            translatedLines.push(line);
            continue;
        }

        if (inCodeBlock) {
            translatedLines.push(line);
            continue;
        }

        // ignore import statements and custom components
        if (line.startsWith('import ') || line.startsWith('<') || line.startsWith(':::')) {
            translatedLines.push(line);
            continue;
        }

        if (line.trim() === '') {
            translatedLines.push(line);
            continue;
        }

        // This is a text line
        textToTranslate.push(line);
        mappings.push({ index: i, type: 'text' });
        translatedLines.push(line); // placeholder
    }

    if (textToTranslate.length > 0) {
        try {
            const res = await translate(textToTranslate, { from: 'es', to: targetLang });
            const results = Array.isArray(res) ? res : [res];
            for (let k = 0; k < mappings.length; k++) {
                const mapInfo = mappings[k];
                if (mapInfo.type === 'title') {
                    translatedLines[mapInfo.index] = 'title: ' + results[k].text;
                } else {
                    translatedLines[mapInfo.index] = results[k].text;
                }
            }
        } catch(e) {
            console.error('Translation error in file ' + filePath, e);
        }
    }

    // copy directory structure
    const relPath = path.relative(DOCS_DIR, filePath);
    const destPath = path.join(destDir, relPath);
    fs.mkdirSync(path.dirname(destPath), { recursive: true });
    fs.writeFileSync(destPath, translatedLines.join('\n'));
    console.log(`Translated ${relPath} to ${targetLang}`);
}

function walk(dir, callback) {
    fs.readdirSync(dir).forEach(f => {
        let dirPath = path.join(dir, f);
        let isDirectory = fs.statSync(dirPath).isDirectory();
        isDirectory ? walk(dirPath, callback) : callback(path.join(dir, f));
    });
}

async function main() {
    const files = [];
    walk(DOCS_DIR, filePath => {
        if (filePath.endsWith('.md') || filePath.endsWith('.mdx')) {
            files.push(filePath);
        }
    });

    for (const f of files) {
        await processFile(f, I18N_EN_DIR, 'en');
        await processFile(f, I18N_IT_DIR, 'it');
        // wait to not rate limit
        await new Promise(r => setTimeout(r, 1000));
    }
}

main().catch(console.error);
