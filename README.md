# No-Code Resume Builder

Professional resume generation from Excel to PDF using Jinja2 templates and LaTeX. Edit a spreadsheet, commit, and get a beautifully formatted PDF automatically.

## 🚀 Quick Start

### 1. Edit Your Resume
Open `profiles/resume_data.xlsx` and fill in your information:
- **header** sheet: Name, phone, email, LinkedIn
- **summary** sheet: Professional summary
- **experience** sheet: Jobs with bullets
- **education** sheet: Degrees and details
- **skills** sheet: Categories and skills
- **volunteering** sheet: Volunteer work
- **Custom sheets**: Add any section (Hobbies, Certificates, etc.)

### 2. Generate & Build
```bash
# Local development
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Generate LaTeX from Excel
python scripts/generate_resume.py

# Build PDF
cd build
latexmk -pdf -jobname=resume_output main.tex
```

### 3. Or Just Push to GitHub
```bash
git add profiles/resume_data.xlsx
git commit -m "Update resume"
git push
```
→ GitHub Actions builds **all profiles** automatically!

### 4. Download Your PDFs
- **Direct from repo:** `builds` branch → `pdfs/` folder
- **Artifacts:** GitHub Actions tab (90 days)
- **Releases:** Release page (dev*/codex-* branches, permanent)

## 🔧 How It Works

```
┌─────────────────────┐
│ profiles/           │
│   resume_data.xlsx  │◄── You edit this
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ scripts/            │
│   generate_resume.py│◄── Reads Excel
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ templates/latex/    │
│   includes/*.j2     │◄── Jinja2 templates
└──────────┬──────────┘
           │
           ▼ (renders with data)
┌─────────────────────┐
│ build/              │
│   includes/*.tex    │◄── Generated LaTeX
│   main.tex          │
└──────────┬──────────┘
           │
           ▼ (LaTeX compilation)
┌─────────────────────┐
│ build/              │
│   resume_output.pdf │◄── Your resume!
└─────────────────────┘
```

## 📁 Project Structure

```
no-code-cv/
├── profiles/
│   └── *.xlsx                    # Resume profiles (edit these)
│
├── templates/latex/
│   ├── resume.cls                # Styling (rarely change)
│   └── includes/                 # Jinja2 templates
│       ├── header.tex.j2         # Name & contact
│       ├── summary.tex.j2        # Summary
│       ├── experience.tex.j2     # Jobs (with loops)
│       ├── education.tex.j2      # Degrees (with loops)
│       ├── skills.tex.j2         # Skills table
│       ├── volunteering.tex.j2   # Volunteer work
│       ├── custom_simple.tex.j2  # Generic list
│       └── custom_two_column.tex.j2  # Generic labeled list
│
├── scripts/
│   └── generate_resume.py        # Excel → LaTeX renderer
│
└── build/                        # Generated (gitignored)
    ├── includes/*.tex            # Generated from templates
    ├── main.tex                  # Generated dynamically
    └── resume_output.pdf         # Final PDF
```

## 🎯 Key Features

### Template-Based Architecture
- **Jinja2 templates** with custom delimiters (`<< >>` instead of `{{ }}`)
- Templates are **committed** to git
- Generated `.tex` files are **not committed**
- Excel is the **single source of truth**

### Smart Section Detection
- **Core sections**: header, summary, experience, education, skills, volunteering
- **Custom sections**: Add any Excel sheet name
  - Simple list (1 column): Hobbies, Awards, etc.
  - Two-column list (label + value): Certificates, Publications, etc.

### Automatic Workflows
- **Local**: Run `generate_resume.py` → build PDF locally
- **GitHub Actions**: Push → builds **ALL** `.xlsx` profiles in parallel
- **Multi-output**: PDFs available via artifacts, releases, AND `builds` branch
- **ETL Pattern**: Source (`main`/`dev`) → Build (CI/CD) → Output (`builds` branch)

## 🔑 Why This Works

### 1. Separation of Concerns
- **Data** (Excel) ≠ **Templates** (Jinja2) ≠ **Output** (LaTeX/PDF)
- Edit data without touching code or templates
- Modify templates without regenerating from scratch

### 2. LaTeX Compatibility
- Custom Jinja2 delimiters avoid conflicts with LaTeX `{ }`
- Full LaTeX character escaping (automatically handles `&`, `%`, `$`, etc.)
- Professional typesetting with single-page layout

### 3. Version Control Friendly
- Only source files committed (Excel, templates, scripts)
- Generated files properly gitignored
- Full history of resume changes
- Collaborative editing with git branches

### 4. Extensible & Maintainable
- Add sections: Create new Excel sheet
- Modify layout: Edit `.j2` templates
- Change styling: Update `resume.cls`
- No code changes needed for content updates

## 🛠️ Technical Details

### Jinja2 Template Syntax
```latex
% Variables
<<name>>
<<email>>

% Loops
<<% for job in jobs %>>
  Job: <<job.title>>
  <<% for bullet in job.bullets %>>
    - <<bullet>>
  <<% endfor %>>
<<% endfor %>>

% Conditionals
<<% if vol.organization %>>
  at <<vol.organization>>
<<% endif %>>
```

### LaTeX Generation
1. Read Excel with pandas
2. Parse each sheet based on type
3. Escape LaTeX special characters
4. Render Jinja2 templates with data
5. Write to `build/includes/*.tex`
6. Generate `build/main.tex` dynamically
7. Compile with `latexmk`

### CI/CD Pipeline (Matrix Build)
```yaml
- Discover: Find all *.xlsx in profiles/
- Matrix: Build each profile in parallel
  - Generate LaTeX from Excel
  - Compile PDF with latexmk
  - Upload artifact (90 days)
  - Create release (dev*/codex-* branches)
  - Push to builds branch (permanent, in repo)
```

**Result:** All profiles → separate PDFs, accessible 3 ways!

## 📚 Further Reading

See `USAGE_GUIDE.md` for:
- Detailed Excel structure
- Custom section examples
- Template customization
- Troubleshooting
- Advanced usage

## 🤝 Contributing

This project demonstrates template-based document generation. Contributions welcome that maintain:
- Clean separation (data/templates/scripts)
- Template-based approach (not code generation)
- Excel as single source of truth
- Professional project structure

## 📄 License

See LICENSE file.
