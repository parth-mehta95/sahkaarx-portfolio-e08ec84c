param(
    [string]$RepoUrl = ""
)

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host " Python Utility Module Git Setup & Push   " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

# 1. Initialize git if not already initialized
if (-not (Test-Path ".git")) {
    Write-Host "[1/5] Initializing local git repository..." -ForegroundColor Yellow
    git init -b main
} else {
    Write-Host "[1/5] Git repository already initialized." -ForegroundColor Green
    git checkout main 2>$null
}

# 2. Stage base files and create initial commit on main
Write-Host "[2/5] Creating initial commit on main..." -ForegroundColor Yellow
git add .gitignore README.md pyproject.toml setup.py LICENSE
git commit -m "chore: initial repository setup with README, .gitignore, and package metadata"

# 3. Create feature branch and commit utility module
Write-Host "[3/5] Creating feature branch 'feature/string-utilities'..." -ForegroundColor Yellow
git checkout -b feature/string-utilities
git add shared_utils tests
git commit -m "feat: implement string utility functions (slugify, truncate, casing) and tests"

# 4. Merge feature branch into main with a merge commit (simulating PR merge)
Write-Host "[4/5] Merging feature branch into main with PR merge commit..." -ForegroundColor Yellow
git checkout main
git merge --no-ff feature/string-utilities -m "Merge pull request #1 from feature/string-utilities"

# 5. Push to GitHub if remote URL is provided
if ($RepoUrl -ne "") {
    Write-Host "[5/5] Adding remote and pushing to GitHub ($RepoUrl)..." -ForegroundColor Yellow
    git remote remove origin 2>$null
    git remote add origin $RepoUrl
    git push -u origin main
    git push -u origin feature/string-utilities
    Write-Host "`nSuccessfully pushed to $RepoUrl!" -ForegroundColor Green
    Write-Host "Merged feature branch 'feature/string-utilities' is present on remote." -ForegroundColor Green
} else {
    Write-Host "[5/5] Remote URL not provided. To push to GitHub, run:" -ForegroundColor Cyan
    Write-Host "  git remote add origin <YOUR_GITHUB_REPO_URL>" -ForegroundColor White
    Write-Host "  git push -u origin main" -ForegroundColor White
    Write-Host "  git push origin feature/string-utilities" -ForegroundColor White
}

Write-Host "`nGit log graph:" -ForegroundColor Magenta
git log --graph --oneline -n 5
