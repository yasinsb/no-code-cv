# No-Code Resume Builder

**Turn a simple spreadsheet into a beautiful PDF resume. Automatically.**

No design skills needed. No LaTeX knowledge required. Just edit an Excel file and let the system do the magic! ✨

---

## 🎯 What Does This Do?

You edit a spreadsheet → GitHub builds a professional PDF → You download and use it.

That's it! No complicated software, no formatting headaches, no design struggles.

**Truly No-Code:** You never need to touch a terminal or write a single line of code. Everything happens through GitHub's web interface and your favorite spreadsheet editor.

## 🚀 Quick Start (Really Quick!)

### True No-Code Way (Zero Terminal Required!)

1. **Fork this repo** to your GitHub account (click "Fork" button)
2. **Download** the Excel file:
   - Go to `profiles/resume_data.xlsx` in your forked repo
   - Click "Download" or "Raw" button to save it
3. **Edit** on your computer:
   - Open with Excel, Google Sheets (download as .xlsx), or LibreOffice
   - Fill in your information (name, experience, skills, etc.)
   - Save the file
4. **Upload** back to GitHub:
   - Go back to `profiles/` folder in your repo
   - Click "Add file" → "Upload files"
   - Drag your edited `resume_data.xlsx`
   - Click "Commit changes" (green button)
5. **Wait 2 minutes** for the magic ✨
6. **Download your PDF** from:
   - "Actions" tab → Latest workflow → Artifacts
   - OR "Releases" page → Latest release

**That's it! No coding, no terminal, no Git commands!**

---

### For Developers / Advanced Users

Want to customize templates, add new sections, or work with Git locally? 

<details>
<summary>Click to see the developer workflow</summary>

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/no-code-cv.git
cd no-code-cv

# Edit the Excel file
open profiles/resume_data.xlsx

# Test locally (optional - requires Python + LaTeX)
python scripts/generate_resume.py
cd build && latexmk -pdf -jobname=resume_output main.tex

# Push your changes
git add profiles/resume_data.xlsx
git commit -m "Updated my resume"
git push

# Your PDF will be ready in ~2 minutes!
```

For template customization, see `VIBE_CODING_GUIDE.md`

</details>

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
**Absolutely not!** The whole point is **no-code**. Just:
- A web browser (to access GitHub)
- Excel, Google Sheets, or LibreOffice (to edit the file)

That's it! No Git, no Python, no LaTeX, no terminal commands.

If you're a developer and want to customize templates or test locally, you'll need Python + LaTeX, but that's totally optional.

### What if I mess something up?
Git keeps all your history. You can always undo changes or go back to a previous version.

### Can I change the design?
Yes! If you're comfortable with LaTeX, you can edit `templates/latex/resume.cls` to change fonts, colors, spacing, etc. But the default looks great!

### Can I use this for my team/company?
Absolutely! Fork it and customize for your needs.

### I'm not technical - can I really use this?
**Yes!** If you can edit an Excel file and use GitHub's website (which is just clicking buttons), you can use this. No coding required.

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
