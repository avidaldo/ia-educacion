import React, { useState, useEffect } from 'react';
import yaml from 'js-yaml';
import ReactMarkdown from 'react-markdown';
import rehypeRaw from 'rehype-raw';
import remarkGfm from 'remark-gfm';
import { useColorMode } from '@docusaurus/theme-common';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from './styles.module.css';
import { ChatConversationProps, UserMessageProps, AssistantMessageProps, ConversationData, Message } from './types';

// A component to render markdown content with proper image path resolution
function MarkdownContent({ children, baseUrl }: { children: React.ReactNode; baseUrl?: string }): JSX.Element {
  if (typeof children === 'string') {
    return (
      <ReactMarkdown 
        rehypePlugins={[rehypeRaw]} 
        remarkPlugins={[remarkGfm]}
        components={{
          h1: ({node, ...props}) => <h1 className={styles.chatHeading} {...props} />,
          h2: ({node, ...props}) => <h2 className={styles.chatHeading} {...props} />,
          h3: ({node, ...props}) => <h3 className={styles.chatHeading} {...props} />,
          h4: ({node, ...props}) => <h4 className={styles.chatHeading} {...props} />,
          h5: ({node, ...props}) => <h5 className={styles.chatHeading} {...props} />,
          h6: ({node, ...props}) => <h6 className={styles.chatHeading} {...props} />,
          img: ({node, src, ...props}) => {
            // Fix image paths by prepending baseUrl if needed
            let fixedSrc = src;
            if (src && src.startsWith('/') && baseUrl && !src.startsWith(baseUrl)) {
              fixedSrc = `${baseUrl.replace(/\/$/, '')}${src}`;
            }
            return <img src={fixedSrc} {...props} />;
          }
        }}
      >
        {children}
      </ReactMarkdown>
    );
  }
  return <>{children}</>;
}

// User Message Component with Markdown support
export function UserMessage({ children, baseUrl }: UserMessageProps & { baseUrl?: string }): JSX.Element {
  return (
    <div className={styles.userMessageRow}>
      <div className={styles.userAvatar}>
        <span>👤</span>
      </div>
      <div className={styles.userMessage}>
        <MarkdownContent baseUrl={baseUrl}>{children}</MarkdownContent>
      </div>
    </div>
  );
}

// Assistant Message Component with Markdown support
export function AssistantMessage({ children, baseUrl }: AssistantMessageProps & { baseUrl?: string }): JSX.Element {
  return (
    <div className={styles.messageRow}>
      <div className={styles.assistantAvatar}>
        <span>🤖</span>
      </div>
      <div className={styles.assistantMessage}>
        <MarkdownContent baseUrl={baseUrl}>{children}</MarkdownContent>
      </div>
    </div>
  );
}

// Main Chat Conversation Component
export function ChatConversation({
  children,
  model: initialModel = "Asistente IA",
  date: initialDate = "",
  source
}: ChatConversationProps): JSX.Element {
  const [messages, setMessages] = useState<Message[]>([]);
  const [model, setModel] = useState<string>(initialModel);
  const [date, setDate] = useState<string>(initialDate);
  const [loading, setLoading] = useState<boolean>(Boolean(source));
  const [error, setError] = useState<string | null>(null);
  
  const { siteConfig } = useDocusaurusContext();
  const { colorMode } = useColorMode();
  
  // Use useBaseUrl to properly resolve the source path
  const resolvedUrl = useBaseUrl(source || '');

  useEffect(() => {
    if (!source) return;
    
    async function loadConversation() {
      try {
        // Use the resolved URL from useBaseUrl hook
        const url = source.startsWith('http') ? source : resolvedUrl;
        
        // Fetch the YAML file
        const response = await fetch(url);
        
        if (!response.ok) {
          throw new Error(`Failed to load conversation: ${response.status}`);
        }
        
        const yamlText = await response.text();
        const conversationData = yaml.load(yamlText) as ConversationData;
        
        // Update component state with the loaded data
        if (conversationData.model) setModel(conversationData.model);
        if (conversationData.date) setDate(conversationData.date);
        
        if (Array.isArray(conversationData.messages)) {
          setMessages(conversationData.messages);
        } else {
          throw new Error('Invalid conversation format: messages should be an array');
        }
      } catch (err) {
        const errorMessage = err instanceof Error ? err.message : 'Unknown error';
        setError(errorMessage);
        console.error('Error loading conversation:', err);
      } finally {
        setLoading(false);
      }
    }
    
    loadConversation();
  }, [source, resolvedUrl]);
  
  // Render based on the current state
  if (loading) return <div className={styles.loading}>Loading conversation...</div>;
  if (error) return <div className={styles.error}>Error: {error}</div>;
  
  return (
    <div className={styles.chatContainer}>
      <div className={styles.chatHeader}>
        <div className={styles.modelInfo}>
          <span className={styles.modelName}>{model}</span>
          <span className={styles.chatDate}>{date}</span>
        </div>
      </div>
      <div className={styles.messagesContainer}>
        {messages.length > 0 ? (
          // Render messages from YAML if available
          messages.map((msg, index) => (
            msg.role === 'user' ? (
              <UserMessage key={index} baseUrl={siteConfig.baseUrl}>{msg.content}</UserMessage>
            ) : (
              <AssistantMessage key={index} baseUrl={siteConfig.baseUrl}>{msg.content}</AssistantMessage>
            )
          ))
        ) : (
          // Otherwise render children elements
          children
        )}
      </div>
    </div>
  );
}