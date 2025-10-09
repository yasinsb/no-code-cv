% resume.cls - Simple Resume Document Class
% Created for the Codex Resume project
% https://github.com/yasinsb/no-code-cv

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{resume}[2025/10/08 v1.0 Simple Resume Class]

% Base class - reduced to 10pt for single page
\LoadClass[10pt,letterpaper]{article}

% Required packages
\RequirePackage[parfill]{parskip}
\RequirePackage{array}
\RequirePackage{ifthen}
\RequirePackage{xcolor}

% No page numbers or auxiliary files
\pagestyle{empty}
\nofiles

%-----------------------------------------------------------
% Header: Name and Contact Information
%-----------------------------------------------------------

\newcommand{\resumename}[1]{\def\@resumename{#1}}
\newcommand{\resumecontact}[1]{\def\@resumecontact{#1}}

\def\@resumename{}
\def\@resumecontact{}

% Command to print header (call manually after \begin{document})
\newcommand{\makeresumehead}{%
  \begingroup
    \centering
    {\Large\bfseries\@resumename}\par
    \vspace{0.3em}
    \@resumecontact\par
  \endgroup
  \vspace{0.5em}
}

%-----------------------------------------------------------
% Section Environment
%-----------------------------------------------------------

\newenvironment{resumesection}[1]{%
  \vspace{0.6em}
  {\large\bfseries #1}
  \vspace{0.2em}
  {\color{gray}\hrule}
  \vspace{0.3em}
  \begin{list}{}{%
    \setlength{\leftmargin}{0em}
  }
  \item[]
}{%
  \end{list}
}

%-----------------------------------------------------------
% Subsection Environment (for jobs, education, etc.)
%-----------------------------------------------------------

\newenvironment{resumeitem}[4]{%
  \textbf{#1} \hfill \textbf{#2}
  \ifthenelse{\equal{#3}{}}{}{%
    \\
    \textit{#3} \hfill \textit{#4}
  }
  \vspace{0.1em}
  \begin{list}{$\bullet$}{%
    \setlength{\leftmargin}{1.5em}
    \setlength{\itemsep}{-0.5em}
    \setlength{\topsep}{0pt}
    \setlength{\partopsep}{0pt}
  }
}{%
  \end{list}
  \vspace{0.3em}
}

\endinput
