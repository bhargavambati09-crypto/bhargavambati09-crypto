# 🚀 GitHub Profile Setup Guide for @bhargavambati09-crypto

Welcome to your custom-engineered, animated GitHub Profile! Everything has been prepared in this folder.

---

## ⚡ Option 1: Git Command Line (Fastest - 1 Minute)

Open your terminal / PowerShell in this directory:
`C:\Users\Chiso\.gemini\antigravity-ide\scratch\bhargavambati09-crypto`

Run these commands:

```bash
# 1. Initialize Git repository
git init

# 2. Add all files (README, assets, workflows)
git add .

# 3. Commit
git commit -m "feat: launch ultra-modern animated github profile"

# 4. Set main branch
git branch -M main

# 5. Link to your GitHub special profile repository
# (Make sure you created https://github.com/bhargavambati09-crypto/bhargavambati09-crypto first!)
git remote add origin https://github.com/bhargavambati09-crypto/bhargavambati09-crypto.git

# 6. Push live!
git push -u origin main --force
```

---

## 🌐 Option 2: Via GitHub Web Interface (No Git CLI Needed)

1. Go to **[GitHub New Repository](https://github.com/new)**.
2. In the **Repository name** field, type exactly: `bhargavambati09-crypto`
   > GitHub will show a special message: *"You found a secret! bhargavambati09-crypto is a special repository that you can use to add a README.md to your GitHub profile."*
3. Make sure **Public** is selected.
4. Click **Create repository**.
5. Click **"uploading an existing file"** or drag-and-drop:
   - `README.md`
   - The entire `assets/` folder (with `header_banner.svg`, `avatar_animated.svg`, `typing_animation.svg`, `cyber_divider.svg`, `bhargav.jpg`, `snake.svg`, and header SVGs)
   - The `.github/` folder
6. Click **Commit changes**.

---

## 🐍 Enabling the Automatic Contribution Snake Game

To have the animated snake automatically update every 12 hours:
1. In your `bhargavambati09-crypto` repository, go to **Settings** -> **Actions** -> **General**.
2. Scroll down to **Workflow permissions**.
3. Select **"Read and write permissions"** and click **Save**.
4. Go to the **Actions** tab in your repo, click **"Generate Snake Animation"**, and click **Run workflow**.

---

## 📁 What's Included in This Package:

| File / Folder | Purpose |
| :--- | :--- |
| `README.md` | Master profile README with animated SVGs, real-time metrics, project showcase, and badges |
| `assets/header_banner.svg` | Custom animated cyber-neon hero banner with glowing gradients and active status |
| `assets/avatar_animated.svg` | High-tech rotating glowing radar frame embedding your portrait (`bhargav.jpg`) |
| `assets/typing_animation.svg` | Animated typewriter effect cycling through your roles, passions, and tech focus |
| `assets/cyber_divider.svg` | Glowing animated energy beam divider |
| `assets/snake.svg` | Animated contribution timeline visualizer |
| `assets/bhargav.jpg` | Your high-resolution professional portrait |
| `assets/header_*.svg` | Futuristic section titles with vector icons for Metrics, Tech, Projects & Connect |
| `.github/workflows/snake.yml` | GitHub Action workflow to generate your dynamic live snake animation |
| `index.html` | Standalone local preview to view your animated profile in any browser |
