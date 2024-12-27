export interface UploadProgress {
    fileName: string;
    uploadProgress: number;
    processingStatus: 'pending' | 'uploading' | 'processing' | 'completed' | 'error';
    error?: string;
  }
  
  export interface UploadResponse {
    status: 'success' | 'error';
    message: string;
    processId?: string;
  }