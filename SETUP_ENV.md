# Setting Up Environment Variables

This guide explains how to configure API keys and environment variables for the Economic Observatory project.

## Why Use Environment Variables?

Environment variables keep sensitive information (API keys, passwords) secure by:
- **NOT committing them to Git** (they're in `.gitignore`)
- **Keeping them local** to your machine
- **Easy to update** without changing code

---

## Quick Setup

### Step 1: Copy the Template

```bash
# Copy the example file to create your .env file
cp .env.example .env
```

### Step 2: Edit the `.env` File

Open `.env` in your text editor and add your actual API keys:

```bash
# Example .env file
FRED_API_KEY=your_actual_fred_api_key_here
WORLD_BANK_API_KEY=your_actual_key_here
INEGI_API_KEY=your_actual_key_here
```

**Important**: Replace `your_actual_fred_api_key_here` with your real API key!

### Step 3: Verify It's Ignored by Git

```bash
# This should show .env is ignored
git status

# .env should NOT appear in the list
```

✅ The `.env` file should never be committed to Git!

---

## Getting API Keys

### FRED API (Federal Reserve Economic Data)

1. Go to: https://fred.stlouisfed.org/
2. Create a free account
3. Navigate to: https://fred.stlouisfed.org/docs/api/api_key.html
4. Request an API key
5. Copy the key to your `.env` file

**Example:**
```bash
FRED_API_KEY=abcdef1234567890abcdef1234567890
```

### World Bank API

The World Bank API is free and doesn't require authentication for most endpoints. You can leave this blank or use it for future enhancements.

```bash
WORLD_BANK_API_KEY=
```

### INEGI API (Mexico)

1. Go to: https://www.inegi.org.mx/
2. Check if API access is available
3. Follow their documentation for API keys
4. Add to `.env` file

```bash
INEGI_API_KEY=your_inegi_key_here
```

---

## Using Environment Variables

### In R Scripts

All R scripts in this project use the `dotenv` package:

```r
library(dotenv)

# Load environment variables from .env file
load_dot_env()

# Access variables
api_key <- Sys.getenv("FRED_API_KEY")
```

**Install dotenv package:**
```r
install.packages("dotenv")
```

### In Python Scripts

All Python scripts use the `python-dotenv` package:

```python
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access variables
api_key = os.getenv("FRED_API_KEY")
```

**Install python-dotenv:**
```bash
pip install python-dotenv
```

---

## File Structure

```
git-practice/
├── .env                 # YOUR API keys (DO NOT COMMIT!)
├── .env.example         # Template (safe to commit)
├── .gitignore          # Ensures .env is not tracked
└── analysis/
    ├── r/
    │   └── fetch_fred_data.R    # Uses Sys.getenv()
    └── python/
        └── fetch_worldbank_data.py    # Uses os.getenv()
```

---

## Troubleshooting

### Error: "API key not found"

**Problem**: Script can't find your API key

**Solutions**:
1. Make sure `.env` file exists in project root
2. Check variable name matches: `FRED_API_KEY=...` (no spaces!)
3. Verify you called `load_dot_env()` (R) or `load_dotenv()` (Python)
4. Try absolute path if needed

### Error: "Permission denied"

**Problem**: File permissions issue

**Solution**:
```bash
chmod 600 .env
```

### Keys Not Loading

**R - Check if loaded:**
```r
library(dotenv)
load_dot_env()
print(Sys.getenv("FRED_API_KEY"))  # Should print your key
```

**Python - Check if loaded:**
```python
from dotenv import load_dotenv
import os
load_dotenv()
print(os.getenv("FRED_API_KEY"))  # Should print your key
```

### .env File in Git

**Problem**: Accidentally committed `.env` to Git

**Solution**:
```bash
# Remove from Git but keep locally
git rm --cached .env

# Commit the removal
git commit -m "fix: remove .env from git tracking"

# Make sure .gitignore has .env
echo ".env" >> .gitignore
git add .gitignore
git commit -m "chore: ensure .env is ignored"
```

---

## Best Practices

### ✅ DO:
- Keep `.env` in `.gitignore`
- Use `.env.example` as template for team
- Rotate keys if accidentally exposed
- Use different keys for dev/production
- Document required variables in `.env.example`

### ❌ DON'T:
- Commit `.env` to Git
- Share API keys in Slack/email
- Hardcode keys in scripts
- Use production keys for testing
- Commit API keys in code comments

---

## Example Workflow

### Scenario: New Team Member Joining

1. **New member clones repo:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/git-practice.git
   cd git-practice
   ```

2. **They see `.env.example` but no `.env`:**
   ```bash
   ls -la | grep env
   # .env.example  ← Template provided
   # .env          ← Missing! They need to create it
   ```

3. **They create their own `.env`:**
   ```bash
   cp .env.example .env
   # Edit .env with their own API keys
   ```

4. **They can now run scripts:**
   ```r
   # R
   source("analysis/r/fetch_fred_data.R")
   ```

   ```bash
   # Python
   python analysis/python/fetch_worldbank_data.py
   ```

---

## Security Checklist

Before pushing code:

- [ ] `.env` is in `.gitignore`
- [ ] No API keys hardcoded in scripts
- [ ] `.env.example` doesn't contain real keys
- [ ] `git status` doesn't show `.env`
- [ ] No keys in commit messages

---

## Additional Resources

- [dotenv R package](https://github.com/gaborcsardi/dotenv)
- [python-dotenv docs](https://pypi.org/project/python-dotenv/)
- [12 Factor App - Config](https://12factor.net/config)
- [GitHub: Removing sensitive data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)

---

**Questions?** Ask your instructor or open an issue!
