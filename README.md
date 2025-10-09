# No-Code Resume Builder

**Turn a simple spreadsheet into a beautiful PDF resume. Automatically.**

No design skills needed. No LaTeX knowledge required. Just edit an Excel file and let the system do the magic! ✨

---

## 🎯 What Does This Do?

You edit a spreadsheet → GitHub builds a professional PDF → You download and use it.

That's it! No complicated software, no formatting headaches, no design struggles.

## 🚀 Quick Start (Really Quick!)

### Option 1: Use on GitHub (Easiest)
1. **Fork this repo** to your GitHub account
2. **Edit** `profiles/resume_data.xlsx` directly on GitHub
3. **Commit** your changes
4. **Wait 2 minutes** for the build to finish
5. **Download** your PDF from the "Actions" tab or "Releases"

### Option 2: Work Locally
```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/no-code-cv.git
cd no-code-cv

# Edit the Excel file (use Excel, Google Sheets, LibreOffice)
open profiles/resume_data.xlsx

# Push your changes
git add profiles/resume_data.xlsx
git commit -m "Updated my resume"
git push

# Your PDF will be ready in ~2 minutes!
```

---

## 📝 How to Fill Your Resume

Open `profiles/resume_data.xlsx` - you'll see multiple sheets (tabs):

### 📋 Required Sheets:
- **header** → Your name, phone, email, LinkedIn
- **summary** → A short paragraph about yourself
- **experience** → Your jobs (company, role, achievements)
- **education** → Your degrees
- **skills** → Your technical skills
- **volunteering** → Volunteer work (optional but nice!)

### ➕ Custom Sheets (Optional):
Want to add more sections? Just create a new sheet!

**Examples:**
- **Hobbies** → One column list: "Photography", "Hiking"
- **Certificates** → Two columns: "Certificate Name" | "Issuer & Year"
- **Awards**, **Publications**, **Languages** - anything you want!

💡 **Pro tip:** Don't worry about formatting in Excel. The system handles all the styling!

---

## 📥 Where Are My PDFs?

Your resume is available in **three places** after each build:

1. **Actions Tab** → Artifacts (good for 90 days)
2. **Releases Page** → Permanent downloads
3. **`builds` Branch** → PDFs stored in the repo itself (in `pdfs/` folder)

Pick whichever is easiest for you!

---

## 🎨 What Makes This Special?

### ✅ No Design Skills Needed
The template is already professional. You just fill in the content.

### ✅ No LaTeX Learning Curve
LaTeX is powerful but scary. We hide all that complexity from you.

### ✅ Version Control Built-In
Every change is tracked in Git. Want to see your resume from last year? Easy!

### ✅ Multiple Versions Support
Need different resumes for different jobs? Create multiple Excel files!
- `profiles/resume_software.xlsx`
- `profiles/resume_management.xlsx`
- `profiles/resume_academic.xlsx`

All will build automatically into separate PDFs.

### ✅ Automatic Updates
Update your Excel → Push → New PDF ready in minutes.

### ✅ Free Forever
Everything runs on GitHub Actions (free tier = 2000 minutes/month).

---

## 🤔 FAQ

### Do I need to install anything?
**Nope!** If you use GitHub's web interface, you don't need to install anything at all.

If you want to work locally, you just need Git (and Excel/LibreOffice to edit the file).

### What if I mess something up?
Git keeps all your history. You can always undo changes or go back to a previous version.

### Can I change the design?
Yes! If you're comfortable with LaTeX, you can edit `templates/latex/resume.cls` to change fonts, colors, spacing, etc. But the default looks great!

### Can I use this for my team/company?
Absolutely! Fork it and customize for your needs.

### How does this actually work?
<details>
<summary>Click to see the technical flow (for curious minds)</summary>

```
📊 Excel File (your data)
    ↓
🐍 Python Script (reads data)
    ↓
📄 Jinja2 Templates (fills in placeholders)
    ↓
📝 LaTeX Files (structured document)
    ↓
🔧 LaTeX Compiler (renders PDF)
    ↓
📄 Beautiful PDF Resume
```

**Technologies used:**
- Python + pandas (read Excel)
- Jinja2 (templating)
- LaTeX (typesetting)
- GitHub Actions (automation)

</details>

### Where's my data stored?
Your Excel file lives in **your** GitHub repo. Only you control it. The system never sends your data anywhere else.

---

## 🎓 Learning Resources

- **New to GitHub?** → [GitHub Hello World Guide](https://guides.github.com/activities/hello-world/)
- **Want to customize?** → Check `USAGE_GUIDE.md` for detailed instructions
- **Developer mode?** → See `VIBE_CODING_GUIDE.md` for technical details

---

## 🤝 Contributing

Found a bug? Have an idea? Open an issue or submit a pull request!

This project is designed to be simple and accessible. Let's keep it that way.

---

## 📄 License

MIT License - Use it however you want!

---

## 💡 Credits

Built with love for people who want great resumes without the hassle.

**Stack:** Python • Jinja2 • LaTeX • GitHub Actions

---

**Questions? Issues? Ideas?** Open an issue on GitHub - I'm happy to help! 😊
