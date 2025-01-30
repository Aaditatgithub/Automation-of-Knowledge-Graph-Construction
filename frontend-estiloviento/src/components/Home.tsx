import { Wind, Github, Upload } from 'lucide-react';
import { Link } from 'react-router-dom';
import bgVideo from '../assets/bg.mp4';

function Home() {
  return (
    <div className="relative min-h-screen overflow-hidden font-serif">
      {/* Video Background */}
      <div className="absolute inset-0 w-full h-full overflow-hidden">
        <div className="absolute inset-0 bg-black/30 z-10" /> {/* Reduced Dark Overlay for better visibility */}
        <video
          className="w-full h-full object-cover"
          autoPlay
          loop
          playsInline
        >
          <source src={bgVideo} type="video/mp4" />
        </video>
      </div>

      {/* Header */}
      <header className="relative z-20 px-6 py-6">
        <nav className="max-w-7xl mx-auto flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <Wind className="h-8 w-8 text-white" />
          </div>

          <h1 className="text-4xl font-light tracking-[0.15em] text-white text-center absolute left-1/2 -translate-x-1/2">
            ESTILOVIENTO
          </h1>

          <div className="flex items-center space-x-12">
            <a 
              href="https://github.com/Aaditatgithub/Automation-of-Knowledge-Graph-Construction"
              target="_blank"
              rel="noopener noreferrer"
              className="text-white hover:text-gray-300 transition relative group"
            >
              <Github className="h-5 w-5 inline mr-1" />
              <span className="underline-effect">View Work</span>
            </a>
            <Link
              to="/upload"
              className="text-white hover:text-gray-300 transition relative group"
              onClick={(e) => {
                e.preventDefault();
                window.location.href = '/upload';
              }}
            >
              <Upload className="h-5 w-5 inline mr-1" />
              <span className="underline-effect">Try It Out</span>
            </Link>
          </div>
        </nav>
      </header>

      {/* Main Content */}
      <main className="relative z-20 flex items-center justify-center min-h-screen overflow-hidden">
        <div className="text-center text-white px-4">
          <h2 className="text-5xl font-light mb-6 tracking-wider uppercase">
            Mini Dolcevita
          </h2>
          <p className="text-lg font-light tracking-wide max-w-2xl mx-auto italic">
            Experience the next generation of knowledge graph construction
          </p>
        </div>
      </main>

      {/* Tailwind Custom Styles */}
      <style>{`
        html, body {
          overflow: hidden;
        }
        .underline-effect {
          position: relative;
        }
        .underline-effect::after {
          content: '';
          position: absolute;
          left: 0;
          bottom: -3px;
          width: 0;
          height: 2px;
          background-color: white;
          transition: width 0.3s ease-in-out;
        }
        .underline-effect:hover::after {
          width: 100%;
        }
      `}</style>
    </div>
  );
}

export default Home;
