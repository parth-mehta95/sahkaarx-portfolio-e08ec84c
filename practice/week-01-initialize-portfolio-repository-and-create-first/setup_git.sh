#!/usr/bin/env bash
set -e

REPO_URL="$1"

echo "=========================================="
echo " Python Utility Module Git Setup & Push   "
echo "=========================================="

# 1. Initialize git if not already initialized
if [ ! -d ".git" ]; then
    echo "[1/5] Initializing local git repository..."
    git init -b main
else
    echo "[1/5] Git repository already initialized."
    git checkout main 2>/dev/null || true
fi

# 2. Stage base files and create initial commit on main
echo "[2/5] Creating initial commit on main..."
git add .gitignore README.md pyproject.toml setup.py LICENSE
git commit -m "chore: initial repository setup with README, .gitignore, and package metadata"

# 3. Create feature branch and commit utility module
echo "[3/5] Creating feature branch 'feature/string-utilities'..."
git checkout -b feature/string-utilities
git add shared_utils tests
git commit -m "feat: implement string utility functions (slugify, truncate, casing) and tests"

# 4. Merge feature branch into main with a merge commit (simulating PR merge)
echo "[4/5] Merging feature branch into main with PR merge commit..."
git checkout main
git merge --no-ff feature/string-utilities -m "Merge pull request #1 from feature/string-utilities"

# 5. Push to GitHub if remote URL is provided
if [ -n "$REPO_URL" ]; then
    echo "[5/5] Adding remote and pushing to GitHub ($REPO_URL)..."
    git remote remove origin 2>/dev/null || true
    git remote add origin "$REPO_URL"
    git push -u origin main
    git push -u origin feature/string-utilities
    echo "Successfully pushed to $REPO_URL!"
else
    echo "[5/5] Remote URL not provided. To push to GitHub, run:"
    echo "  git remote add origin <YOUR_GITHUB_REPO_URL>"
    echo "  git push -u origin main"
    echo "  git push origin feature/string-utilities"
fi

echo ""
echo "Git log graph:"
git log --graph --oneline -n 5
