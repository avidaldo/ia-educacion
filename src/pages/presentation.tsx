import React, { useEffect, useRef, useState } from 'react';
import Layout from '@theme/Layout';
import BrowserOnly from '@docusaurus/BrowserOnly';
import { useColorMode } from '@docusaurus/theme-common';
import { ChatConversation } from '@site/src/components/ChatConversation';
import styles from './presentation.module.css';

// Reveal.js styles - imported globally for proper layout
import 'reveal.js/dist/reset.css';
import 'reveal.js/dist/reveal.css';
import 'reveal.js/dist/theme/black.css';

// Slide components
function TitleSlide() {
  return (
    <section data-background-gradient="linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%)">
      <h1>🤖 Docencia con IA</h1>
      <p>Usando Inteligencia Artificial en educación</p>
      <p className="small">
        Usa ← → para navegar | ESC para vista general | C para pizarra
      </p>
    </section>
  );
}

function IndexSlide() {
  return (
    <section>
      <h2>📋 Índice</h2>
      <ol>
        <li>¿Cómo hemos llegado hasta aquí?</li>
        <li>Chatbots y herramientas</li>
        <li>Diseño de prompts</li>
        <li>Aplicaciones en docencia</li>
        <li>Ética en IA</li>
      </ol>
    </section>
  );
}

// Section 1: History
function HistorySection() {
  return (
    <section>
      <section className="section-title">
        <h1>1️⃣ ¿Cómo hemos llegado hasta aquí?</h1>
      </section>

      <section>
        <h2>Conceptos básicos</h2>
        <ul>
          <li><span className="highlight">IA</span> (1956): Sistemas que realizan tareas que requieren inteligencia humana</li>
          <li><span className="highlight">Machine Learning</span> (1959): Algoritmos que aprenden de los datos</li>
          <li><span className="highlight">Deep Learning</span>: Redes neuronales profundas</li>
          <li><span className="highlight">IA Generativa</span>: Sistemas que crean contenido original</li>
        </ul>
      </section>

      <section>
        <h2>La paradoja de Moravec</h2>
        <blockquote>
          "Es relativamente fácil hacer que las computadoras realicen operaciones matemáticas y lógicas, 
          pero es difícil hacer que realicen tareas simples que cualquier niño de 4 años puede hacer"
        </blockquote>
        <p className="small">Moravec, 1980</p>
      </section>

      <section>
        <h2>Línea temporal del boom</h2>
        <ul className="timeline">
          <li><strong>2012</strong>: AlexNet - Inicio del deep learning</li>
          <li><strong>2017</strong>: Transformer - Arquitectura revolucionaria</li>
          <li><strong>2022</strong>: ChatGPT - Populariza asistentes conversacionales</li>
          <li><strong>2023</strong>: GPT-4 - Modelos multimodales</li>
          <li><strong>2024</strong>: o1 - Capacidades de razonamiento</li>
          <li><strong>2025</strong>: DeepSeek-R1 - Open weights, bajo coste</li>
        </ul>
      </section>

      <section>
        <h2>Expectativas futuras</h2>
        <div className="two-columns">
          <div>
            <h3>Corto plazo</h3>
            <ul>
              <li>🧠 Human Augmentation</li>
              <li>🎬 Creación audiovisual</li>
              <li>🤖 Agentes autónomos</li>
            </ul>
          </div>
          <div>
            <h3>Largo plazo</h3>
            <ul>
              <li>📚 IA en educación</li>
              <li>🌐 ¿AGI?</li>
            </ul>
          </div>
        </div>
      </section>
    </section>
  );
}

// Section 2: Tools
function ToolsSection() {
  return (
    <section>
      <section className="section-title">
        <h1>2️⃣ Chatbots y herramientas</h1>
      </section>

      <section>
        <h2>Principales chatbots</h2>
        <div className="two-columns">
          <div>
            <h3>OpenAI</h3>
            <ul>
              <li>ChatGPT (GPT-5.2)</li>
              <li>DALL-E, Sora</li>
              <li>GPTs personalizados</li>
            </ul>
            <h3>Google</h3>
            <ul>
              <li>Gemini</li>
              <li>NotebookLM</li>
              <li>AI Studio</li>
            </ul>
          </div>
          <div>
            <h3>Otros</h3>
            <ul>
              <li><strong>Claude</strong> (Anthropic)</li>
              <li><strong>Perplexity</strong> - Búsqueda</li>
              <li><strong>DeepSeek</strong> - Open weights</li>
              <li><strong>Copilot</strong> (Microsoft)</li>
              <li><strong>Mistral</strong> - Europeo</li>
            </ul>
          </div>
        </div>
      </section>

      <section>
        <h2>Funcionalidades clave</h2>
        <ul>
          <li>💾 <strong>Memoria</strong>: Recuerdan preferencias entre conversaciones</li>
          <li>🔒 <strong>Chats temporales</strong>: Privacidad, no entrenan el modelo</li>
          <li>✏️ <strong>Canvas</strong>: Edición colaborativa con la IA</li>
        </ul>
      </section>

      <section>
        <h2>Otras herramientas</h2>
        <ul>
          <li>📊 <strong>Mermaid</strong>: Diagramas desde texto</li>
          <li>🎥 <strong>Video Highlight</strong>: Transcribe y resume vídeos</li>
          <li>📽️ <strong>Presentaciones</strong>: Gamma, Canva, Beautiful.AI</li>
          <li>🎨 <strong>Imágenes</strong>: Midjourney, Stable Diffusion, Ideogram</li>
        </ul>
      </section>
    </section>
  );
}

// Section 3: Prompts
function PromptsSection() {
  return (
    <section>
      <section className="section-title">
        <h1>3️⃣ Diseño de prompts</h1>
      </section>

      <section>
        <h2>¿Qué es un prompt?</h2>
        <p>Un prompt eficaz funciona como una <strong>especificación técnica</strong> precisa.</p>
        <p>En educación, orientado a producir:</p>
        <ul>
          <li>Fichas de actividad</li>
          <li>Bancos de preguntas (GIFT, Moodle)</li>
          <li>Rúbricas de evaluación</li>
          <li>Adaptaciones curriculares</li>
        </ul>
      </section>

      <section>
        <h2>Estructura de referencia</h2>
        <pre><code>{`Eres un consultor experto en diseño curricular.

Tarea:
- Quiero crear: [actividad / banco de preguntas]

Contexto:
- Materia/tema:
- Nivel (curso o FP):
- Duración:

Antes de responder:
- Hazme 3–5 preguntas de aclaración.

Salida:
- Formato: Markdown`}</code></pre>
      </section>

      <section>
        <h2>Técnicas fundamentales (1/2)</h2>
        <ol>
          <li><strong>Definición de rol</strong>: Configura el "quién" (perspectiva)</li>
          <li><strong>Claridad del objetivo</strong>: Evidencia verificable</li>
          <li><strong>Contexto mínimo</strong>: Nivel, tiempo, recursos, producto</li>
        </ol>
      </section>

      <section>
        <h2>Técnicas fundamentales (2/2)</h2>
        <ol start={4}>
          <li><strong>Interacción inversa</strong>: Que la IA pregunte primero</li>
          <li><strong>Supuestos explícitos</strong>: Hacer visible la "imaginación"</li>
          <li><strong>Control del formato</strong>: Tablas, checklists, Markdown</li>
        </ol>
      </section>

      <section>
        <h2>Prácticas avanzadas</h2>
        <ul>
          <li>📝 <strong>Dos pasadas</strong>: Borrador → Auditoría → Final</li>
          <li>⚖️ <strong>Comparación A/B</strong>: Tabla por criterios</li>
          <li>❌ <strong>Anti-alucinaciones</strong>: "Si no sabes, indícalo"</li>
          <li>🌳 <strong>Tree of Thoughts</strong>: Alternativas + criterios</li>
        </ul>
      </section>

      <section>
        <h2>Ejemplo: Prompt de rol específico</h2>
        <div className="chat-slide">
          <ChatConversation source="/data/chats/specific-role.yaml" />
        </div>
      </section>

      <section>
        <h2>Ejemplo: Few-shot</h2>
        <div className="chat-slide">
          <ChatConversation source="/data/chats/few-shot-one.yaml" />
        </div>
      </section>
    </section>
  );
}

// Section 4: Teaching Applications
function TeachingSection() {
  return (
    <section>
      <section className="section-title">
        <h1>4️⃣ Aplicaciones en docencia</h1>
      </section>

      <section>
        <h2>Apoyo al docente</h2>
        <ul>
          <li>📅 <strong>Planificación</strong>: Programaciones, roadmaps, tareas</li>
          <li>📚 <strong>Materiales</strong>: Preguntas, ejercicios, H5P, Moodle</li>
          <li>✅ <strong>Evaluación</strong>: Rúbricas, corrección de exámenes</li>
          <li>🎥 <strong>Autoevaluación</strong>: Análisis de clases grabadas</li>
          <li>💬 <strong>Tutorización</strong>: Chatbots para responder dudas</li>
        </ul>
      </section>

      <section>
        <h2>Apoyo al alumno</h2>
        <blockquote>
          "Enseñar a los alumnos a usarlo bien"
        </blockquote>
        <ul>
          <li>"Plantéame preguntas similares..."</li>
          <li>"Corrige rigurosamente mis respuestas..."</li>
          <li>"Ayúdame a estudiar con esquemas..."</li>
          <li>"Genera flashcards para memorizar..."</li>
        </ul>
      </section>

      <section>
        <h2>🚫 No pongas puertas al campo</h2>
        <ul>
          <li>Normalizar el trabajo con chatbots</li>
          <li>Son una herramienta con la que <strong>todos trabajaremos</strong></li>
          <li>Si no la usan bien, se nota</li>
          <li>Si la usan bien, están aprendiendo</li>
          <li>Que citen cuándo y cómo lo usan</li>
        </ul>
      </section>

      <section>
        <h2>¿Y si queremos auditarlo?</h2>
        <ul>
          <li>📋 <strong>Entrevista</strong> con el alumno</li>
          <li>🤖 <strong>Preguntar a las IAs</strong>: adjuntar textos del propio alumno</li>
          <li>🔍 <strong>Detectores de plagio</strong></li>
        </ul>
      </section>
    </section>
  );
}

// Section 5: Ethics
function EthicsSection() {
  return (
    <section>
      <section className="section-title">
        <h1>5️⃣ Ética en IA</h1>
      </section>

      <section>
        <h2>Principios fundamentales (UE)</h2>
        <ul>
          <li>🧑‍💻 <strong>Supervisión humana</strong>: IA como herramienta</li>
          <li>🔒 <strong>Robustez y seguridad</strong>: Algoritmos fiables</li>
          <li>🛡️ <strong>Privacidad</strong>: Protección de datos (RGPD)</li>
          <li>👁️ <strong>Transparencia</strong>: Saber que interactúas con IA</li>
          <li>⚖️ <strong>No discriminación</strong>: Sin sesgos ni exclusión</li>
        </ul>
      </section>

      <section>
        <h2>Los sesgos en la IA</h2>
        <ul>
          <li>📊 <strong>Sesgo de muestreo</strong>: Datos no representativos</li>
          <li>📜 <strong>Sesgo histórico</strong>: Datos con prejuicios sociales</li>
          <li>🏷️ <strong>Sesgo de etiquetado</strong>: Confirmar creencias previas</li>
          <li>⚙️ <strong>Sesgo algorítmico</strong>: Optimización sin "fairness"</li>
        </ul>
      </section>

      <section>
        <h2>Ejemplo: UK 2020</h2>
        <blockquote>
          Algoritmo de calificaciones durante la pandemia penalizó sistemáticamente 
          a estudiantes de escuelas con peores resultados históricos.
        </blockquote>
        <p className="small">
          Miles de estudiantes vieron sus calificaciones rebajadas injustamente.
        </p>
      </section>

      <section>
        <h2>Tu rol como docente</h2>
        <ul>
          <li>🔍 <strong>Usuario crítico</strong>: No delegar el juicio</li>
          <li>📚 <strong>Alfabetización en IA</strong>: Enseñar cómo funciona</li>
          <li>⚖️ <strong>Agente de equidad</strong>: Observar impacto diferencial</li>
          <li>🔐 <strong>Privacidad</strong>: RGPD y datos educativos</li>
        </ul>
      </section>
    </section>
  );
}

function ClosingSlide() {
  return (
    <section data-background-gradient="linear-gradient(135deg, #0f3460 0%, #16213e 50%, #1a1a2e 100%)">
      <h2>📖 Más información</h2>
      <p>
        <a href="/ia-educacion/docs/10-historia-y-llms">
          Ver documentación completa →
        </a>
      </p>
      <p className="small" style={{ marginTop: '2em' }}>
        Usa ← → para navegar | ESC para vista general | C para pizarra
      </p>
    </section>
  );
}

// Client-side only presentation component
function RevealPresentation() {
  const revealRef = useRef<HTMLDivElement>(null);
  const revealInstance = useRef<any>(null);
  const { colorMode } = useColorMode();
  const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
    const initReveal = async () => {
      // Dynamically import reveal.js
      const Reveal = (await import('reveal.js')).default || (await import('reveal.js'));
      const RevealHighlight = ((await import('reveal.js/plugin/highlight/highlight')) as any).default;

      // Load chalkboard plugin from CDN
      await new Promise<void>((resolve) => {
        const script = document.createElement('script');
        script.src = 'https://cdn.jsdelivr.net/npm/reveal.js-plugins@latest/chalkboard/plugin.js';
        script.onload = () => resolve();
        document.head.appendChild(script);
      });

      const RevealChalkboard = (window as any).RevealChalkboard;

      if (revealRef.current && !revealInstance.current) {
        const deck = new (Reveal as any)(revealRef.current, {
          hash: true,
          slideNumber: true,
          transition: 'slide',
          backgroundTransition: 'fade',
          plugins: [RevealHighlight, RevealChalkboard].filter(Boolean),
          chalkboard: {
            toggleChalkboardButton: true,
            toggleNotesButton: true,
          },
        });

        await deck.initialize();
        revealInstance.current = deck;
        setIsLoaded(true);
      }
    };

    initReveal();

    return () => {
      if (revealInstance.current) {
        revealInstance.current.destroy();
        revealInstance.current = null;
      }
    };
  }, []);

  // Update theme when colorMode changes
  useEffect(() => {
    if (revealInstance.current && isLoaded) {
      const slidesElement = revealRef.current?.querySelector('.slides');
      if (slidesElement) {
        if (colorMode === 'dark') {
          slidesElement.classList.add('dark-theme');
          slidesElement.classList.remove('light-theme');
        } else {
          slidesElement.classList.add('light-theme');
          slidesElement.classList.remove('dark-theme');
        }
      }
    }
  }, [colorMode, isLoaded]);

  return (
    <div className={styles.presentationContainer}>
      <div className={`reveal ${styles.reveal}`} ref={revealRef}>
        <div className={`slides ${colorMode === 'dark' ? 'dark-theme' : 'light-theme'}`}>
          <TitleSlide />
          <IndexSlide />
          <HistorySection />
          <ToolsSection />
          <PromptsSection />
          <TeachingSection />
          <EthicsSection />
          <ClosingSlide />
        </div>
      </div>
    </div>
  );
}

// Loading fallback during SSR
function LoadingFallback() {
  return (
    <div className={styles.presentationContainer}>
      <div style={{ 
        display: 'flex', 
        justifyContent: 'center', 
        alignItems: 'center', 
        height: '100%',
        fontSize: '1.5em'
      }}>
        Cargando presentación...
      </div>
    </div>
  );
}

export default function Presentation(): JSX.Element {
  return (
    <Layout
      title="Presentación"
      description="Presentación sobre el uso de IA en docencia"
    >
      <BrowserOnly fallback={<LoadingFallback />}>
        {() => <RevealPresentation />}
      </BrowserOnly>
    </Layout>
  );
}
