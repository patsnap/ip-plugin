/** 挂载只读专利阅读器，关闭弹窗时调用返回的清理函数。 */
export function mountPatentReader(root: HTMLElement, reader: HTMLElement | null): () => void;
