---
title: Normativa
description: Lo que dicen el RGPD, la LOPDGDD, la LOE, el Reglamento de IA y las normas gallegas sobre el uso de la IA en un centro educativo, con su calendario de aplicación y lo que todavía está en tramitación.
reviewed: 2026-10-27
review_every: 3
---

> [!NOTE]
> **Una lectura docente de la normativa**
> Esta página explica las normas desde el trabajo de un docente y cita sus artículos para que puedas comprobarlos. No es asesoramiento jurídico: ante un caso concreto, la referencia es la persona delegada de protección de datos de la Consellería, que todas las administraciones públicas tienen que designar. Situación revisada el 27 de octubre de 2026.

## Cómo se ordenan las normas

Un **reglamento europeo** es obligatorio y directamente aplicable en todos los Estados, sin que haga falta una ley nacional que lo trasponga; una **directiva**, en cambio, fija objetivos que cada Estado incorpora con su propia ley. Pero «directamente aplicable» no significa «aplicable desde que se publica»: cada reglamento fija su fecha de entrada en vigor y sus plazos de aplicación. El Reglamento de IA, por ejemplo, se publicó en julio de 2024, entró en vigor el 1 de agosto de 2024 y se aplica por fases hasta 2028 ([calendario](#calendario)).

Por debajo están las normas españolas (leyes orgánicas como la LOPDGDD o la LOE, reales decretos) y las gallegas. Y fuera de esa jerarquía, las **guías y recomendaciones** (de la Comisión Europea, del INTEF, de la Xunta), que orientan pero no obligan.

## Protección de datos

Las normas son el Reglamento General de Protección de Datos (RGPD), que es europeo, y la Ley Orgánica de Protección de Datos (LOPDGDD), que lo completa en España. Con ellas, la Ley Orgánica de Educación (LOE) regula los datos del alumnado.

### Qué es un dato personal

El RGPD lo define de forma muy amplia: «toda información sobre una persona física identificada o identificable», y es identificable quien puede ser identificado «directa o indirectamente», por ejemplo mediante «uno o varios elementos propios de la identidad física, fisiológica, genética, psíquica, económica, cultural o social».[^rgpd] Una nota, un comentario sobre la conducta o una descripción que permite saber de quién se habla son datos personales, aunque no aparezca el nombre.

### Quién puede tratar los datos del alumnado

La LOE habilita a los centros: «podrán recabar los datos personales de su alumnado que sean necesarios para el ejercicio de su función educativa», y añade dos condiciones que importan aquí:[^loe]

- «se aplicarán normas técnicas y organizativas que garanticen su seguridad y confidencialidad»;
- el profesorado que acceda a esos datos «quedará sujeto al deber de sigilo».

Esa habilitación es del centro y de la administración educativa, no de cada herramienta que use un docente. Cuando un tercero trata datos por cuenta del centro, el RGPD exige que sea un **encargado del tratamiento** elegido entre quienes ofrezcan «garantías suficientes», con un contrato que lo regule.[^rgpd] Un *chatbot* con cuenta personal no es eso: por eso los datos del alumnado solo van a herramientas que la administración ha contratado o autorizado. Y aun en ellas, solo los imprescindibles: los datos han de ser «limitados a lo necesario en relación con los fines» (minimización).[^rgpd]

### Datos especialmente protegidos

Algunas categorías tienen una protección reforzada: el RGPD prohíbe en principio tratar datos que revelen el origen étnico, las convicciones religiosas, la salud o la orientación sexual, entre otros, salvo en los supuestos que enumera.[^rgpd] Un informe de necesidades educativas, un diagnóstico o una adaptación por motivos de salud entran aquí: son los últimos datos que deberían acabar en una herramienta de IA.

### La edad del alumnado

En España, un menor puede consentir por sí mismo el tratamiento de sus datos «cuando sea mayor de catorce años»; por debajo hace falta el consentimiento de quien ejerce la patria potestad o la tutela.[^lopdgdd] El RGPD fija 16 años para los servicios en línea ofrecidos directamente a menores y permite a cada Estado bajarla hasta 13; España eligió 14.[^rgpd]

Esto puede cambiar. El proyecto de ley orgánica de protección de las personas menores de edad en los entornos digitales, en tramitación en el Congreso en octubre de 2026, eleva esa edad a dieciséis años en el texto que presentó el Gobierno.[^menores]

### Decisiones automatizadas y evaluaciones de impacto

Toda persona tiene derecho «a no ser objeto de una decisión basada únicamente en el tratamiento automatizado, incluida la elaboración de perfiles, que produzca efectos jurídicos en él o le afecte significativamente de modo similar».[^rgpd] Una calificación, una sanción o una decisión de promoción no pueden salir solo de una herramienta.

Y cuando una administración quiere usar una tecnología nueva con datos que suponen un alto riesgo, antes tiene que hacer una **evaluación de impacto relativa a la protección de datos**.[^rgpd] Es responsabilidad de la administración que implanta la herramienta, no del docente que la usa, pero explica por qué un centro no debería adoptar por su cuenta una plataforma de IA con datos del alumnado.

## Reglamento de IA

Su lógica es graduar las obligaciones según el riesgo: unas pocas prácticas están prohibidas, ciertos usos son de alto riesgo y cargan con obligaciones estrictas, algunos sistemas tienen obligaciones de transparencia, y el resto, que es la mayoría de los usos, no tiene obligaciones específicas. Aparte, los modelos de uso general, como los que hay detrás de los *chatbots*, tienen sus propias obligaciones, que recaen en quien los desarrolla.

### Calendario

El Reglamento (UE) 2024/1689, conocido como RIA o *AI Act*, se aplica por fases. En julio de 2026 lo modificó el Reglamento (UE) 2026/1744, el llamado *Digital Omnibus*, que retrasó las obligaciones de los sistemas de alto riesgo y añadió nuevas prohibiciones.[^ria] [^omnibus]

| Desde | Qué se aplica | Relevancia en un centro |
| --- | --- | --- |
| 1 de agosto de 2024 | Entrada en vigor | Ninguna obligación todavía |
| 2 de febrero de 2025 | Disposiciones generales, alfabetización y prácticas prohibidas | Prohibido inferir emociones en centros educativos |
| 2 de agosto de 2025 | Modelos de uso general, gobernanza y sanciones | Obligaciones para los proveedores de los modelos |
| 2 de agosto de 2026 | Aplicación general, incluidas las obligaciones de transparencia | Avisar de que se habla con una IA; etiquetar ultrasuplantaciones |
| 2 de diciembre de 2026 | Nuevas prohibiciones del *Omnibus* | Prohibidos los sistemas para generar imágenes íntimas sin consentimiento |
| 2 de diciembre de 2027 | Sistemas de alto riesgo del anexo III, entre ellos los educativos | Obligaciones para quien implante sistemas que evalúan o admiten alumnado |
| 2 de agosto de 2028 | Sistemas de alto riesgo integrados en productos (anexo I) | Poca |

Las fechas de alto riesgo eran el 2 de agosto de 2026 y 2027. Muchas guías publicadas antes de julio de 2026, incluidas las directrices europeas para docentes, todavía dan las fechas antiguas.

### Quién es quién

El Reglamento reparte las obligaciones entre el **proveedor**, quien desarrolla el sistema y lo comercializa, y el **responsable del despliegue**, que es quien lo usa «bajo su propia autoridad, salvo cuando su uso se enmarque en una actividad personal de carácter no profesional».[^ria] En un centro público, cuando la Consellería implanta una herramienta, el responsable del despliegue es la administración, y el docente la usa por cuenta de ella. Lo que haga un docente por su cuenta para su trabajo queda en una zona menos clara, y es otro motivo para usar las herramientas que proporciona la administración.

### Alfabetización

El artículo 4 obligaba inicialmente a proveedores y responsables del despliegue a «garantizar que, en la mayor medida posible», su personal tuviera «un nivel suficiente de alfabetización en materia de IA». Desde el 27 de julio de 2026, tras el *Omnibus*, la obligación es más suave: deben adoptar «medidas para apoyar la promoción de la alfabetización en materia de IA» de su personal, y el texto aclara que no les exige garantizar «un nivel específico» de nadie. La Comisión y los Estados deben apoyar ese esfuerzo.[^omnibus]

En Galicia, además, la ley de IA obliga a la administración a velar porque el personal que interviene en el ciclo de vida de estos sistemas mantenga «as capacidades precisas para que poida garantir un debido uso destes».[^lei-ia]

### Prácticas prohibidas

La más relevante en educación es la del artículo 5.1.f: el uso de sistemas de IA «para inferir las emociones de una persona física en los lugares de trabajo y en los centros educativos», salvo por motivos médicos o de seguridad. Está prohibida desde el 2 de febrero de 2025.[^ria] Las directrices de la Comisión lo concretan con ejemplos:[^directrices]

- Una aplicación para aprender idiomas con reconocimiento de emociones no está prohibida si se usa fuera del centro; si el centro obliga al alumnado a usarla, sí lo está.
- Un sistema de supervisión de exámenes en línea que sigue la mirada para detectar material no autorizado no está prohibido; si además detecta nerviosismo o ansiedad, sí.
- Usar el reconocimiento de emociones para inferir el interés o la atención del alumnado está prohibido.

El resto de la lista (manipulación subliminal, explotación de vulnerabilidades, puntuación social, bases de datos de reconocimiento facial, categorización biométrica para deducir datos sensibles, identificación biométrica en tiempo real en espacios públicos con fines policiales) afecta poco al trabajo de un centro.

Desde el 2 de diciembre de 2026 se añaden dos prohibiciones con consecuencias directas para la convivencia escolar: los sistemas que generen imágenes, vídeos o audios realistas «de las partes íntimas de una persona física identificable» o de una persona identificable en actividades sexualmente explícitas sin su consentimiento, y los que generen material de abuso sexual infantil.[^omnibus] Afecta a las aplicaciones de «desnudos» falsos, cuyo uso entre estudiantes es un riesgo para la convivencia.

### Alto riesgo en educación

El anexo III considera de alto riesgo cuatro usos en educación y formación profesional:[^ria]

- a) determinar el acceso o la admisión a los centros, o distribuir al alumnado entre ellos;
- b) evaluar los resultados del aprendizaje, también cuando se usan para orientar el proceso de aprendizaje;
- c) evaluar el nivel de educación adecuado que recibirá una persona o al que podrá acceder;
- d) vigilar y detectar comportamientos prohibidos durante los exámenes.

No todo sistema que toque esos ámbitos es de alto riesgo. Según el artículo 6.3, no lo es cuando no influye sustancialmente en la decisión: si hace una tarea de procedimiento limitada, mejora el resultado de una actividad humana ya hecha, detecta desviaciones en patrones de decisión sin sustituir la valoración humana, o hace una tarea preparatoria. Pero lo es siempre que elabore perfiles de personas.[^ria]

Las obligaciones correspondientes se aplican desde el 2 de diciembre de 2027. Para la administración que implante uno de estos sistemas incluyen encargar la supervisión humana «a personas físicas que tengan la competencia, la formación y la autoridad necesarias» y, por ser un organismo público, hacer una evaluación de impacto sobre los derechos fundamentales antes de desplegarlo.[^ria]

Queda una cuestión abierta: el artículo 25.1.c convierte en proveedor de un sistema de alto riesgo a quien «modifique la finalidad prevista de un sistema de IA, incluido un sistema de IA de uso general», de modo que pase a ser de alto riesgo.[^ria] Cómo se aplica a un docente que usa un *chatbot* general para poner notas no está resuelto en el texto. Es un argumento más, junto al artículo 22 del RGPD, para que la IA no decida la calificación.

### Transparencia

Desde el 2 de agosto de 2026, los proveedores deben avisar a las personas de que interactúan con un sistema de IA y marcar el contenido sintético para que sea detectable. Quien use un sistema para generar ultrasuplantaciones (*deepfakes*) debe hacer público que se han generado artificialmente, y quien publique textos generados por IA «con el fin de informar al público sobre asuntos de interés público» debe indicarlo, salvo que hayan tenido revisión humana y alguien asuma la responsabilidad editorial.[^ria] Un material de clase normal no entra en esos supuestos: etiquetarlo es una buena práctica, no una obligación.

### Quién supervisa

En España, la Agencia Española de Supervisión de Inteligencia Artificial (AESIA), con sede en A Coruña, tiene funciones de «supervisión, el asesoramiento, la concienciación y la formación» y de «inspección, comprobación, sanción».[^aesia] Lo relativo a los datos personales sigue siendo competencia de la Agencia Española de Protección de Datos.

## Galicia

### La ley gallega de IA

La Lei 2/2025, para o desenvolvemento e o impulso da intelixencia artificial en Galicia, se aplica a la administración autonómica y su sector público, y por tanto a la Consellería de Educación y a los sistemas de IA que implante.[^lei-ia] Su artículo 12 establece una **reserva de humanidade**: cuando un sistema de IA sirva de apoyo a un acto o decisión administrativa, «en ningún caso tales actuacións nas que se empreguen sistemas de intelixencia artificial constituirán de seu decisións ou actos administrativos sen validación pola persoa titular do órgano competente». La ley fue modificada por la Lei 5/2025, que cambió entre otros su objeto y sus definiciones, pero no los artículos citados aquí.[^lei-5]

### Lo que está en marcha

- **Estratexia galega de intelixencia artificial 2030 (EGIA).** Su medida 4 prevé incorporar la IA a todas las etapas educativas, un grupo de personas expertas que diseñe la hoja de ruta y un programa específico de formación del profesorado.[^xunta-egia]
- **Plan integral de benestar dixital** (enero de 2026). Prevé incorporar a los currículos el uso responsable de la IA, un programa de formación del alumnado en IA y la publicación de una guía de *Orientacións para o uso e a integración da IA no ámbito educativo*.[^benestar]
- **Lei de educación dixital de Galicia.** El proyecto (expediente 12/PL-000015) está en el Parlamento desde julio de 2026, con la previsión de entrar en vigor en 2027.[^xunta-lei] Según la Xunta, dedicará un capítulo a los usos permitidos y prohibidos de la IA en la enseñanza.[^xunta-ia] Lo más relevante para el profesorado: **solo se podrán usar sistemas de IA homologados y autorizados por la Consellería**, que publicará un catálogo. Además, se prohibirán las decisiones académicas, organizativas y administrativas basadas únicamente en resultados de IA, los sistemas de control automatizado del comportamiento, la atención o el rendimiento, el uso de la IA para predecir o identificar condiciones como el TEA o el TDAH, y el reconocimiento facial. Es un texto en tramitación: puede cambiar, y conviene seguir su aprobación.
- **EdugalIA.** Proyecto de la Consellería para reducir el abandono escolar temprano mediante el análisis de datos con IA, que la formación de la Xunta presenta como la integración en «unha única plataforma» de los datos que hoy están dispersos.[^xunta-edugalia] Una plataforma así está en tensión con el principio de minimización y, si elabora perfiles del alumnado, necesita una evaluación de impacto previa y no puede tomar por sí sola decisiones que les afecten significativamente.

[^rgpd]: Reglamento (UE) 2016/679, General de Protección de Datos ([BOE](https://www.boe.es/buscar/doc.php?id=DOUE-L-2016-80807)): artículos 4.1 (dato personal), 5.1.c (minimización), 8.1 (consentimiento de menores en servicios en línea), 9.1 (categorías especiales), 22.1 (decisiones automatizadas), 28.1 (encargado del tratamiento), 35.1 (evaluación de impacto) y 37.1.a (delegado de protección de datos de las autoridades públicas).
[^loe]: Ley Orgánica 2/2006, de Educación, [disposición adicional vigesimotercera](https://www.boe.es/buscar/act.php?id=BOE-A-2006-7899#davigesimotercera).
[^lopdgdd]: Ley Orgánica 3/2018, de Protección de Datos Personales y garantía de los derechos digitales, [artículo 7](https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673#a7).
[^menores]: Proyecto de Ley Orgánica para la protección de las personas menores de edad en los entornos digitales, [BOCG, Congreso, serie A, núm. 52-1](https://www.congreso.es/public_oficiales/L15/CONG/BOCG/A/BOCG-15-A-52-1.PDF), 11 de abril de 2025, disposición final sexta.
[^ria]: Reglamento (UE) 2024/1689, de Inteligencia Artificial ([BOE](https://www.boe.es/buscar/doc.php?id=DOUE-L-2024-81079)): artículos 3.4 (responsable del despliegue), 5.1.f, 6.3, 25.1.c, 26.2, 27, 50 y 113, y anexo III, punto 3.
[^omnibus]: Reglamento (UE) 2026/1744, de 8 de julio de 2026 ([BOE](https://www.boe.es/buscar/doc.php?id=DOUE-L-2026-81147)): nuevo artículo 4; artículo 5.1, letras b bis y b ter; artículo 113.
[^lei-ia]: [Lei 2/2025, do 2 de abril](https://www.xunta.gal/dog/Publicados/2025/20250404/AnuncioC3B0-030425-0001_gl.html), para o desenvolvemento e o impulso da intelixencia artificial en Galicia, artigos 3, 12 e 19.
[^lei-5]: [Lei 5/2025, do 23 de decembro](https://www.xunta.gal/dog/Publicados/2025/20251231/AnuncioC3B0-231225-0002_gl.html), de medidas fiscais e administrativas, artigo 48.
[^directrices]: Comisión Europea, [*Guidelines on the ethical use of artificial intelligence and data in teaching and learning for educators*](https://data.europa.eu/doi/10.2766/7967834), 2026, tabla 1, con ejemplos de las directrices de la Comisión sobre prácticas prohibidas. Traducción propia.
[^aesia]: Real Decreto 729/2023, Estatuto de la AESIA, [artículo 4](https://www.boe.es/buscar/act.php?id=BOE-A-2023-18911).
[^benestar]: Xunta de Galicia, [*Plan integral de benestar dixital de Galicia*](https://ficheiros-web.xunta.gal/plans/educacion-ciencia/plan-integral-benestar-dixital.pdf), actuaciones 18, 19 y 28.
[^xunta-lei]: Xunta de Galicia, [nota de prensa del 29 de junio de 2026](https://www.xunta.gal/notas-de-prensa/-/nova/026191/rueda-anuncia-aprobacion-anteproxecto-lei-educacion-dixital-unha-norma-pioneira); Parlamento de Galicia, [ficha del proyecto 12/PL-000015](https://www.parlamentodegalicia.es/ParticipacionCidada/LexislaConNos/3482/proxecto-de-lei-de-educacion-dixital-de-galicia.-12pl-000015).
[^xunta-ia]: Xunta de Galicia, [nota de prensa del 11 de abril de 2026](https://www.xunta.gal/es/notas-de-prensa/-/nova/023351/galicia-autorizara-uso-educacion-para-deteccion-temprana-dificultades-aprendizaje).
[^xunta-egia]: Presentación de la Xunta *Intelixencia artificial (Ética e normativa en materia de Educación)*, p. 40.
[^xunta-edugalia]: Presentación de la Xunta *Intelixencia artificial (Ética e normativa en materia de Educación)*, pp. 64–68, comentada en el [anexo](anexo-formacion-xunta.md).
