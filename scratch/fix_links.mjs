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
            content = content.replace(/41-cases-use/g, '41-casos-uso');
            content = content.replace(/31-examples/g, '31-ejemplos');
            content = content.replace(/09-custom-wizard.mdx/g, '09-asistente-personalizado.mdx');
            
            // Fix absolute URL translations
            content = content.replace(/\/docs\/examples\/agents-and-orchestration/g, '/docs/ejemplos/agentes-y-orquestacion');
            content = content.replace(/\/docs\/examples\/agents-and-orquestation/g, '/docs/ejemplos/agentes-y-orquestacion');
            content = content.replace(/\/docs\/examples\/advanced-reasoning/g, '/docs/ejemplos/razonamiento-avanzado');
            content = content.replace(/\/docs\/examples\/specific-instructions/g, '/docs/ejemplos/instrucciones-especificas');
            content = content.replace(/\/docs\/examples\/evaluacion-critica/g, '/docs/ejemplos/evaluacion-critica');
            content = content.replace(/\/docs\/examples\/custom-wizard/g, '/docs/ejemplos/asistente-personalizado');
            content = content.replace(/\/docs\/examples\/deep-research/g, '/docs/ejemplos/deep-research');

            // Fix img translations
            content = content.replace(/\/img\/rulas_vs_ml.jpg/g, '/img/reglas_vs_ml.jpg');
            content = content.replace(/\/img\/rules_vs_ml.jpg/g, '/img/reglas_vs_ml.jpg');
            
            // Other fixes
            content = content.replace(/31-esempi/g, '31-ejemplos');
            content = content.replace(/41-casi-uso/g, '41-casos-uso');
            content = content.replace(/41-casi-d'uso/g, '41-casos-uso');
            
            if (content !== originalContent) {
                fs.writeFileSync(filePath, content);
                console.log('Fixed', filePath);
            }
        }
    });
}
