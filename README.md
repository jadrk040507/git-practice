# Economic Observatory - Interactive Data Visualization Platform

Welcome to the Economic Observatory! This cutting-edge platform combines Git version control with modern data visualization to create an interactive economic analysis environment.

## Project Overview

This repository is a complete economic data visualization platform where students:
- **Build interactive Streamlit dashboards** with real-time data
- **Visualize economic trends** using Plotly and modern charting libraries
- **Analyze data with Python and R** in an integrated environment
- **Collaborate using GitHub** for team-based economic research
- **Deploy web applications** to share insights with stakeholders

### 🚀 Featured: Live Economic Dashboard

This platform showcases a production-ready Streamlit dashboard featuring:
- **📊 Interactive GDP Analysis** - Dual-axis charts with growth rates
- **💰 Inflation Tracker** - CPI trends with Banco de México targets
- **👥 Labor Market Monitor** - Real-time employment statistics
- **🎛️ Dynamic Filters** - Date range selection and indicator toggles
- **📱 Mobile Responsive** - Access anywhere, anytime

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

### 🎯 Launch the Dashboard in 2 Minutes!

Experience the power of interactive economic visualization:

```bash
# Step 1: Clone the repository
git clone https://github.com/YOUR-USERNAME/git-practice.git
cd git-practice

# Step 2: Install dependencies (one-time setup)
pip install -r requirements.txt

# Step 3: Launch the dashboard
streamlit run dashboard_app.py
```

**Boom!** 💥 Your browser opens at `http://localhost:8501` with:
- Live economic charts
- Interactive data exploration
- Professional visualizations

**Want to learn more?** Check out:
- 📖 [Dashboard Features](DASHBOARD_FEATURES.md) - Complete documentation
- 🎓 [Exercise 1](exercises/exercise-1-setup.md) - Learn Git basics
- 🔧 [Dashboard Customization](DASHBOARD_README.md) - Make it your own

---

## Learning Path

Master Git and data visualization through hands-on exercises:

### 🎯 Level 1: Foundations
1. **[Getting Started](exercises/exercise-1-setup.md)** - Fork, clone, and setup
2. **[API Configuration](exercises/exercise-2-setup-environment.md)** - Secure INEGI token management

### 📊 Level 2: Data & Analysis
3. **[Repository Management](exercises/exercise-3-gitignore.md)** - .gitignore best practices
4. **[Running Analyses](exercises/exercise-4-running-scripts.md)** - Execute R scripts, generate insights

### 🚀 Level 3: Collaboration & Deployment
5. **[Branch Workflow](exercises/exercise-5-branching-merging.md)** - Branches, PRs, **merge conflicts** (you'll practice merging this dashboard branch!)

**Pro Tip**: Start with the dashboard to see the end goal, then work through exercises to build your skills!

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
