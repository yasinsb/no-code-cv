# Usage Guide: No-Code Resume Builder

Comprehensive guide for using and customizing the template-based resume system.

## 📊 Excel Structure

### Core Sheets (Required)

#### 1. `header` Sheet
| Field | Value |
|-------|-------|
| name | Your Full Name |
| phone | +1 (555) 123-4567 |
| email | your.email@example.com |
| linkedin | linkedin.com/in/yourprofile |

**Format**: 2 columns, no headers, field name in column A, value in column B

#### 2. `summary` Sheet  
| Summary Text |
|--------------|
| Your professional summary in one cell. Brief overview of expertise, experience, and value proposition. |

**Format**: Single cell (A1), no header

#### 3. `experience` Sheet
| Title | Company | Location | Start Date | End Date | Bullet 1 | Bullet 2 | Bullet 3 | ... |
|-------|---------|----------|------------|----------|----------|----------|----------|-----|
| Senior Engineer | TechCorp | SF, CA | 2020 | Present | Achievement 1 | Achievement 2 | Achievement 3 | ... |
| Engineer | StartupXYZ | NY, NY | 2017 | 2020 | Achievement 1 | Achievement 2 | | |

**Format**: No headers, columns 1-5 are structured, columns 6+ are bullet points

#### 4. `education` Sheet
| Degree | Institution | Location | Start Year | End Year | Bullet 1 | Bullet 2 | ... |
|--------|-------------|----------|------------|----------|----------|----------|-----|
| BS Computer Science | MIT | Boston, MA | 2013 | 2017 | Focus area... | Coursework... | |

**Format**: No headers, columns 1-5 are structured, columns 6+ are details

#### 5. `skills` Sheet
| Category | Skills |
|----------|--------|
| Programming & Frameworks | Python, JavaScript, React, Node.js |
| Tools & Technologies | Git, Docker, AWS, PostgreSQL |

**Format**: No headers, 2 columns (category and comma-separated skills)

#### 6. `volunteering` Sheet
| Role | Organization | Dates |
|------|--------------|-------|
| Tech Mentor | Local Nonprofit | 2021 - Present |

**Format**: No headers, 3 columns

---

### Custom Sheets (Optional)

Add any section by creating a new sheet with your desired name.

#### Type 1: Simple List (1 column)
**Example: "Hobbies" sheet**
```
A1: Gardening
A2: Playing Board Games
A3: Reading Science Fiction
```

**Renders as:**
```
HOBBIES
• Gardening
• Playing Board Games  
• Reading Science Fiction
```

#### Type 2: Two-Column List (Label + Description)
**Example: "Certificates" sheet**
```
A1: Python Programming    B1: Python A to Z by Coursera
A2: Project Management    B2: Intro to PM - PMI 2022
```

**Renders as:**
```
CERTIFICATES
• Python Programming: Python A to Z by Coursera
• Project Management: Intro to PM - PMI 2022
```

---

## 🎨 Customizing Templates

### Modifying Existing Sections

Edit files in `templates/latex/includes/`:

**Example: Change experience format**

File: `templates/latex/includes/experience.tex.j2`
```latex
<<% for job in jobs %>>
\begin{resumeitem}{<<job.title>>}{<<job.start_date>> -- <<job.end_date>>}{<<job.company>>}{<<job.location>>}
<<% for bullet in job.bullets %>>
\item <<bullet>>
<<% endfor %>>
\end{resumeitem}
<<% endfor %>>
```

**Customize:**
- Change `\begin{resumeitem}` arguments order
- Add conditional sections
- Modify spacing or formatting
- Add new LaTeX commands

### Adding New Template Logic

Edit `scripts/generate_resume.py`:

**Example: Add a new core section**

1. Create template: `templates/latex/includes/projects.tex.j2`
2. Add reader function:
```python
def read_projects(df):
    """Read projects data."""
    projects = []
    for _, row in df.iterrows():
        if pd.isna(row.iloc[0]):
            continue
        project = {
            'name': escape_latex(row.iloc[0]),
            'description': escape_latex(row.iloc[1]),
            'tech': escape_latex(row.iloc[2])
        }
        projects.append(project)
    return projects
```

3. Add to `core_sections` dict:
```python
core_sections = {
    ...
    'projects': ('projects.tex.j2', read_projects),
}
```

### Styling Changes

Edit `templates/latex/resume.cls`:

**Common modifications:**
- Font size: Change `\LoadClass[10pt,letterpaper]{article}` to `11pt`
- Margins: Adjust in `main.tex` geometry settings
- Colors: Add `\definecolor` commands
- Section heading style: Modify `resumesection` environment
- Bullet style: Change `$\bullet$` to other symbols

---

## 🔧 Advanced Usage

### Multiple Resume Variants

Create different Excel files for different roles:

```bash
data/
├── resume_data_technical.xlsx    # For engineering roles
├── resume_data_leadership.xlsx   # For management roles
└── resume_data_academic.xlsx     # For academic positions
```

Generate specific variant:
```python
# Modify generate_resume.py to accept argument
data_file = sys.argv[1] if len(sys.argv) > 1 else 'resume_data.xlsx'
```

### Conditional Sections

Add logic to skip empty sections:

**In Python:**
```python
jobs = read_experience(df)
if jobs:  # Only process if has content
    rendered = template.render(jobs=jobs)
```

**In Template:**
```latex
<<% if jobs %>>
\begin{resumesection}{Professional Experience}
...
\end{resumesection}
<<% endif %>>
```

### Custom LaTeX Commands

Add to `templates/latex/resume.cls`:
```latex
% Custom command for highlighting
\newcommand{\highlight}[1]{\textcolor{blue}{\textbf{#1}}}

% Custom environment for projects
\newenvironment{project}[2]{
  \textbf{#1} \hfill \textit{#2}
  \begin{itemize}
}{
  \end{itemize}
}
```

Use in templates:
```latex
\highlight{<<job.title>>}
```

---

## 🐛 Troubleshooting

### Issue: PDF not generated
**Cause**: LaTeX compilation error  
**Solution**: Check `build/resume_output.log` for errors

### Issue: Special characters appear wrong
**Cause**: LaTeX special chars not escaped  
**Solution**: The script auto-escapes `&`, `%`, `$`, `#`, `_`, `{`, `}`, `~`, `^`
For other chars, add to `escape_latex()` function

### Issue: Template syntax error
**Cause**: Wrong Jinja2 delimiters  
**Solution**: Use `<< >>` for variables, `<<% %>>` for blocks, not `{{ }}`

### Issue: Custom section not appearing
**Cause**: Empty sheet or wrong format  
**Solution**: 
- Ensure sheet has data in first column
- Check format matches simple (1 col) or two-column (2 cols)

### Issue: Build fails on GitHub Actions
**Cause**: Missing dependencies or path errors  
**Solution**: 
- Verify `requirements.txt` is committed
- Check workflow uses correct paths (`scripts/`, `build/`)
- Ensure `profiles/resume_data.xlsx` is committed

### Issue: Skills showing as objects
**Cause**: Dict key name conflicts with Python methods  
**Solution**: Already fixed - using `skills_list` instead of `items`

---

## 📝 Best Practices

### Excel Data Entry
- ✅ Keep bullet points concise (1-2 lines each)
- ✅ Use consistent date formats (YYYY or "Month YYYY")
- ✅ Leave empty cells for optional bullets (don't delete columns)
- ✅ Test with sample data first

### Template Modifications
- ✅ Test locally before committing
- ✅ Keep backups of working templates
- ✅ Use version control for template changes
- ✅ Document custom modifications

### Version Control
- ✅ Commit Excel file after each update
- ✅ Use meaningful commit messages
- ✅ Branch for major changes
- ✅ Review PDF output before merging

### LaTeX Compilation
- ✅ Clean build directory if errors persist
- ✅ Check log files for detailed errors
- ✅ Verify all templates use correct syntax
- ✅ Test character escaping with special symbols

---

## 🚀 Workflow Examples

### Quick Update
```bash
# 1. Edit Excel file
open profiles/resume_data.xlsx

# 2. Generate & preview
source .venv/bin/activate
python scripts/generate_resume.py
cd build && latexmk -pdf -jobname=resume_output main.tex

# 3. Commit if satisfied
git add profiles/resume_data.xlsx
git commit -m "Update work experience"
git push
```

### Major Refactor
```bash
# 1. Create feature branch
git checkout -b update-format

# 2. Modify templates
vim templates/latex/includes/experience.tex.j2

# 3. Test locally
python scripts/generate_resume.py
cd build && latexmk -pdf -jobname=resume_output main.tex

# 4. Review output
open build/resume_output.pdf

# 5. Commit and push
git add templates/
git commit -m "Refactor experience section layout"
git push origin update-format
```

### CI/CD Testing
```bash
# Push to test branch
git checkout -b dev-test-layout
git push origin dev-test-layout

# GitHub Actions will:
# 1. Build PDF automatically
# 2. Create artifact
# 3. Create release (for dev* and codex-* branches)

# Download from GitHub Actions tab or Releases
```

---

## 💡 Tips & Tricks

### Fit More Content
- Reduce font size in `resume.cls`: `10pt` → `9pt`
- Tighten spacing: Adjust `\vspace` values in templates
- Use abbreviations: "San Francisco" → "SF"
- Consolidate bullets: Combine related points

### Improve Visual Appeal
- Add section icons (requires fontawesome package)
- Use color accents (modify `resume.cls`)
- Add subtle borders or shading
- Adjust line thickness for `\hrule`

### Optimize for ATS (Applicant Tracking Systems)
- Use standard section names
- Avoid tables for main content (except skills)
- Include keywords from job description
- Keep formatting simple

### Speed Up Local Builds
```bash
# Use draft mode (faster compilation)
latexmk -pdf -interaction=batchmode main.tex

# Clean before build (if issues)
latexmk -c && latexmk -pdf main.tex
```

---

## 🔗 Resources

- **Jinja2 Documentation**: https://jinja.palletsprojects.com/
- **LaTeX Project**: https://www.latex-project.org/
- **Pandas Documentation**: https://pandas.pydata.org/
- **GitHub Actions**: https://docs.github.com/actions

---

**Need help?** Open an issue on GitHub or check IMPLEMENTATION_SUMMARY.md for technical details.

