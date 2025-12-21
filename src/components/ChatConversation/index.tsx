import React from 'react';
import ReactMarkdown from 'react-markdown';
import rehypeRaw from 'rehype-raw';
import remarkGfm from 'remark-gfm';
import { useColorMode } from '@docusaurus/theme-common';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import { usePluginData } from '@docusaurus/useGlobalData';
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
  const { siteConfig } = useDocusaurusContext();
  const { colorMode } = useColorMode();
  
  // Get chat data from plugin (loaded at build time)
  const chatData = usePluginData('docusaurus-plugin-chat-data') as Record<string, ConversationData>;
  
  // If source is provided, get data from plugin
  let messages: Message[] = [];
  let model = initialModel;
  let date = initialDate;
  
  if (source && chatData) {
    const conversationData = chatData[source];
    
    if (!conversationData) {
      // Chat not found - show error
      return (
        <div className={styles.error}>
          Chat conversation not found: {source}
          <br />
          <small>Available chats: {Object.keys(chatData).join(', ')}</small>
        </div>
      );
    }
    
    // Extract data from loaded conversation
    if (conversationData.model) model = conversationData.model;
    if (conversationData.date) date = conversationData.date;
    if (Array.isArray(conversationData.messages)) {
      messages = conversationData.messages;
    }
  }
  
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
          // Render messages from plugin data
          messages.map((msg, index) => (
            msg.role === 'user' ? (
              <UserMessage key={index} baseUrl={siteConfig.baseUrl}>{msg.content}</UserMessage>
            ) : (
              <AssistantMessage key={index} baseUrl={siteConfig.baseUrl}>{msg.content}</AssistantMessage>
            )
          ))
        ) : (
          // Otherwise render children elements (manual messages)
          children
        )}
      </div>
    </div>
  );
}