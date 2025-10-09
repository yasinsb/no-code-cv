# 📄 Resume Builds Archive

**This is an automated archive branch.** PDFs are built and stored here automatically by GitHub Actions.

## 🎯 What Is This Branch?

Every time you update your resume data on the `main` or `dev` branches, GitHub Actions automatically:
1. Generates the PDF from your Excel data
2. Commits it to this `builds` branch
3. Stores it in the `pdfs/` folder

This gives you **version-controlled PDF storage** right in your repository - no need to download from Artifacts or Releases if you don't want to.

## 📥 How to Download Your Resume

### Option 1: Direct Download (Easiest)
Navigate to the [`pdfs/`](./pdfs) folder and click on any PDF to view/download it.

### Option 2: Clone Locally
```bash
git clone -b builds https://github.com/YOUR_USERNAME/no-code-cv.git resume-pdfs
cd resume-pdfs/pdfs
```

### Option 3: Download Specific PDF
```bash
# Replace YOUR_USERNAME and FILENAME
wget https://github.com/YOUR_USERNAME/no-code-cv/raw/builds/pdfs/FILENAME.pdf
```

## 📂 Folder Structure

```
builds/
├── README.md          ← You are here!
└── pdfs/
    ├── INDEX.md       ← Build metadata (auto-generated)
    └── *.pdf          ← Your resume PDFs
```

## 🔄 How This Works

```
[Push to main/dev] 
    ↓
[GitHub Actions builds PDF]
    ↓
[PDF saved to builds branch]
    ↓
[You download from pdfs/ folder]
```

Each build includes:
- **Source branch** - Which branch triggered the build
- **Commit SHA** - Exact code version used
- **Build number** - Sequential build ID
- **Timestamp** - When the build occurred

Check [`pdfs/INDEX.md`](./pdfs/INDEX.md) for the latest build details.

## ⚠️ Important Notes

- **Don't manually edit this branch** - It's managed by automation
- **Don't commit directly** - Changes will be overwritten on next build
- **PDFs are always fresh** - Each build replaces old PDFs with new ones
- **This is your fork** - Your data stays in your repo, nowhere else

## 🔗 Related

- **Main Branch** → [Go to main branch](../../tree/main) for source code and data
- **Actions Tab** → [View build logs](../../actions) to see build history
- **Releases** → [View releases](../../releases) for tagged/permanent versions

---

**Built with:** Python • Jinja2 • LaTeX • GitHub Actions  
**Automation:** Fully automatic, no manual intervention needed

