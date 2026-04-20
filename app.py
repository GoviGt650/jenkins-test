from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
  <title>GOVIND // NEO-SYNTHESIS CORE</title>
  <!-- Fonts: Space Grotesk + Inter -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,600;14..32,700;14..32,800&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
  <!-- Font Awesome 6 -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">
  <!-- Typed.js -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/typed.js/2.0.11/typed.min.js"></script>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      background-color: #03050b;
      font-family: 'Inter', sans-serif;
      color: #eef5ff;
      overflow-x: hidden;
      line-height: 1.5;
      cursor: none;
    }

    /* animated grain overlay */
    .noise::before {
      content: "";
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: repeating-radial-gradient(circle at 20% 30%, rgba(0, 20, 40, 0.2) 0px, rgba(10, 30, 55, 0.15) 2px, transparent 3px);
      pointer-events: none;
      z-index: 5;
      opacity: 0.5;
      mix-blend-mode: overlay;
    }

    /* custom cursor futuristic */
    .cursor-follower {
      width: 32px;
      height: 32px;
      border: 2px solid #0ef;
      border-radius: 50%;
      position: fixed;
      pointer-events: none;
      z-index: 9999;
      transition: 0.08s linear;
      transform: translate(-50%, -50%);
      backdrop-filter: invert(0.2);
      mix-blend-mode: difference;
      opacity: 0.7;
    }
    @media (max-width: 768px) { .cursor-follower { display: none; } body { cursor: auto; } }

    /* glitch effect */
    .glitch {
      font-weight: 800;
      position: relative;
      text-shadow: 0.05em 0 0 rgba(255, 0, 100, 0.6), -0.05em -0.025em 0 rgba(0, 255, 255, 0.6);
      animation: glitch-shake 0.3s infinite alternate;
    }
    @keyframes glitch-shake {
      0% { transform: translate(0); }
      100% { transform: translate(-0.5px, 0.8px); }
    }

    .main-container {
      max-width: 1400px;
      margin: 0 auto;
      padding: 2rem 4rem;
      position: relative;
      z-index: 10;
    }

    /* glass morphism panels */
    .glass-panel {
      background: rgba(12, 20, 35, 0.38);
      backdrop-filter: blur(14px);
      border-radius: 2.5rem;
      border: 1px solid rgba(0, 255, 255, 0.25);
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4), inset 0 1px 1px rgba(255,255,255,0.1);
      transition: all 0.4s ease;
    }
    .glass-panel:hover {
      border-color: #0ef;
      box-shadow: 0 0 20px rgba(0, 238, 255, 0.2);
    }

    /* hero */
    .hero {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 3rem;
      margin-bottom: 5rem;
      padding: 2rem 2rem;
    }
    .hero-badge {
      background: rgba(0, 238, 255, 0.12);
      border-radius: 40px;
      padding: 0.3rem 1rem;
      width: fit-content;
      font-size: 0.8rem;
      letter-spacing: 2px;
      font-weight: 500;
      backdrop-filter: blur(4px);
      border: 0.5px solid #0ef;
      color: #8effff;
      margin-bottom: 1.5rem;
    }
    .hero h1 {
      font-size: 4.5rem;
      font-weight: 800;
      line-height: 1.1;
      background: linear-gradient(135deg, #fff, #0ef, #aaffff);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
      font-family: 'Space Grotesk', monospace;
    }
    .hero-desc {
      font-size: 1.2rem;
      color: #b0d4ff;
      max-width: 550px;
      margin-top: 1.2rem;
    }
    .quantum-btn {
      margin-top: 2rem;
      display: inline-flex;
      align-items: center;
      gap: 12px;
      background: linear-gradient(95deg, #0ef, #00a3b0);
      border: none;
      padding: 0.9rem 2rem;
      border-radius: 60px;
      font-weight: 700;
      color: #010514;
      cursor: pointer;
      font-size: 1rem;
      transition: 0.25s;
      box-shadow: 0 0 12px #0ef8;
    }
    .quantum-btn:hover {
      transform: scale(1.02);
      box-shadow: 0 0 28px #0ef;
      letter-spacing: 1px;
    }
    .avatar-holo {
      position: relative;
      width: 280px;
      height: 280px;
      background: radial-gradient(circle at 30% 20%, rgba(0,200,255,0.2), rgba(2,10,30,0.8));
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      backdrop-filter: blur(6px);
      border: 2px solid rgba(0,255,255,0.5);
      box-shadow: 0 0 40px rgba(0,230,250,0.3);
    }
    .avatar-inner {
      width: 90%;
      height: 90%;
      border-radius: 50%;
      background: url('https://api.dicebear.com/9.x/identicon/svg?seed=GovindNeo&backgroundColor=0a0f1f&radius=50') center/cover;
      border: 2px solid cyan;
      box-shadow: inset 0 0 20px cyan, 0 0 30px cyan;
      transition: all 0.3s;
    }
    .section-title {
      font-size: 2.5rem;
      font-weight: 700;
      margin: 3rem 0 1.5rem;
      letter-spacing: -0.02em;
      border-left: 6px solid #0ef;
      padding-left: 1.2rem;
    }
    .card-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 2rem;
      margin: 2rem 0;
    }
    .neo-card {
      background: rgba(8, 16, 28, 0.65);
      backdrop-filter: blur(12px);
      border-radius: 2rem;
      padding: 1.8rem;
      border: 1px solid rgba(0, 238, 255, 0.3);
      transition: 0.2s ease-in-out;
      box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    }
    .neo-card:hover {
      transform: translateY(-8px);
      border-color: #0ef;
      box-shadow: 0 20px 35px -12px #0ef3;
    }
    .card-icon { font-size: 2.5rem; color: #0ef; margin-bottom: 1rem; }
    .card-title { font-size: 1.7rem; font-weight: 600; margin-bottom: 0.75rem; font-family: 'Space Grotesk', monospace; }
    .skill-tag {
      display: inline-block;
      background: rgba(0, 238, 255, 0.15);
      padding: 0.3rem 1rem;
      border-radius: 30px;
      font-size: 0.8rem;
      margin: 0.3rem 0.3rem 0 0;
      border: 0.5px solid #0ef6;
    }
    .projects-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 2rem;
      margin-top: 1.5rem;
    }
    .project-card {
      background: rgba(8, 16, 28, 0.7);
      backdrop-filter: blur(10px);
      border-radius: 1.8rem;
      padding: 1.5rem;
      border: 1px solid rgba(0,255,255,0.3);
      transition: 0.2s;
      text-align: center;
    }
    .project-card:hover { transform: translateY(-6px); border-color: #0ef; }
    .project-card img { width: 100%; border-radius: 1.2rem; margin-bottom: 1rem; border: 1px solid cyan; max-height: 160px; object-fit: cover; background: #0a1428; }
    .skills-container {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 1.2rem;
      margin: 2rem 0;
    }
    .skill-card {
      background: rgba(0,20,30,0.6);
      backdrop-filter: blur(8px);
      padding: 0.8rem 1.2rem;
      border-radius: 2rem;
      border: 1px solid cyan;
      transition: 0.2s;
    }
    .skill-card img { height: 48px; width: auto; filter: drop-shadow(0 0 6px cyan); }
    .contact-area {
      background: rgba(0, 15, 25, 0.6);
      border-radius: 2.5rem;
      padding: 2rem;
      margin-top: 3rem;
      border: 1px solid cyan;
    }
    .input-futuristic {
      background: rgba(0, 0, 0, 0.4);
      border: 1px solid #0ef5;
      border-radius: 2rem;
      padding: 0.9rem 1.2rem;
      width: 100%;
      color: white;
      font-size: 1rem;
      outline: none;
      transition: 0.2s;
    }
    .input-futuristic:focus { border-color: #0ef; box-shadow: 0 0 15px #0ef6; }
    footer {
      margin-top: 5rem;
      text-align: center;
      padding: 2rem;
      border-top: 1px solid rgba(0,255,255,0.2);
      font-size: 0.8rem;
    }
    .social-icons a { color: #0ef; margin: 0 10px; font-size: 1.8rem; transition: 0.2s; display: inline-block; }
    .social-icons a:hover { text-shadow: 0 0 12px cyan; transform: scale(1.1); }
    .timeline-item {
      display: flex;
      gap: 1.2rem;
      border-bottom: 1px dashed rgba(0,238,255,0.3);
      padding: 1rem 0;
    }
    @media (max-width: 850px) {
      .main-container { padding: 1rem; }
      .hero h1 { font-size: 2.8rem; }
      .hero { flex-direction: column; text-align: center; }
    }
  </style>
</head>
<body class="noise">
  <div class="cursor-follower" id="cursorDot"></div>
  <div class="main-container">
    <!-- HERO SECTION with Govind's identity -->
    <div class="glass-panel hero">
      <div>
        <div class="hero-badge"><i class="fas fa-satellite-dish"></i> // GOVIND // PORTAL // v.INFINITY</div>
        <h1 class="glitch">GOVIND JADAPALLI</h1>
        <h1 style="font-size: 2rem; margin-top: -10px;">⚡︎ WEB ARCHITECT & FUTURIST</h1>
        <p class="hero-desc" id="typed-desc"></p>
        <button class="quantum-btn" id="quantumConnectBtn"><i class="fas fa-microchip"></i> RESONATE WITH ME</button>
        <div class="social-icons" style="margin-top: 1.5rem;">
          <a href="https://www.linkedin.com/in/govind28" target="_blank"><i class="fa-brands fa-linkedin"></i></a>
          <a href="https://github.com/GoviGt650" target="_blank"><i class="fa-brands fa-square-github"></i></a>
          <a href="https://x.com/govindj28" target="_blank"><i class="fa-brands fa-square-x-twitter"></i></a>
          <a href="https://www.instagram.com/govind.18_/" target="_blank"><i class="fa-brands fa-instagram"></i></a>
        </div>
      </div>
      <div class="avatar-holo">
        <div class="avatar-inner" style="background: url('https://api.dicebear.com/9.x/identicon/svg?seed=GovindNeo&backgroundColor=0a0f1f&radius=50') center/cover;"></div>
      </div>
    </div>

    <!-- ABOUT section (modern cards) -->
    <div class="section-title"><i class="fas fa-user-astronaut"></i> CORE·PERSONA // ABOUT ME</div>
    <div class="card-grid">
      <div class="neo-card">
        <div class="card-icon"><i class="fas fa-brain"></i></div>
        <div class="card-title">Cognitive Blueprint</div>
        <p>Passionate <b>Web Developer</b> with expertise in frontend & backend technologies — HTML, CSS, JavaScript, React, Node.js. I craft seamless, user-friendly web apps with a focus on performance & scalability.</p>
        <div><span class="skill-tag">#React</span><span class="skill-tag">#Node.js</span><span class="skill-tag">#UI/UX</span></div>
      </div>
      <div class="neo-card">
        <div class="card-icon"><i class="fas fa-graduation-cap"></i></div>
        <div class="card-title">Academic Orbit</div>
        <p>Final year <b>Computer Science & Engineering</b> at <b>Audisankara College, Gudur</b>. Actively preparing for coding interviews, sharpening DSA, algorithms & optimization techniques.</p>
        <div><i class="fas fa-map-marker-alt" style="color:#0ef;"></i> Nellore, AP, India</div>
      </div>
      <div class="neo-card">
        <div class="card-icon"><i class="fas fa-phone-alt"></i></div>
        <div class="card-title">Contact Resonance</div>
        <p><i class="fas fa-phone"></i> +91 9381753363<br><i class="fas fa-envelope"></i> govindjadapalli28@gmail.com<br><i class="fas fa-globe"></i> github.com/GoviGt650</p>
      </div>
    </div>

    <!-- PROJECTS section (extracted from original) -->
    <div class="section-title"><i class="fas fa-cubes"></i> QUANTUM·PROJECTS</div>
    <div class="projects-grid">
      <div class="project-card">
        <img src="https://placehold.co/400x200/0a1428/0ef?text=E-Commerce+Hub" alt="E-Commerce">
        <h3>E-Commerce Website</h3>
        <p>Fully responsive e-commerce platform with modern UI/UX — Trendify.in concept.</p>
        <a href="https://govigt650.github.io/Trendify.in/" target="_blank"><button class="quantum-btn" style="background:#1f3a5f; padding:0.5rem 1rem;"><i class="fa-brands fa-github"></i> GitHub</button></a>
      </div>
      <div class="project-card">
        <img src="https://placehold.co/400x200/0a1428/0ef?text=Arsha+Clone" alt="Arsha Clone">
        <h3>Arsha Clone</h3>
        <p>Professional business website clone — HTML, CSS, JavaScript.</p>
        <a href="https://govigt650.github.io/arsha/" target="_blank"><button class="quantum-btn" style="background:#1f3a5f; padding:0.5rem 1rem;"><i class="fa-brands fa-github"></i> GitHub</button></a>
      </div>
      <div class="project-card">
        <img src="https://placehold.co/400x200/0a1428/0ef?text=Omni+Foods" alt="Omni Food">
        <h3>Omni Food Clone</h3>
        <p>Dynamic food delivery website with smooth animations & responsive design.</p>
        <a href="https://govigt650.github.io/Omni-foods/" target="_blank"><button class="quantum-btn" style="background:#1f3a5f; padding:0.5rem 1rem;"><i class="fa-brands fa-github"></i> GitHub</button></a>
      </div>
    </div>

    <!-- SKILLS section (visual icons) -->
    <div class="section-title"><i class="fas fa-code"></i> NEURAL·STACK // SKILLS</div>
    <div class="skills-container">
      <div class="skill-card"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python"></div>
      <div class="skill-card"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" alt="HTML5"></div>
      <div class="skill-card"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" alt="CSS3"></div>
      <div class="skill-card"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg" alt="Java"></div>
      <div class="skill-card"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" alt="MySQL"></div>
      <div class="skill-card"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg" alt="C"></div>
      <div class="skill-card"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" alt="JS"></div>
      <div class="skill-card"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg" alt="React"></div>
    </div>

    <!-- TIMELINE / ACHIEVEMENTS from your data -->
    <div class="section-title"><i class="fas fa-chart-line"></i> TEMPORAL·ARC</div>
    <div class="glass-panel" style="padding: 2rem;">
      <div class="timeline-item"><div style="min-width: 100px; color:#0ef;"><i class="fas fa-calendar-alt"></i> 2025</div><div><strong>Final Year CSE</strong> — Audisankara College, building advanced full-stack solutions.</div></div>
      <div class="timeline-item"><div style="min-width: 100px; color:#0ef;"><i class="fas fa-code-branch"></i> 2024</div><div><strong>Open Source Contributor</strong> — multiple frontend libraries & portfolio projects.</div></div>
      <div class="timeline-item"><div style="min-width: 100px; color:#0ef;"><i class="fas fa-trophy"></i> 2023</div><div><strong>Web Dev Hackathon</strong> — Top 5 finish with responsive design innovation.</div></div>
    </div>

    <!-- CONTACT SECTION (futuristic + your contact info) -->
    <div class="contact-area">
      <div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 2rem;">
        <div style="flex:1;">
          <h3><i class="fas fa-paper-plane"></i> TRANSMIT QUANTUM ECHO</h3>
          <p style="margin: 0.5rem 0 1.2rem;">Send a direct message — I'll resonate back.</p>
          <input type="text" class="input-futuristic" placeholder="// your alias" id="visitorName" style="margin-bottom: 1rem;">
          <input type="email" class="input-futuristic" placeholder="your@email.space" id="visitorEmail" style="margin-bottom: 1rem;">
          <textarea class="input-futuristic" rows="2" placeholder="transmit message..." id="msgContent" style="resize: none;"></textarea>
          <button class="quantum-btn" id="sendMsgBtn" style="margin-top: 1rem; background: #1f3a5f; color:white;"><i class="fas fa-bolt"></i> Send HyperSignal</button>
        </div>
        <div style="flex:1; text-align: right;">
          <div style="margin-bottom: 1.5rem;">
            <a href="https://api.whatsapp.com/send/?phone=9381753363" style="color:#0ef; font-size:1.6rem; margin-right:1rem;"><i class="fa-brands fa-whatsapp"></i></a>
            <a href="https://www.instagram.com/govind.18_/" style="color:#0ef; font-size:1.6rem; margin-right:1rem;"><i class="fa-brands fa-instagram"></i></a>
            <a href="mailto:govindjadapalli28@gmail.com" style="color:#0ef; font-size:1.6rem;"><i class="fa-regular fa-envelope"></i></a>
          </div>
          <p><i class="fas fa-envelope"></i> govindjadapalli28@gmail.com</p>
          <p><i class="fas fa-phone-alt"></i> +91 9381753363</p>
          <p><i class="fas fa-map-marker-alt"></i> Nellore, AP, India</p>
          <div class="skill-tag" style="background: rgba(0,0,0,0.6); margin-top:1rem;">🔗 Quantum handshake ready</div>
        </div>
      </div>
      <div id="feedbackMessage" style="margin-top: 1.5rem; font-size: 0.9rem; color: cyan;"></div>
    </div>

    <footer>
      <span>✦ GOVIND JADAPALLI // NEO-SYNTHESIS v1.0 | Full-Stack Alchemist ✦</span><br>
      <span style="font-size: 0.7rem;">© 2025 Govind Jadapalli. All rights reserved. | Embedded in the noosphere</span>
    </footer>
  </div>

  <script>
    (function() {
      // futuristic cursor
      const cursor = document.getElementById('cursorDot');
      if(cursor) {
        document.addEventListener('mousemove', (e) => {
          cursor.style.left = e.clientX + 'px';
          cursor.style.top = e.clientY + 'px';
        });
        document.addEventListener('mouseleave', () => cursor.style.opacity = '0');
        document.addEventListener('mouseenter', () => cursor.style.opacity = '0.7');
      }

      // Typed.js integration with your description
      if (typeof Typed !== 'undefined') {
        new Typed('#typed-desc', {
          strings: ["I'm a passionate web developer with expertise in front-end and back-end technologies. I love building responsive and user-friendly websites.", "Final year CSE student @ Audisankara College. DSA enthusiast & open-source contributor."],
          typeSpeed: 40,
          backSpeed: 25,
          loop: true,
          showCursor: true,
          cursorChar: "⚡"
        });
      } else {
        document.getElementById('typed-desc').innerHTML = "I'm a passionate web developer with expertise in front-end and back-end technologies.";
      }

      // quantum connection button
      const connectBtn = document.getElementById('quantumConnectBtn');
      if(connectBtn) {
        connectBtn.addEventListener('click', () => {
          const toast = document.createElement('div');
          toast.innerText = '⚡ QUANTUM LINK ESTABLISHED ⚡ Welcome Govind\'s neural core.';
          toast.style.position = 'fixed';
          toast.style.bottom = '30px';
          toast.style.left = '50%';
          toast.style.transform = 'translateX(-50%)';
          toast.style.backgroundColor = '#0a1a2fcc';
          toast.style.backdropFilter = 'blur(16px)';
          toast.style.border = '1px solid #0ef';
          toast.style.borderRadius = '60px';
          toast.style.padding = '12px 28px';
          toast.style.fontWeight = 'bold';
          toast.style.color = '#c0ffff';
          toast.style.zIndex = '9999';
          document.body.appendChild(toast);
          setTimeout(() => toast.remove(), 3000);
        });
      }

      // message sender
      const sendBtn = document.getElementById('sendMsgBtn');
      const feedbackDiv = document.getElementById('feedbackMessage');
      const nameInput = document.getElementById('visitorName');
      const emailInput = document.getElementById('visitorEmail');
      const msgInput = document.getElementById('msgContent');

      if(sendBtn) {
        sendBtn.addEventListener('click', () => {
          let nameVal = nameInput ? nameInput.value.trim() : "";
          let emailVal = emailInput ? emailInput.value.trim() : "";
          let msgVal = msgInput ? msgInput.value.trim() : "";
          if(!nameVal) nameVal = "Quantum Wanderer";
          if(!msgVal) {
            if(feedbackDiv) feedbackDiv.innerHTML = "<span style='color:#ffaa44;'><i class='fas fa-exclamation-triangle'></i> TRANSMISSION VOID: insert message before sending.</span>";
            setTimeout(() => { if(feedbackDiv) feedbackDiv.innerHTML = ""; }, 2000);
            return;
          }
          if(feedbackDiv) {
            feedbackDiv.innerHTML = `<i class="fas fa-satellite"></i> ✦ HyperSignal encrypted. Thanks ${nameVal}, Govind will reach back through quantum channel. ✦`;
            feedbackDiv.style.opacity = '1';
          }
          if(msgInput) msgInput.value = "";
          if(emailInput) emailInput.value = "";
          if(nameInput && nameInput.value === "Quantum Wanderer") nameInput.value = "";
          setTimeout(() => {
            if(feedbackDiv) feedbackDiv.innerHTML = "";
          }, 4000);
        });
      }

      // starfield background (dynamic)
      const canvas = document.createElement('canvas');
      canvas.style.position = 'fixed';
      canvas.style.top = '0';
      canvas.style.left = '0';
      canvas.style.width = '100%';
      canvas.style.height = '100%';
      canvas.style.pointerEvents = 'none';
      canvas.style.zIndex = '1';
      document.body.appendChild(canvas);
      const ctx = canvas.getContext('2d');
      let stars = [];
      function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
      }
      window.addEventListener('resize', resizeCanvas);
      resizeCanvas();
      for(let i=0; i<150; i++) {
        stars.push({
          x: Math.random() * canvas.width,
          y: Math.random() * canvas.height,
          radius: Math.random() * 1.8,
          alpha: Math.random() * 0.6 + 0.2,
          speed: 0.05 + Math.random() * 0.2
        });
      }
      function drawStars() {
        if(!ctx) return;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#03050b';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        for(let s of stars) {
          ctx.beginPath();
          ctx.arc(s.x, s.y, s.radius, 0, Math.PI*2);
          ctx.fillStyle = `rgba(120, 230, 255, ${s.alpha})`;
          ctx.fill();
          s.y += s.speed;
          if(s.y > canvas.height) {
            s.y = 0;
            s.x = Math.random() * canvas.width;
          }
        }
        requestAnimationFrame(drawStars);
      }
      drawStars();
    })();
  </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)