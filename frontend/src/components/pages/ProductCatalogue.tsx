import React from 'react';
import { Database } from 'lucide-react';
import { FileUpload } from '../upload/FileUpload';
import { sendRowToKafka } from '../../services/uploadService';

export function ProductCatalogue() {
  const handleRowUpload = async (row: Record<string, any>, index: number, total: number) => {
    // console.log(`Uploading row ${index} of ${total}`, row);
    await sendRowToKafka(row);
  };

  return (
    <div className="p-6">
      <div className="flex items-center gap-3 mb-6">
        <Database className="w-6 h-6 text-blue-500" />
        <h1 className="text-2xl font-bold">Products Catalogue</h1>
      </div>
      <FileUpload onUpload={handleRowUpload} />
    </div>
  );
}
