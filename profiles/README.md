# Resume Data Files

This directory contains Excel files with resume content.

## Files

### `resume_data.xlsx` (Active)
The active resume data file used by the build system. Currently contains **John Doe** profile.

### `resume_data_alt.xlsx` (Showcase)
Alternative resume data showcasing **Jill Doe** profile - a data scientist with ML/AI expertise.

## How to Use

### Switch Profiles
To build with a different profile, simply rename/swap the files:

```bash
# Build with Jill Doe profile
mv profiles/resume_data.xlsx profiles/resume_data_john.xlsx
mv profiles/resume_data_alt.xlsx profiles/resume_data.xlsx
python scripts/generate_resume.py
```

### Create Your Own
1. Duplicate `resume_data.xlsx`
2. Edit the new file with your information
3. Keep the same sheet structure
4. Use as `resume_data.xlsx` to build

## Notes

- Only `resume_data.xlsx` is used by the build system
- Other `.xlsx` files are for reference/showcase
- See `USAGE_GUIDE.md` for Excel structure details

