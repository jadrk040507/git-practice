# Git Command Cheatsheet

## Setup
```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

## Starting a Repository
```bash
git init                    # Initialize new repo
git clone <url>            # Clone existing repo
```

## Basic Snapshotting
```bash
git status                 # Check status
git add <file>            # Stage specific file
git add .                 # Stage all changes
git commit -m "message"   # Commit staged changes
git commit -am "message"  # Stage and commit tracked files
```

## Branching & Merging
```bash
git branch                    # List branches
git branch <name>            # Create branch
git checkout <name>          # Switch branch
git checkout -b <name>       # Create and switch
git merge <branch>           # Merge branch into current
git branch -d <name>         # Delete branch
```

## Sharing & Updating
```bash
git push origin <branch>     # Push to remote
git pull origin <branch>     # Fetch and merge
git fetch origin            # Download remote changes
git remote -v               # List remotes
```

## Inspection & Comparison
```bash
git log                     # View commit history
git log --oneline          # Compact log
git diff                   # Show unstaged changes
git diff --staged          # Show staged changes
```

## Undo Changes
```bash
git restore <file>                # Discard changes
git restore --staged <file>       # Unstage
git commit --amend               # Modify last commit
git revert <commit>              # Create new commit that undoes
git reset --hard HEAD~1          # Delete last commit (⚠️)
```

## Stashing
```bash
git stash                   # Save changes temporarily
git stash pop              # Apply and remove stash
git stash list             # List all stashes
git stash drop             # Delete most recent stash
```

## Tips
- Commit often!
- Write clear commit messages
- Always pull before push
- Use branches for features
- Never commit secrets/passwords