import fs from 'fs';
import path from 'path';

function walk(dir, callback) {
    fs.readdirSync(dir).forEach(f => {
        let dirPath = path.join(dir, f);
        let isDirectory = fs.statSync(dirPath).isDirectory();
        isDirectory ? walk(dirPath, callback) : callback(path.join(dir, f));
    });
}

const enDir = path.resolve('../i18n/en/docusaurus-plugin-content-docs/current');
const itDir = path.resolve('../i18n/it/docusaurus-plugin-content-docs/current');

const admonitionsEn = {
    "Artículo interesante": "Interesting article",
    "Los sesgos como consecuencia del funcionamiento": "Biases as a consequence of how it works",
    "Concepto clave": "Key concept",
    "En más profundidad": "In more depth",
    "Implicación práctica": "Practical implication",
    "Perspectiva": "Perspective",
    "Utilidad": "Utility",
    "Cuidado con el prompt": "Careful with the prompt",
    "Ejemplo de chat": "Chat example",
    "Privacidad en el aula": "Privacy in the classroom",
    "Cambios frecuentes": "Frequent changes",
    "Error común al escribir instrucciones": "Common error when writing instructions"
};

const admonitionsIt = {
    "Artículo interesante": "Articolo interessante",
    "Los sesgos como consecuencia del funcionamiento": "I bias come conseguenza del funzionamento",
    "Concepto clave": "Concetto chiave",
    "En más profundidad": "In maggiore profondità",
    "Implicación práctica": "Implicazione pratica",
    "Perspectiva": "Prospettiva",
    "Utilidad": "Utilità",
    "Cuidado con el prompt": "Attenzione al prompt",
    "Ejemplo de chat": "Esempio di chat",
    "Privacidad en el aula": "Privacy in classe",
    "Cambios frecuentes": "Cambiamenti frequenti",
    "Error común al escribir instrucciones": "Errore comune nello scrivere istruzioni"
};

function processDir(dir, lang) {
    walk(dir, filePath => {
        if (filePath.endsWith('.md') || filePath.endsWith('.mdx')) {
            let content = fs.readFileSync(filePath, 'utf-8');
            let originalContent = content;

            // Fix broken URLs with spaces
            content = content.replace(/HV ZSt2Sks4COowshXz1d-2qcawJEbIr3kF3pCskfK9pFV8Oh0MgTvC1otw_aem_9YONOGize2uCs327bG33gA/g, 'HVZSt2Sks4COowshXz1d-2qcawJEbIr3kF3pCskfK9pFV8Oh0MgTvC1otw_aem_9YONOGize2uCs327bG33gA');

            // Fix ApriAI -> OpenAI
            content = content.replace(/ApriAI/g, 'OpenAI');
            content = content.replace(/Apri AI/g, 'OpenAI');
            
            // Fix Perplessità -> Perplexity
            if (lang === 'it') {
                content = content.replace(/Perplessità/g, 'Perplexity');
            }

            // Fix Admonitions
            const admonitions = lang === 'en' ? admonitionsEn : admonitionsIt;
            for (const [es, translated] of Object.entries(admonitions)) {
                // regex to match :::info[Spanish]
                const regex = new RegExp(`:::(.*)\\[${es}\\]`, 'g');
                content = content.replace(regex, `:::$1[${translated}]`);
            }

            if (content !== originalContent) {
                fs.writeFileSync(filePath, content);
                console.log('Fixed', filePath);
            }
        }
    });
}

processDir(enDir, 'en');
processDir(itDir, 'it');
