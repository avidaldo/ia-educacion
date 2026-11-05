---
title: Datos del alumnado
description: Cómo usar la IA para corregir, analizar notas o redactar informes sin exponer datos del alumnado, cuándo basta con anonimizar y qué dice la ley en cada caso típico.
reviewed: 2026-11-05
review_every: 3
---

> [!NOTE]
> **Una lectura docente, no asesoramiento jurídico**
> Esta página aplica a casos típicos lo que se explica en [Normativa](../etica-legal/normativa.md#protección-de-datos), con el mismo criterio que el resto del bloque: cada indicación dice si es una **obligación legal**, una **recomendación institucional** o una **buena práctica**. Ante un caso concreto, la referencia es la persona delegada de protección de datos de la Consellería.

## La pregunta previa: ¿necesita la IA los datos?

Antes de anonimizar nada conviene preguntarse si la IA necesita ver al alumnado. Casi nunca: en la mayoría de las tareas lo que aporta es redactar, estructurar o calcular, y eso se puede pedir sin datos reales. Hay tres vías, y se prueban en este orden:

1. **Sin datos del alumnado.** La IA escribe la plantilla, la fórmula o el procedimiento, y tú lo aplicas a los datos en tu equipo. Sirve para informes, comunicaciones a las familias, análisis de notas y rúbricas.
2. **Con el trabajo del alumno, anonimizado de verdad.** Cuando lo que hace falta es el contenido (una redacción, las respuestas de un examen), se envía solo ese contenido, sin nada que permita saber de quién es. Es más difícil de lo que parece, como se ve en la sección siguiente.
3. **Con datos personales.** Solo en herramientas que la administración educativa haya contratado o autorizado para ese uso (**obligación legal**; el porqué está en [quién puede tratar los datos del alumnado](../etica-legal/normativa.md#quién-puede-tratar-los-datos-del-alumnado)). En Galicia, además, el protocolo de protección de datos de la Consellería pide a los centros usar solo las herramientas que ella proporciona y no usar plataformas externas no autorizadas (**recomendación institucional**).[^protocolo] Mientras no haya entre ellas una herramienta de IA para este uso (el catálogo de sistemas homologados que prevé la Lei de educación dixital todavía no existe), esta vía está cerrada para la IA generativa.

Un modelo ejecutado en tu propio equipo, sin conexión, no envía nada fuera ([la demostración](../etica-legal/index.md#privacidad-la-regla-práctica)). Pero los datos siguen siendo datos del alumnado, sujetos a las normas de seguridad y confidencialidad del centro.

## Quitar el nombre no basta

Cambiar el nombre por un código (`R-07`) mientras guardas la lista que dice quién es cada código es **seudonimizar**, no anonimizar. Para el RGPD, los datos seudonimizados «deben considerarse información sobre una persona física identificable»: siguen siendo datos personales. Solo la información anónima, la que no permite identificar a nadie con los medios que razonablemente puedan usar «el responsable del tratamiento o cualquier otra persona», queda fuera del Reglamento.[^rgpd] Seudonimizar sigue siendo útil, porque reduce el riesgo, y el RGPD la cita como medida de protección, pero no saca los datos del Reglamento. El detalle está en [Anonimizar y seudonimizar](../etica-legal/normativa.md#anonimizar-y-seudonimizar).

Tampoco basta con mirar el nombre, porque el trabajo entero habla de quien lo hizo. Para el Tribunal de Justicia de la UE, las respuestas de un examen y las anotaciones de quien lo corrige son datos personales, y si el examen está escrito a mano contienen, además, «información sobre su escritura».[^nowak] Esto es lo que puede identificar a un alumno o alumna en un trabajo:

| Qué | Ejemplos |
| --- | --- |
| Identificadores directos | Nombre, firma, foto, correo, usuario del aula virtual, número de lista |
| Metadatos del fichero | Autor y «modificado por» en las propiedades, comentarios, control de cambios, la ubicación de una foto |
| Cuasiidentificadores | Grupo, edad, localidad, club, el trabajo de un familiar: por separado no dicen nada, pero juntos señalan a una persona |
| Categorías especiales | Salud, religión, origen étnico, orientación sexual: aunque no identifiquen, son los datos con más protección |
| La voz y la cara | Audios y vídeos de exposiciones orales |

Los cuasiidentificadores son los que más se escapan. El RGPD cuenta la **singularización** entre los medios para identificar a alguien:[^rgpd] aislar a una persona dentro de un grupo sin saber su nombre. En una clase de veinte, «la única de 4.º B que juega en la selección gallega» no necesita nombre.

Lo que cuenta es lo que puede deducir quien recibe el texto. El Tribunal de Justicia ha precisado que, para quien recibe datos seudonimizados sin la tabla que los deshace, pueden no ser datos personales, pero solo si no puede atribuirlos razonablemente a nadie ([Anonimizar y seudonimizar](../etica-legal/normativa.md#anonimizar-y-seudonimizar)). Por eso la vía 2 exige quitar todo lo que permita reconocer a la persona, no solo el nombre.

Y hay textos que no se pueden anonimizar sin destruirlos: una redacción autobiográfica llena de detalles personales sigue siendo reconocible por mucho que se quite. Entonces no es la vía 2, y lo que queda es la 1 o la 3.

## Cómo anonimizar un trabajo

1. **Trabaja sobre una copia**, nunca sobre el fichero que entregó el alumno.
2. **Si basta con el texto, cópialo y pégalo en el chat**: así no viaja ningún metadato. Si tienes que subir el fichero, límpialo antes (paso 4).
3. **Quita la cabecera, la firma y los identificadores**: nombre, usuario, correo, número de lista.
4. **Limpia los metadatos y los comentarios.**
   - En Word: Archivo → Información → Comprobar si hay problemas → Inspeccionar documento, y quita «Comentarios, revisiones, versiones y anotaciones» y «Propiedades del documento e información personal».[^word]
   - En LibreOffice, la opción «Eliminar información personal al guardar» (Herramientas → Opciones → LibreOffice → Seguridad → Opciones) quita los datos de autoría y sustituye el autor de los comentarios por un valor genérico, pero **no borra los comentarios**: hay que eliminarlos aparte.[^libreoffice]
5. **Reescribe los cuasiidentificadores** que no hagan falta para la tarea: «el pabellón de Moaña» pasa a «el pabellón», y «la única de 4.º B que…» desaparece. Cambia lo mínimo: si vas a corregir la expresión, lo que corriges tiene que seguir ahí.
6. **Quita las categorías especiales**: un diagnóstico, una creencia, una situación familiar.
7. **En las fotos**, recorta la cabecera y la firma, y fíjate en la ubicación: la cámara del móvil puede guardar dónde se hizo la foto. En iPhone se puede compartir sin ella (en la hoja de compartir, Opciones → desactivar Ubicación) o impedir que la cámara la guarde (Ajustes → Privacidad y seguridad → Localización → Cámara → Nunca).[^apple] En Android depende de la app de cámara de cada fabricante. Lo más seguro es fotografiar los trabajos con la ubicación de la cámara desactivada.
8. **Guarda la tabla código → alumno fuera de la herramienta**, en tu equipo o en el espacio del centro.
9. **No uses un servicio en línea para anonimizar**: para quitar los datos, ese servicio tiene que recibirlos.

> [!IMPORTANT]
> **Anonimizar no siempre es posible**
> La AEPD y el Supervisor Europeo de Protección de Datos recogen diez malentendidos frecuentes sobre la anonimización (**recomendación institucional**).[^malentendidos] Tres afectan directamente a un docente. Seudonimizar no es anonimizar. Los datos no siempre pueden anonimizarse, entre otros casos cuando «el número total de posibles individuos (“universo de sujetos”) es demasiado reducido», y un grupo-clase lo es. Y no se puede automatizar del todo: encontrar los identificadores directos «es algo trivial», pero los indirectos «no siempre son obvios».

## Casos típicos

| Caso | Vía | Qué hacer |
| --- | --- | --- |
| Retroalimentación sobre una redacción o un trabajo | 2 | Pegar el texto anonimizado con la rúbrica; la nota la pones tú |
| Corregir un examen escrito a mano | 2 | Foto recortada, sin cabecera ni ubicación |
| Analizar las notas de un grupo | 1 | La IA escribe la fórmula a partir de una muestra inventada |
| Informes y comunicaciones a las familias | 1 | Plantilla con huecos que rellenas en tu equipo |
| Adaptar materiales para alumnado con necesidades específicas | 1 | Describir la necesidad didáctica, no el diagnóstico ni a la persona |
| Revisar el código de un proyecto de FP | 2 | Quitar autores, correos y nombres de los ficheros |
| Exposiciones orales grabadas | 3 | La voz y la cara identifican: solo herramientas contratadas, o un modelo local |
| Convivencia y expedientes disciplinarios | 1 | Solo casos inventados |

### Retroalimentación sobre una redacción o un trabajo

Anonimiza el texto con los pasos anteriores y pégalo junto con la rúbrica. Pide la valoración por criterios, con una cita del texto que la justifique, y una sugerencia de mejora para el alumno:

```text
Eres profesor de [materia] en [curso]. Te paso una redacción y la rúbrica con la que se evalúa.
Para cada criterio, dime qué nivel le asignarías, con una cita breve del texto que lo justifique,
y una sugerencia concreta de mejora dirigida al alumno. No pongas la nota final: la decido yo.

[rúbrica]

[texto anonimizado]
```

**Obligación legal.** La IA propone y la nota la decides tú, revisando el trabajo. Una calificación que saliera solo de la herramienta sería una decisión automatizada (artículo 22 del RGPD), y los sistemas que evalúan resultados de aprendizaje son de alto riesgo para el Reglamento de IA: lo explica [Alto riesgo en educación](../etica-legal/normativa.md#alto-riesgo-en-educación).

### Corregir un examen escrito a mano

Los modelos que admiten imágenes leen la letra manuscrita, aunque conviene comprobar su transcripción antes de fiarse de la corrección. Antes de subirla, recorta la cabecera (nombre, grupo, firma) y comprueba la ubicación (paso 7). Si el examen tiene preguntas personales o datos de salud, no es la vía 2.

### Analizar las notas de un grupo

La IA no necesita las notas para escribir la fórmula: le basta con las columnas y unas filas inventadas. Después copias la fórmula en tu hoja, que nunca sale de tu equipo.

```text
Tengo una hoja de cálculo con estas columnas: alumno, prueba_1, prueba_2, proyecto, cuaderno.
Estas tres filas son inventadas, solo para que veas el formato:
Alumno A, 6.5, 7.0, 8.0, 9
Alumno B, 4.0, 5.5, 6.0, 5
Alumno C, 3.0, 4.5, 5.0, 5
Escribe la fórmula de LibreOffice Calc para la nota media ponderada (30 %, 30 %, 30 % y 10 %)
y otra que cuente cuántos alumnos tienen menos de 5 en cada prueba.
```

Es la vía más segura y la que más se olvida: pedir el **procedimiento** en lugar del resultado. Funciona igual con una macro, un script o una tabla dinámica.

### Informes y comunicaciones a las familias

Pide la plantilla con marcadores (`[NOMBRE]`, `[FORTALEZAS]`, `[A_MEJORAR]`) y rellénala en tu equipo, a mano o con la combinación de correspondencia del procesador de textos. La IA aporta la redacción; los datos de cada alumno no salen de tu equipo.

### Adaptar materiales para alumnado con necesidades específicas

Describe la necesidad didáctica, no el diagnóstico ni a la persona: «adapta este texto para alguien que necesita frases cortas, vocabulario básico y una idea por párrafo» funciona igual de bien que nombrar un trastorno, y no revela un dato de salud. **Obligación legal**: los datos de salud son una [categoría especialmente protegida](../etica-legal/normativa.md#datos-especialmente-protegidos). Y el expediente de orientación no se trata «en ningún caso» con herramientas que no sean de la Consellería, según su protocolo (**recomendación institucional**).[^protocolo-orientacion]

### Revisar el código de un proyecto de FP

Un repositorio identifica a su autor en varios sitios: el nombre y el correo de cada *commit*, los comentarios de cabecera de los ficheros y, a veces, las rutas (`/home/<usuario>/…`). Para pedir una revisión, copia solo los ficheros que importan y limpia esos datos; no subas el repositorio entero.

### Exposiciones orales grabadas

La voz y la cara identifican a la persona, y no hay forma razonable de anonimizarlas. Una grabación solo puede ir a una herramienta contratada por la administración. Si lo que necesitas es la transcripción, hay modelos de transcripción que funcionan en el propio equipo, sin conexión.

### Convivencia y expedientes disciplinarios

Son los datos más delicados del centro, y casi nunca es posible anonimizarlos: los hechos identifican a las personas. Si quieres ayuda para redactar, pide un modelo de escrito a partir de un caso inventado y adáptalo tú.

## Para practicar

Este fragmento de una redacción es inventado. Antes de leer la solución, anota todo lo que quitarías o cambiarías para pedir retroalimentación sobre la expresión escrita:

> El lugar más importante para mí es el pabellón municipal de Moaña, donde entreno con el equipo cadete femenino de balonmano. Desde que me diagnosticaron diabetes tipo 1 el año pasado, mi madre viene a todos los entrenamientos con el glucómetro. Este año soy la única de 4.º B que juega en la selección gallega, y cuando vuelvo de las concentraciones el pabellón es el sitio donde me siento en casa, aunque mi padre, que trabaja de noche en la conservera, no pueda venir.

Lo que había que tocar:

- **La salud**: «me diagnosticaron diabetes tipo 1» y el glucómetro. Es una categoría especial, y no hace falta para valorar la expresión.
- **La singularización**: «la única de 4.º B que juega en la selección gallega».
- **Los cuasiidentificadores**: Moaña, el equipo cadete femenino y el trabajo del padre. Juntos, señalan a una sola persona.
- **Lo que no se ve en el fragmento**: si llegó como fichero, la cabecera, las propiedades y los comentarios.

Con todo eso quitado, la frase sigue sirviendo para corregir la expresión: «Cuando vuelvo de los partidos fuera, el pabellón es el sitio donde me siento en casa, aunque alguien de mi familia no pueda venir».

[^rgpd]: Reglamento (UE) 2016/679, General de Protección de Datos ([BOE](https://www.boe.es/buscar/doc.php?id=DOUE-L-2016-80807)), considerando 26.
[^nowak]: Sentencia del Tribunal de Justicia de 20 de diciembre de 2017, *Nowak*, C-434/16, apartados 37 y 62 ([EUR-Lex](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:62016CJ0434)). Interpreta la Directiva 95/46, a la que sustituyó el RGPD con una definición de dato personal del mismo alcance.
[^protocolo]: Consellería de Cultura, Educación, Formación Profesional e Universidades, [*Protocolo de protección de datos persoais*](https://www.edu.xunta.gal/portal/sites/web/files/protocolo_de_proteccion_de_datos_persoais_160823.pdf), septiembre de 2022, apartados 12.1 y 21.
[^protocolo-orientacion]: Consellería de Cultura, Educación, Formación Profesional e Universidades, [*Protocolo de protección de datos persoais*](https://www.edu.xunta.gal/portal/sites/web/files/protocolo_de_proteccion_de_datos_persoais_160823.pdf), septiembre de 2022, apartado 22.3.
[^malentendidos]: AEPD y Supervisor Europeo de Protección de Datos, [*10 malentendidos relacionados con la anonimización*](https://www.edps.europa.eu/system/files/2021-04/21-04-27_aepd-edps_anonymisation_es.pdf_0.pdf), 2021, equívocos 1, 3 y 7.
[^word]: Microsoft, [*Quitar datos ocultos e información personal inspeccionando documentos, presentaciones o libros*](https://support.microsoft.com/es-es/office/quitar-datos-ocultos-e-informaci%C3%B3n-personal-inspeccionando-documentos-presentaciones-o-libros-356b7b5d-77af-44fe-a07f-9aa4d085966f), consultado el 5 de noviembre de 2026.
[^libreoffice]: Ayuda de LibreOffice, [*Opciones de seguridad y alertas*](https://help.libreoffice.org/latest/es/text/shared/optionen/securityoptionsdialog.html), consultada el 5 de noviembre de 2026.
[^apple]: Apple, [*Gestionar los metadatos de ubicación en Fotos*](https://support.apple.com/es-es/guide/personal-safety/ips0d7a5df82/web), consultada el 5 de noviembre de 2026.
