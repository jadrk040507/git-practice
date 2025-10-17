# Instructor Notes - Economic Observatory Git Practice Repository

## Repository Overview

This repository has been transformed from a general Git practice repo into an **Economics-focused GitHub tutorial** where students learn Git/GitHub while building a collaborative economic data analysis platform.

---

## Key Features

### 1. **Economics Context**
- All exercises use economic data and analysis
- Real-world scenario: Building an economic observatory
- Uses actual economic indicators (GDP, inflation, unemployment)
- Data from real sources (INEGI, FRED, World Bank, OECD)

### 2. **Complete Git Workflow**
Students learn progressively:
- **Phase 1**: Basics (fork, clone, commit, push)
- **Phase 2**: Branching (feature branches, merge)
- **Phase 3**: Collaboration (Pull Requests, code review)
- **Phase 4**: Conflict Resolution (merge conflicts)
- **Phase 5**: Advanced (stash, tags, releases)

### 3. **Real Programming Environment**
- **R scripts**: Use APIs with `dotenv` for API keys
- **Python scripts**: Data analysis with pandas, visualization
- **Streamlit dashboard**: Interactive economic data visualization
- **Data files**: Sample CSV files with economic indicators

### 4. **Security Best Practices**
- `.env` for API keys (excluded from Git via `.gitignore`)
- `.env.example` template for team sharing
- All scripts use environment variables
- Documentation on secure key management

---

## Repository Structure

```
economic-observatory/
├── README.md                          # Main overview with roadmap
├── CONTRIBUTING.md                    # Contribution guidelines
├── SETUP_ENV.md                       # API keys setup guide
├── MERGE_CONFLICT_EXERCISE.md         # Conflict resolution tutorial
├── DASHBOARD_README.md                # Dashboard setup instructions
├── DASHBOARD_FEATURES.md              # Dashboard documentation (feature branch)
├── .gitignore                         # Ignores .env, Python/R cache, data
├── .env.example                       # Template for API keys
├── requirements.txt                   # Python dependencies
├── dashboard_app.py                   # Streamlit dashboard app
│
├── economists/                        # Student profiles
│   ├── README.md
│   └── example-economist.txt
│
├── data/                              # Economic data
│   ├── gdp/
│   │   ├── README.md
│   │   └── mexico_gdp_sample.csv
│   ├── inflation/
│   │   ├── README.md
│   │   └── mexico_inflation_sample.csv
│   └── unemployment/
│       ├── README.md
│       └── mexico_unemployment_sample.csv
│
├── analysis/                          # Analysis scripts
│   ├── python/
│   │   ├── README.md
│   │   ├── fetch_worldbank_data.py
│   │   └── inflation_analysis.py
│   └── r/
│       ├── README.md
│       ├── fetch_fred_data.R
│       ├── gdp_analysis.R
│       └── inflation_analysis.R
│
├── reports/                           # Economic reports
│   ├── README.md
│   └── templates/
│       └── quarterly-report-template.md
│
├── visualizations/                    # Output charts
│   └── README.md
│
├── exercises/                         # Step-by-step exercises
│   └── exercise-1-setup.md
│
└── resources/                         # Learning resources
    (to be completed)
```

---

## Branch Setup for Merge Conflicts

### Main Branch (`main`)
- Standard README with normal quick start
- Complete economic observatory setup
- All analysis scripts and data

### Feature Branch (`feature/dashboard-streamlit`)
- Modified README promoting dashboard as primary feature
- Added DASHBOARD_FEATURES.md
- Same codebase but different documentation focus

### Intentional Conflicts
When students merge `feature/dashboard-streamlit` into `main`, they will encounter conflicts in:
1. **README.md** - "Project Overview" section
2. **README.md** - "Quick Start" section

These conflicts are realistic and teach students how to:
- Identify conflict markers
- Understand both versions
- Resolve by combining changes
- Complete the merge

---

## Student Workflow

### Week 1-2: Git Basics
1. **Exercise 1**: Fork, clone, add profile, commit, push
   - Students add their economist profile
   - Learn basic Git commands
   - Practice good commit messages

### Week 3: Branching
2. **Exercise 2**: Create branch, add data, merge
   - Students add economic data (CSV)
   - Learn feature branch workflow
   - Practice clean merges

### Week 3-4: Collaboration
3. **Exercise 3**: Analysis scripts, Pull Requests
   - Students write Python/R scripts
   - Create PRs, review code
   - Learn collaborative workflow

### Week 4-5: Conflict Resolution
4. **Exercise 4**: Reports, merge conflicts
   - Multiple students edit same report
   - Practice resolving conflicts
   - **Merge conflict exercise with dashboard branch**

### Week 5-6: Advanced & Dashboard
5. **Exercise 5**: Streamlit dashboard, tags, releases
   - Build/modify dashboard
   - Tag versions
   - Create releases

---

## API Keys Setup

### Required APIs
1. **FRED API** (Federal Reserve Economic Data)
   - Free account at https://fred.stlouisfed.org/
   - Used in R script `fetch_fred_data.R`

2. **World Bank API**
   - No key required (open API)
   - Used in Python script `fetch_worldbank_data.py`

3. **INEGI** (Optional for Mexico data)
   - Check https://www.inegi.org.mx/ for API access

### Student Instructions
1. Copy `.env.example` to `.env`
2. Add their API keys
3. Never commit `.env` to Git
4. Verify `.env` is in `.gitignore`

---

## Teaching the Merge Conflict Exercise

### Setup (Instructor)
The repository is already set up with:
- `main` branch with standard README
- `feature/dashboard-streamlit` branch with modified README
- Conflicts will occur in Project Overview and Quick Start sections

### Instructions for Students

**Step 1**: Clone and explore
```bash
git clone [student-fork]
cd git-practice
git branch -a  # Show all branches
```

**Step 2**: See the branches
```bash
git log --oneline --graph --all --decorate
```

**Step 3**: Attempt the merge
```bash
git checkout main
git merge feature/dashboard-streamlit
# CONFLICT will appear
```

**Step 4**: Guide through resolution
- Show conflict markers in README.md
- Explain `<<<<<<< HEAD`, `=======`, `>>>>>>>`
- Demonstrate combining both versions
- Remove markers
- Stage and commit

**Step 5**: Verify
```bash
git log --oneline --graph
streamlit run dashboard_app.py  # Test it works
```

### Expected Outcome
Students will:
- See a real merge conflict
- Practice reading conflict markers
- Make decisions about what to keep
- Successfully complete a merge
- Understand why conflicts happen

---

## Grading Rubric

### Git Skills (40%)
- [ ] Proper use of fork and clone
- [ ] Meaningful commit messages (conventional commits)
- [ ] Clean branching strategy
- [ ] Successful merge conflict resolution
- [ ] Appropriate use of .gitignore

### Economic Analysis (30%)
- [ ] Data quality and sourcing
- [ ] Proper citations
- [ ] Analysis methodology
- [ ] Visualization quality
- [ ] Report clarity

### Collaboration (20%)
- [ ] Code review participation
- [ ] Pull request descriptions
- [ ] Response to feedback
- [ ] Communication in PRs

### Documentation (10%)
- [ ] Clear README updates
- [ ] Code comments
- [ ] Docstrings in functions
- [ ] Data documentation

---

## Common Issues & Solutions

### Issue: `.env` committed to Git
**Solution**:
```bash
git rm --cached .env
git commit -m "fix: remove .env from git tracking"
```

### Issue: Merge conflict panic
**Solution**:
- Show `git merge --abort` to reset
- Walk through conflict markers slowly
- Use `MERGE_CONFLICT_EXERCISE.md`

### Issue: Dashboard won't start
**Solution**:
```bash
pip install -r requirements.txt
streamlit run dashboard_app.py
```

### Issue: R scripts can't find API keys
**Solution**:
- Check `.env` exists
- Verify `load_dot_env()` is called
- Install `dotenv` package: `install.packages("dotenv")`

### Issue: Students don't understand data sources
**Solution**:
- Point to `resources/economic-data-sources.md` (when created)
- Show sample data in `data/` folders
- Demonstrate API fetch scripts

---

## Additional Exercises (Optional)

### Exercise: Collaborative Report
1. Divide class into teams
2. Each team works on different report section
3. Teams create PRs simultaneously
4. Practice reviewing each other's work
5. Handle conflicts when merging

### Exercise: Dashboard Enhancement
1. Students fork the repository
2. Add new economic indicator to dashboard
3. Create PR with their addition
4. Code review process
5. Best additions get merged

### Exercise: Data Pipeline
1. Students write script to fetch live data
2. Store in appropriate `data/` folder
3. Update analysis scripts to use new data
4. Create visualization
5. Document in report

---

## Future Enhancements

### To Do:
- [ ] Complete exercises 2-5
- [ ] Add `resources/economic-data-sources.md`
- [ ] Add `resources/git-cheatsheet.md`
- [ ] Create sample reports in `reports/`
- [ ] Add GitHub Actions workflow (optional)
- [ ] Add pre-commit hooks (optional)
- [ ] Create video tutorials

### Nice to Have:
- [ ] Docker setup for consistent environment
- [ ] Jupyter notebooks for analysis
- [ ] API rate limiting handling
- [ ] Data validation scripts
- [ ] Automated testing
- [ ] CI/CD pipeline

---

## Quick Start for Instructors

### 1. Fork the Repository
Fork to your organization's GitHub account

### 2. Customize
- Update `.env.example` with relevant APIs
- Modify exercises for your course
- Add your institution's data sources
- Adjust grading rubric

### 3. Student Setup
- Students fork YOUR fork
- They follow Exercise 1
- Monitor PRs for participation

### 4. Teach Merge Conflicts
- Use the `feature/dashboard-streamlit` branch
- Follow `MERGE_CONFLICT_EXERCISE.md`
- Have students work in pairs

### 5. Dashboard Demo
```bash
streamlit run dashboard_app.py
```
Show students the end goal!

---

## Contact & Support

For questions or issues:
1. Check exercise documentation
2. Review `SETUP_ENV.md` for configuration
3. Consult `MERGE_CONFLICT_EXERCISE.md` for conflicts
4. Open an issue on GitHub

---

## License

MIT License - Free to use and modify for educational purposes

---

**Happy Teaching! 📚**

The combination of economics context + Git skills + real programming creates an engaging learning experience for students.
