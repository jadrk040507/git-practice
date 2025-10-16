# Exercise 2: Working with Branches

## Objective
Create a feature branch and add your hobbies.

## Steps

1. **Create a new branch**
```bash
   git checkout -b feature/add-hobbies
```

2. **Create your hobbies file**
   - Navigate to `hobbies/` folder
   - Create: `your-name-hobbies.txt`
   - List 3-5 hobbies

3. **Commit your changes**
```bash
   git add hobbies/your-name-hobbies.txt
   git commit -m "feat: add my hobbies list"
```

4. **Push your branch**
```bash
   git push -u origin feature/add-hobbies
```

5. **Merge into main**
```bash
   git checkout main
   git merge feature/add-hobbies
   git push origin main
```

## Success Criteria
- [ ] Created a feature branch
- [ ] Added hobbies file
- [ ] Successfully merged into main
- [ ] Both branches show on GitHub

## Bonus Challenge
- Create another branch for favorite books/movies
- Practice switching between branches