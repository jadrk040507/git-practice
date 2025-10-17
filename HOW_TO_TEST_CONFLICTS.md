# How to Test Merge Conflicts - Student Perspective

## 🎯 Current Setup

### `main` Branch (No Dashboard)
- Focus on R scripts and traditional Git learning
- README promotes Git basics first
- **No dashboard files** - students learn Git with R scripts only

### `feature/dashboard-streamlit` Branch (Has Dashboard)
- Contains `dashboard_app.py` - the Streamlit dashboard
- Contains `DASHBOARD_FEATURES.md` - dashboard documentation
- README promotes dashboard-first learning
- **Dashboard files only exist here**

---

## 🧪 Testing the Merge Conflict

### Step 1: Clone and Check Main Branch

```bash
# Clone the repository
git clone https://github.com/YOUR-USERNAME/git-practice.git
cd git-practice

# Verify you're on main
git branch
# * main

# Check for dashboard - should NOT exist!
ls -la | grep dashboard
# (no results)
```

✅ **Expected**: NO dashboard files in main

---

### Step 2: Discover the Feature Branch

```bash
# List all branches including remote
git branch -a

# Output:
# * main
#   remotes/origin/HEAD -> origin/main
#   remotes/origin/feature/dashboard-streamlit
#   remotes/origin/main
```

✅ **Expected**: See `feature/dashboard-streamlit` branch exists

---

### Step 3: Inspect the Feature Branch

```bash
# View what's different in the feature branch
git log --oneline --graph --all --decorate

# See the divergence
git diff main feature/dashboard-streamlit --name-only
```

✅ **Expected**: See README.md, dashboard_app.py, and other differences

---

### Step 4: Attempt the Merge

```bash
# Make sure you're on main
git checkout main

# Try to merge the feature branch
git merge feature/dashboard-streamlit
```

**💥 BOOM! Merge Conflict!**

```
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

✅ **Expected**: Conflict in README.md

---

### Step 5: Check What Happened

```bash
# See status
git status
```

**Output:**
```
On branch main
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Changes to be committed:
        new file:   DASHBOARD_FEATURES.md
        new file:   dashboard_app.py

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   README.md
```

✅ **Analysis**:
- ✅ `dashboard_app.py` - Will be added (no conflict, only in feature)
- ✅ `DASHBOARD_FEATURES.md` - Will be added (no conflict, only in feature)
- ❌ `README.md` - **CONFLICT!** (modified in both branches)

---

### Step 6: Examine the Conflict

```bash
# Open README.md in editor
code README.md
# or
vim README.md
# or
nano README.md
```

**You'll see conflict markers:**

```markdown
<<<<<<< HEAD
# Economic Observatory - Git & GitHub Practice Repository

This repository simulates a real-world economic observatory where students collaborate to:
- Collect and track economic indicators from INEGI
- Analyze economic data using R programming
- Generate professional reports and visualizations
=======
# Economic Observatory - Interactive Data Visualization Platform

This repository is a complete economic data visualization platform where students:
- **Build interactive Streamlit dashboards** with real-time data
- **Visualize economic trends** using Plotly and modern charting libraries
>>>>>>> feature/dashboard-streamlit
```

---

### Step 7: Resolve the Conflict

**Option A: Keep Main Version (Simple)**
```markdown
# Economic Observatory - Git & GitHub Practice Repository

This repository simulates a real-world economic observatory where students collaborate to:
- Collect and track economic indicators from INEGI
- Analyze economic data using R programming
- Generate professional reports and visualizations
```

**Option B: Keep Feature Version (Dashboard-focused)**
```markdown
# Economic Observatory - Interactive Data Visualization Platform

This repository is a complete economic data visualization platform where students:
- **Build interactive Streamlit dashboards** with real-time data
- **Visualize economic trends** using Plotly and modern charting libraries
```

**Option C: Combine Both (Recommended)**
```markdown
# Economic Observatory - Git & GitHub Practice Repository

This repository is an economic data analysis platform where students:
- Collect and track economic indicators from INEGI
- Analyze economic data using R programming
- **Build interactive Streamlit dashboards** for visualization
- Generate professional reports and visualizations
- Share findings through collaborative Git workflows
```

---

### Step 8: Complete the Merge

```bash
# After removing ALL conflict markers and saving README.md

# Stage the resolved file
git add README.md

# Complete the merge
git commit -m "fix: merge dashboard feature into main

- Resolved README.md conflicts
- Combined R workflow with dashboard features
- Added dashboard_app.py to main branch
- Integrated dashboard documentation"

# Check the result
git log --oneline --graph --all -10
```

✅ **Success**: Merge completed!

---

### Step 9: Test the Dashboard

```bash
# Now dashboard should exist in main!
ls -la | grep dashboard
# dashboard_app.py
# DASHBOARD_FEATURES.md

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run dashboard_app.py
```

✅ **Expected**: Dashboard opens at http://localhost:8501

---

## 📚 What Students Learn

### Technical Skills
1. **Discovering branches**: `git branch -a`
2. **Viewing differences**: `git diff branch1 branch2`
3. **Merging branches**: `git merge branch-name`
4. **Identifying conflicts**: Reading `git status`
5. **Resolving conflicts**: Editing files, removing markers
6. **Completing merge**: `git add`, `git commit`

### Conceptual Understanding
1. **Why conflicts happen**: Same file, different changes
2. **Conflict anatomy**: `<<<<<<<`, `=======`, `>>>>>>>`
3. **Decision making**: Which version to keep?
4. **Testing results**: Does it still work after merge?
5. **Team collaboration**: How to coordinate changes

---

## 🔍 Debugging Common Issues

### Issue 1: "Already up to date"

**Problem**: Merge says "Already up to date" - no conflict

**Cause**: You're trying to merge main into feature (wrong direction)

**Solution**:
```bash
git checkout main           # Switch to main
git merge feature/dashboard-streamlit  # Merge feature INTO main
```

---

### Issue 2: No Conflict Appears

**Problem**: Files merge without conflict

**Cause**: Branches aren't diverged properly

**Check**:
```bash
git log --oneline --graph --all
# Should see branches split from a common ancestor
```

---

### Issue 3: Dashboard Still in Main

**Problem**: Dashboard files exist in main before merge

**Cause**: Dashboard wasn't removed from main

**Solution**:
```bash
git checkout main
git rm dashboard_app.py DASHBOARD_FEATURES.md
git commit -m "remove dashboard from main"
git push origin main
```

---

## 🎓 Exercise Workflow for Students

### As Part of Exercise 5

**Context**: Students have completed Exercises 1-4, learning Git basics and running R scripts.

**Exercise 5 Steps**:

1. **Discover the feature branch**
   ```bash
   git branch -a
   # Oh! There's a feature/dashboard-streamlit branch!
   ```

2. **Read about it**
   - Check Exercise 5 instructions
   - Learn about branches and merging

3. **Attempt the merge**
   ```bash
   git merge feature/dashboard-streamlit
   # CONFLICT!
   ```

4. **Don't panic!**
   - Read [MERGE_CONFLICT_EXERCISE.md](MERGE_CONFLICT_EXERCISE.md)
   - Follow step-by-step instructions

5. **Resolve the conflict**
   - Open README.md
   - Understand both versions
   - Decide what to keep
   - Remove conflict markers
   - Save file

6. **Complete the merge**
   ```bash
   git add README.md
   git commit -m "fix: resolve merge conflict"
   ```

7. **Test the result**
   ```bash
   streamlit run dashboard_app.py
   # Success! Dashboard works!
   ```

---

## ✅ Success Criteria

Students have successfully completed the exercise when:

- [ ] Can explain why the conflict happened
- [ ] Successfully identified all conflict markers
- [ ] Made an informed decision about what to keep
- [ ] Removed all conflict markers from README.md
- [ ] Completed the merge commit
- [ ] Dashboard runs successfully after merge
- [ ] `git status` shows clean working tree
- [ ] Can explain the process to a peer

---

## 🎯 Expected Outcomes

After this exercise, students will:

✅ **Understand** what causes merge conflicts
✅ **Recognize** conflict markers in files
✅ **Read** both versions critically
✅ **Decide** what content to keep
✅ **Resolve** conflicts independently
✅ **Complete** merges successfully
✅ **Feel confident** about future conflicts

---

## 📊 Instructor Notes

### Why This Design?

1. **Real consequence**: Dashboard only exists after successful merge
2. **Meaningful decision**: Both README versions have merit
3. **Visible result**: Can see/test dashboard after merge
4. **Authentic scenario**: Like merging a feature branch in real work
5. **Progressive difficulty**: README conflict is manageable for beginners

### Grading Rubric

- **50%**: Correctly resolved all conflict markers
- **20%**: README.md is valid Markdown after resolution
- **15%**: Merge commit has descriptive message
- **10%**: Dashboard runs successfully after merge
- **5%**: Can explain the process

---

## 🚀 Next Steps

After successfully merging:

1. **Clean up**: Delete the feature branch (optional)
   ```bash
   git branch -d feature/dashboard-streamlit
   ```

2. **Push to GitHub**:
   ```bash
   git push origin main
   ```

3. **Explore the dashboard**: Modify it, add features

4. **Practice again**: Create your own feature branch with intentional conflicts

---

**Status**: ✅ Ready for Student Testing

**Last Updated**: 2024-10-16

**Tested By**: Instructor

**Conflict Confirmed**: YES - README.md in main vs feature branches
