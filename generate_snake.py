import os

assets_dir = r"C:\Users\Chiso\.gemini\antigravity-ide\scratch\bhargavambati09-crypto\assets"

snake_svg = """<svg width="860" height="150" viewBox="0 0 860 150" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="gridBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d16" />
      <stop offset="100%" stop-color="#04060a" />
    </linearGradient>
    <filter id="neonBlur" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    .snake-head {
      animation: snakeMove 10s linear infinite;
    }
    @keyframes snakeMove {
      0% { transform: translate(30px, 30px); }
      15% { transform: translate(250px, 30px); }
      20% { transform: translate(250px, 60px); }
      35% { transform: translate(480px, 60px); }
      40% { transform: translate(480px, 90px); }
      55% { transform: translate(720px, 90px); }
      60% { transform: translate(720px, 120px); }
      75% { transform: translate(350px, 120px); }
      80% { transform: translate(350px, 75px); }
      90% { transform: translate(80px, 75px); }
      100% { transform: translate(30px, 30px); }
    }
    .pulse-dot-1 {
      animation: dotPulse 1.8s ease-in-out infinite alternate;
    }
    .pulse-dot-2 {
      animation: dotPulse 2.4s ease-in-out infinite alternate;
    }
    @keyframes dotPulse {
      0% { opacity: 0.2; transform: scale(0.9); }
      100% { opacity: 1; transform: scale(1.1); }
    }
  </style>

  <!-- Background Container -->
  <rect x="2" y="2" width="856" height="146" rx="14" fill="url(#gridBg)" stroke="#1F2937" stroke-width="1.2" />

  <!-- GitHub Contribution-Style Grid Dots -->
  <g opacity="0.8">
"""

# Generate 53 columns x 7 rows of contribution squares
import random
random.seed(42)

for col in range(46):
    for row in range(5):
        x = 32 + col * 17
        y = 30 + row * 19
        rand_val = random.random()
        if rand_val < 0.35:
            color = "#161b22" # empty
        elif rand_val < 0.60:
            color = "#0e4429" # level 1
        elif rand_val < 0.80:
            color = "#006d32" # level 2
        elif rand_val < 0.94:
            color = "#26a641" # level 3
        else:
            color = "#39d353" # level 4
        snake_svg += f'    <rect x="{x}" y="{y}" width="12" height="12" rx="2.5" fill="{color}" />\n'

snake_svg += """  </g>

  <!-- Animated Snake Body & Head -->
  <g class="snake-head">
    <!-- Snake Trail -->
    <rect x="-30" y="0" width="12" height="12" rx="2.5" fill="#39d353" opacity="0.4" />
    <rect x="-15" y="0" width="12" height="12" rx="2.5" fill="#00F5A0" opacity="0.7" />
    <!-- Snake Head -->
    <rect x="0" y="0" width="13" height="13" rx="3" fill="#00F2FE" filter="url(#neonBlur)" />
    <!-- Eyes -->
    <circle cx="9" cy="3.5" r="1.5" fill="#05080E" />
    <circle cx="9" cy="9.5" r="1.5" fill="#05080E" />
  </g>

  <!-- Legend & Header Text -->
  <g transform="translate(32, 20)">
    <text x="0" y="0" fill="#64748B" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="600" letter-spacing="1">CONTRIBUTION TIMELINE VISUALIZER</text>
  </g>
  <g transform="translate(680, 20)">
    <text x="0" y="0" fill="#475569" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10.5">Less</text>
    <rect x="28" y="-9" width="10" height="10" rx="2" fill="#161b22" />
    <rect x="42" y="-9" width="10" height="10" rx="2" fill="#0e4429" />
    <rect x="56" y="-9" width="10" height="10" rx="2" fill="#006d32" />
    <rect x="70" y="-9" width="10" height="10" rx="2" fill="#26a641" />
    <rect x="84" y="-9" width="10" height="10" rx="2" fill="#39d353" />
    <text x="100" y="0" fill="#475569" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10.5">More</text>
  </g>
</svg>
"""

with open(os.path.join(assets_dir, "snake.svg"), "w", encoding="utf-8") as f:
    f.write(snake_svg)

print("Saved snake.svg successfully!")
