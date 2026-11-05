---
derived_from:
  es/datos-alumnado/index.md: "09bee5b7d030916665d1f922e82b34664bd31f81"
---

<!-- .slide: id="idea-central" class="statement" -->
## La IA casi nunca necesita ver al alumnado

Pide la plantilla o el procedimiento; anonimiza solo cuando haga falta el contenido.

Notas:
**Mensaje clave:** antes de preguntarse cómo anonimizar, la pregunta es si hace falta enviar datos. En la mayoría de las tareas, lo que aporta la IA es redactar, estructurar o calcular, y eso se pide sin datos reales.

---

<!-- .slide: id="tres-vias" class="cards fragments" -->
## Tres vías, en este orden

### 1. Sin datos
La IA escribe la plantilla, la fórmula o el procedimiento; tú lo aplicas en tu equipo.

### 2. Sin nada que diga de quién es
Solo el contenido del trabajo. Tú puedes saberlo; quien lo recibe, no.

### 3. Datos personales
Solo en herramientas contratadas o autorizadas por la administración.

Notas:
La segunda tiene una duda sin resolver: el protocolo de la Consellería pide usar solo sus herramientas con los datos del alumnado, y no aclara si eso incluye un trabajo ya limpio, del que solo el docente sabe el autor. Si está bien limpio, el riesgo para el alumno es mínimo; para tener certeza, se pregunta a la persona delegada de protección de datos. La tercera es una obligación legal: la habilitación para tratar los datos del alumnado es del centro y de la administración, no de cada herramienta que use un docente. Un modelo local, sin conexión, no envía nada fuera, pero los datos siguen sujetos a las normas de seguridad del centro.

---

<!-- .slide: id="seudonimizar" class="statement" -->
## Cambiar el nombre es solo el primer paso

Tú puedes saber de quién es; quien recibe el texto no debe poder saberlo.

Notas:
El procedimiento habitual es razonable: código en lugar del nombre, la tabla en tu equipo, ayuda de la IA y la valoración de vuelta a cada alumno. Que el docente sepa de quién es cada trabajo no es un problema: es su profesor. Para él, con la tabla, siguen siendo datos del alumno (la ley lo llama seudonimizar), y por eso la tabla se guarda como el cuaderno de notas. Lo que se juega es lo que puede deducir quien lo recibe: el fichero lleva el autor y los comentarios, y el propio texto puede bastar.

---

<!-- .slide: id="que-identifica" class="table" -->
## Lo que identifica además del nombre

| Qué | Ejemplos |
| --- | --- |
| Identificadores | Nombre, firma, correo, usuario del aula virtual |
| Metadatos | Autor en las propiedades, comentarios, ubicación de una foto |
| Cuasiidentificadores | Grupo, edad, localidad, club, el trabajo de un familiar |
| Categorías especiales | Salud, religión, origen étnico |
| Voz y cara | Audios y vídeos de exposiciones |

---

<!-- .slide: id="singularizacion" class="statement" -->
## Sin nombre también se identifica

«La única de 4.º B que juega en la selección gallega» no necesita nombre.

Notas:
El RGPD llama a esto singularización: aislar a una persona dentro de un grupo. En una clase de veinte, dos o tres detalles bastan. Y hay textos que no se pueden limpiar sin destruirlos, como una redacción autobiográfica: entonces no es la vía 2.

---

<!-- .slide: id="demo-quitar-nombre" class="demo" -->
## Demo: quitar el nombre no basta

- Una redacción inventada, en un procesador de textos y un *chatbot*.
- Fíjate en lo que no se ve al abrir el fichero.

Notas:
**Demo (10 min)**. Word o LibreOffice, y cualquier *chatbot* en un chat temporal. Material: una redacción inventada en `.docx`, como la del apartado «Para practicar» de la página, con el nombre en la cabecera, la autora en las propiedades y un comentario de la alumna con un dato de salud.

1. Abrir la redacción y pedir al grupo que diga qué datos ve: el nombre de la cabecera.
2. Enseñar las propiedades del fichero (autora, «modificado por») y el comentario. En Word, Archivo → Información → Comprobar si hay problemas → Inspeccionar documento.
3. En LibreOffice, activar «Eliminar información personal al guardar», guardar y volver a abrir: el comentario sigue ahí, con un autor genérico. Hay que borrarlo aparte.
4. Leer el texto en voz alta y pedir al grupo que señale los cuasiidentificadores y el dato de salud.
5. Pegar solo el texto ya limpio en el chat, con la rúbrica, y pedir la valoración por criterios sin nota final.

**Resultado esperado:** el grupo descubre al menos un dato que no había visto (los metadatos o el comentario), y la retroalimentación sobre la expresión sale igual de útil con el texto limpio.
**Si falla:** hacer el ejercicio «Para practicar» de la página, en voz alta.
**Mensaje clave:** lo más seguro es copiar solo el texto; el fichero lleva más de lo que se ve.

---

<!-- .slide: id="pasos-anonimizar" class="checklist" -->
## Antes de pedir ayuda con un trabajo

- [ ] Una copia, y si basta con el texto, solo el texto.
- [ ] Sin cabecera, firma ni identificadores.
- [ ] Sin metadatos ni comentarios.
- [ ] Cuasiidentificadores reescritos, lo mínimo.
- [ ] Sin categorías especiales.
- [ ] Fotos recortadas y sin ubicación.
- [ ] La tabla de códigos, fuera de la herramienta.

Notas:
Y dos pasos que se olvidan: nada de servicios en línea para anonimizar, porque para quitar los datos tienen que recibirlos, y desactivar que las conversaciones se usen para entrenar modelos (en la página de Chatbots está dónde se hace).

---

<!-- .slide: id="nota-docente" class="statement" -->
## La IA propone; la nota la pones tú

Una calificación que saliera solo de la herramienta sería una decisión automatizada (artículo 22 del RGPD).

Notas:
Además, los sistemas que evalúan resultados de aprendizaje son de alto riesgo para el Reglamento de IA. Lo detalla la página de normativa del bloque de ética.

---

<!-- .slide: id="demo-procedimiento" class="demo" -->
## Demo: la IA escribe la fórmula, no ve las notas

- Una hoja de cálculo con notas inventadas y cualquier *chatbot*.
- Fíjate en lo que recibe la IA: tres filas falsas.

Notas:
**Demo (5 min)**. LibreOffice Calc o Excel, y cualquier *chatbot* en un chat temporal. Material: una hoja con unos veinte alumnos inventados y cuatro notas cada uno.

1. Enseñar la hoja completa y decir que es la que nunca va a salir del equipo.
2. Pegar en el chat el *prompt* de la página: solo las columnas y tres filas inventadas.
3. Copiar las fórmulas que devuelve en la hoja y comprobar una fila a mano.

**Resultado esperado:** dos fórmulas que funcionan sobre la hoja real sin que la IA la haya visto.
**Si falla:** si la fórmula da error, pegar el mensaje de error en el chat; si no hay red, enseñar la fórmula ya preparada.
**Mensaje clave:** pedir el procedimiento en lugar del resultado es la vía más segura, y la que más se olvida.

---

<!-- .slide: id="prompt-procedimiento" class="prompt" -->
## Las columnas y tres filas inventadas bastan

```text
Tengo una hoja con estas columnas: alumno, prueba_1, prueba_2, proyecto, cuaderno.
Estas tres filas son inventadas, solo para que veas el formato: […]
Escribe la fórmula de LibreOffice Calc para la media ponderada (30 %, 30 %, 30 % y 10 %)
y otra que cuente cuántos alumnos tienen menos de 5 en cada prueba.
```

Notas:
La versión completa, con las tres filas, está en la página.

---

<!-- .slide: id="demo-plantilla" class="demo" -->
## Demo: una plantilla con huecos

- Un informe para las familias, con marcadores que se rellenan en local.
- Fíjate en que la IA solo aporta la redacción.

Notas:
**Demo (5 min)**. Cualquier *chatbot* en un chat temporal y un procesador de textos. Material: una tabla inventada con los datos de cinco alumnos (nombre, grupo, fortalezas, aspectos a mejorar, propuesta).

1. Pedir al chat un informe de tutoría de primera evaluación con los marcadores `[NOMBRE]`, `[GRUPO]`, `[FORTALEZAS]`, `[A_MEJORAR]` y `[PROPUESTA]`.
2. Pegar la plantilla en el procesador de textos.
3. Rellenar un informe con buscar y reemplazar, o todos con la combinación de correspondencia a partir de la tabla.

**Resultado esperado:** un informe bien redactado con datos que no salieron del equipo.
**Si falla:** enseñar una plantilla ya generada y rellenarla.
**Mensaje clave:** la IA aporta la redacción; los datos de cada alumno los pones tú.

---

<!-- .slide: id="demo-examen" class="demo" -->
## Demo: un examen escrito a mano

- La foto de un examen inventado, rellenado a mano.
- Fíjate en la cabecera, la firma y la ubicación de la foto.

Notas:
**Demo (5 min)**. Un móvil, el visor de fotos del ordenador y un *chatbot* que admita imágenes. Material: un examen inventado rellenado a mano con un nombre inventado, fotografiado con la ubicación de la cámara activada.

1. Enseñar en las propiedades de la foto la ubicación que guardó la cámara.
2. Recortar la cabecera y la firma, y compartir o exportar la foto sin ubicación (en iPhone, Opciones → desactivar Ubicación al compartir).
3. Subir la foto recortada al chat y pedir que transcriba las respuestas antes de valorarlas.
4. Comparar la transcripción con el original: los errores de lectura se ven ahí, antes de la corrección.

**Resultado esperado:** una transcripción revisable y una valoración por pregunta, sin nombre, firma ni ubicación.
**Si falla:** enseñar la foto recortada y explicar los pasos.
**Mensaje clave:** la foto lleva más que lo que se ve, y la transcripción se comprueba antes de fiarse de la corrección.

---

<!-- .slide: id="casos-anonimizables" class="table" -->
## Casos típicos y su vía

| Caso | Vía | Qué hacer |
| --- | --- | --- |
| Redacción o trabajo | 2 | Texto anonimizado y rúbrica |
| Examen a mano | 2 | Foto recortada, sin ubicación |
| Notas de un grupo | 1 | La fórmula, con una muestra inventada |
| Informes y familias | 1 | Plantilla con huecos |
| Necesidades específicas | 1 | La necesidad didáctica, no el diagnóstico |

Notas:
Para adaptar un material, «necesita frases cortas, vocabulario básico y una idea por párrafo» funciona igual de bien que nombrar un trastorno, y no revela un dato de salud. En la página están los siete casos.

---

<!-- .slide: id="sin-anonimizacion" class="bullets" -->
## Donde no hay anonimización posible

- **Grabaciones**: la voz y la cara identifican; solo herramientas contratadas, o transcripción en el propio equipo.
- **Convivencia y expedientes**: los hechos identifican a las personas; solo casos inventados.
- **Textos autobiográficos**: si al limpiarlos no queda nada, no es la vía 2.

---

<!-- .slide: id="practica-fragmento" class="practice" -->
## ¿Qué quitarías?

1. Lee el fragmento de redacción del apartado «Para practicar» de la página.
2. Anota todo lo que quitarías o reescribirías para pedir retroalimentación sobre la expresión.
3. Compara tu lista con la de otra persona y después con la solución.

10 minutos, en parejas.

Notas:
En la puesta en común, buscar los tres tipos de dato: el de salud (la diabetes y el glucómetro), la singularización («la única de 4.º B…») y los cuasiidentificadores (Moaña, el equipo cadete femenino, el trabajo del padre). Preguntar al final qué no se ve en el fragmento: la cabecera, las propiedades y los comentarios si llegó como fichero.
