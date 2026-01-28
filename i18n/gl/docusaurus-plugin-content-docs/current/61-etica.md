# Ética en IA

## Principios éticos fundamentais

A Comisión Europea define os seguintes principios éticos fundamentais da IA:

* **Acción e Supervisión Humanas:** A IA debe actuar como unha ferramenta para apoiar ao ser humano, non para substituír a súa autonomía. As decisións finais importantes deben ser tomadas por persoas.
* **Robustez Técnica e Seguridade:** Os algoritmos deben ser seguros, fiables e o suficientemente robustos para non causar danos non intencionados.
* **Privacidade e Gobernanza dos Datos:** Débese garantir a privacidade dos datos dos estudantes e establecer protocolos claros sobre quen ten acceso a eles e para que se utilizan.
* **Transparencia:** Debe ser posible trazar o funcionamento dun sistema de IA. Os usuarios deben saber que están interactuando cunha IA e comprender (na medida do posible) como toma as súas "decisións".
* **Diversidade, Non Discriminación e Equidade:** Os sistemas de IA deben ser accesibles para todos e non deben introducir ou amplificar sesgos que prexudiquen a determinados grupos de estudantes.
* **Benestar Social e Medioambiental:** A IA debe usarse para promover un cambio social positivo, incluíndo a educación de calidade.
* **Rendición de Contas (Accountability):** Deben existir mecanismos para asegurar a responsabilidade polos sistemas de IA e os seus resultados.


## Os sesgos na IA

O "sesgo" no contexto da intelixencia artificial (IA) refírese á tendencia sistemática dun sistema de IA a producir resultados que son consistentemente inexactos, inxustos ou desfavorables para certos grupos de persoas, ou que reforzan prexuízos e estereotipos existentes. Este sesgo maniféstase nos resultados, decisións ou predicións da IA.

Un modelo de Machine Learning aprende a partir de datos. Se os datos cos que se adestra reflicten prexuízos ou desigualdades do mundo real, a IA aprenderaos.


### Tipos de sesgos

- **Sesgo de mostraxe**: Se un conxunto de datos para o recoñecemento facial contén predominantemente imaxes de persoas de pel clara, o modelo resultante pode ter un rendemento deficiente ao recoñecer a persoas de pel máis escura.

- **Sesgo histórico**: Datos históricos reflicten prexuízos sociais.  
  - *Exemplo*: IA de contratación de Amazon (2018) penalizaba CVs coa palabra "muller", ao adestrarse con datos dunha industria dominada por homes.

- **Sesgo de medición**: Provén de erros sistemáticos na forma en que se miden ou recollen os datos. A variable que se mide non representa de forma precisa a característica que se quere avaliar.

- **Sesgo algorítmico**: É o sesgo introducido polo propio algoritmo. Pode ser o resultado de simplificacións ou da optimización de métricas que non capturan a "xustiza" (fairness).

- **Sesgo de etiquetado**: É unha manifestación do sesgo de confirmación dos desenvolvedores ou usuarios. Tenden a crear e confiar en modelos que confirman as súas crenzas preexistentes, etiquetando os datos ou interpretando os resultados de xeito que se axusten aos seus prexuízos.

### Exemplos

#### [O algoritmo de cualificacións en Reino Unido (2020)](https://www.xataka.com/robotica-e-ia/cuando-nota-no-te-pone-profesor-sino-algoritmo-caos-estudiantes-reino-unido)

* **Problema:** Debido á cancelación de exames pola pandemia, o goberno británico usou un algoritmo para predicir as cualificacións dos estudantes.
* **O Sesgo:** O modelo daba un peso significativo ao rendemento histórico da escola. Isto penalizou sistematicamente a estudantes brillantes de escolas con peores resultados históricos (xeralmente en zonas de menores ingresos), mentres que beneficiaba a estudantes de centros de elite.
* **Consecuencia:** Miles de estudantes viron as súas cualificacións rebaixadas inxustamente, o que lles impediu acceder á universidade desexada. O caso xerou protestas masivas e o goberno tivo que dar marcha atrás. Foi un claro exemplo de **sesgo algorítmico e de selección** cun impacto devastador.

#### Sesgos corrixidos con sesgos

<div style={{maxWidth: "600px"}}>

<a href="https://elpais.com/tecnologia/2024-02-24/nazis-chinas-y-vikingos-negros-google-suspende-su-ia-de-imagenes-por-sobrerrepresentar-a-minorias.html" target="_blank" rel="noopener noreferrer">

![](/img/black-ss.png)

</a>

</div>

> "Non podes ter un sistema que non teña sesgos, ou que sexa percibido como non sesgado por todo o mundo" ([Yann LeCun](https://www.youtube.com/watch?v=ZQXHf6gv6s8))


## Consideracións especiais para docentes

Como docente, non necesitas ser un experto en *machine learning*, pero si un **usuario crítico e consciente**. O teu rol é fundamental para mitigar os riscos da IA na aula. Ao seleccionar ferramentas de IA, debes avaliar tres aspectos críticos: a **transparencia** do funcionamento (evitando "caixas negras" sen explicación), a **ausencia de sesgos** mediante auditorías independentes, e o **cumprimento de normativas de privacidade** coma o RGPD, especialmente tratándose de datos educativos altamente sensibles.

No uso cotián, é esencial **non delegar o xuízo crítico** e utilizar a IA como asistente, non como oráculo, supervisando constantemente as recomendacións para evitar o encasillamento de estudantes. O aspecto máis importante é **fomentar a alfabetización en IA** entre os estudantes: ensinándolles como funcionan estas ferramentas, promovendo o pensamento crítico cara aos seus resultados, e establecendo normas éticas claras de uso. Finalmente, debes actuar como **axente de equidade**, observando o impacto diferencial en diversos grupos de estudantes, informando sobre problemas detectados e garantindo acceso equitativo para evitar que a IA xere novas fendas dixitais.

A integración ética da IA é un proceso continuo de aprendizaxe e adaptación. O teu papel como docente é insubstituíble para guiar aos estudantes neste novo paradigma, asegurando que a tecnoloxía sirva para potenciar a aprendizaxe humana nun marco de xustiza e equidade.
