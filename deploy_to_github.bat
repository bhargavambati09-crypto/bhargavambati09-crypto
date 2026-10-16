@echo off
echo ========================================================
echo   Deploying Bhargav Ambati's Animated Profile to GitHub
echo ========================================================
echo.

cd /d "C:\Users\Chiso\.gemini\antigravity-ide\scratch\bhargavambati09-crypto"

echo [1/5] Initializing Git repository...
git init

echo [2/5] Staging all profile files and animated assets...
git add .

echo [3/5] Committing changes...
git commit -m "feat: launch high-performance animated github profile"

echo [4/5] Setting main branch...
git branch -M main

echo [5/5] Linking to GitHub and pushing...
git remote remove origin >nul 2>&1
git remote add origin https://github.com/bhargavambati09-crypto/bhargavambati09-crypto.git

echo.
echo Pushing to https://github.com/bhargavambati09-crypto/bhargavambati09-crypto...
echo (If prompted, sign in via browser or Personal Access Token)
git push -u origin main --force

echo.
echo ========================================================
echo   Done! Check your live profile at:
echo   https://github.com/bhargavambati09-crypto
echo ========================================================
pause
