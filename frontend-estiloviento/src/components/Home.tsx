import { Wind, Github, Upload, Users } from 'lucide-react';
import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { useState, useEffect } from 'react';
import bgVideo from '../assets/bg.mp4';

const taglines = [
  { main: "Trends. Insights. Evolution.", sub: "See beyond the hype, shape the next wave." },
  { main: "Structure. Predict. Lead.", sub: "From raw data to runway predictions." },
  { main: "Analyze. Forecast. Dominate.", sub: "Turn patterns into power, fashion into foresight." },
  { main: "Decode. Design. Innovate.", sub: "Fashion meets intelligence—where ideas take flight." },
  { main: "Fashion. Data. Intelligence.", sub: "Redefining the industry, one insight at a time." }
];

function Home() {
  const [index, setIndex] = useState(0);
  const [displayedText, setDisplayedText] = useState('');

  useEffect(() => {
    let i = 0;
    const interval = setInterval(() => {
      if (i <= taglines[index].main.length) {
        setDisplayedText(taglines[index].main.slice(0, i));
        i++;
      } else {
        clearInterval(interval);
        setTimeout(() => {
          setIndex((prevIndex) => (prevIndex + 1) % taglines.length);
          setDisplayedText('');
        }, 2000);
      }
    }, 100);

    return () => clearInterval(interval);
  }, [index]);

  return (
    <div className="relative min-h-screen overflow-hidden font-serif">
      {/* Video Background with Blur Effect */}
      <div className="absolute inset-0 w-full h-full overflow-hidden">
        <div className="absolute inset-0  z-10" /> {/* Increased blur effect */}
        <video className="w-full h-full object-cover brightness-[75%]" autoPlay loop playsInline muted>
          <source src={bgVideo} type="video/mp4" />
        </video>
      </div>

      {/* Header */}
      <header className="relative z-20 px-6 py-6">
        <nav className="max-w-7xl mx-auto flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <Wind className="h-8 w-8 text-white animate-spin-slow" />
          </div>

          <h1 className="text-4xl font-light tracking-[0.15em] text-white text-center absolute left-1/2 -translate-x-1/2">
            ESTILOVIENTO
          </h1>

          <div className="flex items-center space-x-12">
            {/* GitHub Link */}
            <a 
              href="https://github.com/Aaditatgithub/Automation-of-Knowledge-Graph-Construction"
              target="_blank"
              rel="noopener noreferrer"
              className="text-white hover:text-gray-300 transition relative group"
            >
              <Github className="h-5 w-5 inline mr-1" />
              <span className="underline-effect">View Work</span>
            </a>

            {/* Upload Page Link */}
            <Link
              to="/upload"
              className="text-white hover:text-gray-300 transition relative group"
            >
              <Upload className="h-5 w-5 inline mr-1" />
              <span className="underline-effect">Try It Out</span>
            </Link>

            {/* About Us Page Link with New Icon */}
<Link
  to="/about"
  className="text-white hover:text-gray-300 transition relative group"
>
  <Users className="h-5 w-5 inline mr-1" />  {/* Changed Icon */}
  <span className="underline-effect">About Us</span>
</Link>
          </div>
        </nav>
      </header>

      {/* Main Content with Motion Effects */}
      <main className="relative z-20 flex items-center justify-center min-h-screen overflow-hidden">
        <div className="text-center text-white px-4">
          {/* Animated Tagline */}
          <motion.h2 
            key={index}
            className="text-5xl font-bold mb-4 tracking-wider uppercase"
            initial={{ opacity: 0, scale: 0.8, filter: "blur(5px)" }}
            animate={{ opacity: 1, scale: 1, filter: "blur(0px)" }}
            transition={{ duration: 1 }}
          >
            {displayedText}
          </motion.h2>

          {/* Subtext with Smooth Motion */}
          <motion.p 
            key={`sub-${index}`}
            className="text-lg font-light tracking-wide max-w-2xl mx-auto italic text-gray-300"
            initial={{ opacity: 0, y: 10, filter: "blur(5px)" }}
            animate={{ opacity: 1, y: 0, filter: "blur(0px)" }}
            transition={{ duration: 1.5 }}
          >
            {taglines[index].sub}
          </motion.p>
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