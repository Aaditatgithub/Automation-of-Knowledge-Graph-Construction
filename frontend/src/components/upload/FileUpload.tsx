import React, { useState } from 'react';
import Papa from 'papaparse'; // To parse CSV
import { Upload, CheckCircle, AlertCircle, Loader2 } from 'lucide-react';
import { UploadProgress } from '../../types/upload';

interface FileUploadProps {
  onUpload: (row: Record<string, any>, index: number, total: number) => Promise<void>;
}

export function FileUpload({ onUpload }: FileUploadProps) {
  const [dragActive, setDragActive] = useState(false);
  const [uploadProgress, setUploadProgress] = useState<UploadProgress | null>(null);

  const handleDrag = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === 'dragenter' || e.type === 'dragover') {
      setDragActive(true);
    } else if (e.type === 'dragleave') {
      setDragActive(false);
    }
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);

    const file = e.dataTransfer.files?.[0];
    if (file?.type === 'text/csv') {
      handleFile(file);
    } else {
      setUploadProgress({
        fileName: file?.name || 'Unknown file',
        uploadProgress: 0,
        processingStatus: 'error',
        error: 'Only CSV files are supported',
      });
    }
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) handleFile(file);
  };

  const handleFile = async (file: File) => {
    setUploadProgress({
      fileName: file.name,
      uploadProgress: 0,
      processingStatus: 'uploading',
    });

    Papa.parse(file, {
      header: true, // Parse rows into objects
      skipEmptyLines: true,
      complete: async (results) => {
        const rows = results.data;
        const totalRows = rows.length;

        for (let i = 0; i < totalRows; i++) {
          try {
            const rowWithDomain = { ...rows[i], domain: file.name };
            await onUpload(rowWithDomain, i + 1, totalRows);
            setUploadProgress({
              fileName: file.name,
              uploadProgress: Math.round(((i + 1) / totalRows) * 100),
              processingStatus: i + 1 === totalRows ? 'completed' : 'uploading',
            });
          } catch (error) {
            console.error('Error uploading row:', error);
            setUploadProgress({
              fileName: file.name,
              uploadProgress: Math.round((i / totalRows) * 100),
              processingStatus: 'error',
              error: `Error uploading row ${i + 1}: ${error.message}`,
            });
            return;
          }
        }
      },
      error: (error) => {
        console.error('Error parsing CSV:', error);
        setUploadProgress({
          fileName: file.name,
          uploadProgress: 0,
          processingStatus: 'error',
          error: 'Error parsing CSV file.',
        });
      },
    });
  };

  return (
    <div className="mb-8">
      <div
        className={`relative border-2 border-dashed rounded-lg p-8 text-center transition-colors
          ${dragActive ? 'border-blue-500 bg-blue-50' : 'border-gray-300'}
          ${uploadProgress?.processingStatus === 'completed' ? 'border-green-500 bg-green-50' : ''}
          ${uploadProgress?.processingStatus === 'error' ? 'border-red-500 bg-red-50' : ''}`}
        onDragEnter={handleDrag}
        onDragLeave={handleDrag}
        onDragOver={handleDrag}
        onDrop={handleDrop}
      >
        <input
          type="file"
          accept=".csv"
          onChange={handleChange}
          className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
          disabled={uploadProgress?.processingStatus === 'uploading'}
        />
        <div className="flex flex-col items-center gap-2">
          {!uploadProgress && (
            <>
              <Upload className="w-8 h-8 text-gray-400" />
              <p className="text-gray-600">Drag and drop your CSV file here or click to browse</p>
              <p className="text-sm text-gray-500">Supported format: CSV</p>
            </>
          )}

          {uploadProgress?.processingStatus === 'uploading' && (
            <>
              <Loader2 className="w-8 h-8 text-blue-500 animate-spin" />
              <p className="text-blue-600">Uploading: {uploadProgress.uploadProgress}%</p>
              <div className="w-full max-w-xs h-2 bg-gray-200 rounded-full overflow-hidden">
                <div
                  className="h-full bg-blue-500 transition-all duration-300"
                  style={{ width: `${uploadProgress.uploadProgress}%` }}
                />
              </div>
            </>
          )}

          {uploadProgress?.processingStatus === 'completed' && (
            <>
              <CheckCircle className="w-8 h-8 text-green-500" />
              <p className="text-green-600">File uploaded successfully!</p>
            </>
          )}

          {uploadProgress?.processingStatus === 'error' && (
            <>
              <AlertCircle className="w-8 h-8 text-red-500" />
              <p className="text-red-600">
                {uploadProgress.error || 'Error uploading file. Please try again.'}
              </p>
            </>
          )}
        </div>
      </div>
    </div>
  );
}
