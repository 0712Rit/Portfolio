from flask import Flask, render_template_string

app = Flask(__name__)

template = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Ritam Mallick - Portfolio</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
  <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
  <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Fira+Code&display=swap" rel="stylesheet">
  <style>
    body {
      transition: background 0.6s ease, color 0.6s ease;
      background: linear-gradient(135deg, #01012a, #0f0f3d);
      color: #c0f0ff;
      font-family: 'Fira Code', monospace;
      overflow-x: hidden;
    }
    h1, h2, h3 {
      font-family: 'Orbitron', sans-serif;
    }
    .glass-card {
      background: rgba(158, 255, 0, 0.05);
      backdrop-filter: blur(10px);
      border: 1px solid rgba(158, 255, 0, 0.2);
      border-radius: 1rem;
      padding: 1.5rem;
      transition: all 0.4s ease-in-out;
      animation: fadeInUp 1s ease-in;
    }
    .glass-card:hover {
      transform: translateY(-8px);
      box-shadow: 0 8px 30px rgba(158, 255, 0, 0.5); transform: scale(1.03);
    }
    .nav-link {
      color: #c0f0ff;
      transition: all 0.4s ease-in-out;
    }
    .nav-link:hover {
      color: #9eff00;
      text-shadow: 0 0 5px #9eff00;
    }
    .social-icon:hover {
      transform: scale(1.15);
    }
    #particles-js {
      position: absolute;
      width: 100%;
      height: 100%;
      top: 0;
      left: 0;
      z-index: -1;
    }
    .neon-button {
      background: #9eff00;
      color: #01012a;
      padding: 0.75rem 2rem;
      border-radius: 9999px;
      font-weight: bold;
      transition: all 0.3s;
    }
    .neon-button:hover {
      background: #01012a;
      color: #9eff00;
      box-shadow: 0 0 10px #9eff00, 0 0 30px #9eff00; transform: scale(1.05);
    }
    @keyframes fadeInUp {
      from {opacity: 0; transform: translateY(20px);}
      to {opacity: 1; transform: translateY(0);}
    }
    .dark {
      transition: background 0.6s ease, color 0.6s ease;
      background: linear-gradient(135deg, #ffffff, #dfe6e9);
      color: #01012a;
    }
    .dark .glass-card {
      background: rgba(0, 0, 0, 0.05);
      border-color: rgba(0, 0, 0, 0.1);
    }
    .dark .nav-link:hover {
      color: #01012a;
      text-shadow: none;
    }
    .dark .neon-button {
      background: #01012a;
      color: #9eff00;
    }
    .dark .neon-button:hover {
      background: #9eff00;
      color: #01012a;
      box-shadow: 0 0 10px #01012a, 0 0 20px #01012a;
    }
  </style>
</head>
<body>
  <div id="preloader" class="fixed inset-0 bg-[#01012a] flex items-center justify-center z-50">
    <div class="w-16 h-16 border-4 border-dashed rounded-full animate-spin border-[#9eff00]"></div>
  </div>
  <div id="particles-js"></div>
<!--
  <nav class="fixed top-0 w-full bg-[#01012a] bg-opacity-90 z-50">
    <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between">
      <div class="text-2xl font-bold text-[#9eff00]">RM</div>
      <div class="space-x-6">
        <a href="#about" class="nav-link">About</a>
        <a href="#skills" class="nav-link">Skills</a>
        <a href="#experience" class="nav-link">Experience</a>
        <a href="#projects" class="nav-link">Projects</a>
        <a href="#education" class="nav-link">Education</a>
        <a href="#certifications" class="nav-link">Certifications</a>
        <a href="#achievements" class="nav-link">Achievements</a>
        <a href="#interests" class="nav-link">Interests</a>
        <a href="#contact" class="nav-link">Contact</a>
      </div>
    </div>
  </nav>
-->
  <div class="fixed top-4 right-4 z-50">
    <button id="theme-toggle" class="bg-[#9eff00] text-[#01012a] px-4 py-2 rounded-full font-bold shadow hover:shadow-lg transition">🌗</button>
  </div>

  <section class="min-h-screen flex items-center justify-center text-center px-6">
    <div data-aos="fade-up">
      <h1 class="text-5xl md:text-7xl mb-4 animate-pulse">Ritam Mallick</h1>
      <p id="typewriter" class="text-xl mb-6"></p>
      <a href="#contact" class="neon-button animate-bounce">Let's Connect</a>
    </div>
  </section>

  <section id="about" class="py-20 bg-gradient-to-br from-[#0f0f3d] to-[#01012a] text-[#c0f0ff]">
    <div class="max-w-6xl mx-auto px-6 flex flex-col md:flex-row items-center gap-12">

      <!-- Text content -->
      <div class="md:w-1/2" data-aos="fade-right">
        <h2 class="text-5xl font-bold leading-tight mb-6 text-[#9eff00]"><i class="fas fa-user"></i> Hey, I'm Ritam</h2>
        <p class="text-lg mb-6">
          A <span class="font-semibold text-[#9eff00]">Computer Engineer</span> turned 
          <span class="font-semibold text-[#9eff00]">AI Developer</span> with a love for data and design.
          I build intelligent apps and dashboards that tell stories with numbers.<span class="font-semibold text-[#9eff00]"> My superpower? Translating tech talk into business results.</span>
        </p>
        <ul class="space-y-3 text-base">
          <li><i class="fas fa-code text-[#9eff00] mr-2"></i> Python, ML & Flask developer</li>
          <li><i class="fas fa-chart-line text-[#9eff00] mr-2"></i> Passionate about Business Analytics</li>
          <li><i class="fas fa-rocket text-[#9eff00] mr-2"></i> Fast learner with a passion for AI innovation</li>
        </ul>
        <div class="mt-8 flex gap-4">
          <a href="/static/resume.pdf" download class="neon-button">Download Resume</a>
          <a href="#projects" class="neon-button  border border-[#9eff00] hover:bg-[#9eff00] hover:text-[#01012a] transition">
            View Projects
          </a>
        </div>
      </div>

      <!-- Avatar / Illustration -->
      <div class="md:w-1/2 flex justify-center" data-aos="fade-left">
        <img src="/static/avatar.png" alt="Ritam Mallick" class="w-80 h-80 rounded-full object-cover shadow-xl border-4 border-[#9eff00]">
      </div>

    </div>
  </section>

  <section id="skills" class="py-20 bg-[#0f172a] bg-opacity-50">
    <div class="container mx-auto px-6">
      <h2 class="text-4xl font-bold mb-10 text-center"><i class="fas fa-code"></i> Technical Skills</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div class="glass-card p-6" data-aos="flip-left">
          <h3 class="text-xl mb-4">Programming Languages</h3>
          <ul class="list-disc list-inside">
            <li>Python</li>
            <li>SQL</li>
            <li>HTML</li>
          </ul>
        </div>
        <div class="glass-card p-6" data-aos="flip-left" data-aos-delay="100">
          <h3 class="text-xl mb-4">Frameworks & Libraries</h3>
          <ul class="list-disc list-inside">
            <li>Pandas</li>
            <li>NumPy</li>
            <li>Matplotlib</li>
            <li>Streamlit</li>
            <li>Flask</li>
          </ul>
        </div>
        <div class="glass-card p-6" data-aos="flip-left" data-aos-delay="200">
          <h3 class="text-xl mb-4">Tools</h3>
          <ul class="list-disc list-inside">
            <li>Power BI</li>
            <li>MS Excel</li>
            <li>MySQL</li>
            <li>MS PowerPoint</li>
            <li>IBM Cognos Analytics</li>
          </ul>
        </div>
        <div class="glass-card p-6" data-aos="flip-left" data-aos-delay="300">
          <h3 class="text-xl mb-4">Platforms & Cloud</h3>
          <ul class="list-disc list-inside">
            <li>PyCharm</li>
            <li>Jupyter Notebook</li>
            <li>Google Colab</li>
            <li>Kaggle</li>
            <li>Streamlit Cloud</li>
            <li>IBM Cloud</li>
            <li>GitHub</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section id="experience" class="py-20">
    <div class="container mx-auto px-6">
      <h2 class="text-4xl font-bold mb-10 text-center"><i class="fas fa-briefcase"></i> Work Experience</h2>
      <div class="space-y-8">
        <div class="glass-card p-8" data-aos="fade-left">
          <h3 class="text-xl font-bold">Artificial Intelligence Developer Intern</h3>
          <p class="text-sm text-gray-400">Starapp Solutions, Canada (Remote) • May 2025 – Present</p>
          <ul class="list-disc list-inside mt-4">
            <li>Contributing to 3+ AI-powered web and mobile applications</li>
            <li>Applied machine learning models and integrated APIs to enhance functionality and performance by 30%</li>
          </ul>
        </div>
        <div class="glass-card p-8" data-aos="fade-left" data-aos-delay="100">
          <h3 class="text-xl font-bold">Software Testing Engineer Intern</h3>
          <p class="text-sm text-gray-400">ERTL(E), STQC, MCIT, DIT, Govt of India, Kolkata • Oct 2023 – Apr 2024</p>
          <ul class="list-disc list-inside mt-4">
            <li>Conducted functional testing of e-District Chhattisgarh portal, reducing errors by 30%</li>
            <li>Monitored Integrated eProcurement System with IBM, reducing procurement time by 45%</li>
          </ul>
        </div>
        <div class="glass-card p-8" data-aos="fade-left" data-aos-delay="200">
          <h3 class="text-xl font-bold">Project Management Intern</h3>
          <p class="text-sm text-gray-400">Foruppo, Bangalore (Remote) • Jun 2023 – Aug 2023</p>
          <ul class="list-disc list-inside mt-4">
            <li>Streamlined virtual meetings, reducing prep time by 30%</li>
            <li>Enhanced team coordination, improving outcomes by 15%</li>
          </ul>
        </div>
      </div>
    </div>
  </section>
  <section id="projects" class="py-20 bg-[#0f172a] bg-opacity-50">
  <div class="container mx-auto px-6">
    <h2 class="text-4xl font-bold mb-10 text-center"><i class="fas fa-diagram-project"></i> Featured Projects</h2>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">

      <a href="https://github.com/0712Rit/popcornai" target="_blank" class="relative block group">
        <div class="glass-card p-6 hover:bg-opacity-30 transition" data-aos="zoom-in">
          <h3 class="text-xl mb-2">PopcornAI - Movie Recommendation</h3>
          <ul class="list-disc list-inside">
            <li>85% precision with content-based filtering</li>
            <li>Processed genres into binary features for classification</li>
          </ul>
          <div class="absolute top-4 right-4 opacity-0 group-hover:opacity-100 transition-opacity text-[#9eff00] text-lg">
            <i class="fas fa-link"></i>
          </div>
        </div>
      </a>

      <a href="https://github.com/0712Rit/bigbasket-cart-predictor" target="_blank" class="relative block group">
        <div class="glass-card p-6 hover:bg-opacity-30 transition" data-aos="zoom-in" data-aos-delay="100">
          <h3 class="text-xl mb-2">Big Basket Smart Cart Predictor</h3>
          <ul class="list-disc list-inside">
            <li>Boosted accuracy by 25% using purchase history</li>
          </ul>
          <div class="absolute top-4 right-4 opacity-0 group-hover:opacity-100 transition-opacity text-[#9eff00] text-lg">
            <i class="fas fa-link"></i>
          </div>
        </div>
      </a>

      <a href="https://github.com/0712Rit/sales-dashboard" target="_blank" class="relative block group">
        <div class="glass-card p-6 hover:bg-opacity-30 transition" data-aos="zoom-in" data-aos-delay="200">
          <h3 class="text-xl mb-2">Sales Intelligence Dashboard</h3>
          <ul class="list-disc list-inside">
            <li>Improved forecasting by 25% and optimized inventory by 15%</li>
          </ul>
          <div class="absolute top-4 right-4 opacity-0 group-hover:opacity-100 transition-opacity text-[#9eff00] text-lg">
            <i class="fas fa-link"></i>
          </div>
        </div>
      </a>

      <a href="https://github.com/0712Rit/blinkit-retail-dashboard" target="_blank" class="relative block group">
        <div class="glass-card p-6 hover:bg-opacity-30 transition" data-aos="zoom-in" data-aos-delay="300">
          <h3 class="text-xl mb-2">Blinkit Retail Analytics Dashboard</h3>
          <ul class="list-disc list-inside">
            <li>Increased operational efficiency by 20% through BI visualizations</li>
          </ul>
          <div class="absolute top-4 right-4 opacity-0 group-hover:opacity-100 transition-opacity text-[#9eff00] text-lg">
            <i class="fas fa-link"></i>
          </div>
        </div>
      </a>

    </div>
  </div>
</section>


  <section id="education" class="py-20">
    <div class="container mx-auto px-6">
      <h2 class="text-4xl font-bold mb-10 text-center"><i class="fas fa-graduation-cap"></i> Education</h2>
      <div class="space-y-6">
        <div class="glass-card p-6" data-aos="fade-right">
          <h3 class="text-xl mb-2">PGP + MBA - Business Analytics & Data Science</h3>
          <p class="text-sm text-gray-400">Bengal Institute of Business Studies – VU • 2024 - Present • 80%</p>
        </div>
        <div class="glass-card p-6" data-aos="fade-right" data-aos-delay="100">
          <h3 class="text-xl mb-2">B.Tech - Computer Science & Engineering</h3>
          <p class="text-sm text-gray-400">Haldia Institute of Technology • 2019 - 2023 • 82%</p>
        </div>
        <div class="glass-card p-6" data-aos="fade-right" data-aos-delay="200">
          <h3 class="text-xl mb-2">C.B.S.E – Computer Science</h3>
          <p class="text-sm text-gray-400">DAV Model School, Durgapur • 2019 • 70%</p>
        </div>
      </div>
    </div>
  </section>

  <section id="certifications" class="py-20 bg-[#0f172a] bg-opacity-50">
  <div class="container mx-auto px-6">
    <h2 class="text-4xl font-bold mb-10 text-center"><i class="fas fa-certificate"></i> Professional Certifications</h2>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">

      <a href="https://www.netacad.com/courses/python-essentials-1" target="_blank" class="relative block group">
        <div class="glass-card p-6 hover:bg-opacity-30 transition" data-aos="flip-up">
          <h3 class="text-xl mb-2">Python Essentials I</h3>
          <p class="text-sm text-gray-400">Cisco Networking Academy</p>
          <div class="absolute top-4 right-4 opacity-0 group-hover:opacity-100 transition-opacity text-[#9eff00] text-lg">
            <i class="fas fa-link"></i>
          </div>
        </div>
      </a>

      <a href="https://skillshop.withgoogle.com" target="_blank" class="relative block group">
        <div class="glass-card p-6 hover:bg-opacity-30 transition" data-aos="flip-up" data-aos-delay="100">
          <h3 class="text-xl mb-2">Google Analytics Certification</h3>
          <p class="text-sm text-gray-400">Google Digital Academy (Skillshop)</p>
          <div class="absolute top-4 right-4 opacity-0 group-hover:opacity-100 transition-opacity text-[#9eff00] text-lg">
            <i class="fas fa-link"></i>
          </div>
        </div>
      </a>

      <a href="https://onlinecourses.nptel.ac.in" target="_blank" class="relative block group">
        <div class="glass-card p-6 hover:bg-opacity-30 transition" data-aos="flip-up" data-aos-delay="200">
          <h3 class="text-xl mb-2">Machine Learning with Python</h3>
          <p class="text-sm text-gray-400">E & ICT Academy, IIT Kanpur</p>
          <div class="absolute top-4 right-4 opacity-0 group-hover:opacity-100 transition-opacity text-[#9eff00] text-lg">
            <i class="fas fa-link"></i>
          </div>
        </div>
      </a>

      <a href="https://www.theforage.com" target="_blank" class="relative block group">
        <div class="glass-card p-6 hover:bg-opacity-30 transition" data-aos="flip-up" data-aos-delay="300">
          <h3 class="text-xl mb-2">Deloitte Analytics Job Simulation</h3>
          <p class="text-sm text-gray-400">Forage Platform</p>
          <div class="absolute top-4 right-4 opacity-0 group-hover:opacity-100 transition-opacity text-[#9eff00] text-lg">
            <i class="fas fa-link"></i>
          </div>
        </div>
      </a>

      <a href="https://talentnext.wipro.com" target="_blank" class="relative block group">
        <div class="glass-card p-6 hover:bg-opacity-30 transition" data-aos="flip-up" data-aos-delay="400">
          <h3 class="text-xl mb-2">Wipro Talent Next Program</h3>
          <p class="text-sm text-gray-400">Wipro Technologies</p>
          <div class="absolute top-4 right-4 opacity-0 group-hover:opacity-100 transition-opacity text-[#9eff00] text-lg">
            <i class="fas fa-link"></i>
          </div>
        </div>
      </a>

    </div>
  </div>
</section>

  <section id="achievements" class="py-20">
  <div class="container mx-auto px-6">
    <h2 class="text-4xl font-bold mb-10 text-center"><i class="fas fa-trophy"></i> Notable Achievements</h2>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="glass-card p-6 text-center" data-aos="zoom-in">
        <h3 class="text-xl mb-2">IBM Technovate 2025 Winner</h3>
        <p>Won the technology innovation competition organized by IBM at Bengal Institute of Business Studies.</p>
      </div>
      <div class="glass-card p-6 text-center" data-aos="zoom-in" data-aos-delay="100">
        <h3 class="text-xl mb-2">CSI Leadership</h3>
        <p>Former member of Computer Society of India, organized workshops on AI and Machine Learning.</p>
      </div>
      <div class="glass-card p-6 text-center" data-aos="zoom-in" data-aos-delay="200">
        <h3 class="text-xl mb-2">NCC 'A' Certificate</h3>
        <p>Completed National Cadet Corps training at 10 Bengal Battalion NCC, Asansol.</p>
      </div>
    </div>
  </div>
</section>


  <section id="interests" class="py-20 bg-[#0f172a] bg-opacity-50">
    <div class="container mx-auto px-6">
      <h2 class="text-4xl font-bold mb-10 text-center"><i class="fas fa-heart"></i> Interests</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="glass-card p-6 text-center" data-aos="fade-up">
          <h3 class="text-xl mb-2">Data Enthusiast</h3>
          <p>Passionate about uncovering insights from data and building impactful solutions.</p>
        </div>
        <div class="glass-card p-6 text-center" data-aos="fade-up" data-aos-delay="100">
          <h3 class="text-xl mb-2">Painting</h3>
          <p>Exploring creativity through visual art as a way to balance technical work.</p>
        </div>
        <div class="glass-card p-6 text-center" data-aos="fade-up" data-aos-delay="200">
          <h3 class="text-xl mb-2">Listening to Music</h3>
          <p>Enjoying music to unwind and stay inspired.</p>
        </div>
      </div>
    </div>
  </section>

  <section id="contact" class="py-20">
    <div class="max-w-xl mx-auto px-6 text-center">
      <h2 class="text-4xl mb-6"><i class="fas fa-envelope"></i> Contact</h2>
      <p><i class="fas fa-envelope"></i> Email: rk.rit7@gmail.com</p>
      <p><i class="fas fa-phone"></i> Phone: +91 7098199401</p>
      <div class="flex justify-center mt-4 gap-x-4">
        <a href="mailto:rk.rit7@gmail.com" class="social-icon" title="Email"><i class="fas fa-envelope"></i></a>
        <a href="https://www.linkedin.com/in/iamritam" class="social-icon" target="_blank" title="LinkedIn"><i class="fab fa-linkedin"></i></a>
        <a href="https://github.com/0712Rit" class="social-icon" target="_blank" title="GitHub"><i class="fab fa-github"></i></a>
      </div>
    </div>
  </section>

  <footer class="py-6 text-center">
    <p class="text-sm">© 2025 Ritam Mallick. All rights reserved.</p>
  </footer>

  <script>
    AOS.init({ duration: 1500 });
    particlesJS('particles-js', {
      particles: {
        number: { value: 90 },
        color: { value: '#9eff00' },
        shape: { type: 'circle' },
        opacity: { value: 0.6, random: true },
        size: { value: 3, random: true },
        line_linked: { enable: true, distance: 140, color: '#9eff00', opacity: 0.5, width: 1 },
        move: { enable: true, speed: 4 }
      },
      interactivity: {
        events: { onhover: { enable: true, mode: 'repulse' } },
        modes: { repulse: { distance: 100 } }
      },
      retina_detect: true
    });

    const phrases = ["Computer Engineer", "AI Developer", "Data Enthusiast", "Problem Solver"];
    let currentPhrase = 0, currentChar = 0, isDeleting = false;
    function typeEffect() {
      const element = document.getElementById("typewriter");
      const currentText = phrases[currentPhrase];
      element.innerHTML = isDeleting
        ? currentText.substring(0, currentChar--)
        : currentText.substring(0, currentChar++);
      if (!isDeleting && currentChar === currentText.length + 1) {
        isDeleting = true; setTimeout(typeEffect, 1000);
      } else if (isDeleting && currentChar === 0) {
        isDeleting = false;
        currentPhrase = (currentPhrase + 1) % phrases.length;
        setTimeout(typeEffect, 500);
      } else setTimeout(typeEffect, isDeleting ? 30 : 75);
    }

    window.onload = function () {
      AOS.init({ duration: 1500 });
      typeEffect();
      document.getElementById('preloader').style.display = 'none';
      const toggle = document.getElementById('theme-toggle');
      toggle.addEventListener('click', () => {
        document.body.classList.toggle('dark');
        toggle.innerText = document.body.classList.contains('dark') ? '☀️' : '🌗';
      });
    };
  </script>

</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(template)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
