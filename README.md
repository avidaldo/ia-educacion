# IA para educación

Este repositorio contiene material educativo sobre Inteligencia Artificial y su aplicación en la educación.

## Estructura del proyecto

El proyecto está organizado de la siguiente manera:

```
.
├── index.html                 # Página principal
├── src/                       # Código fuente
│   ├── css/                   # Estilos CSS
│   │   └── styles.css         # Archivo de estilos principal
│   └── js/                    # JavaScript
│       └── main.js            # Lógica principal
├── content/                   # Contenido en markdown
│   ├── 1_historia_y_llms.md   # Historia y modelos de lenguaje
│   ├── 2_herramientas.md      # Herramientas de IA
│   ├── 3_prompt.md            # Introducción a prompts
│   └── ...                    # Otros archivos de contenido
└── img/                       # Imágenes utilizadas en el contenido
    └── ...                    # Archivos de imagen
```

## Características

- Menú lateral ocultable para navegar entre secciones
- Información de contacto y autor en la barra de título
- Diseño responsive para diferentes tamaños de pantalla
- Soporte para conversaciones estilo chat en el contenido markdown
- Actualización automática de la fecha de última modificación

## Cómo añadir nuevo contenido

1. Añade un nuevo archivo markdown en la carpeta `content/`
2. Añade un nuevo elemento de menú en `index.html`
3. Añade un nuevo section en `index.html`
4. Añade el archivo a la lista `mdFiles` en `src/js/main.js`

## Desarrollo local

Para probar el sitio localmente, puedes usar un servidor web simple:

```bash
cd ia-educacion
python -m http.server
```

Luego visita `http://localhost:8000` en tu navegador. 