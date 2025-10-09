# Vibe Coding Guide: No-Code Resume Builder

**Quick reference for AI/developers to navigate and modify this codebase.**

## 📂 File Map

```
profiles/*.xlsx                          ← Resume profiles (user edits)
templates/latex/resume.cls               ← Styling (fonts, colors, spacing)
templates/latex/includes/*.tex.j2        ← Jinja2 templates (8 files)
scripts/generate_resume.py               ← Excel reader + Jinja2 renderer
build/                                   ← Generated (gitignored)
.github/workflows/build.yml              ← CI/CD pipeline
```

## 🔑 Key Conventions

### Jinja2 Delimiters (Custom!)
```
Variables:   << >>      not {{ }}
Blocks:      <<% %>>    not {% %}
Comments:    <<# #>>    not {# #}
```
**Why:** Avoids conflict with LaTeX `{}` syntax.  
**Set in:** `scripts/generate_resume.py` → `Environment()`

### LaTeX Escaping
All Excel content auto-escaped: `& % $ # _ { } ~ ^ \`  
**Function:** `escape_latex()` in `generate_resume.py`

### Section Types
- **Core sections:** `header`, `summary`, `experience`, `education`, `skills`, `volunteering`
  - Each has: reader function + `.tex.j2` template
  - Registered in: `core_sections` dict in Python
- **Custom sections:** Any other Excel sheet name
  - 1 column → `custom_simple.tex.j2`
  - 2 columns → `custom_two_column.tex.j2`

## 🎯 Common Tasks

### Add New Core Section
1. Create `templates/latex/includes/newsection.tex.j2`
2. Write `read_newsection(df)` function in Python
3. Add to `core_sections` dict: `'newsection': ('newsection.tex.j2', read_newsection)`
4. Create Excel sheet named `newsection` in `profiles/resume_data.xlsx`

### Modify Template Layout
Edit `.tex.j2` files directly. Use `<< >>` for variables, `<<% %>>` for loops/conditionals.

### Change Styling
- **Global:** `templates/latex/resume.cls` (font size, colors, spacing)
- **Section-specific:** Edit `.tex.j2` templates
- **Margins:** Generated in `generate_main_tex()` → geometry package

### Change Section Order
Modify `generate_main_tex()` function, reorder `\input{includes/...}` lines.

## 🐛 Debug Checklist

- Template not rendering? → Check delimiters `<< >>`, balanced tags
- LaTeX error? → Read `build/resume_output.log`
- Section missing? → Check Excel sheet name (case-sensitive), has data
- Wrong output? → Verify reader function column order matches Excel

## 🚫 Don't Touch

- `build/` directory (regenerated)
- Generated `.tex` files (from templates)
- Don't change Jinja2 delimiters (breaks all templates)
- Don't edit `resume.cls` without testing (can break builds)

## 🔧 Quick Lookups

**Python functions:** `read_header()`, `read_experience()`, `read_skills()`, etc. in `generate_resume.py`  
**LaTeX commands:** `\resumename{}`, `\makeresumehead`, `\begin{resumesection}`, `\begin{resumeitem}` in `resume.cls`  
**CI/CD triggers:** `main`, `dev*`, `codex-*` branches in `.github/workflows/build.yml`

---

**Flow:** Excel → Python reads → Jinja2 renders → LaTeX files → PDF  
**Test locally:** `python scripts/generate_resume.py && cd build && latexmk -pdf`

