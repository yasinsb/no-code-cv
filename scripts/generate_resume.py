#!/usr/bin/env python3
"""
Generate LaTeX resume files from Excel data using Jinja2 templates.
Reads data/resume_data.xlsx and renders templates/latex/includes/*.j2
"""

import pandas as pd
import sys
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
import re


def escape_latex(text):
    """Escape special LaTeX characters and normalize common Unicode characters."""
    if pd.isna(text):
        return ""
    
    text = str(text).strip()
    
    # First, normalize common Unicode characters to ASCII equivalents
    # This handles text pasted from Word, LinkedIn, etc.
    unicode_replacements = {
        # Smart quotes → regular quotes
        '\u201c': '"',  # Left double quotation mark
        '\u201d': '"',  # Right double quotation mark
        '\u2018': "'",  # Left single quotation mark
        '\u2019': "'",  # Right single quotation mark
        '\u2033': '"',  # Double prime
        # Dashes → hyphens
        '\u2013': '-',  # En dash
        '\u2014': '-',  # Em dash
        '\u2015': '-',  # Horizontal bar
        # Bullets → dash
        '\u2022': '-',  # Bullet
        '\u2023': '-',  # Triangular bullet
        '\u2043': '-',  # Hyphen bullet
        # Other common characters
        '\u2026': '...',  # Ellipsis
        '\u00a0': ' ',    # Non-breaking space
        '\u00ad': '',     # Soft hyphen (remove)
        # Comparison/math operators → safe equivalents
        '\u2264': '<=',   # Less than or equal
        '\u2265': '>=',   # Greater than or equal
        '\u00d7': 'x',    # Multiplication sign
        '\u00f7': '/',    # Division sign
    }
    
    for unicode_char, ascii_char in unicode_replacements.items():
        text = text.replace(unicode_char, ascii_char)
    
    # Now escape LaTeX special characters
    latex_replacements = {
        '\\': r'\textbackslash{}',
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}',
        '<': r'\textless{}',
        '>': r'\textgreater{}',
        '|': r'\textbar{}',
    }
    
    for char, replacement in latex_replacements.items():
        text = text.replace(char, replacement)
    
    return text


def read_header(df):
    """Read header data from sheet."""
    data = {}
    for _, row in df.iterrows():
        if len(row) >= 2 and pd.notna(row.iloc[0]):
            field = str(row.iloc[0]).strip().lower()
            value = escape_latex(row.iloc[1])
            data[field] = value
    return data


def read_summary(df):
    """Read summary text."""
    if df.empty or pd.isna(df.iloc[0, 0]):
        return ""
    return escape_latex(df.iloc[0, 0])


def read_experience(df):
    """Read experience data."""
    jobs = []
    for _, row in df.iterrows():
        if pd.isna(row.iloc[0]):
            continue
        
        job = {
            'title': escape_latex(row.iloc[0]) if len(row) > 0 else "",
            'company': escape_latex(row.iloc[1]) if len(row) > 1 else "",
            'location': escape_latex(row.iloc[2]) if len(row) > 2 else "",
            'start_date': escape_latex(row.iloc[3]) if len(row) > 3 else "",
            'end_date': escape_latex(row.iloc[4]) if len(row) > 4 else "",
            'bullets': []
        }
        
        # Add bullets (columns 5 onwards)
        for i in range(5, len(row)):
            if pd.notna(row.iloc[i]) and str(row.iloc[i]).strip():
                job['bullets'].append(escape_latex(row.iloc[i]))
        
        jobs.append(job)
    
    return jobs


def read_education(df):
    """Read education data."""
    degrees = []
    for _, row in df.iterrows():
        if pd.isna(row.iloc[0]):
            continue
        
        degree = {
            'degree': escape_latex(row.iloc[0]) if len(row) > 0 else "",
            'institution': escape_latex(row.iloc[1]) if len(row) > 1 else "",
            'location': escape_latex(row.iloc[2]) if len(row) > 2 else "",
            'start_year': escape_latex(row.iloc[3]) if len(row) > 3 else "",
            'end_year': escape_latex(row.iloc[4]) if len(row) > 4 else "",
            'bullets': []
        }
        
        # Add bullets
        for i in range(5, len(row)):
            if pd.notna(row.iloc[i]) and str(row.iloc[i]).strip():
                degree['bullets'].append(escape_latex(row.iloc[i]))
        
        degrees.append(degree)
    
    return degrees


def read_skills(df):
    """Read skills data."""
    skills = []
    for _, row in df.iterrows():
        if pd.isna(row.iloc[0]):
            continue
        
        skill = {
            'category': escape_latex(row.iloc[0]),
            'skills_list': escape_latex(row.iloc[1]) if len(row) > 1 else ""
        }
        skills.append(skill)
    
    return skills


def read_volunteering(df):
    """Read volunteering data."""
    volunteering = []
    for _, row in df.iterrows():
        if pd.isna(row.iloc[0]):
            continue
        
        vol = {
            'role': escape_latex(row.iloc[0]) if len(row) > 0 else "",
            'organization': escape_latex(row.iloc[1]) if len(row) > 1 else "",
            'dates': escape_latex(row.iloc[2]) if len(row) > 2 else ""
        }
        volunteering.append(vol)
    
    return volunteering


def detect_custom_format(df):
    """Detect if custom section is simple list or two-column."""
    df = df.dropna(how='all')
    if df.empty:
        return None
    
    first_col = df.iloc[:, 0].notna().sum() if df.shape[1] > 0 else 0
    second_col = df.iloc[:, 1].notna().sum() if df.shape[1] > 1 else 0
    
    if first_col > 0 and second_col > 0:
        return 'two_column'
    elif first_col > 0:
        return 'simple'
    else:
        return None


def read_custom_simple(df):
    """Read custom section as simple list."""
    items = []
    for _, row in df.iterrows():
        if pd.notna(row.iloc[0]) and str(row.iloc[0]).strip():
            items.append(escape_latex(row.iloc[0]))
    return items


def read_custom_two_column(df):
    """Read custom section as two-column list."""
    items = []
    for _, row in df.iterrows():
        if pd.notna(row.iloc[0]) and str(row.iloc[0]).strip():
            item = {
                'label': escape_latex(row.iloc[0]),
                'value': escape_latex(row.iloc[1]) if len(row) > 1 and pd.notna(row.iloc[1]) else ""
            }
            items.append(item)
    return items


def main():
    """Main function."""
    # Setup paths
    root_dir = Path(__file__).parent.parent
    
    # Accept profile file as command line argument, default to resume_data.xlsx
    if len(sys.argv) > 1:
        profile_name = sys.argv[1]
    else:
        profile_name = 'resume_data.xlsx'
    
    data_file = root_dir / 'profiles' / profile_name
    template_dir = root_dir / 'templates' / 'latex' / 'includes'
    build_dir = root_dir / 'build'
    includes_dir = build_dir / 'includes'
    
    # Create build directories
    build_dir.mkdir(exist_ok=True)
    includes_dir.mkdir(exist_ok=True)
    
    # Check data file
    if not data_file.exists():
        print(f"❌ Error: {data_file} not found!")
        print(f"Expected location: {data_file}")
        sys.exit(1)
    
    # Setup Jinja2 environment with custom delimiters for LaTeX compatibility
    env = Environment(
        loader=FileSystemLoader(template_dir),
        block_start_string='<<%',
        block_end_string='%>>',
        variable_start_string='<<',
        variable_end_string='>>',
        comment_start_string='<<#',
        comment_end_string='#>>',
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True
    )
    
    print(f"📖 Reading {data_file.name}...")
    
    try:
        excel_file = pd.ExcelFile(data_file)
        sheet_names = excel_file.sheet_names
        print(f"📋 Found {len(sheet_names)} sheets: {', '.join(sheet_names)}\n")
        
        generated_sections = []
        
        # Core sections with templates
        core_sections = {
            'header': ('header.tex.j2', read_header),
            'summary': ('summary.tex.j2', read_summary),
            'experience': ('experience.tex.j2', read_experience),
            'education': ('education.tex.j2', read_education),
            'skills': ('skills.tex.j2', read_skills),
            'volunteering': ('volunteering.tex.j2', read_volunteering),
        }
        
        # Process core sections
        for sheet_name in sheet_names:
            df = pd.read_excel(data_file, sheet_name=sheet_name, header=None, skiprows=1)
            sheet_lower = sheet_name.lower()
            
            print(f"  Processing: {sheet_name}...", end=" ")
            
            if sheet_lower in core_sections:
                template_name, reader_func = core_sections[sheet_lower]
                template = env.get_template(template_name)
                
                # Read data
                if sheet_lower == 'header':
                    data = reader_func(df)
                    rendered = template.render(**data)
                elif sheet_lower == 'summary':
                    summary = reader_func(df)
                    rendered = template.render(summary=summary)
                elif sheet_lower == 'experience':
                    jobs = reader_func(df)
                    rendered = template.render(jobs=jobs)
                elif sheet_lower == 'education':
                    degrees = reader_func(df)
                    rendered = template.render(degrees=degrees)
                elif sheet_lower == 'skills':
                    skills = reader_func(df)
                    rendered = template.render(skills=skills)
                elif sheet_lower == 'volunteering':
                    volunteering = reader_func(df)
                    rendered = template.render(volunteering=volunteering)
                
                # Write output
                output_file = includes_dir / f"{sheet_lower}.tex"
                output_file.write_text(rendered, encoding='utf-8')
                generated_sections.append(sheet_lower)
                print("✅")
                
            else:
                # Custom section
                format_type = detect_custom_format(df)
                
                if format_type == 'simple':
                    template = env.get_template('custom_simple.tex.j2')
                    items = read_custom_simple(df)
                    rendered = template.render(section_name=sheet_name, items=items)
                    output_file = includes_dir / f"{sheet_name.lower()}.tex"
                    output_file.write_text(rendered, encoding='utf-8')
                    generated_sections.append(sheet_name.lower())
                    print("✅ (custom)")
                    
                elif format_type == 'two_column':
                    template = env.get_template('custom_two_column.tex.j2')
                    items = read_custom_two_column(df)
                    rendered = template.render(section_name=sheet_name, items=items)
                    output_file = includes_dir / f"{sheet_name.lower()}.tex"
                    output_file.write_text(rendered, encoding='utf-8')
                    generated_sections.append(sheet_name.lower())
                    print("✅ (custom)")
                    
                else:
                    print("⏭️  (skipped - empty)")
        
        # Generate main.tex
        print(f"\n📝 Generating main.tex...")
        section_order = ['summary', 'experience', 'education', 'skills', 'volunteering']
        
        main_content = r"""\documentclass{../templates/latex/resume}
\usepackage[left=0.85in,top=0.7in,right=0.70in,bottom=0.9in]{geometry}
\usepackage{graphicx}
\usepackage{marvosym}
\usepackage{hyperref}
\usepackage{setspace}
\usepackage{amsmath}

% Import header information
\input{includes/header.tex}

\begin{document}

% Print header
\makeresumehead

"""
        
        # Add sections in order
        for section in section_order:
            if section in generated_sections:
                main_content += f"\\input{{includes/{section}.tex}}\n\n"
        
        # Add custom sections
        for section in generated_sections:
            if section not in section_order and section != 'header':
                main_content += f"\\input{{includes/{section}.tex}}\n\n"
        
        main_content += "\\setstretch{1.0}\n\n\\end{document}\n"
        
        main_file = build_dir / 'main.tex'
        main_file.write_text(main_content, encoding='utf-8')
        
        print(f"\n✅ Successfully generated {len(generated_sections)} sections!")
        print(f"📁 Output directory: {build_dir}/")
        print(f"📄 Main file: {main_file}")
        print(f"\n🚀 Ready to build PDF:")
        print(f"   cd {build_dir}")
        print(f"   latexmk -pdf -jobname=resume_output main.tex")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

