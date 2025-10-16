# Exercise 3: Collaboration Simulation

## Objective
Practice the full GitHub workflow including conflicts.

## Part 1: The Happy Path

1. **Create a collaboration file**
```bash
   git checkout -b feature/collaboration
   echo "Collaborator 1: [Your name]" > collaboration.txt
   git add collaboration.txt
   git commit -m "feat: start collaboration file"
   git push -u origin feature/collaboration
```

2. **Merge it**
```bash
   git checkout main
   git merge feature/collaboration
   git push origin main
```

## Part 2: Creating a Conflict

1. **In main branch:**
```bash
   git checkout main
   echo "Version from main" > conflict-test.txt
   git add conflict-test.txt
   git commit -m "docs: add conflict test from main"
```

2. **Create feature branch from older commit:**
```bash
   git checkout -b feature/will-conflict HEAD~1
   echo "Version from feature" > conflict-test.txt
   git add conflict-test.txt
   git commit -m "docs: add conflict test from feature"
```

3. **Try to merge (will fail!):**
```bash
   git checkout main
   git merge feature/will-conflict
```

4. **Resolve the conflict:**
   - Open `conflict-test.txt`
   - Choose which version to keep (or combine them)
   - Remove conflict markers
```bash
   git add conflict-test.txt
   git commit -m "fix: resolve conflict in conflict-test.txt"
   git push origin main
```

## Success Criteria
- [ ] Created and merged a feature branch
- [ ] Intentionally created a conflict
- [ ] Successfully resolved the conflict
- [ ] Understand conflict markers

## Reflection Questions
1. What do the conflict markers mean?
2. How could conflicts be prevented?
3. When should you use `git fetch` vs `git pull`?