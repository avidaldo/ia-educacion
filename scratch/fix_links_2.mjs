import fs from 'fs';
import path from 'path';

function walk(dir, callback) {
    fs.readdirSync(dir).forEach(f => {
        let dirPath = path.join(dir, f);
        let isDirectory = fs.statSync(dirPath).isDirectory();
        isDirectory ? walk(dirPath, callback) : callback(path.join(dir, f));
    });
}

const dirs = [
    path.resolve('../i18n/en/docusaurus-plugin-content-docs/current'),
    path.resolve('../i18n/it/docusaurus-plugin-content-docs/current')
];

for (const dir of dirs) {
    walk(dir, filePath => {
        if (filePath.endsWith('.md') || filePath.endsWith('.mdx')) {
            let content = fs.readFileSync(filePath, 'utf-8');
            let originalContent = content;

            // Fix broken folder and file paths
            content = content.replace(/\/docs\/examples\/agentes-y-orquestacion/g, '/docs/ejemplos/agentes-y-orquestacion');
            content = content.replace(/\/img\/nero-ss\.png/g, '/img/black-ss.png');
            content = content.replace(/\/img\/black-ss\.png/g, '/img/black-ss.png'); // Just in case
            
            if (content !== originalContent) {
                fs.writeFileSync(filePath, content);
                console.log('Fixed additional links in', filePath);
            }
        }
    });
}
