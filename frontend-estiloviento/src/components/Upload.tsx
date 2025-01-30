import { Link } from 'react-router-dom';
import { Wind, ArrowLeft, Upload as UploadIcon } from 'lucide-react';
import { FileUpload } from '../upload-uilities/FileUpload';
import { sendRowToKafka } from '../services/uploadService';

function Upload() {
  return (
    <div className="min-h-screen bg-gray-900">
      {/* Header */}
      <header className="px-6 py-4 bg-transparent">
        <nav className="max-w-7xl mx-auto flex items-center justify-between">
          <Link to="/" className="flex items-center space-x-2 text-white">
            <ArrowLeft className="h-6 w-6" />
            <span>Back</span>
          </Link>
          
          <div className="flex items-center space-x-2">
            <Wind className="h-8 w-8 text-white" />
            <h1 className="text-2xl font-light tracking-[0.2em] text-white">
              ESTILOVIENTO
            </h1>
          </div>
          <div className="w-24" /> {/* Spacer for alignment */}
        </nav>
      </header>

      {/* Main Content */}
      <main className="max-w-4xl mx-auto px-4 py-16">
        <FileUpload onUpload={sendRowToKafka} />
      </main>
    </div>
  );
}

export default Upload;
