# GitHub Workflow Guide

## The Standard Flow

### 1. Fork the Repository
- Click "Fork" button on GitHub
- Creates your own copy

### 2. Clone Your Fork
```bash
git clone https://github.com/YOUR-USERNAME/repo-name.git
cd repo-name
```

### 3. Create a Feature Branch
```bash
git checkout -b feature/my-feature
```

### 4. Make Changes
- Edit files
- Test your changes

### 5. Stage and Commit
```bash
git add .
git commit -m "feat: add my awesome feature"
```

### 6. Push to Your Fork
```bash
git push origin feature/my-feature
```

### 7. Create Pull Request
- Go to your fork on GitHub
- Click "Compare & pull request"
- Fill out description
- Submit!

### 8. Address Feedback
- Make requested changes
- Commit and push again
- PR updates automatically

### 9. After Merge
```bash
git checkout main
git pull upstream main
git push origin main
git branch -d feature/my-feature
```

## Branch Naming Conventions

- `feature/` - New features
- `bugfix/` - Bug fixes
- `hotfix/` - Urgent fixes
- `docs/` - Documentation
- `refactor/` - Code improvements
- `test/` - Adding tests

Examples:
- `feature/user-authentication`
- `bugfix/fix-login-error`
- `docs/update-readme`

## Commit Message Format
```
<type>: <description>

[optional body]

[optional footer]
```

Types:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation
- `style:` - Formatting
- `refactor:` - Code restructuring
- `test:` - Adding tests
- `chore:` - Maintenance

Examples:
```
feat: add user profile page
fix: correct email validation
docs: update installation instructions
```