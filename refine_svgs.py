import os

assets_dir = r"C:\Users\Chiso\.gemini\antigravity-ide\scratch\bhargavambati09-crypto\assets"

# 1. OPTIMIZED CYBER DIVIDER
divider_svg = """<svg width="860" height="26" viewBox="0 0 860 26" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="divGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" stop-opacity="0" />
      <stop offset="25%" stop-color="#00F2FE" stop-opacity="0.7" />
      <stop offset="50%" stop-color="#9B51E0" stop-opacity="1" />
      <stop offset="75%" stop-color="#00F2FE" stop-opacity="0.7" />
      <stop offset="100%" stop-color="#00F2FE" stop-opacity="0" />
    </linearGradient>

    <linearGradient id="beamGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" stop-opacity="0" />
      <stop offset="50%" stop-color="#FFFFFF" stop-opacity="1" />
      <stop offset="100%" stop-color="#9B51E0" stop-opacity="0" />
    </linearGradient>

    <filter id="divGlow" x="-10%" y="-100%" width="120%" height="300%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    .pulse-core {
      animation: coreGlow 2.5s ease-in-out infinite alternate;
    }
    @keyframes coreGlow {
      0% { transform: scale(0.9); opacity: 0.7; }
      100% { transform: scale(1.2); opacity: 1; }
    }
    .energy-beam {
      animation: sweep 4s ease-in-out infinite alternate;
    }
    @keyframes sweep {
      0% { transform: translateX(0); }
      100% { transform: translateX(460px); }
    }
  </style>

  <!-- Horizontal Glow Base Line -->
  <rect x="40" y="12" width="780" height="2" rx="1" fill="url(#divGrad)" />

  <!-- Animated Gliding Energy Beam -->
  <g class="energy-beam">
    <rect x="180" y="11" width="120" height="4" rx="2" fill="url(#beamGrad)" filter="url(#divGlow)" opacity="0.8" />
  </g>

  <!-- Center Diamond Tech Core -->
  <g transform="translate(430, 13)">
    <polygon class="pulse-core" points="0,-7 7,0 0,7 -7,0" fill="#00F2FE" filter="url(#divGlow)" />
    <polygon points="0,-3.5 3.5,0 0,3.5 -3.5,0" fill="#FFFFFF" />
  </g>

  <!-- Lateral Accent Nodes -->
  <circle cx="340" cy="13" r="2.5" fill="#00F2FE" opacity="0.8" />
  <circle cx="520" cy="13" r="2.5" fill="#00F2FE" opacity="0.8" />
  <circle cx="230" cy="13" r="2" fill="#9B51E0" opacity="0.6" />
  <circle cx="630" cy="13" r="2" fill="#9B51E0" opacity="0.6" />
</svg>
"""

with open(os.path.join(assets_dir, "cyber_divider.svg"), "w", encoding="utf-8") as f:
    f.write(divider_svg)

# 2. OPTIMIZED TYPING ANIMATION (BALANCED FONT & SAFE MARGINS)
typing_svg = """<svg width="860" height="54" viewBox="0 0 860 54" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="typeBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a101d" />
      <stop offset="100%" stop-color="#070a12" />
    </linearGradient>
    <linearGradient id="typeBorder" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" stop-opacity="0.6" />
      <stop offset="50%" stop-color="#7B2CBF" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#00F2FE" stop-opacity="0.6" />
    </linearGradient>
  </defs>

  <style>
    .type-container {
      font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
      font-size: 13.5px;
      font-weight: 500;
      letter-spacing: -0.2px;
    }
    .cursor {
      animation: blink 0.8s infinite;
      fill: #00F2FE;
    }
    @keyframes blink {
      0%, 100% { opacity: 1; }
      50% { opacity: 0; }
    }
    
    .msg-1 { animation: cycle1 16s infinite; }
    .msg-2 { animation: cycle2 16s infinite; }
    .msg-3 { animation: cycle3 16s infinite; }
    .msg-4 { animation: cycle4 16s infinite; }

    @keyframes cycle1 {
      0%, 20% { opacity: 1; transform: translateY(0); }
      24%, 96% { opacity: 0; transform: translateY(-6px); }
      100% { opacity: 1; transform: translateY(0); }
    }
    @keyframes cycle2 {
      0%, 22% { opacity: 0; transform: translateY(6px); }
      26%, 46% { opacity: 1; transform: translateY(0); }
      50%, 100% { opacity: 0; transform: translateY(-6px); }
    }
    @keyframes cycle3 {
      0%, 48% { opacity: 0; transform: translateY(6px); }
      52%, 72% { opacity: 1; transform: translateY(0); }
      76%, 100% { opacity: 0; transform: translateY(-6px); }
    }
    @keyframes cycle4 {
      0%, 74% { opacity: 0; transform: translateY(6px); }
      78%, 96% { opacity: 1; transform: translateY(0); }
      100% { opacity: 0; transform: translateY(-6px); }
    }
  </style>

  <!-- Container -->
  <rect x="2" y="2" width="856" height="50" rx="10" fill="url(#typeBg)" stroke="url(#typeBorder)" stroke-width="1.2" />

  <!-- Terminal Prompt Icon -->
  <g transform="translate(20, 18)">
    <text x="0" y="15" fill="#00F2FE" font-family="monospace" font-size="16" font-weight="bold">&gt;</text>
  </g>

  <!-- Animated Rotating Phrases -->
  <g transform="translate(42, 32)" class="type-container">
    <g class="msg-1">
      <text fill="#E2E8F0">👋 Hello World! I'm <tspan fill="#00F2FE" font-weight="bold">Bhargav Ambati</tspan> — Building scalable software &amp; AI architectures.</text>
    </g>
    <g class="msg-2">
      <text fill="#E2E8F0">🤖 Architecting <tspan fill="#38BDF8" font-weight="bold">AI Agents</tspan> &amp; Automated Systems like <tspan fill="#F472B6" font-weight="bold">WorkFlowX-AI</tspan>.</text>
    </g>
    <g class="msg-3">
      <text fill="#E2E8F0">⚡ Engineering Scalable <tspan fill="#34D399" font-weight="bold">Full-Stack Solutions</tspan> with Next.js, TypeScript &amp; Python.</text>
    </g>
    <g class="msg-4">
      <text fill="#E2E8F0">🌐 Passionate about <tspan fill="#A78BFA" font-weight="bold">Web3, Cryptography</tspan> &amp; Contributing to Open Source.</text>
    </g>
  </g>

  <!-- Blinking Cursor Tag -->
  <rect class="cursor" x="820" y="18" width="9" height="17" rx="2" />
</svg>
"""

with open(os.path.join(assets_dir, "typing_animation.svg"), "w", encoding="utf-8") as f:
    f.write(typing_svg)

print("Updated cyber_divider.svg and typing_animation.svg successfully!")
