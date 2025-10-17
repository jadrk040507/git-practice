# Contributing to Economic Observatory

Thank you for contributing to the Economic Observatory project! This guide will help you understand how to contribute effectively.

## Project Goals

This repository serves as:
1. A learning platform for Git and GitHub
2. A collaborative economic data analysis project
3. A simulated professional research environment

## What You Can Contribute

### 1. Economic Data
- GDP, inflation, unemployment data
- Trade statistics
- Financial indicators
- Regional economic data
- Time series datasets

### 2. Analysis Scripts
- Python scripts for data processing
- R scripts for statistical analysis
- Data visualization code
- Economic modeling scripts

### 3. Reports
- Economic analysis reports
- Quarterly reviews
- Sector-specific studies
- Methodology documentation

### 4. Visualizations
- Charts and graphs
- Interactive dashboards
- Time series plots
- Comparative visualizations

### 5. Documentation
- Methodology explanations
- Tutorial improvements
- Data source documentation
- Code examples

---

## Contribution Workflow

### Step 1: Fork and Clone

```bash
# Fork on GitHub, then clone your fork
git clone https://github.com/YOUR-USERNAME/git-practice.git
cd git-practice
```

### Step 2: Create a Branch

Always create a feature branch for your work:

```bash
# For data contributions
git checkout -b data/mexico-gdp-q1-2024

# For analysis scripts
git checkout -b feature/inflation-analysis

# For reports
git checkout -b report/unemployment-quarterly

# For documentation
git checkout -b docs/update-methodology
```

**Branch Naming Conventions:**
- `data/description` - Adding or updating data
- `feature/description` - New analysis or functionality
- `report/description` - Writing or updating reports
- `docs/description` - Documentation changes
- `fix/description` - Bug fixes
- `viz/description` - Visualizations

### Step 3: Make Your Changes

Follow these guidelines:

#### For Data Files:
- Use CSV format for tabular data
- Include metadata header with source and date
- Name files descriptively: `mexico_gdp_2020-2024.csv`
- Keep files under 10MB
- Update relevant README files

Example CSV structure:
```csv
# Source: INEGI
# Date: 2024-01-15
# Unit: Millions of Pesos
Date,GDP,Growth_Rate
2020-Q1,23456789,2.3
2020-Q2,23567890,2.4
```

#### For Analysis Scripts:
- Use clear, descriptive function names
- Comment your code thoroughly
- Include docstrings for functions
- Cite data sources in comments
- Make scripts reproducible

Example Python script structure:
```python
"""
GDP Growth Analysis Script
Author: Your Name
Date: 2024-01-15
Data Source: INEGI
"""

import pandas as pd
import matplotlib.pyplot as plt

def load_gdp_data(filepath):
    """
    Load GDP data from CSV file.

    Args:
        filepath: Path to CSV file

    Returns:
        DataFrame with GDP data
    """
    # Implementation
    pass
```

#### For Reports:
- Write in Markdown format
- Use proper headings hierarchy
- Include data sources and citations
- Add visualizations with captions
- Keep language clear and professional

Example report structure:
```markdown
# Quarterly Economic Report - Q1 2024

## Executive Summary
Brief overview of key findings...

## Methodology
Data sources and analytical approach...

## Analysis
### GDP Growth
- Key findings
- Visualizations

### Inflation
- Key findings
- Visualizations

## Conclusions
Summary and implications...

## References
- Source 1
- Source 2
```

### Step 4: Commit Your Changes

Use [Conventional Commits](https://www.conventionalcommits.org/):

```bash
# Stage your changes
git add data/mexico_gdp_2024.csv

# Commit with descriptive message
git commit -m "data: add Mexico GDP data for Q1 2024

- Source: INEGI
- Includes quarterly figures
- Updated through March 2024"
```

**Commit Message Format:**
```
type: short description (50 chars max)

- Detailed point 1
- Detailed point 2
- References or sources
```

**Types:**
- `data:` - Data additions or updates
- `feat:` - New features or analysis
- `fix:` - Bug fixes
- `docs:` - Documentation updates
- `style:` - Code formatting
- `refactor:` - Code restructuring
- `test:` - Adding tests
- `chore:` - Maintenance tasks

### Step 5: Push to Your Fork

```bash
git push -u origin data/mexico-gdp-q1-2024
```

### Step 6: Create a Pull Request

1. Go to your fork on GitHub
2. Click "Compare & pull request"
3. Fill out the PR template:

```markdown
## Description
Brief description of your contribution

## Type of Change
- [ ] Data addition/update
- [ ] New analysis script
- [ ] Report
- [ ] Visualization
- [ ] Documentation
- [ ] Bug fix

## Data Sources
- List sources used
- Include URLs if available

## Testing
- [ ] Script runs without errors
- [ ] Data loads correctly
- [ ] Visualizations display properly

## Checklist
- [ ] Code follows project conventions
- [ ] Comments added where necessary
- [ ] Commit messages are clear
- [ ] No large files added (>10MB)
```

4. Submit the PR
5. Wait for review and address feedback

---

## Code Review Process

### For Contributors

When your PR is reviewed:
1. Respond to comments promptly
2. Make requested changes
3. Push updates to your branch
4. Request re-review when ready

### For Reviewers

When reviewing PRs:
1. Check code quality and documentation
2. Verify data sources
3. Test scripts locally
4. Provide constructive feedback
5. Approve when ready

**Review Checklist:**
- [ ] Code is well-documented
- [ ] Data sources are cited
- [ ] Scripts run without errors
- [ ] Commit messages follow conventions
- [ ] No sensitive data included
- [ ] Files are appropriately sized

---

## File Organization

### Data Files
```
data/
├── gdp/
│   ├── mexico_gdp_2020-2024.csv
│   └── usa_gdp_2020-2024.csv
├── inflation/
│   └── cpi_mexico_2024.csv
└── unemployment/
    └── unemployment_rates_2024.csv
```

### Analysis Scripts
```
analysis/
├── python/
│   ├── gdp_analysis.py
│   └── inflation_trends.py
└── r/
    └── unemployment_model.R
```

### Reports
```
reports/
├── 2024-Q1-quarterly-report.md
├── inflation-analysis-2024.md
└── templates/
    └── quarterly-report-template.md
```

---

## Quality Standards

### Data Quality
- Verify data sources are reputable
- Check for data completeness
- Ensure proper units are specified
- Include collection dates

### Code Quality
- Follow PEP 8 (Python) or tidyverse style guide (R)
- Write clear variable names
- Add comments for complex logic
- Make code reproducible

### Report Quality
- Use clear, professional language
- Cite all sources
- Include visualizations
- Proofread for errors

---

## Best Practices

### Before Starting Work
```bash
# Always pull latest changes
git checkout main
git pull origin main

# Then create your branch
git checkout -b feature/my-feature
```

### During Work
- Commit frequently with clear messages
- Keep commits focused and atomic
- Test your code before committing
- Update documentation as you go

### Before Submitting PR
- Review your own changes
- Test everything works
- Update relevant README files
- Check for sensitive information

### Working with Large Datasets
- Never commit files >10MB
- Use `.gitignore` for large raw data
- Provide download links instead
- Consider using Git LFS if necessary

---

## Common Scenarios

### Adding New Economic Indicator Data

1. Create branch: `git checkout -b data/new-indicator`
2. Add CSV to appropriate folder
3. Update data/README.md with description
4. Commit: `git commit -m "data: add [indicator] data for [period]"`
5. Push and create PR

### Creating Analysis Script

1. Create branch: `git checkout -b feature/analysis-name`
2. Write script in analysis/python/ or analysis/r/
3. Test thoroughly
4. Document functions and methodology
5. Commit: `git commit -m "feat: add [analysis] script"`
6. Push and create PR

### Writing Economic Report

1. Create branch: `git checkout -b report/topic-name`
2. Use template from reports/templates/
3. Add visualizations to reports/images/
4. Cite all data sources
5. Commit: `git commit -m "docs: add [topic] report"`
6. Push and create PR

---

## Commit Message Examples

**Good:**
```bash
git commit -m "data: add Mexico GDP data Q1-Q4 2024

- Source: INEGI quarterly reports
- Includes real and nominal figures
- All values in millions of pesos"
```

```bash
git commit -m "feat: create inflation analysis script

- Calculates CPI trends
- Generates time series visualizations
- Includes year-over-year comparisons"
```

**Bad:**
```bash
git commit -m "updated files"
git commit -m "fixed stuff"
git commit -m "gdp"
```

---

## Getting Help

### Questions About Contributing
- Open a Discussion on GitHub
- Ask in PR comments
- Contact your instructor/TA

### Technical Git Issues
- See README troubleshooting section
- Check [Git documentation](https://git-scm.com/doc)
- Search Stack Overflow

### Economic Data Questions
- Refer to resources/economic-data-sources.md
- Ask in Discussions
- Consult with peers

---

## Code of Conduct

### Be Respectful
- Treat all contributors with respect
- Provide constructive feedback
- Be patient with learning process
- Welcome questions and new contributors

### Be Collaborative
- Help others learn
- Share knowledge and resources
- Review PRs thoughtfully
- Communicate clearly

### Be Professional
- Keep discussions on-topic
- Avoid sensitive political debates
- Focus on data and methodology
- Maintain academic integrity

### Academic Integrity
- Cite all data sources properly
- Don't plagiarize code or analysis
- Give credit where due
- Be honest about uncertainties

---

## Recognition

Contributors will be recognized through:
- Commit history
- PR acknowledgments
- Contributors list
- Course credit (for students)

---

## Questions?

- **Git/GitHub Issues**: Open an issue with `question` label
- **Economic Data**: Post in Discussions
- **Course-Related**: Contact your instructor

---

## Additional Resources

- [Conventional Commits](https://www.conventionalcommits.org/)
- [Writing Good Commit Messages](https://chris.beams.io/posts/git-commit/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Code Review Best Practices](https://google.github.io/eng-practices/review/)

---

Thank you for contributing to the Economic Observatory! Your work helps everyone learn and builds a valuable resource for economic analysis.

Happy collaborating!
