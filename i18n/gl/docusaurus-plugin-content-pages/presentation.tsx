import React, { useEffect, useRef, useState } from 'react';
import Layout from '@theme/Layout';
import BrowserOnly from '@docusaurus/BrowserOnly';
import { useColorMode } from '@docusaurus/theme-common';
import { ChatConversation } from '@site/src/components/ChatConversation';
import styles from '@site/src/pages/presentation.module.css';

// Slide components
function TitleSlide() {
    return (
        <section data-background-gradient="linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%)">
            <h1>🤖 Docencia con IA</h1>
            <p>Usando Intelixencia Artificial na educación</p>
            <p className="small">
                Usa ← → para navegar | ESC para vista xeral | C para o encerado
            </p>
        </section>
    );
}

function IndexSlide() {
    return (
        <section>
            <h2>📋 Índice</h2>
            <ol>
                <li>Como chegamos ata aquí?</li>
                <li>Chatbots e ferramentas</li>
                <li>Deseño de prompts</li>
                <li>Aplicacións na docencia</li>
                <li>Ética na IA</li>
            </ol>
        </section>
    );
}

// Section 1: History
function HistorySection() {
    return (
        <section>
            <section className="section-title">
                <h1>1️⃣ Como chegamos ata aquí?</h1>
            </section>

            <section>
                <h2>Conceptos básicos</h2>
                <img src="/ia-educacion/img/venn.gif" alt="Diagrama IA/ML/DL" style={{ maxWidth: '70%', maxHeight: '60vh', display: 'block', margin: '0 auto' }} />
            </section>

            <section>
                <h2>Conceptos básicos</h2>
                <ul>
                    <li><span className="highlight">IA</span> (1956): Sistemas que realizan tarefas que requiren intelixencia humana</li>
                    <li><span className="highlight">Machine Learning</span> (1959): Algoritmos que aprenden dos datos</li>
                    <li><span className="highlight">Deep Learning</span>: Redes neuronais profundas</li>
                    <li><span className="highlight">IA Xenerativa</span>: Sistemas que crean contido orixinal</li>
                </ul>
            </section>

            <section>
                <h2>O paradoxo de Moravec</h2>
                <blockquote>
                    "É relativamente fácil facer que as computadoras realicen operacións matemáticas e loxísticas,
                    pero é difícil facer que realicen tarefas simples que calquera neno de 4 anos pode facer"
                </blockquote>
                <p className="small">Moravec, 1980</p>
            </section>

            <section>
                <h2>Liña temporal do boom</h2>
                <ul className="timeline">
                    <li><strong>2012</strong>: AlexNet - Inicio do deep learning</li>
                    <li><strong>2017</strong>: Transformer - Arquitectura revolucionaria</li>
                    <li><strong>2022</strong>: ChatGPT - Populariza asistentes conversacionais</li>
                    <li><strong>2023</strong>: GPT-4 - Modelos multimodais</li>
                    <li><strong>2024</strong>: o1 - Capacidades de razoamento</li>
                    <li><strong>2025</strong>: DeepSeek-R1 - Open weights, baixo custo</li>
                </ul>
            </section>

            <section>
                <h2>Expectativas futuras</h2>
                <div className="two-columns">
                    <div>
                        <h3>Curto prazo</h3>
                        <ul>
                            <li>🧠 Human Augmentation</li>
                            <li>🎬 Creación audiovisual</li>
                            <li>🤖 Axentes autónomos</li>
                        </ul>
                    </div>
                    <div>
                        <h3>Longo prazo</h3>
                        <ul>
                            <li>📚 IA na educación</li>
                            <li>🌐 AGI?</li>
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
                <h1>2️⃣ Chatbots e ferramentas</h1>
            </section>

            <section>
                <h2>Principais chatbots</h2>
                <div className="two-columns">
                    <div>
                        <h3>OpenAI</h3>
                        <ul>
                            <li><a href="https://chat.openai.com" target="_blank" rel="noopener noreferrer">ChatGPT</a> (GPT-5.2)</li>
                            <li>DALL-E, Sora</li>
                            <li><a href="https://chatgpt.com/gpts" target="_blank" rel="noopener noreferrer">GPTs personalizados</a></li>
                        </ul>
                        <h3>Google</h3>
                        <ul>
                            <li><a href="https://gemini.google.com" target="_blank" rel="noopener noreferrer">Gemini</a></li>
                            <li><a href="https://notebooklm.google" target="_blank" rel="noopener noreferrer">NotebookLM</a></li>
                            <li><a href="https://aistudio.google.com" target="_blank" rel="noopener noreferrer">AI Studio</a></li>
                        </ul>
                    </div>
                    <div>
                        <h3>Outros</h3>
                        <ul>
                            <li><a href="https://claude.ai" target="_blank" rel="noopener noreferrer"><strong>Claude</strong></a> (Anthropic)</li>
                            <li><a href="https://www.perplexity.ai" target="_blank" rel="noopener noreferrer"><strong>Perplexity</strong></a> - Busca</li>
                            <li><a href="https://chat.deepseek.com" target="_blank" rel="noopener noreferrer"><strong>DeepSeek</strong></a> - Open weights</li>
                            <li><a href="https://copilot.microsoft.com" target="_blank" rel="noopener noreferrer"><strong>Copilot</strong></a> (Microsoft)</li>
                            <li><a href="https://chat.mistral.ai" target="_blank" rel="noopener noreferrer"><strong>Mistral</strong></a> - Europeo</li>
                        </ul>
                    </div>
                </div>
            </section>

            <section>
                <h2>Funcionalidades clave</h2>
                <ul>
                    <li>💾 <strong>Memoria</strong>: Lembran preferencias entre conversas</li>
                    <li>🔒 <strong>Chats temporais</strong>: Privacidade, non adestran o modelo</li>
                    <li>✏️ <strong>Canvas</strong>: Edición colaborativa coa IA</li>
                </ul>
            </section>

            <section>
                <h2>Outras ferramentas</h2>
                <ul>
                    <li>📊 <a href="https://mermaid.js.org" target="_blank" rel="noopener noreferrer"><strong>Mermaid</strong></a>: Diagramas desde texto</li>
                    <li>🎥 <a href="https://videohighlight.com" target="_blank" rel="noopener noreferrer"><strong>Video Highlight</strong></a>: Transcribe e resume vídeos</li>
                    <li>📽️ <strong>Presentacións</strong>: <a href="https://gamma.app" target="_blank" rel="noopener noreferrer">Gamma</a>, <a href="https://www.canva.com" target="_blank" rel="noopener noreferrer">Canva</a>, <a href="https://www.beautiful.ai" target="_blank" rel="noopener noreferrer">Beautiful.AI</a></li>
                    <li>🎨 <strong>Imaxes</strong>: <a href="https://www.midjourney.com" target="_blank" rel="noopener noreferrer">Midjourney</a>, <a href="https://stability.ai" target="_blank" rel="noopener noreferrer">Stable Diffusion</a>, <a href="https://ideogram.ai" target="_blank" rel="noopener noreferrer">Ideogram</a></li>
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
                <h1>3️⃣ Deseño de prompts</h1>
            </section>

            <section>
                <h2>Que é un prompt?</h2>
                <p>Un prompt eficaz funciona como unha <strong>especificación técnica</strong> precisa.</p>
                <p>Na educación, orientado a producir:</p>
                <ul>
                    <li>Fichas de actividade</li>
                    <li>Bancos de preguntas (GIFT, Moodle)</li>
                    <li>Rúbricas de avaliación</li>
                    <li>Adaptacións curriculares</li>
                </ul>
            </section>

            <section>
                <h2>Estrutura de referencia</h2>
                <pre><code>{`Es un consultor experto en deseño curricular.

Tarefa:
- Quero crear: [actividade / banco de preguntas]

Contexto:
- Materia/tema:
- Nivel (curso ou FP):
- Duración:

Antes de responder:
- Faime 3–5 preguntas de aclaración.

Saída:
- Formato: Markdown`}</code></pre>
            </section>

            <section>
                <h2>Técnicas fundamentais (1/2)</h2>
                <ol>
                    <li><strong>Definición de rol</strong>: Configura o "quén" (perspectiva)</li>
                    <li><strong>Claridade do obxectivo</strong>: Evidencia verificable</li>
                    <li><strong>Contexto mínimo</strong>: Nivel, tempo, recursos, produto</li>
                </ol>
            </section>

            <section>
                <h2>Técnicas fundamentais (2/2)</h2>
                <ol start={4}>
                    <li><strong>Interacción inversa</strong>: Que a IA pregunte primeiro</li>
                    <li><strong>Supostos explícitos</strong>: Facer visible a "imaxinación"</li>
                    <li><strong>Control do formato</strong>: Táboas, checklists, Markdown</li>
                </ol>
            </section>

            <section>
                <h2>Prácticas avanzadas</h2>
                <ul>
                    <li>📝 <strong>Dúas pasadas</strong>: Borrador → Auditoría → Final</li>
                    <li>⚖️ <strong>Comparación A/B</strong>: Táboa por criterios</li>
                    <li>❌ <strong>Anti-alucinacións</strong>: "Se non o sabes, indícao"</li>
                    <li>🌳 <strong>Tree of Thoughts</strong>: Alternativas + criterios</li>
                </ul>
            </section>

            <section>
                <h2>Exemplo: Prompt de rol específico</h2>
                <div className="chat-slide">
                    <ChatConversation source="/data/chats/specific-role.yaml" />
                </div>
            </section>

            <section>
                <h2>Exemplo: Few-shot</h2>
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
                <h1>4️⃣ Aplicacións na docencia</h1>
            </section>

            <section>
                <h2>Apoio ao docente</h2>
                <ul>
                    <li>📅 <strong>Planificación</strong>: Programacións, roadmaps, tarefas</li>
                    <li>📚 <strong>Materiais</strong>: Preguntas, exercicios, H5P, Moodle</li>
                    <li>✅ <strong>Avaliación</strong>: Rúbricas, corrección de exames</li>
                    <li>🎥 <strong>Autoavaliación</strong>: Análise de clases gravadas</li>
                    <li>💬 <strong>Tutorización</strong>: Chatbots para responder dúbidas</li>
                </ul>
            </section>

            <section>
                <h2>Apoio ao alumno</h2>
                <blockquote>
                    "Ensinar aos alumnos a usalo ben"
                </blockquote>
                <ul>
                    <li>"Plantéame preguntas similares..."</li>
                    <li>"Corrixe rigorosamente as miñas respostas..."</li>
                    <li>"Axúdame a estudar con esquemas..."</li>
                    <li>"Xera flashcards para memorizar..."</li>
                </ul>
            </section>

            <section>
                <h2>🚫 Non poñas portas ao campo</h2>
                <ul>
                    <li>Normalizar o traballo con chatbots</li>
                    <li>Son unha ferramenta coa que <strong>todos traballaremos</strong></li>
                    <li>Se non a usan ben, nótase</li>
                    <li>Se a usan ben, están aprendendo</li>
                    <li>Que citen cando e como o usan</li>
                </ul>
            </section>

            <section>
                <h2>E se queremos auditalo?</h2>
                <ul>
                    <li>📋 <strong>Entrevista</strong> co alumno</li>
                    <li>🤖 <strong>Preguntar ás IAs</strong>: adxuntar textos do propio alumno</li>
                    <li>🔍 <strong>Detectores de plaxio</strong></li>
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
                <h1>5️⃣ Ética na IA</h1>
            </section>

            <section>
                <h2>Principios fundamentais (UE)</h2>
                <ul>
                    <li>🧑‍💻 <strong>Supervisión humana</strong>: IA como ferramenta</li>
                    <li>🔒 <strong>Robustez e seguridade</strong>: Algoritmos fiables</li>
                    <li>🛡️ <strong>Privacidade</strong>: Protección de datos (RGPD)</li>
                    <li>👁️ <strong>Transparencia</strong>: Saber que interactúas con IA</li>
                    <li>⚖️ <strong>Non discriminación</strong>: Sen sesgos nin exclusión</li>
                </ul>
            </section>

            <section>
                <h2>Os sesgos na IA</h2>
                <ul>
                    <li>📊 <strong>Sesgo de mostraxe</strong>: Datos non representativos</li>
                    <li>📜 <strong>Sesgo histórico</strong>: Datos con prexuízos sociais</li>
                    <li>🏷️ <strong>Sesgo de etiquetado</strong>: Confirmar crenzas previas</li>
                    <li>⚙️ <strong>Sesgo algorítmico</strong>: Optimización sen "fairness"</li>
                </ul>
            </section>

            <section>
                <h2>Exemplo: UK 2020</h2>
                <blockquote>
                    Algoritmo de cualificacións durante a pandemia penalizou sistematicamente
                    a estudantes de escolas con peores resultados históricos.
                </blockquote>
                <p className="small">
                    Miles de estudantes viron as súas cualificacións rebaixadas inxustamente.
                </p>
            </section>

            <section>
                <h2>O teu rol como docente</h2>
                <ul>
                    <li>🔍 <strong>Usuario crítico</strong>: Non delegar o xuízo</li>
                    <li>📚 <strong>Alfabetización na IA</strong>: Enseñar como funciona</li>
                    <li>⚖️ <strong>Axente de equidade</strong>: Observar impacto diferencial</li>
                    <li>🔐 <strong>Privacidade</strong>: RGPD e datos educativos</li>
                </ul>
            </section>
        </section>
    );
}

function ClosingSlide() {
    return (
        <section data-background-gradient="linear-gradient(135deg, #0f3460 0%, #16213e 50%, #1a1a2e 100%)">
            <h2>📖 Máis información</h2>
            <p>
                <a href="/gl/docs/historia-y-llms">
                    Ver documentación completa →
                </a>
            </p>
            <p className="small" style={{ marginTop: '2em' }}>
                Usa ← → para navegar | ESC para vista xeral | C para o encerado
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
        // Track injected stylesheets for cleanup
        const injectedStyles: HTMLLinkElement[] = [];

        const initReveal = async () => {
            // Dynamically import reveal.js
            const Reveal = (await import('reveal.js')).default || (await import('reveal.js'));
            const RevealHighlight = ((await import('reveal.js/plugin/highlight/highlight')) as any).default;

            // Inject reveal.js stylesheets as link elements (properly cleaned up on unmount)
            const revealStyles = [
                { id: 'reveal-reset-css', href: 'https://cdn.jsdelivr.net/npm/reveal.js@5.2.1/dist/reset.css' },
                { id: 'reveal-core-css', href: 'https://cdn.jsdelivr.net/npm/reveal.js@5.2.1/dist/reveal.css' },
                { id: 'reveal-theme-css', href: 'https://cdn.jsdelivr.net/npm/reveal.js@5.2.1/dist/theme/black.css' },
            ];

            for (const style of revealStyles) {
                if (!document.getElementById(style.id)) {
                    const link = document.createElement('link');
                    link.id = style.id;
                    link.rel = 'stylesheet';
                    link.href = style.href;
                    document.head.appendChild(link);
                    injectedStyles.push(link);
                }
            }

            // Load chalkboard plugin CSS
            if (!document.getElementById('chalkboard-css')) {
                const chalkboardCss = document.createElement('link');
                chalkboardCss.id = 'chalkboard-css';
                chalkboardCss.rel = 'stylesheet';
                chalkboardCss.href = 'https://cdn.jsdelivr.net/npm/reveal.js-plugins@latest/chalkboard/style.css';
                document.head.appendChild(chalkboardCss);
                injectedStyles.push(chalkboardCss);
            }

            // Load chalkboard plugin from CDN (only once)
            if (!(window as any).RevealChalkboard) {
                await new Promise<void>((resolve) => {
                    const script = document.createElement('script');
                    script.src = 'https://cdn.jsdelivr.net/npm/reveal.js-plugins@latest/chalkboard/plugin.js';
                    script.onload = () => resolve();
                    document.head.appendChild(script);
                });
            }

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
            // Clean up reveal.js instance
            if (revealInstance.current) {
                revealInstance.current.destroy();
                revealInstance.current = null;
            }

            // Remove injected stylesheets to prevent style leakage
            injectedStyles.forEach(link => {
                if (link.parentNode) {
                    link.parentNode.removeChild(link);
                }
            });
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
            description="Presentación sobre o uso da IA na docencia"
        >
            <BrowserOnly fallback={<LoadingFallback />}>
                {() => <RevealPresentation />}
            </BrowserOnly>
        </Layout>
    );
}
