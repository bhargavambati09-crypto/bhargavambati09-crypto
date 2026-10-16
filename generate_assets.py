import base64
import os

assets_dir = r"C:\Users\Chiso\.gemini\antigravity-ide\scratch\bhargavambati09-crypto\assets"
photo_path = os.path.join(assets_dir, "bhargav.jpg")

# Read photo and convert to base64
with open(photo_path, "rb") as f:
    photo_b64 = base64.b64encode(f.read()).decode('utf-8')
photo_data_url = f"data:image/jpeg;base64,{photo_b64}"

print("Photo loaded, base64 length:", len(photo_b64))

# 1. GENERATE HEADER BANNER SVG
header_banner_svg = """<svg width="860" height="230" viewBox="0 0 860 230" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Gradients -->
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#07090e" />
      <stop offset="45%" stop-color="#0d131f" />
      <stop offset="100%" stop-color="#080c14" />
    </linearGradient>

    <!-- Neon Text Gradient -->
    <linearGradient id="textGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE">
        <animate attributeName="stop-color" values="#00F2FE; #4FACFE; #9B51E0; #00F2FE" dur="8s" repeatCount="indefinite" />
      </stop>
      <stop offset="50%" stop-color="#4FACFE">
        <animate attributeName="stop-color" values="#4FACFE; #9B51E0; #00F2FE; #4FACFE" dur="8s" repeatCount="indefinite" />
      </stop>
      <stop offset="100%" stop-color="#9B51E0">
        <animate attributeName="stop-color" values="#9B51E0; #00F2FE; #4FACFE; #9B51E0" dur="8s" repeatCount="indefinite" />
      </stop>
    </linearGradient>

    <!-- Border Glow Gradient -->
    <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F2FE" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#7B2CBF" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#00F2FE" stop-opacity="0.8" />
    </linearGradient>

    <!-- Beam Glow Filter -->
    <filter id="neonGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <filter id="subtleGlow" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <!-- Grid Pattern -->
    <pattern id="cyberGrid" width="30" height="30" patternUnits="userSpaceOnUse">
      <path d="M 30 0 L 0 0 0 30" fill="none" stroke="#1f293d" stroke-width="0.7" stroke-opacity="0.5" />
      <circle cx="0" cy="0" r="1.2" fill="#00f2fe" fill-opacity="0.4" />
    </pattern>
  </defs>

  <style>
    .glow-title {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      font-weight: 800;
      font-size: 38px;
      letter-spacing: 5px;
      fill: url(#textGrad);
    }
    .subtitle {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      font-weight: 500;
      font-size: 13.5px;
      letter-spacing: 3.5px;
      fill: #8E9BAE;
    }
    .badge-text {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      font-weight: 600;
      font-size: 11px;
      letter-spacing: 1.5px;
      fill: #00F2FE;
    }
    .pulse-dot {
      animation: pulse 2s infinite ease-in-out;
    }
    @keyframes pulse {
      0%, 100% { opacity: 0.3; transform: scale(0.9); }
      50% { opacity: 1; transform: scale(1.2); }
    }
    .streamer {
      animation: drift 6s linear infinite;
    }
    @keyframes drift {
      0% { transform: translateX(0); opacity: 0; }
      20% { opacity: 0.8; }
      80% { opacity: 0.8; }
      100% { transform: translateX(400px); opacity: 0; }
    }
    .beam-line {
      stroke-dasharray: 80 200;
      animation: beamRun 5s linear infinite;
    }
    @keyframes beamRun {
      0% { stroke-dashoffset: 0; }
      100% { stroke-dashoffset: -560; }
    }
  </style>

  <!-- Card Background -->
  <rect x="2" y="2" width="856" height="226" rx="16" fill="url(#bgGrad)" stroke="url(#borderGrad)" stroke-width="1.5" />

  <!-- Grid Layer -->
  <rect x="4" y="4" width="852" height="222" rx="14" fill="url(#cyberGrid)" />

  <!-- Ambient Glow Blobs -->
  <circle cx="150" cy="50" r="90" fill="#00F2FE" fill-opacity="0.07" filter="url(#neonGlow)" />
  <circle cx="720" cy="170" r="110" fill="#9B51E0" fill-opacity="0.08" filter="url(#neonGlow)" />

  <!-- Cybernetic Corner Brackets -->
  <path d="M 22 40 L 22 22 L 40 22" fill="none" stroke="#00F2FE" stroke-width="2.5" stroke-linecap="round" />
  <path d="M 838 40 L 838 22 L 820 22" fill="none" stroke="#00F2FE" stroke-width="2.5" stroke-linecap="round" />
  <path d="M 22 190 L 22 208 L 40 208" fill="none" stroke="#9B51E0" stroke-width="2.5" stroke-linecap="round" />
  <path d="M 838 190 L 838 208 L 820 208" fill="none" stroke="#9B51E0" stroke-width="2.5" stroke-linecap="round" />

  <!-- Animated Top Border Beam -->
  <path class="beam-line" d="M 60 2 L 800 2" stroke="#00F2FE" stroke-width="2.5" stroke-linecap="round" filter="url(#subtleGlow)" />

  <!-- Top Pill / Status Tag -->
  <g transform="translate(325, 32)">
    <rect x="0" y="0" width="210" height="26" rx="13" fill="#0e1726" stroke="#00F2FE" stroke-opacity="0.4" stroke-width="1" />
    <circle class="pulse-dot" cx="16" cy="13" r="4.5" fill="#00F5A0" />
    <text x="32" y="17" class="badge-text">STATUS: ACTIVE &amp; BUILDING</text>
  </g>

  <!-- Name Title -->
  <g transform="translate(430, 110)">
    <text text-anchor="middle" class="glow-title" filter="url(#neonGlow)">BHARGAV AMBATI</text>
  </g>

  <!-- Subtitle -->
  <g transform="translate(430, 145)">
    <text text-anchor="middle" class="subtitle">FULL-STACK DEVELOPER • AI WORKFLOWS • WEB3 ARCHITECT</text>
  </g>

  <!-- Floating Tech Mini Badges -->
  <g transform="translate(195, 175)">
    <!-- Badge 1 -->
    <rect x="0" y="0" width="82" height="24" rx="6" fill="#131B2E" stroke="#223656" stroke-width="1" />
    <text x="41" y="16" text-anchor="middle" fill="#38BDF8" font-family="sans-serif" font-size="11" font-weight="600">TypeScript</text>

    <!-- Badge 2 -->
    <rect x="94" y="0" width="82" height="24" rx="6" fill="#131B2E" stroke="#223656" stroke-width="1" />
    <text x="135" y="16" text-anchor="middle" fill="#A78BFA" font-family="sans-serif" font-size="11" font-weight="600">React/Next</text>

    <!-- Badge 3 -->
    <rect x="188" y="0" width="94" height="24" rx="6" fill="#131B2E" stroke="#223656" stroke-width="1" />
    <text x="235" y="16" text-anchor="middle" fill="#34D399" font-family="sans-serif" font-size="11" font-weight="600">AI Automation</text>

    <!-- Badge 4 -->
    <rect x="294" y="0" width="86" height="24" rx="6" fill="#131B2E" stroke="#223656" stroke-width="1" />
    <text x="337" y="16" text-anchor="middle" fill="#F472B6" font-family="sans-serif" font-size="11" font-weight="600">Web3 / DeFi</text>

    <!-- Badge 5 -->
    <rect x="392" y="0" width="78" height="24" rx="6" fill="#131B2E" stroke="#223656" stroke-width="1" />
    <text x="431" y="16" text-anchor="middle" fill="#FBBF24" font-family="sans-serif" font-size="11" font-weight="600">Python</text>
  </g>
</svg>
"""

with open(os.path.join(assets_dir, "header_banner.svg"), "w", encoding="utf-8") as f:
    f.write(header_banner_svg)
print("Saved header_banner.svg")

# 2. GENERATE ANIMATED AVATAR SVG (WITH USER'S ACTUAL EMBEDDED PHOTO)
avatar_svg = f"""<svg width="240" height="240" viewBox="0 0 240 240" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Avatar Circular Clip -->
    <clipPath id="avatarClip">
      <circle cx="120" cy="120" r="92" />
    </clipPath>

    <!-- Neon Glow Filter -->
    <filter id="haloGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <linearGradient id="ringGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="50%" stop-color="#7B2CBF" />
      <stop offset="100%" stop-color="#00F2FE" />
    </linearGradient>

    <linearGradient id="ringGrad2" x1="100%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#00F5A0" />
      <stop offset="50%" stop-color="#00F2FE" />
      <stop offset="100%" stop-color="#9B51E0" />
    </linearGradient>
  </defs>

  <style>
    .spin-ring-cw {{
      transform-origin: 120px 120px;
      animation: spinCW 12s linear infinite;
    }}
    .spin-ring-ccw {{
      transform-origin: 120px 120px;
      animation: spinCCW 8s linear infinite;
    }}
    .pulse-halo {{
      transform-origin: 120px 120px;
      animation: pulseHalo 3s ease-in-out infinite;
    }}
    @keyframes spinCW {{
      0% {{ transform: rotate(0deg); }}
      100% {{ transform: rotate(360deg); }}
    }}
    @keyframes spinCCW {{
      0% {{ transform: rotate(360deg); }}
      100% {{ transform: rotate(0deg); }}
    }}
    @keyframes pulseHalo {{
      0%, 100% {{ opacity: 0.6; }}
      50% {{ opacity: 1; }}
    }}
  </style>

  <!-- Ambient Outer Glow -->
  <circle class="pulse-halo" cx="120" cy="120" r="106" stroke="url(#ringGrad1)" stroke-width="2" fill="none" opacity="0.4" filter="url(#haloGlow)" />

  <!-- Inner Rotating Tech Segment 1 -->
  <circle class="spin-ring-cw" cx="120" cy="120" r="101" stroke="url(#ringGrad1)" stroke-width="3" stroke-dasharray="140 30 50 30" stroke-linecap="round" fill="none" filter="url(#haloGlow)" />

  <!-- Outer Counter-Rotating Tech Segment 2 -->
  <circle class="spin-ring-ccw" cx="120" cy="120" r="96" stroke="url(#ringGrad2)" stroke-width="2" stroke-dasharray="80 40 100 40" stroke-linecap="round" fill="none" />

  <!-- Black Background Behind Portrait -->
  <circle cx="120" cy="120" r="92" fill="#080c14" />

  <!-- Bhargav's Actual Photo Cropped into Hex/Circle -->
  <image href="{photo_data_url}" x="28" y="28" width="184" height="184" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatarClip)" />

  <!-- Sleek Border Ring Over Photo -->
  <circle cx="120" cy="120" r="92" stroke="#00F2FE" stroke-width="2" fill="none" stroke-opacity="0.8" />

  <!-- Bottom Mini Badge: Verified Developer -->
  <g transform="translate(68, 204)">
    <rect x="0" y="0" width="104" height="24" rx="12" fill="#0A111E" stroke="#00F2FE" stroke-width="1.2" />
    <circle cx="12" cy="12" r="4" fill="#00F5A0" />
    <text x="24" y="16" fill="#F1F5F9" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="700" letter-spacing="1">VERIFIED</text>
    <!-- Checkmark SVG icon -->
    <path d="M 84 12 L 87 15 L 94 8" fill="none" stroke="#00F2FE" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" />
  </g>
</svg>
"""

with open(os.path.join(assets_dir, "avatar_animated.svg"), "w", encoding="utf-8") as f:
    f.write(avatar_svg)
print("Saved avatar_animated.svg")

# 3. GENERATE ANIMATED TYPING SVG
typing_svg = """<svg width="860" height="58" viewBox="0 0 860 58" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="typeBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a101d" />
      <stop offset="100%" stop-color="#070a12" />
    </linearGradient>
    <linearGradient id="typeBorder" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" stop-opacity="0.6" />
      <stop offset="50%" stop-color="#7B2CBF" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#00F2FE" stop-opacity="0.6" />
    </linearGradient>
  </defs>

  <style>
    .type-container {
      font-family: 'Courier New', Courier, monospace, -apple-system, BlinkMacSystemFont, sans-serif;
      font-size: 15px;
      font-weight: 600;
    }
    .cursor {
      animation: blink 0.8s infinite;
      fill: #00F2FE;
    }
    @keyframes blink {
      0%, 100% { opacity: 1; }
      50% { opacity: 0; }
    }
    
    /* 4-Sentence Carousel Animation */
    .msg-1 {
      animation: cycle1 16s infinite;
    }
    .msg-2 {
      animation: cycle2 16s infinite;
    }
    .msg-3 {
      animation: cycle3 16s infinite;
    }
    .msg-4 {
      animation: cycle4 16s infinite;
    }

    @keyframes cycle1 {
      0%, 20% { opacity: 1; transform: translateY(0); }
      24%, 96% { opacity: 0; transform: translateY(-8px); }
      100% { opacity: 1; transform: translateY(0); }
    }
    @keyframes cycle2 {
      0%, 22% { opacity: 0; transform: translateY(8px); }
      26%, 46% { opacity: 1; transform: translateY(0); }
      50%, 100% { opacity: 0; transform: translateY(-8px); }
    }
    @keyframes cycle3 {
      0%, 48% { opacity: 0; transform: translateY(8px); }
      52%, 72% { opacity: 1; transform: translateY(0); }
      76%, 100% { opacity: 0; transform: translateY(-8px); }
    }
    @keyframes cycle4 {
      0%, 74% { opacity: 0; transform: translateY(8px); }
      78%, 96% { opacity: 1; transform: translateY(0); }
      100% { opacity: 0; transform: translateY(-8px); }
    }
  </style>

  <!-- Container -->
  <rect x="2" y="2" width="856" height="54" rx="12" fill="url(#typeBg)" stroke="url(#typeBorder)" stroke-width="1.2" />

  <!-- Terminal Prompt Icon -->
  <g transform="translate(24, 20)">
    <text x="0" y="15" fill="#00F2FE" font-family="monospace" font-size="18" font-weight="bold">&gt;</text>
  </g>

  <!-- Animated Rotating Phrases -->
  <g transform="translate(50, 35)" class="type-container">
    <g class="msg-1">
      <text fill="#E2E8F0">👋 Hello World! I'm <tspan fill="#00F2FE" font-weight="bold">Bhargav Ambati</tspan> — Building smart software that transforms ideas into reality.</text>
    </g>
    <g class="msg-2">
      <text fill="#E2E8F0">🤖 Architecting <tspan fill="#38BDF8" font-weight="bold">AI Agents</tspan> &amp; Automated Systems like <tspan fill="#F472B6" font-weight="bold">WorkFlowX-AI</tspan>.</text>
    </g>
    <g class="msg-3">
      <text fill="#E2E8F0">⚡ Engineering Scalable <tspan fill="#34D399" font-weight="bold">Full-Stack Solutions</tspan> with Next.js, TypeScript &amp; Python.</text>
    </g>
    <g class="msg-4">
      <text fill="#E2E8F0">🌐 Passionate about <tspan fill="#A78BFA" font-weight="bold">Web3, Cryptography</tspan> &amp; Contributing to Open Source!</text>
    </g>
  </g>

  <!-- Blinking Cursor Tag -->
  <rect class="cursor" x="815" y="21" width="10" height="18" rx="2" />
</svg>
"""

with open(os.path.join(assets_dir, "typing_animation.svg"), "w", encoding="utf-8") as f:
    f.write(typing_svg)
print("Saved typing_animation.svg")

# 4. GENERATE CYBER DIVIDER SVG
divider_svg = """<svg width="860" height="24" viewBox="0 0 860 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="divGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" stop-opacity="0" />
      <stop offset="35%" stop-color="#00F2FE" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#9B51E0" stop-opacity="1" />
      <stop offset="65%" stop-color="#00F2FE" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#00F2FE" stop-opacity="0" />
    </linearGradient>
    <filter id="divGlow" x="-20%" y="-50%" width="140%" height="200%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    .pulse-core {
      animation: glowPulse 2.5s ease-in-out infinite;
    }
    @keyframes glowPulse {
      0%, 100% { opacity: 0.6; transform: scale(0.9); }
      50% { opacity: 1; transform: scale(1.15); }
    }
  </style>

  <!-- Horizontal Beam Line -->
  <line x1="20" y1="12" x2="840" y2="12" stroke="url(#divGrad)" stroke-width="1.8" filter="url(#divGlow)" />

  <!-- Center Diamond Tech Core -->
  <g transform="translate(430, 12)" class="pulse-core">
    <polygon points="0,-7 7,0 0,7 -7,0" fill="#00F2FE" filter="url(#divGlow)" />
    <polygon points="0,-4 4,0 0,4 -4,0" fill="#FFFFFF" />
  </g>

  <!-- Left / Right Micro Nodes -->
  <circle cx="360" cy="12" r="2.5" fill="#00F2FE" opacity="0.8" />
  <circle cx="500" cy="12" r="2.5" fill="#00F2FE" opacity="0.8" />
  <circle cx="280" cy="12" r="2" fill="#9B51E0" opacity="0.6" />
  <circle cx="580" cy="12" r="2" fill="#9B51E0" opacity="0.6" />
</svg>
"""

with open(os.path.join(assets_dir, "cyber_divider.svg"), "w", encoding="utf-8") as f:
    f.write(divider_svg)
print("Saved cyber_divider.svg")

# 5. GENERATE STATS SECTION HEADER SVG
def make_section_header(title, subtitle, icon_path):
    return f"""<svg width="860" height="52" viewBox="0 0 860 52" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="headerBg_{title.replace(' ', '_')}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="60%" stop-color="#090d16" />
      <stop offset="100%" stop-color="#05080e" />
    </linearGradient>
    <linearGradient id="accentGrad_{title.replace(' ', '_')}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="100%" stop-color="#9B51E0" />
    </linearGradient>
  </defs>

  <!-- Background bar -->
  <rect x="0" y="4" width="860" height="44" rx="10" fill="url(#headerBg_{title.replace(' ', '_')})" stroke="#1E293B" stroke-width="1.2" />

  <!-- Left Accent Accent Line -->
  <rect x="0" y="4" width="5" height="44" rx="2" fill="url(#accentGrad_{title.replace(' ', '_')})" />

  <!-- Icon SVG -->
  <g transform="translate(20, 16)">
    {icon_path}
  </g>

  <!-- Title Text -->
  <text x="56" y="28" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="16" font-weight="700" letter-spacing="1.5">{title}</text>
  <text x="56" y="40" fill="#64748B" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="500" letter-spacing="0.8">{subtitle}</text>
</svg>
"""

# Section icons
metrics_icon = '<path d="M2 16 L6 10 L10 13 L16 4 L22 10" fill="none" stroke="#00F2FE" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>'
tech_icon = '<rect x="2" y="3" width="18" height="14" rx="2" fill="none" stroke="#38BDF8" stroke-width="2"/><line x1="7" y1="21" x2="15" y2="21" stroke="#38BDF8" stroke-width="2"/><line x1="11" y1="17" x2="11" y2="21" stroke="#38BDF8" stroke-width="2"/>'
projects_icon = '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" fill="none" stroke="#FBBF24" stroke-width="2"/>'
connect_icon = '<circle cx="6" cy="12" r="3" fill="#A78BFA"/><circle cx="18" cy="6" r="3" fill="#A78BFA"/><circle cx="18" cy="18" r="3" fill="#A78BFA"/><line x1="8.5" y1="10.5" x2="15.5" y2="7.5" stroke="#A78BFA" stroke-width="1.8"/><line x1="8.5" y1="13.5" x2="15.5" y2="16.5" stroke="#A78BFA" stroke-width="1.8"/>'

with open(os.path.join(assets_dir, "header_metrics.svg"), "w", encoding="utf-8") as f:
    f.write(make_section_header("GITHUB TELEMETRY &amp; PERFORMANCE", "LIVE DEVELOPER ACTIVITY &amp; REPOSITORY METRICS", metrics_icon))

with open(os.path.join(assets_dir, "header_tech.svg"), "w", encoding="utf-8") as f:
    f.write(make_section_header("TECHNICAL ARSENAL &amp; CORE STACK", "LANGUAGES, FRAMEWORKS, DATABASES &amp; CLOUD INFRASTRUCTURE", tech_icon))

with open(os.path.join(assets_dir, "header_projects.svg"), "w", encoding="utf-8") as f:
    f.write(make_section_header("FEATURED CREATIONS &amp; WORKFLOWS", "PRODUCTION PLATFORMS &amp; HIGH-IMPACT OPEN SOURCE PROJECTS", projects_icon))

with open(os.path.join(assets_dir, "header_connect.svg"), "w", encoding="utf-8") as f:
    f.write(make_section_header("TRANSMISSION &amp; CONNECTIVITY", "LET'S BUILD SOMETHING EXTRAORDINARY TOGETHER", connect_icon))

print("Saved all headers successfully!")
