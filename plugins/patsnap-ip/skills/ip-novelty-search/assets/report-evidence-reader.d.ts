export function evidenceReaderWord(language: string, key: "title" | "point" | "facts" | "context" | "figure"): string;
export function evidenceIdentity(entry: HTMLElement): { source: string; locator: string };
export function evidencePoint(root: HTMLElement, link: HTMLElement): { title: string; status: string };
export function formatEvidenceParagraphs(container: HTMLElement): void;
export function renderEvidenceReader(modal: HTMLElement, body: HTMLElement, heading: HTMLElement, target: HTMLElement, context: HTMLElement | null, entries: HTMLElement[], language?: string): void;
export function resetComparisonReader(modal: HTMLElement, heading: HTMLElement): void;
export function renderComparisonReader(root: HTMLElement, modal: HTMLElement, body: HTMLElement, heading: HTMLElement, row: HTMLElement, language?: string): boolean;
