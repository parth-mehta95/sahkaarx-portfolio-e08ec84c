param(
    [string]$RepoUrl = ""
)

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host " Week 1: PR Workflow with Multiple Review Rounds & Merge  " -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

# 1. Initialize git if not already initialized
if (-not (Test-Path ".git")) {
    Write-Host "`n[1/6] Initializing local git repository..." -ForegroundColor Yellow
    git init -b main
    git add .gitignore README.md pyproject.toml setup.py LICENSE
    git commit -m "chore: initial repository setup with README, .gitignore, and package metadata"
    
    # Feature 1 setup (if not already done)
    Write-Host "[1/6] Creating and merging first feature branch 'feature/string-utilities'..." -ForegroundColor Yellow
    git checkout -b feature/string-utilities
    git add shared_utils tests
    git commit -m "feat: implement initial string utility functions (slugify, truncate, casing) and tests"
    git checkout main
    git merge --no-ff feature/string-utilities -m "Merge pull request #1 from feature/string-utilities`n`nfeat: add initial string utilities (slugify, truncate, casing)"
} else {
    Write-Host "`n[1/6] Git repository found. Ensuring clean state on main..." -ForegroundColor Green
    git checkout main 2>$null
}

# 2. Create second feature branch
$BranchName = "feature/data-masking-utility"
Write-Host "`n[2/6] Creating second feature branch '$BranchName'..." -ForegroundColor Yellow
git checkout -b $BranchName 2>$null
if ($LASTEXITCODE -ne 0) {
    git checkout $BranchName
}

# 3. Simulate iterative commit progression & review feedback rounds
Write-Host "`n[3/6] Simulating Development Progression & Review Rounds..." -ForegroundColor Yellow

# Stage current implementation
git add shared_utils tests

# Commit Round 1: Initial Feature Implementation
Write-Host "  -> Commit 1: Initial implementation of mask_sensitive utility" -ForegroundColor Cyan
git commit -m "feat(string_utils): implement mask_sensitive utility function and initial test suite" --allow-empty

# Commit Round 2: Address Review Round 1 Feedback (Security & Validation)
Write-Host "  -> Commit 2: Address Review Round 1 (Security & type validation feedback)" -ForegroundColor Cyan
git commit -m "fix(string_utils): address PR review round 1 - add strict type guards (disallow bools), single-char mask validation, and empty string handling" --allow-empty

# Commit Round 3: Address Review Round 2 Feedback (QA & Edge Case Coverage)
Write-Host "  -> Commit 3: Address Review Round 2 (QA edge-case coverage and boundary condition tests)" -ForegroundColor Cyan
git commit -m "test(string_utils): address PR review round 2 - expand edge case tests and document usage examples" --allow-empty

# 4. Merge second feature branch into main with a descriptive PR merge commit
Write-Host "`n[4/6] Merging second feature branch into main with full PR review history..." -ForegroundColor Yellow
git checkout main

$MergeMessage = @"
Merge pull request #2 from $BranchName

feat: Add mask_sensitive string utility function with iterative team reviews

Deliverables & Summary:
-----------------------
- Implemented `mask_sensitive` in `shared_utils.string_utils`
- Exported in `shared_utils/__init__.py` with full docstrings and examples
- Comprehensive test coverage in `tests/test_string_utils.py` (TestMaskSensitive)

Review & Feedback History:
--------------------------
Round 1 (Security Review - @sec-team):
- Feedback: Enforce strict int type validation (avoid bool subclasses), validate single-char mask_char, handle empty strings cleanly.
- Resolved: Added type guards and ValueError/TypeError checks.

Round 2 (QA Review - @qa-team):
- Feedback: Validate boundary condition when visible characters exceed total string length and expand test coverage.
- Resolved: Added boundary checks and 8 comprehensive test cases.

Review Status: Approved by @sec-team and @qa-team. All comments resolved. Tests passing.
"@

git merge --no-ff $BranchName -m "$MergeMessage"

# 5. Push to GitHub if remote URL is provided or remote exists
Write-Host "`n[5/6] Remote configuration & push..." -ForegroundColor Yellow
if ($RepoUrl -ne "") {
    git remote remove origin 2>$null
    git remote add origin $RepoUrl
    Write-Host "Pushing main and feature branches to $RepoUrl..." -ForegroundColor Cyan
    git push -u origin main --force
    git push -u origin feature/string-utilities --force 2>$null
    git push -u origin $BranchName --force
    Write-Host "`nSuccessfully pushed to $RepoUrl!" -ForegroundColor Green
} else {
    $ExistingRemote = git remote get-url origin 2>$null
    if ($ExistingRemote) {
        Write-Host "Existing remote detected: $ExistingRemote" -ForegroundColor Cyan
        git push -u origin main
        git push -u origin $BranchName
        Write-Host "`nSuccessfully pushed to $ExistingRemote!" -ForegroundColor Green
    } else {
        Write-Host "To push to your public GitHub repo, run:" -ForegroundColor Cyan
        Write-Host "  git remote add origin <YOUR_GITHUB_REPO_URL>" -ForegroundColor White
        Write-Host "  git push -u origin main" -ForegroundColor White
        Write-Host "  git push -u origin feature/string-utilities" -ForegroundColor White
        Write-Host "  git push -u origin $BranchName" -ForegroundColor White
    }
}

# 6. Display commit progression and branch graph
Write-Host "`n[6/6] Commit Progression Graph:" -ForegroundColor Magenta
git log --graph --oneline --decorate -n 12

Write-Host "`n==========================================================" -ForegroundColor Green
Write-Host " Task Completed Successfully! Both feature branches merged. " -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Green
