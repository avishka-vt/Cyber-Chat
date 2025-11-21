import type { ChatState } from '../utils/constants';

// --- Type Definitions for State Configuration ---

/** Defines the structure of a single button option in a menu state. */
export interface OptionConfig {
  id: number;
  text: string;
  nextState: ChatState;
}

/** Defines the structure of any single chatbot state configuration. */
export interface StateConfig {
  message: string;
  options?: OptionConfig[];
  isInput?: boolean; // True if the state requires the user to type text (e.g., S_2)
}

/** Defines the overall map of all chatbot states. */
export const stateConfigs: Record<string, StateConfig> = {
  S_0: {
    message: 'Please select an option:',
    options: [
      { id: 1, text: 'Access Dedicated Country Information', nextState: 'S_1' },
      { id: 2, text: 'Ask General Cyber Question', nextState: 'S_2' },
      { id: 3, text: 'Exit Chatbot', nextState: 'EXIT' }
    ]
  },
  S_1: {
    message: 'Please select a country to view its dedicated cybersecurity laws and regulatory portals:',
    options: [
      { id: 1, text: 'View Germany Cyber Law & Portals', nextState: 'S_1_1' },
      { id: 2, text: 'View South Korea Cyber Law & Portals', nextState: 'S_1_2' },
      { id: 3, text: 'View New York (USA) Cyber Law & Portals', nextState: 'S_1_3' },
      { id: 4, text: 'Back to Main Menu', nextState: 'S_0' }
    ]
  },
  S_1_1: {
    message: 'You have selected Germany. Choose an option to get official information:',
    options: [
      { id: 1, text: 'Federal IT Security (BSI)', nextState: 'S_1_1_1' },
      { id: 2, text: 'Data Protection (BfDI)', nextState: 'S_1_1_2' },
      { id: 3, text: 'Cybercrime & Law Enforcement (BKA)', nextState: 'S_1_1_3' },
      { id: 4, text: 'Back to Country Menu', nextState: 'S_1' }
    ]
  },
  S_1_1_1: {
    message: `**Bundesamt für Sicherheit in der Informationstechnik (BSI)**
The BSI is the central Cyber Security Agency for the German federal government.
• **Primary Purpose:** Develops technical guidance, standards like IT-Grundschutz, and issues national threat warnings.
• **Official Portal:** https://www.bsi.bund.de/EN/Home/home_node.html
• **Key Feature:** Operates the Cyber-Security-Warning-Ticker for real-time threat status.`,
    options: [
      { id: 1, text: 'Back to Germany Menu', nextState: 'S_1_1' },
      { id: 2, text: 'Back to Main Menu', nextState: 'S_0' }
    ]
  },
  S_1_1_2: {
    message: `**Federal Commissioner for Data Protection (BfDI)**
The BfDI oversees GDPR enforcement and federal data protection oversight in Germany.
• **Primary Purpose:** Ensures compliance with data protection regulations and provides guidance.
• **Official Portal:** https://www.bfdi.bund.de/EN/Home/home_node.html
• **Key Feature:** Independent authority for data protection matters.`,
    options: [
      { id: 1, text: 'Back to Germany Menu', nextState: 'S_1_1' },
      { id: 2, text: 'Back to Main Menu', nextState: 'S_0' }
    ]
  },
  S_1_1_3: {
    message: `**Federal Criminal Police Office (BKA)**
The BKA investigates serious, organized cybercrime in Germany.
• **Primary Purpose:** Law enforcement agency combating cyber threats and digital crimes.
• **Official Portal:** https://www.bka.de/EN/Home/home_node.html
• **Key Feature:** Coordinates national and international cybercrime investigations.`,
    options: [
      { id: 1, text: 'Back to Germany Menu', nextState: 'S_1_1' },
      { id: 2, text: 'Back to Main Menu', nextState: 'S_0' }
    ]
  },
  S_1_2: {
    message: 'You have selected South Korea. Choose an option to get official information:',
    options: [
      { id: 1, text: 'Private Sector & Internet Security (KISA)', nextState: 'S_1_2_1' },
      { id: 2, text: 'Data Protection & PIPA (PIPC)', nextState: 'S_1_2_2' },
      { id: 3, text: 'Financial Sector Security (FSI)', nextState: 'S_1_2_3' },
      { id: 4, text: 'Back to Country Menu', nextState: 'S_1' }
    ]
  },
  S_1_2_1: {
    message: `**Korea Internet & Security Agency (KISA)**
Primary national agency for private-sector cyber and KrCERT/CC.
• **Primary Purpose:** Internet security, KrCERT/CC operations, and private sector protection.
• **Official Portal:** https://www.kisa.or.kr/eng/
• **Key Feature:** Operates Korea's Computer Emergency Response Team.`,
    options: [
      { id: 1, text: 'Back to South Korea Menu', nextState: 'S_1_2' },
      { id: 2, text: 'Back to Main Menu', nextState: 'S_0' }
    ]
  },
  S_1_2_2: {
    message: `**Personal Information Protection Commission (PIPC)**
Independent authority enforcing the Personal Information Protection Act (PIPA).
• **Primary Purpose:** Data protection oversight and PIPA enforcement.
• **Official Portal:** https://www.pipc.go.kr/eng/
• **Key Feature:** South Korea's primary data protection authority.`,
    options: [
      { id: 1, text: 'Back to South Korea Menu', nextState: 'S_1_2' },
      { id: 2, text: 'Back to Main Menu', nextState: 'S_0' }
    ]
  },
  S_1_2_3: {
    message: `**Financial Security Institute (FSI)**
Specialized organization for financial sector security and F-CERT/CC.
• **Primary Purpose:** Protects financial institutions from cyber threats.
• **Official Portal:** https://www.fsec.or.kr/en
• **Key Feature:** Operates Financial CERT for the banking sector.`,
    options: [
      { id: 1, text: 'Back to South Korea Menu', nextState: 'S_1_2' },
      { id: 2, text: 'Back to Main Menu', nextState: 'S_0' }
    ]
  },
  S_1_3: {
    message: 'You have selected New York (USA). Choose an option to get official regulatory and agency information:',
    options: [
      { id: 1, text: 'Financial Regulation (NYS DFS)', nextState: 'S_1_3_1' },
      { id: 2, text: 'NYC Municipal Defense (NYC3)', nextState: 'S_1_3_2' },
      { id: 3, text: 'State-wide Government Defense (NYS ITS)', nextState: 'S_1_3_3' },
      { id: 4, text: 'Back to Country Menu', nextState: 'S_1' }
    ]
  },
  S_1_3_1: {
    message: `**New York State Department of Financial Services (NYS DFS)**
Enforces the landmark 23 NYCRR Part 500 Cybersecurity Regulation.
• **Primary Purpose:** Financial services cybersecurity regulation and enforcement.
• **Official Portal:** https://www.dfs.ny.gov/
• **Key Feature:** Part 500 requires robust cybersecurity programs for financial institutions.`,
    options: [
      { id: 1, text: 'Back to New York Menu', nextState: 'S_1_3' },
      { id: 2, text: 'Back to Main Menu', nextState: 'S_0' }
    ]
  },
  S_1_3_2: {
    message: `**New York City Cyber Command (NYC3)**
Leads cyber defense for all New York City systems and runs the NYC Secure App.
• **Primary Purpose:** Protects NYC government infrastructure from cyber threats.
• **Official Portal:** https://www.nyc.gov/cyber
• **Key Feature:** Coordinates citywide cybersecurity initiatives and incident response.`,
    options: [
      { id: 1, text: 'Back to New York Menu', nextState: 'S_1_3' },
      { id: 2, text: 'Back to Main Menu', nextState: 'S_0' }
    ]
  },
  S_1_3_3: {
    message: `**New York State Information Technology Services (NYS ITS)**
Coordinates policies across all state agencies and manages the NYS Cyber Alert Level.
• **Primary Purpose:** State-wide IT and cybersecurity governance.
• **Official Portal:** https://its.ny.gov/
• **Key Feature:** Manages the NYS Cyber Alert Level system for threat communication.`,
    options: [
      { id: 1, text: 'Back to New York Menu', nextState: 'S_1_3' },
      { id: 2, text: 'Back to Main Menu', nextState: 'S_0' }
    ]
  },
  S_2: {
    message: 'Please type your general cybersecurity question (e.g., "What are the penalties for GDPR non-compliance?" or "How does the NIS2 Directive affect German companies?").',
    isInput: true
  },
  S_3: {
    message: 'I apologize, but I am specifically designed to provide information on global cybersecurity laws, guidelines, and regulatory portals. I cannot answer general knowledge questions. Please rephrase your question to focus on cybersecurity or select an option from the main menu.',
    options: [
      { id: 1, text: 'Return to Main Menu', nextState: 'S_0' },
      { id: 2, text: 'Ask New Cyber Question', nextState: 'S_2' }
    ]
  },
  EXIT: {
    message: 'Thank you for using the Cybersecurity Information Portal. Goodbye!'
  }
};