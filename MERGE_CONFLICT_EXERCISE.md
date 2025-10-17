# Exercise: Resolving Merge Conflicts

## Objective

Learn how to handle merge conflicts by merging the `feature/dashboard-streamlit` branch into `main`.

## Background

The `feature/dashboard-streamlit` branch contains updates to the README that conflict with changes in `main`. Both branches modified the same sections of the README.md file.

## What You'll Learn

- How to identify merge conflicts
- How to read conflict markers
- How to resolve conflicts manually
- How to complete a merge after resolving conflicts

---

## Step 1: Understand the Situation

Two branches have diverged:

```
main branch:
  - Updated README with standard quick start

feature/dashboard-streamlit branch:
  - Updated README promoting dashboard as primary quick start
  - Added DASHBOARD_FEATURES.md documentation
```

When you try to merge `feature/dashboard-streamlit` into `main`, Git will find conflicts in README.md.

---

## Step 2: Attempt the Merge

```bash
# Make sure you're on main branch
git checkout main

# Try to merge the feature branch
git merge feature/dashboard-streamlit
```

You'll see output like:
```
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

---

## Step 3: Check the Status

```bash
git status
```

You'll see:
```
On branch main
You have unmerged paths.
  (fix conflicts and run "git commit")

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   README.md
```

---

## Step 4: Open the Conflicted File

Open `README.md` in your text editor. You'll see conflict markers like this:

```markdown
<<<<<<< HEAD
## Project Overview

This repository simulates a real-world economic observatory where students collaborate to:
- Collect and track economic indicators
- Analyze economic data using Python/R
- Generate reports and visualizations
- Share findings through collaborative workflows
=======
## Project Overview

This repository simulates a real-world economic observatory where students collaborate to:
- Collect and track economic indicators
- Analyze economic data using Python/R
- **Build interactive dashboards with Streamlit** ✨
- Generate reports and visualizations
- Share findings through collaborative workflows

### 🎯 NEW: Interactive Dashboard Feature

This branch adds a powerful Streamlit dashboard for visualizing economic data:
- Real-time interactive charts (GDP, Inflation, Unemployment)
- Dynamic date range filters
- Professional Plotly visualizations
- Perfect for presentations and analysis
>>>>>>> feature/dashboard-streamlit
```

### Understanding Conflict Markers

- `<<<<<<< HEAD`: Start of YOUR version (main branch)
- `=======`: Separator between versions
- `>>>>>>> feature/dashboard-streamlit`: End of THEIR version (feature branch)

---

## Step 5: Decide How to Resolve

You have three options:

### Option A: Keep Main Version Only
Delete the feature branch changes, keep only what's between `<<<<<<< HEAD` and `=======`

### Option B: Keep Feature Branch Version Only
Delete main branch changes, keep only what's between `=======` and `>>>>>>> feature/dashboard-streamlit`

### Option C: Combine Both (Recommended)
Keep the best parts of both versions

---

## Step 6: Resolve the Conflict

**Recommended Resolution** - Combine both:

1. Remove the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
2. Merge the content intelligently:

```markdown
## Project Overview

This repository simulates a real-world economic observatory where students collaborate to:
- Collect and track economic indicators
- Analyze economic data using Python/R
- Build interactive dashboards with Streamlit
- Generate reports and visualizations
- Share findings through collaborative workflows

### Interactive Dashboard Feature

This repository now includes a Streamlit dashboard for visualizing economic data:
- Real-time interactive charts (GDP, Inflation, Unemployment)
- Dynamic date range filters
- Professional Plotly visualizations
- Perfect for presentations and analysis
```

3. Do the same for the Quick Start section conflict

---

## Step 7: Mark as Resolved

After fixing all conflicts:

```bash
# Stage the resolved file
git add README.md

# Check status
git status
```

Should show:
```
On branch main
All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)
```

---

## Step 8: Complete the Merge

```bash
# Commit the merge
git commit -m "fix: merge feature/dashboard-streamlit into main

- Resolved README.md conflicts
- Combined dashboard features with main documentation
- Kept dashboard quick start option
- Maintained original project structure"
```

---

## Step 9: Verify the Merge

```bash
# View the merge in history
git log --oneline --graph --all --decorate

# Check that both branches are merged
git branch --merged
```

---

## Step 10: Test Everything Works

```bash
# Test the dashboard
streamlit run dashboard_app.py

# Verify documentation
cat DASHBOARD_FEATURES.md
```

---

## Common Mistakes to Avoid

### ❌ DON'T: Forget to remove conflict markers
```markdown
<<<<<<< HEAD
Some text
=======
Other text
>>>>>>> branch-name
```
This will show up in your file if you forget to remove markers!

### ❌ DON'T: Just pick one side blindly
Think about what makes sense to keep from each version

### ❌ DON'T: Commit without testing
Always test after resolving conflicts

### ✅ DO: Understand both changes
Read what each branch was trying to accomplish

### ✅ DO: Combine thoughtfully
Take the best from both versions

### ✅ DO: Test after merging
Make sure everything still works

---

## Alternative: Using a Merge Tool

Instead of manually editing, you can use a visual merge tool:

```bash
# Configure merge tool (e.g., VS Code)
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd 'code --wait $MERGED'

# Launch merge tool
git mergetool
```

---

## If You Need to Abort

Made a mistake? You can abort the merge:

```bash
# Abort the merge and start over
git merge --abort

# Your repository returns to pre-merge state
```

---

## Exercise Checklist

- [ ] Switched to main branch
- [ ] Attempted merge of feature/dashboard-streamlit
- [ ] Saw conflict error message
- [ ] Opened README.md and found conflict markers
- [ ] Understood what each version was changing
- [ ] Resolved conflicts by combining both versions
- [ ] Removed all conflict markers (<, =, >)
- [ ] Staged resolved files with `git add`
- [ ] Completed merge with `git commit`
- [ ] Verified merge in git log
- [ ] Tested that dashboard still works

---

## Key Takeaways

1. **Conflicts are normal** - They happen when two branches modify the same lines
2. **Conflict markers show both versions** - `<<<<<<<`, `=======`, `>>>>>>>`
3. **You decide the resolution** - Keep one, keep both, or create a new version
4. **Always test after resolving** - Make sure you didn't break anything
5. **Communicate with team** - If unsure, ask the person who made the other changes

---

## Next Steps

After successfully merging:
1. Delete the feature branch (optional): `git branch -d feature/dashboard-streamlit`
2. Push to GitHub: `git push origin main`
3. Share your merged code with the team

Congratulations! You've successfully resolved a merge conflict! 🎉

---

**Need help?** Ask your instructor or check [Git conflict resolution docs](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging#_basic_merge_conflicts)
