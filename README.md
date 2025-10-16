# Git and GitHub practice repository

This is a practice repository built so you can practice your Git and GitHub skills. This is meant to be tweaked and even breaked, so no worries if you mess up.

# Git and GitHub Practice Repository

This is a practice repository built so you can practice your Git and GitHub skills. This is meant to be tweaked and even broken, so no worries if you mess up!

## 🎯 Learning Objectives

By the end of this practice, you will know how to:
- Fork a repository
- Clone a repository to your local machine
- Create and modify files
- Use the staging area (git add)
- Make commits with good messages
- Amend commits
- Push changes to GitHub
- Revert commits
- Create and switch between branches
- Merge branches
- Handle basic merge conflicts

---

## 📚 Step-by-Step Guide

### **Step 1: Fork this Repository**

Forking creates your own copy of this repository on your GitHub account.

**Instructions:**
1. Click the "Fork" button at the top-right of this page
2. Select your account as the destination
3. Wait for GitHub to create your fork
4. You now have your own copy at: `https://github.com/YOUR-USERNAME/git-practice`

✅ **Checkpoint:** You should see this repository under your GitHub profile.

---

### **Step 2: Clone Your Fork**

Cloning downloads the repository to your computer.

**Using GitHub Desktop:**
1. Open GitHub Desktop
2. File → Clone Repository
3. Find your fork in the list
4. Choose where to save it on your computer
5. Click "Clone"

**Using Command Line:**
```bash
# Navigate to where you want the project
cd ~/Desktop

# Clone your fork (replace YOUR-USERNAME)
git clone https://github.com/YOUR-USERNAME/git-practice.git

# Enter the directory
cd git-practice
```

✅ **Checkpoint:** You should see the `git-practice` folder on your computer.

---

### **Step 3: Explore the Repository**

Take a look at what's in this repository.
```bash
# See all files (including hidden ones)
ls -la

# Check Git status
git status

# See branches
git branch

# See remote connections
git remote -v
```

You should see:
- `README.md` (this file)
- `students/` folder
- `.gitignore` file
- Connection to your fork (origin)

---

### **Step 4: Pull Latest Changes**

Always pull before starting work to make sure you have the latest version.

**Using GitHub Desktop:**
- Click "Fetch origin" button
- If there are updates, click "Pull origin"

**Using Command Line:**
```bash
git pull origin main
```

✅ **Checkpoint:** Message should say "Already up to date" (if no changes) or show downloaded changes.

---

### **Step 5: Create Your Profile File**

Now let's add your information to the repository!

1. Navigate to the `students/` folder
2. Create a new file named: `your-name.txt` (replace with your actual name)
3. Add the following information:
```
Name: Your Full Name
Favorite Programming Language: 
What I want to learn: 
Fun fact about me: 
```

**Example:** `students/juan-diaz.txt`
```
Name: Juan Álvaro Díaz
Favorite Programming Language: JavaScript
What I want to learn: How to contribute to open source
Fun fact about me: I love coffee ☕
```

✅ **Checkpoint:** Your file exists in the `students/` folder.

---

### **Step 6: Check Status**

Let's see what Git thinks about our changes.
```bash
git status
```

You should see:
```
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        students/your-name.txt
```

This means Git sees the file but isn't tracking it yet.

---

### **Step 7: Stage Your Changes (git add)**

Staging prepares files to be committed.

**Using GitHub Desktop:**
- Your file appears in the left sidebar
- It's automatically checked (staged)

**Using Command Line:**
```bash
# Stage your specific file
git add students/your-name.txt

# OR stage all changes
git add .
```

Check status again:
```bash
git status
```

Now you should see:
```
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   students/your-name.txt
```

✅ **Checkpoint:** Your file is now in the "staged" state (green in terminal).

---

### **Step 8: Make Your First Commit**

A commit saves your staged changes with a message.

**Using GitHub Desktop:**
1. Write a commit message in the bottom-left: `feat: add [your name] profile`
2. Click "Commit to main"

**Using Command Line:**
```bash
git commit -m "feat: add juan diaz profile"
```

✅ **Checkpoint:** Run `git log` to see your commit in the history.
```bash
git log --oneline
```

---

### **Step 9: Push to GitHub**

Pushing uploads your local commits to GitHub.

**Using GitHub Desktop:**
- Click "Push origin" button at the top

**Using Command Line:**
```bash
git push origin main
```

✅ **Checkpoint:** Go to your fork on GitHub and refresh. You should see your new file in the `students/` folder!

---

### **Step 10: Amend Your Last Commit**

Oops! Let's say you forgot to add something. You can amend the last commit.

1. Open your profile file again
2. Add a new line: `GitHub Username: your-username`
3. Save the file

Now amend the commit:

**Using Command Line:**
```bash
# Stage the change
git add students/your-name.txt

# Amend the last commit (keeps the same message)
git commit --amend --no-edit

# OR change the message too
git commit --amend -m "feat: add complete profile for juan diaz"

# Force push (needed after amend)
git push --force origin main
```

⚠️ **Warning:** Only amend commits that haven't been pushed, or use `--force` carefully!

✅ **Checkpoint:** Your commit now includes the additional information.

---

### **Step 11: Create a New Branch**

Branches let you work on features without affecting the main code.

**Using GitHub Desktop:**
1. Click "Current Branch" dropdown at the top
2. Click "New Branch"
3. Name it: `feature/add-hobby`
4. Click "Create Branch"

**Using Command Line:**
```bash
# Create and switch to new branch
git checkout -b feature/add-hobby

# Verify you're on the new branch
git branch
```

You should see:
```
  main
* feature/add-hobby
```

The `*` shows your current branch.

✅ **Checkpoint:** You're now on the `feature/add-hobby` branch.

---

### **Step 12: Make Changes in Your Feature Branch**

Let's add a hobby file!

1. Create a new file: `hobbies/your-name-hobbies.txt`
2. Add your hobbies:
```
My Hobbies:
- Reading
- Coding
- Playing guitar
- Hiking
```

3. Stage and commit:
```bash
git add hobbies/your-name-hobbies.txt
git commit -m "feat: add my hobbies"
```

4. Push the new branch:

**GitHub Desktop:** Click "Publish branch"

**Command Line:**
```bash
git push -u origin feature/add-hobby
```

✅ **Checkpoint:** Your new branch exists on GitHub with your hobbies file.

---

### **Step 13: Switch Back to Main Branch**

Let's see what happens when we switch branches.

**Using GitHub Desktop:**
- Click "Current Branch" dropdown
- Select "main"

**Using Command Line:**
```bash
git checkout main
```

Look at your file system - the `hobbies/` folder disappeared! Don't worry, it's safe in your feature branch.

✅ **Checkpoint:** You're back on main, and your hobbies file isn't visible.

---

### **Step 14: Merge Your Feature Branch**

Now let's bring your hobbies into the main branch.

**Using Command Line:**
```bash
# Make sure you're on main
git checkout main

# Merge the feature branch
git merge feature/add-hobby

# Push the merge
git push origin main
```

**Using GitHub Desktop:**
1. Make sure you're on "main" branch
2. Click "Branch" menu → "Merge into current branch"
3. Select "feature/add-hobby"
4. Click "Merge"
5. Click "Push origin"

✅ **Checkpoint:** Your hobbies file now appears in the main branch!

---

### **Step 15: Practice Reverting a Commit**

Let's say you made a mistake and want to undo a commit.

First, let's make a "mistake":

1. Edit `README.md` and add at the bottom: `This is a mistake!`
2. Commit:
```bash
git add README.md
git commit -m "docs: accidentally added wrong text"
git push origin main
```

Now let's revert it:
```bash
# See your commits
git log --oneline

# Copy the commit hash of the mistake (first 7 characters)
# For example: abc1234

# Revert it
git revert abc1234

# This opens an editor - save and close
# OR use --no-edit to skip:
git revert abc1234 --no-edit

# Push the revert
git push origin main
```

✅ **Checkpoint:** The mistake text is gone, but the commit history shows what happened.

---

### **Step 16: Create and Resolve a Merge Conflict**

Let's intentionally create a conflict to learn how to resolve it.

**Set up the conflict:**

1. **In main branch:**
```bash
git checkout main
echo "Main branch version" > conflict-practice.txt
git add conflict-practice.txt
git commit -m "docs: add conflict practice file from main"
git push origin main
```

2. **Create and switch to a new branch:**
```bash
git checkout -b feature/conflict-demo
```

3. **Go back to main and make a change:**
```bash
git checkout main
echo "This was written in main branch" > conflict-practice.txt
git add conflict-practice.txt
git commit -m "docs: update conflict file in main"
```

4. **Switch to feature branch and make conflicting change:**
```bash
git checkout feature/conflict-demo
echo "This was written in feature branch" > conflict-practice.txt
git add conflict-practice.txt
git commit -m "docs: update conflict file in feature"
```

5. **Try to merge (this will create a conflict!):**
```bash
git checkout main
git merge feature/conflict-demo
```

You'll see:
```
CONFLICT (content): Merge conflict in conflict-practice.txt
Automatic merge failed; fix conflicts and then commit the result.
```

**Resolve the conflict:**

1. Open `conflict-practice.txt` - you'll see:
```
<<<<<<< HEAD
This was written in main branch
=======
This was written in feature branch
>>>>>>> feature/conflict-demo
```

2. Edit the file to keep what you want:
```
This was written in main branch
This was written in feature branch
(Both versions combined!)
```

3. Remove the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)

4. Stage and commit:
```bash
git add conflict-practice.txt
git commit -m "fix: resolve merge conflict in conflict-practice.txt"
git push origin main
```

✅ **Checkpoint:** Conflict resolved! You combined both versions.

---

## 🎓 Bonus Challenges

Once you've completed all steps, try these:

### Challenge 1: Update from Upstream
If the original repository (the one you forked) gets updates, fetch them:
```bash
# Add the original repo as "upstream"
git remote add upstream https://github.com/ORIGINAL-OWNER/git-practice.git

# Fetch updates
git fetch upstream

# Merge updates into your main
git checkout main
git merge upstream/main
git push origin main
```

### Challenge 2: Create a Pull Request
1. Create a new branch with a feature
2. Push it to your fork
3. Go to GitHub and click "Compare & pull request"
4. Submit it to the original repository

### Challenge 3: Clean Up Branches
```bash
# List all branches
git branch -a

# Delete local branch
git branch -d feature/add-hobby

# Delete remote branch
git push origin --delete feature/add-hobby
```

### Challenge 4: Interactive Rebase
```bash
# Reorganize your last 3 commits
git rebase -i HEAD~3
```

---

## 📋 Quick Command Reference
```bash
# Status and Information
git status                  # Check current state
git log                     # See commit history
git log --oneline          # Compact commit history
git branch                 # List branches
git remote -v              # See remote connections

# Basic Workflow
git pull origin main       # Get latest changes
git add .                  # Stage all changes
git commit -m "message"    # Commit staged changes
git push origin main       # Upload to GitHub

# Branching
git branch branch-name     # Create branch
git checkout branch-name   # Switch branch
git checkout -b branch-name # Create and switch
git merge branch-name      # Merge into current branch
git branch -d branch-name  # Delete branch

# Undoing Things
git restore file.txt       # Discard changes
git restore --staged file.txt # Unstage
git commit --amend         # Modify last commit
git revert commit-hash     # Undo a commit safely
git reset --hard HEAD~1    # Delete last commit (⚠️ dangerous)

# Stashing (save work temporarily)
git stash                  # Save current changes
git stash pop              # Restore stashed changes
git stash list             # See all stashes
```

---

## 🆘 Help! Something Went Wrong

### "I'm on the wrong branch!"
```bash
git checkout correct-branch
```

### "I committed but forgot to add a file!"
```bash
git add forgotten-file.txt
git commit --amend --no-edit
```

### "I want to undo my last commit!"
```bash
# If you haven't pushed:
git reset --soft HEAD~1

# If you already pushed:
git revert HEAD
```

### "I have merge conflicts and I'm scared!"
1. Don't panic! Open the file
2. Look for `<<<<<<<`, `=======`, `>>>>>>>`
3. Decide what to keep
4. Delete the markers
5. `git add file.txt`
6. `git commit -m "fix: resolve conflict"`

### "How do I get back to a clean state?"
```bash
# Discard ALL local changes (⚠️ cannot be undone!)
git reset --hard HEAD
git clean -fd
```

---

## 🎉 Congratulations!

You've now practiced:
- ✅ Forking a repository
- ✅ Cloning to your machine
- ✅ Creating files
- ✅ Staging changes (git add)
- ✅ Making commits
- ✅ Amending commits
- ✅ Pushing to GitHub
- ✅ Reverting commits
- ✅ Creating branches
- ✅ Switching branches
- ✅ Merging branches
- ✅ Resolving conflicts

You're ready to start using Git and GitHub in real projects! 🚀

---

## 📚 Additional Resources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Learn Git Branching](https://learngitbranching.js.org/)
- [First Contributions](https://github.com/firstcontributions/first-contributions)

---

**Remember:** Making mistakes is part of learning Git. This repository is your sandbox - experiment, break things, and learn! 💪