# Merge Conflict Setup - Ready for Students!

## 🎯 Guaranteed Merge Conflicts

This repository is now configured with **intentional merge conflicts** to teach students conflict resolution.

---

## Branch Configuration

### `main` Branch
**Focus**: R programming and traditional Git workflow

**README.md Changes**:
- Title: "Economic Observatory - Git & GitHub Practice Repository"
- **Project Overview**: Emphasizes R programming, INEGI data, professional workflows
- **What Makes This Different**: Lists real economic data, R scripts, API integration
- **Quick Start**: Traditional Git-first approach (Fork → Clone → Exercises)
- **Exercises Section**: Simple list with actual filenames

**Philosophy**: Learn Git fundamentals first, then apply to economic analysis

---

### `feature/dashboard-streamlit` Branch
**Focus**: Interactive dashboards and modern visualization

**README.md Changes**:
- Title: "Economic Observatory - Interactive Data Visualization Platform"
- **Project Overview**: Emphasizes Streamlit dashboards, Python/R integration, web deployment
- **Featured Dashboard**: Detailed list of dashboard features with emojis
- **Quick Start**: Dashboard-first approach ("Launch in 2 Minutes!")
- **Learning Path**: Gamified with "Levels" and pro tips

**Philosophy**: See the end goal (dashboard) first, then learn Git to build it

---

## Conflict Locations

When students run `git merge feature/dashboard-streamlit`, they'll encounter conflicts in:

### 1. Title (Line 1)
```
<<<<<<< HEAD
# Economic Observatory - Git & GitHub Practice Repository
=======
# Economic Observatory - Interactive Data Visualization Platform
>>>>>>> feature/dashboard-streamlit
```

### 2. Project Overview (Lines 5-20)
```
<<<<<<< HEAD
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
=======
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
>>>>>>> feature/dashboard-streamlit
```

### 3. Quick Start Section (Lines 102-130)
```
<<<<<<< HEAD
## Quick Start

### Get Started with Git Basics

**Step 1: Fork this Repository**
1. Click the "Fork" button at the top right
2. This creates your own copy on your GitHub account

**Step 2: Clone to Your Computer**
=======
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
>>>>>>> feature/dashboard-streamlit
```

### 4. Exercises/Learning Path Section (Lines 123-150)
```
<<<<<<< HEAD
## Exercises

Complete these exercises in order to master Git while analyzing Mexican economic data:

1. **[Exercise 1: Setup](exercises/exercise-1-setup.md)** - Fork, clone, add your economist profile
2. **[Exercise 2: Environment Variables](exercises/exercise-2-setup-environment.md)** - Configure INEGI API token securely
3. **[Exercise 3: Git Ignore](exercises/exercise-3-gitignore.md)** - Understand what files to track
4. **[Exercise 4: Running Scripts](exercises/exercise-4-running-scripts.md)** - Execute R analysis scripts
5. **[Exercise 5: Branching](exercises/exercise-5-branching-merging.md)** - Master branches and merge conflicts
=======
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
>>>>>>> feature/dashboard-streamlit
```

---

## Teaching Strategy

### For Instructors

**Setup**:
1. Students complete Exercises 1-4 first
2. In Exercise 5, they learn about branches
3. They discover the `feature/dashboard-streamlit` branch
4. Attempt to merge → **CONFLICT!**

**Learning Moments**:
- 📚 **Understanding conflicts**: Same file, different changes
- 🤔 **Decision making**: Which version is better? Or combine?
- 🔍 **Reading markers**: `<<<<<<<`, `=======`, `>>>>>>>`
- ✍️ **Resolution**: Edit, remove markers, test
- ✅ **Completion**: Stage, commit, push

---

## Student Exercise Flow

### Step 1: Discover the Branch
```bash
git branch -a
# See: remotes/origin/feature/dashboard-streamlit
```

### Step 2: View the Difference
```bash
git log --oneline --graph --all --decorate
# See branches have diverged
```

### Step 3: Attempt Merge
```bash
git checkout main
git merge feature/dashboard-streamlit
# CONFLICT!
```

### Step 4: See the Conflict
```bash
git status
# Shows: both modified: README.md
```

### Step 5: Resolve
Open README.md, see conflict markers, decide what to keep.

**Recommended Resolution**:
- Keep title from feature branch (more exciting)
- Combine project overview (mention both R and dashboard)
- Keep dashboard quick start (it's compelling)
- Combine exercises list (show levels but keep actual links)

### Step 6: Complete Merge
```bash
git add README.md
git commit -m "fix: merge dashboard feature into main

- Combined R workflow with dashboard features
- Kept dashboard quick start for engagement
- Merged exercise list with levels
- Resolved all conflicts by combining best of both"

git push origin main
```

---

## Pedagogical Benefits

### 1. **Real-World Conflict**
Not a contrived example - actual design decisions:
- Should we promote R or dashboards first?
- Traditional Git or modern visualization?
- Simple list or gamified levels?

### 2. **Multiple Valid Solutions**
No single "correct" answer:
- Could keep main version (simpler)
- Could keep feature version (flashier)
- Could combine (best of both)

Teaches judgment, not just mechanics!

### 3. **Meaningful Context**
Students care about the outcome:
- They've built these scripts
- They've seen the dashboard
- They understand both approaches
- Decision matters to them

### 4. **Complexity Levels**
- **Simple conflict**: Title (one line)
- **Medium conflict**: Project overview (paragraph)
- **Complex conflict**: Quick start (multiple sections)
- **Advanced conflict**: Exercises (structure change)

---

## Expected Outcomes

After resolving this conflict, students will:
- ✅ Understand what causes merge conflicts
- ✅ Know how to identify conflict markers
- ✅ Be able to read both versions critically
- ✅ Make informed decisions about what to keep
- ✅ Complete a merge successfully
- ✅ Feel confident about future conflicts

---

## Testing the Conflict

**Instructor should test**:

```bash
# Clone the repo
git clone [repo-url]
cd git-practice

# Try the merge
git checkout main
git merge feature/dashboard-streamlit

# Should see:
# Auto-merging README.md
# CONFLICT (content): Merge conflict in README.md
# Automatic merge failed; fix conflicts and then commit the result.

# Perfect! Conflict is set up correctly.
```

---

## Backup Plan

If students get stuck or panicked:

```bash
# Abort the merge
git merge --abort

# Everything returns to pre-merge state
# Can try again when ready
```

---

## Success Metrics

Students successfully resolved the conflict when:
- ✅ README.md has no conflict markers (`<`, `=`, `>`)
- ✅ README.md is syntactically valid Markdown
- ✅ Merge commit exists in git log
- ✅ Both branch histories are preserved
- ✅ Repository is in clean state (`git status`)

---

## Additional Notes

### Why README.md?

- **Visible impact**: Changes are immediately obvious
- **Meaningful content**: Not just random text
- **Multiple sections**: Various complexity levels
- **Markdown format**: Easy to read and edit
- **Central file**: Students already familiar with it

### Why These Specific Changes?

- **Philosophical difference**: R-first vs dashboard-first
- **Structural difference**: Simple list vs leveled sections
- **Stylistic difference**: Professional vs gamified
- **Technical difference**: Different quick start flows

All create realistic scenarios where both versions have merit!

---

**Status**: ✅ Conflicts Ready
**Tested**: Yes
**Documented**: Yes
**Ready for Students**: YES!

🎉 **Let the conflict resolution training begin!**
