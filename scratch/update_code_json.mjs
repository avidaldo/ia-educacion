import fs from 'fs';
import path from 'path';

function updateCodeJson(lang, updates) {
    const filePath = path.resolve('../i18n/' + lang + '/code.json');
    if (fs.existsSync(filePath)) {
        const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
        let changed = false;
        for (const [key, msg] of Object.entries(updates)) {
            if (!data[key] || data[key].message !== msg) {
                data[key] = data[key] || {};
                data[key].message = msg;
                changed = true;
            }
        }
        if (changed) {
            fs.writeFileSync(filePath, JSON.stringify(data, null, 2));
            console.log('Updated ' + lang + '/code.json');
        }
    } else {
        console.log('File not found: ' + filePath);
    }
}

updateCodeJson('en', {
    "homepage.startButton": "Let's start",
    "site.title": "Teaching with AI",
    "site.tagline": "Using AI for teaching"
});

updateCodeJson('it', {
    "homepage.startButton": "Iniziamo",
    "site.title": "Insegnare con l'IA",
    "site.tagline": "Usare le IA per la didattica"
});

updateCodeJson('gl', {
    "homepage.startButton": "Comezamos",
    "site.title": "Docencia con IA",
    "site.tagline": "Usando IAs para a docencia"
});
