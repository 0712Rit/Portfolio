from flask import Flask, render_template_string
import os

app = Flask(__name__)

# Updated HTML Template with adjusted font color and Montserrat font
template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RM | Ritam Mallick</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Animate.css CDN -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css" rel="stylesheet">
    <!-- Typed.js CDN -->
    <script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.12"></script>
    <!-- Font Awesome CDN -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
    <!-- Particles.js CDN -->
    <script src="https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js"></script>
    <!-- Montserrat Font -->
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        /* Custom Animations */
        @keyframes bounceIn {
            0% { transform: scale(0.3); opacity: 0; }
            50% { transform: scale(1.05); opacity: 1; }
            70% { transform: scale(0.95); }
            100% { transform: scale(1); }
        }
        @keyframes slideInUp {
            from { transform: translateY(50px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        @keyframes pulseGlow {
            0% { box-shadow: 0 0 5px rgba(0, 255, 136, 0.5); }
            50% { box-shadow: 0 0 20px rgba(0, 255, 136, 0.8); }
            100% { box-shadow: 0 0 5px rgba(0, 255, 136, 0.5); }
        }
        @keyframes rotateIn {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
        .animate-bounceIn {
            animation: bounceIn 0.8s ease-out;
        }
        .animate-slideInUp {
            animation: slideInUp 0.8s ease-out;
        }
        .animate-pulseGlow {
            animation: pulseGlow 2s infinite;
        }
        .icon-rotate:hover {
            animation: rotateIn 0.5s ease-out;
        }
        /* Smooth Scroll */
        html {
            scroll-behavior: smooth;
        }
        /* Hover Effects */
        .hover-grow {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .hover-grow:hover {
            transform: translateY(-5px) rotate(2deg) scale(1.03);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.4);
        }
        /* Gradient Background with Overlay */
        body {
            background: linear-gradient(135deg, #4b0082, #00ff88);
            color: #ffffff;
            font-family: 'Montserrat', sans-serif;
            overflow-x: hidden;
            position: relative;
        }
        body::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.1);
            z-index: -2;
        }
        /* Section Styling */
        section {
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(12px);
            border-radius: 1.5rem;
            padding: 2.5rem;
            margin-bottom: 2rem;
            transition: transform 0.5s ease;
        }
        /* Button Styling */
        .custom-btn {
            background: linear-gradient(90deg, #ff00ff, #00ff88);
            padding: 0.75rem 2rem;
            border-radius: 50px;
            font-weight: 700;
            color: #ffffff;
            text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
            transition: background 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
        }
        .custom-btn:hover {
            background: linear-gradient(90deg, #00ff88, #ff00ff);
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.4);
        }
        /* Mobile Navigation */
        .nav-menu {
            transition: max-height 0.5s ease-in-out;
        }
        .nav-menu.hidden {
            max-height: 0;
            overflow: hidden;
        }
        /* Card Styling */
        .card {
            background: rgba(255, 255, 255, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.3);
            border-radius: 1rem;
            padding: 1.5rem;
        }
        /* Text Styling */
        h1, h2, h3 {
            color: #ffffff;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
            font-weight: 700;
        }
        p, li {
            color: #d1d5db;
            text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
        }
        /* Link Hover */
        a:hover {
            color: #22d3ee !important; /* Cyan-300 */
        }
        /* Particles Container */
        #particles-js {
            position: absolute;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            z-index: -1;
        }
    </style>
</head>
<body class="min-h-screen relative">
    <!-- Particles Background for Hero Section -->
    <div id="particles-js"></div>

    <!-- Navigation -->
    <nav class="fixed top-0 w-full bg-opacity-95 bg-gray-900 p-4 z-50">
        <div class="container mx-auto flex justify-between items-center">
            <div class="text-3xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 to-pink-600">RM</div>
            <button class="md:hidden text-white focus:outline-none" onclick="toggleMenu()">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path>
                </svg>
            </button>
            <ul class="nav-menu hidden md:flex md:space-x-6">
                <li><a href="#about" class="hover:text-cyan-300 transition font-semibold"><i class="fas fa-user mr-2"></i>About</a></li>
                <li><a href="#skills" class="hover:text-cyan-300 transition font-semibold"><i class="fas fa-code mr-2"></i>Skills</a></li>
                <li><a href="#experience" class="hover:text-cyan-300 transition font-semibold"><i class="fas fa-briefcase mr-2"></i>Experience</a></li>
                <li><a href="#projects" class="hover:text-cyan-300 transition font-semibold"><i class="fas fa-project-diagram mr-2"></i>Projects</a></li>
                <li><a href="#education" class="hover:text-cyan-300 transition font-semibold"><i class="fas fa-graduation-cap mr-2"></i>Education</a></li>
                <li><a href="#certifications" class="hover:text-cyan-300 transition font-semibold"><i class="fas fa-certificate mr-2"></i>Certifications</a></li>
                <li><a href="#achievements" class="hover:text-cyan-300 transition font-semibold"><i class="fas fa-trophy mr-2"></i>Achievements</a></li>
                <li><a href="#interests" class="hover:text-cyan-300 transition font-semibold"><i class="fas fa-heart mr-2"></i>Interests</a></li>
            </ul>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="min-h-screen flex items-center justify-center text-center pt-20 relative">
        <div class="animate-bounceIn z-10">
            <h1 class="text-5xl md:text-6xl font-extrabold mb-4 text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 to-pink-600">Ritam Mallick</h1>
            <p class="text-xl md:text-2xl mb-6"><span id="typed"></span></p>
            <div class="flex flex-wrap justify-center gap-4 md:gap-6">
                <a href="tel:+917098199401" class="text-lg hover:text-cyan-300 transition"><i class="fas fa-phone-alt mr-2 icon-rotate"></i>+91 7098199401</a>
                <a href="mailto:rk.rit7@gmail.com" class="text-lg hover:text-cyan-300 transition"><i class="fas fa-envelope mr-2 icon-rotate"></i>rk.rit7@gmail.com</a>
                <a href="https://linkedin.com/iamritam" class="text-lg hover:text-cyan-300 transition"><i class="fab fa-linkedin mr-2 icon-rotate"></i>LinkedIn</a>
                <a href="https://github.com/0712Rit" class="text-lg hover:text-cyan-300 transition"><i class="fab fa-github mr-2 icon-rotate"></i>GitHub</a>
            </div>
            <a href="static/resume.pdf" class="custom-btn mt-8 inline-block animate-pulseGlow"><i class="fas fa-file-alt mr-2"></i>Resume</a>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="container mx-auto animate-slideInUp">
        <h2 class="text-4xl font-bold mb-6 text-center"><i class="fas fa-user-circle mr-2"></i>About Me</h2>
        <p class="text-lg mb-6 text-center max-w-2xl mx-auto">Hi, I am Ritam, a fresh Computer Science graduate with hands-on data skills and an eye for business impact. Currently pursuing an MBA in Business Analytics to transform numbers into compelling stories.</p>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
            <div class="card hover-grow animate__animated animate__fadeIn">
                <h3 class="text-xl font-semibold"><i class="fas fa-brain mr-2 icon-rotate"></i>Analytical & Problem Solving</h3>
                <p>I break down complex problems, connect the dots, and engineer smart solutions.</p>
            </div>
            <div class="card hover-grow animate__animated animate__fadeIn" style="animation-delay: 0.2s;">
                <h3 class="text-xl font-semibold"><i class="fas fa-rocket mr-2 icon-rotate"></i>Quick Learner</h3>
                <p>Adaptable to new technologies and methodologies.</p>
            </div>
            <div class="card hover-grow animate__animated animate__fadeIn" style="animation-delay: 0.4s;">
                <h3 class="text-xl font-semibold"><i class="fas fa-comments mr-2 icon-rotate"></i>Data Enthusiast</h3>
                <p>Just a data nerd on a mission to decode the matrix..</p>
            </div>
        </div>
    </section>

    <!-- Skills Section -->
    <section id="skills" class="container mx-auto animate-slideInUp">
        <h2 class="text-4xl font-bold mb-6 text-center"><i class="fas fa-laptop-code mr-2"></i>Technical Skills</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
            <div class="card hover-grow animate__animated animate__fadeIn">
                <h3 class="text-xl font-semibold"><i class="fas fa-code mr-2"></i>Programming Languages</h3>
                <ul class="list-disc pl-5">
                    <li><i class="fab fa-python mr-2 icon-rotate"></i>Python</li>
                    <li><i class="fas fa-database mr-2 icon-rotate"></i>SQL</li>
                    <li><i class="fab fa-html5 mr-2 icon-rotate"></i>HTML</li>
                </ul>
            </div>
            <div class="card hover-grow animate__animated animate__fadeIn" style="animation-delay: 0.2s;">
                <h3 class="text-xl font-semibold"><i class="fas fa-cogs mr-2"></i>Frameworks & Libraries</h3>
                <ul class="list-disc pl-5">
                    <li><i class="fas fa-table mr-2 icon-rotate"></i>Pandas</li>
                    <li><i class="fas fa-calculator mr-2 icon-rotate"></i>NumPy</li>
                    <li><i class="fas fa-chart-line mr-2 icon-rotate"></i>Matplotlib</li>
                    <li><i class="fas fa-stream mr-2 icon-rotate"></i>Streamlit</li>
                    <li><i class="fas fa-flask mr-2 icon-rotate"></i>Flask</li>
                </ul>
            </div>
            <div class="card hover-grow animate__animated animate__fadeIn" style="animation-delay: 0.4s;">
                <h3 class="text-xl font-semibold"><i class="fas fa-tools mr-2"></i>Tools</h3>
                <ul class="list-disc pl-5">
                    <li><i class="fas fa-chart-bar mr-2 icon-rotate"></i>Power BI</li>
                    <li><i class="fas fa-file-excel mr-2 icon-rotate"></i>MS Excel</li>
                    <li><i class="fas fa-database mr-2 icon-rotate"></i>MySQL</li>
                    <li><i class="fas fa-file-powerpoint mr-2 icon-rotate"></i>MS PowerPoint</li>
                    <li><i class="fas fa-chart-pie mr-2 icon-rotate"></i>IBM Cognos Analytics</li>
                </ul>
            </div>
            <div class="card hover-grow animate__animated animate__fadeIn" style="animation-delay: 0.6s;">
                <h3 class="text-xl font-semibold"><i class="fas fa-cloud mr-2"></i>Platforms & Cloud</h3>
                <ul class="list-disc pl-5">
                    <li><i class="fas fa-code-branch mr-2 icon-rotate"></i>PyCharm</li>
                    <li><i class="fas fa-book-open mr-2 icon-rotate"></i>Jupyter Notebook</li>
                    <li><i class="fab fa-google mr-2 icon-rotate"></i>Google Collabs</li>
                    <li><i class="fas fa-kaggle mr-2 icon-rotate"></i>Kaggle</li>
                    <li><i class="fas fa-cloud-upload-alt mr-2 icon-rotate"></i>Streamlit Cloud</li>
                    <li><i class="fas fa-cloud mr-2 icon-rotate"></i>IBM Cloud</li>
                    <li><i class="fab fa-github mr-2 icon-rotate"></i>GitHub</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- Experience Section -->
    <section id="experience" class="container mx-auto animate-slideInUp">
        <h2 class="text-4xl font-bold mb-6 text-center"><i class="fas fa-briefcase mr-2"></i>Work Experience</h2>
        <div class="space-y-6">
            <div class="card hover-grow animate__animated animate__fadeIn">
                <h3 class="text-xl font-semibold"><i class="fas fa-robot mr-2 icon-rotate"></i>Artificial Intelligence Developer Intern</h3>
                <p class="text-gray-400">Starapp Solutions, Canada (Remote) • May 2025 – Present</p>
                <ul class="list-disc pl-5">
                    <li><i class="fas fa-check-circle mr-2"></i>Contributing to 3+ AI-powered web and mobile applications</li>
                    <li><i class="fas fa-check-circle mr-2"></i>Applied machine learning models and integrated APIs to enhance functionality and performance by 30%</li>
                </ul>
            </div>
            <div class="card hover-grow animate__animated animate__fadeIn" style="animation-delay: 0.2s;">
                <h3 class="text-xl font-semibold"><i class="fas fa-vial mr-2 icon-rotate"></i>Software Testing Engineer Intern</h3>
                <p class="text-gray-400">ERTL(E), STQC, MCIT, DIT, Govt of India, Kolkata • October 2023 – April 2024</p>
                <ul class="list-disc pl-5">
                    <li><i class="fas fa-check-circle mr-2"></i>Conducted functional testing of e-District Chhattisgarh portal, reducing errors by 30% and increasing user satisfaction by 25%</li>
                    <li><i class="fas fa-check-circle mr-2"></i>Monitored Integrated eProcurement System with IBM, reducing procurement time by 45% and costs by 20%</li>
                </ul>
            </div>
            <div class="card hover-grow animate__animated animate__fadeIn" style="animation-delay: 0.4s;">
                <h3 class="text-xl font-semibold"><i class="fas fa-tasks mr-2 icon-rotate"></i>Project Management Intern</h3>
                <p class="text-gray-400">Foruppo, Bangalore (Remote) • June 2023 – August 2023</p>
                <ul class="list-disc pl-5">
                    <li><i class="fas fa-check-circle mr-2"></i>Streamlined virtual meeting processes, reducing preparation time by 30% and increasing collaboration by 25%</li>
                    <li><i class="fas fa-check-circle mr-2"></i>Enhanced team coordination, improving project outcomes by 15% and team morale by 20%</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="container mx-auto animate-slideInUp">
        <h2 class="text-4xl font-bold mb-6 text-center"><i class="fas fa-project-diagram mr-2"></i>Featured Projects</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
            <div class="card hover-grow animate__animated animate__fadeIn">
                <h3 class="text-xl font-semibold"><i class="fas fa-film mr-2 icon-rotate"></i>PopcornAI - Movie Recommendation Engine</h3>
                <p class="text-gray-400">Python • Pandas • NumPy • Matplotlib • Seaborn</p>
                <ul class="list-disc pl-5">
                    <li><i class="fas fa-check-circle mr-2"></i>Improved content-based recommender system by 25% using Multinomial Naive Bayes</li>
                    <li><i class="fas fa-check-circle mr-2"></i>Processed movie metadata and user ratings, transforming genres into binary features</li>
                    <li><i class="fas fa-check-circle mr-2"></i>Achieved 85% precision and 80% recall in movie classification</li>
                    <li><i class="fas fa-check-circle mr-2"></i>Increased user engagement by 30% with personalized recommendations</li>
                </ul>
            </div>
            <div class="card hover-grow animate__animated animate__fadeIn" style="animation-delay: 0.2s;">
                <h3 class="text-xl font-semibold"><i class="fas fa-shopping-cart mr-2 icon-rotate"></i>Big Basket Smart Cart Predictor</h3>
                <p class="text-gray-400">Python • Pandas • NumPy • Matplotlib • Seaborn</p>
                <ul class="list-disc pl-5">
                    <li><i class="fas fa-check-circle mr-2"></i>Developed a recommendation system to predict cart items, improving accuracy by 25%</li>
                    <li><i class="fas fa-check-circle mr-2"></i>Processed product data, integrating user purchase history for efficient feature extraction</li>
                    <li><i class="fas fa-check-circle mr-2"></i>Achieved 85% precision and 80% recall in product recommendations</li>
                    <li><i class="fas fa-check-circle mr-2"></i>Enhanced user shopping experience by 30% with tailored suggestions</li>
                </ul>
            </div>
            <div class="card hover-grow animate__animated animate__fadeIn" style="animation-delay: 0.4s;">
                <h3 class="text-xl font-semibold"><i class="fas fa-chart-line mr-2 icon-rotate"></i>Sales Intelligence Dashboard</h3>
                <p class="text-gray-400">Excel • Power BI</p>
                <ul class="list-disc pl-5">
                    <li><i class="fas fa-check-circle mr-2"></i>Improved sales forecasting accuracy by 25%, enabling data-driven decisions</li>
                    <li><i class="fas fa-check-circle mr-2"></i>Identified 10% year-over-year sales decline, prompting strategic adjustments</li>
                    <li><i class="fas fa-check-circle mr-2"></i>Reduced inventory costs by 15% through optimized resource allocation</li>
                    <li><i class="fas fa-check-circle mr-2"></i>Increased sales by 30% during peak seasons via seasonality insights</li>
                </ul>
            </div>
            <div class="card hover-grow animate__animated animate__fadeIn" style="animation-delay: 0.6s;">
                <h3 class="text-xl font-semibold"><i class="fas fa-tachometer-alt mr-2 icon-rotate"></i>Blinkit Retail Analytics Dashboard</h3>
                <p class="text-gray-400">Power BI • DAX • Data Modeling</p>
                <ul class="list-disc pl-5">
                    <li><i class="fas fa-check-circle mr-2"></i>Designed interactive dashboard to analyze retail metrics, improving decision-making</li>
                    <li><i class="fas fa-check-circle mr-2"></i>Utilized DAX for advanced calculations, enhancing data insights</li>
                    <li><i class="fas fa-check-circle mr-2"></i>Created visualizations to track sales and inventory trends</li>
                    <li><i class="fas fa-check-circle mr-2"></i>Increased operational efficiency by 20% through actionable insights</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- Education Section -->
    <section id="education" class="container mx-auto animate-slideInUp">
        <h2 class="text-4xl font-bold mb-6 text-center"><i class="fas fa-graduation-cap mr-2"></i>Education</h2>
        <div class="space-y-6">
            <div class="card hover-grow animate__animated animate__fadeIn">
                <h3 class="text-xl font-semibold"><i class="fas fa-university mr-2 icon-rotate"></i>PGP + MBA - Business Analytics & Data Science</h3>
                <p class="text-gray-400">Bengal Institute of Business Studies – VU • 2024 - Present • 80%</p>
            </div>
            <div class="card hover-grow animate__animated animate__fadeIn" style="animation-delay: 0.2s;">
                <h3 class="text-xl font-semibold"><i class="fas fa-university mr-2 icon-rotate"></i>B.Tech - Computer Science & Engineering</h3>
                <p class="text-gray-400">Haldia Institute of Technology • 2019 - 2023 • 82%</p>
            </div>
            <div class="card hover-grow animate__animated animate__fadeIn" style="animation-delay: 0.4s;">
                <h3 class="text-xl font-semibold"><i class="fas fa-school mr-2 icon-rotate"></i>C.B.S.E – Computer Science</h3>
                <p class="text-gray-400">DAV Model School, Durgapur • 2019 • 70%</p>
            </div>
        </div>
    </section>

    <!-- Certifications Section -->
    <section id="certifications" class="container mx-auto animate-slideInUp">
        <h2 class="text-4xl font-bold mb-6 text-center"><i class="fas fa-certificate mr-2"></i>Professional Certifications</h2>
        <div class="space-y-6">
            <div class="card hover-grow animate__animated animate__fadeIn">
                <h3 class="text-xl font-semibold"><i class="fab fa-python mr-2 icon-rotate"></i>Python Essentials I</h3>
                <p class="text-gray-400">Cisco Networking Academy</p>
                <p>Python programming fundamentals covering syntax, data structures, and object-oriented programming.</p>
            </div>
            <div class="card hover-grow animate__animated animate__fadeIn" style="animation-delay: 0.2s;">
                <h3 class="text-xl font-semibold"><i class="fab fa-google mr-2 icon-rotate"></i>Google Analytics Certification</h3>
                <p class="text-gray-400">Google Digital Academy (Skillshop)</p>
                <p>Web analytics, data interpretation, and digital marketing insights using Google Analytics.</p>
            </div>
            <div class="card hover-grow animate__animated animate__fadeIn" style="animation-delay: 0.4s;">
                <h3 class="text-xl font-semibold"><i class="fas fa-robot mr-2 icon-rotate"></i>Machine Learning with Python</h3>
                <p class="text-gray-400">E & ICT Academy, IIT Kanpur</p>
                <p>Advanced machine learning concepts using Python libraries for data science applications.</p>
            </div>
            <div class="card hover-grow animate__animated animate__fadeIn" style="animation-delay: 0.6s;">
                <h3 class="text-xl font-semibold"><i class="fas fa-chart-bar mr-2 icon-rotate"></i>Deloitte Analytics Job Simulation</h3>
                <p class="text-gray-400">Forage Platform</p>
                <p>Data analysis simulation covering business intelligence, data visualization, and strategic insights.</p>
            </div>
            <div class="card hover-grow animate__animated animate__fadeIn" style="animation-delay: 0.8s;">
                <h3 class="text-xl font-semibold"><i class="fab fa-java mr-2 icon-rotate"></i>Wipro Talent Next Program</h3>
                <p class="text-gray-400">Wipro Technologies</p>
                <p>Secured 71% aggregate in JAVA Enterprise J2EE (Advanced Java) completing 3 milestones.</p>
            </div>
        </div>
    </section>

    <!-- Achievements Section -->
    <section id="achievements" class="container mx-auto animate-slideInUp">
        <h2 class="text-4xl font-bold mb-6 text-center"><i class="fas fa-trophy mr-2"></i>Notable Achievements</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
            <div class="card hover-grow animate__animated animate__fadeIn">
                <h3 class="text-xl font-semibold"><i class="fas fa-medal mr-2 icon-rotate"></i>IBM Technovate 2025 Winner</h3>
                <p>Won the technology innovation competition organized by IBM at Bengal Institute of Business Studies.</p>
            </div>
            <div class="card hover-grow animate__animated animate__fadeIn" style="animation-delay: 0.2s;">
                <h3 class="text-xl font-semibold"><i class="fas fa-users mr-2 icon-rotate"></i>CSI Leadership</h3>
                <p>Former member of Computer Society of India, organized workshops on AI and Machine Learning.</p>
            </div>
            <div class="card hover-grow animate__animated animate__fadeIn" style="animation-delay: 0.4s;">
                <h3 class="text-xl font-semibold"><i class="fas fa-shield-alt mr-2 icon-rotate"></i>NCC 'A' Certificate</h3>
                <p>Completed National Cadet Corps training at 10 Bengal Battalion NCC, Asansol.</p>
            </div>
        </div>
    </section>

    <!-- Interests Section -->
    <section id="interests" class="container mx-auto animate-slideInUp">
        <h2 class="text-4xl font-bold mb-6 text-center"><i class="fas fa-heart mr-2"></i>Interests</h2>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-6">
            <div class="card hover-grow animate__animated animate__fadeIn">
                <h3 class="text-xl font-semibold"><i class="fas fa-chart-bar mr-2 icon-rotate"></i>Data Enthusiast</h3>
                <p>Passionate about uncovering insights from data and building impactful solutions.</p>
            </div>
            <div class="card hover-grow animate__animated animate__fadeIn" style="animation-delay: 0.2s;">
                <h3 class="text-xl font-semibold"><i class="fas fa-paint-brush mr-2 icon-rotate"></i>Painting</h3>
                <p>Exploring creativity through visual art as a way to balance technical work.</p>
            </div>
            <div class="card hover-grow animate__animated animate__fadeIn" style="animation-delay: 0.4s;">
                <h3 class="text-xl font-semibold"><i class="fas fa-music mr-2 icon-rotate"></i>Listening to Songs</h3>
                <p>Enjoying music to unwind and stay inspired.</p>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-gray-900 py-6 text-center">
        <p class="text-gray-300">© 2025 Ritam Mallick. All rights reserved.</p>
    </footer>

    <!-- Scripts -->
    <script>
        // Mobile Menu Toggle
        function toggleMenu() {
            const menu = document.querySelector('.nav-menu');
            menu.classList.toggle('hidden');
            menu.classList.toggle('max-h-screen');
        }

        // Typed.js for Hero Section
        var typed = new Typed('#typed', {
            strings: ['Data Analyst', 'AI Developer', 'Problem Solver'],
            typeSpeed: 50,
            backSpeed: 30,
            backDelay: 1000,
            loop: true
        });

        // Scroll Animations
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate__animated', 'animate__fadeInUp');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });

        document.querySelectorAll('section, .card').forEach(el => {
            observer.observe(el);
        });

        // Particles.js Configuration
        particlesJS('particles-js', {
            particles: {
                number: { value: 80, density: { enable: true, value_area: 800 } },
                color: { value: '#ffffff' },
                shape: { type: 'circle' },
                opacity: { value: 0.5, random: true },
                size: { value: 3, random: true },
                line_linked: { enable: true, distance: 150, color: '#ffffff', opacity: 0.4, width: 1 },
                move: { enable: true, speed: 3, direction: 'none', random: true, out_mode: 'out' }
            },
            interactivity: {
                detect_on: 'canvas',
                events: { onhover: { enable: true, mode: 'repulse' }, onclick: { enable: true, mode: 'push' }, resize: true },
                modes: { repulse: { distance: 100, duration: 0.4 }, push: { particles_nb: 4 } }
            },
            retina: true
        });
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(template)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)