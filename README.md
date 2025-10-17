# Economic Observatory - Git & GitHub Practice Repository

Welcome to the Economic Observatory practice repository! This project teaches economics students how to use Git and GitHub while building a collaborative economic data analysis platform.

## Project Overview

This repository simulates a real-world economic observatory where students collaborate to:
- Collect and track economic indicators from INEGI
- Analyze economic data using R programming
- Generate professional reports and visualizations
- Share findings through collaborative Git workflows
- Learn version control best practices

### What Makes This Different?

Unlike generic Git tutorials, this project uses:
- **Real economic data** from Mexican institutions (INEGI)
- **Professional R scripts** for GDP, inflation, and labor analysis
- **Actual API integration** with secure token management
- **Collaborative workflows** mirroring real research teams

## Learning Objectives

By completing this tutorial, you will:
- Master Git fundamentals (fork, clone, commit, push, pull)
- Work with branches and feature development
- Handle merge conflicts professionally
- Collaborate using GitHub Pull Requests
- Apply version control to data analysis projects
- Document economic research using Markdown
- Manage data files and analysis scripts

---

## Git & GitHub Roadmap

This project follows a realistic workflow for collaborative economic research.

### Phase 1: Getting Started
**Skills**: Fork, Clone, Add, Commit, Push

- Fork and clone the repository
- Add your economist profile
- Make your first commit
- Push changes to GitHub

### Phase 2: Data Collection
**Skills**: Branches, Checkout, Merge

- Create a feature branch for new data
- Add economic indicator data (CSV)
- Merge into main branch

### Phase 3: Analysis Scripts
**Skills**: Pull Requests, Code Review

- Write Python/R analysis scripts
- Create Pull Request
- Review teammate's code

### Phase 4: Report Writing
**Skills**: Merge Conflicts, Amend

- Collaborate on economic reports
- Handle merge conflicts
- Amend commits to fix mistakes

### Phase 5: Visualization
**Skills**: Stash, Tags, Releases

- Build interactive dashboards
- Tag stable versions
- Create releases

---

## Repository Structure

```
economic-observatory/
├── README.md                 # This file
├── CONTRIBUTING.md          # Contribution guidelines
├── .gitignore              # Files to ignore
├── .env.example            # API keys template
├── economists/             # Economist profiles
├── data/                   # Economic data files
│   ├── gdp/
│   ├── inflation/
│   └── unemployment/
├── analysis/              # Analysis scripts
│   ├── python/
│   └── r/
├── reports/              # Economic reports
├── visualizations/       # Charts and graphs
├── exercises/           # Step-by-step tutorials
└── resources/          # Learning resources
```

---

## Quick Start

### Get Started with Git Basics

**Step 1: Fork this Repository**
1. Click the "Fork" button at the top right
2. This creates your own copy on your GitHub account

**Step 2: Clone to Your Computer**

```bash
# Clone your fork
git clone https://github.com/YOUR-USERNAME/git-practice.git
cd git-practice
```

### Complete Exercise 1

Start with [Exercise 1](exercises/exercise-1-setup.md) to learn Git basics by adding your economist profile.

---

## Exercises

Complete these exercises in order to master Git while analyzing Mexican economic data:

1. **[Exercise 1: Setup](exercises/exercise-1-setup.md)** - Fork, clone, add your economist profile
2. **[Exercise 2: Environment Variables](exercises/exercise-2-setup-environment.md)** - Configure INEGI API token securely
3. **[Exercise 3: Git Ignore](exercises/exercise-3-gitignore.md)** - Understand what files to track
4. **[Exercise 4: Running Scripts](exercises/exercise-4-running-scripts.md)** - Execute R analysis scripts
5. **[Exercise 5: Branching](exercises/exercise-5-branching-merging.md)** - Master branches and merge conflicts

---

## Key Commands

```bash
# Basic workflow
git status
git add filename
git commit -m "message"
git push origin main

# Branching
git checkout -b feature/new-feature
git merge feature-branch

# Collaboration
git pull origin main
git fetch origin
```

---

## Economic Data Sources

- **INEGI** (Mexico): https://www.inegi.org.mx
- **World Bank**: https://data.worldbank.org
- **FRED**: https://fred.stlouisfed.org
- **OECD**: https://data.oecd.org

See [resources/economic-data-sources.md](resources/economic-data-sources.md) for details.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Adding economic data
- Writing analysis scripts
- Creating reports
- Code review process

---

## Help & Resources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- Check [exercises/](exercises/) for tutorials
- Open an issue for questions

---

**License**: MIT

Start with [Exercise 1](exercises/exercise-1-setup.md) and begin your journey!
