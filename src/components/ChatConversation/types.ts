export interface Message {
    role: 'user' | 'assistant';
    content: string;
  }
  
  export interface ConversationData {
    model: string;
    date: string;
    messages: Message[];
  }
  
  export interface ChatConversationProps {
    children?: React.ReactNode;
    model?: string;
    date?: string;
    source?: string;
  }
  
  export interface UserMessageProps {
    children: React.ReactNode;
  }
  
  export interface AssistantMessageProps {
    children: React.ReactNode;
  }