\NeedsTeXFormat{LaTeX2e}[1994/06/01]
\ProvidesClass{hiofthesis}[2020/08/28 Hiof Thesis by gunnar.misund@hiof.no]


%% Book options
\DeclareOption{11pt,a4paper,twoside}{
  \PassOptionsToClass{\CurrentOption}{book}
}


%% Custom package options

% Option master: Master version, default bachelor
\newif\ifmaster
\masterfalse
\DeclareOption{master}{
  \mastertrue
}

% Option sans: Uses HiØ official font "Source Sans Pro", default Latex standard Times Roman
\newif\ifsans
\sansfalse
\DeclareOption{sans}{
  \sanstrue
}

% Option us: Norwegian language, default american
\newif\ifus
\usfalse
\DeclareOption{us}{
  \ustrue
}

% Option other: An other language will be used
\newif\ifother
\otherfalse
\DeclareOption{other}{
  \othertrue
}

% Option word: The ugly M$ standard paragraph formatting, no indentation, one line separation, default: What is considered normal by the rest of the world.
\newif\ifword
\wordfalse
% Uses custom title page provided as "titlepage.pdf", OBS: MUST BE EXACTLY A4 SIZE

\DeclareOption{word}{
  \ClassWarning{hiofthesis}{Your thesis will now look like a standard formatted MicroSoft document, hmmm, up to you.}
  \wordtrue
}

% Option cover: Uses custom title page provided as "titlepage.pdf", OBS: MUST BE EXACTLY A4 SIZE, default HiØ standard thesis title page

\newif\ifcover
\coverfalse

\DeclareOption{cover}{
  \covertrue
}

% Fallback
\DeclareOption*{
  \ClassWarning{myclass}{Unknown option '\CurrentOption'}
}

% Execute default options
\ExecuteOptions{11pt,a4paper,twoside,openright}

% Process given options
\ProcessOptions\relax

% Load base
\LoadClass[11pt,a4paper,twoside]{book}

% Load additional packages and commands.

\RequirePackage{fancyhdr,xcolor,paralist,lipsum,geometry,pdfpages,url,nameref,subfigure,wrapfig,tabularx,amssymb,emptypage,relsize,microtype,xparse}
\RequirePackage[export]{adjustbox}
\RequirePackage[T1]{fontenc}
\RequirePackage[utf8]{inputenc}
%\RequirePackage{listings}

% Remove self reference in table of contents
%\ProvideDocumentCommand{\addchaptertocentry}{ m }{%
%	\addcontentsline{toc}{chapter}{#1}%
	

%\addchaptertocentry{\contentsname}\@starttoc{toc}}{}{}


%\ifus
%    \RequirePackage[american]{babel}
%\else
%    \ifother
%        %...
%
%    \else
%        \renewcommand\lstlistingname{Kode}
%        \renewcommand\lstlistlistingname{Kode}
%        \RequirePackage[norsk]{babel}
%    \fi
%\fi

%\RequirePackage{listings}

% Implement options
%% Source sans pro font
\ifsans
    \RequirePackage[lining,light,default]{sourcesanspro}
    %\RequirePackage[T1]{fontenc}
\fi

\newcommand{\doctype}[1]{\newcommand{\dtype}{#1}}
\newcommand{\affiliation}[1]{\newcommand{\aff}{#1}}
\newcommand{\department}[1]{\newcommand{\dep}{#1}}
\newcommand{\place}[1]{\newcommand{\plc}{#1}}
\newcommand{\subtitle}[1]{\newcommand{\subt}{#1}}


\ifcover
    \renewcommand{\maketitle}{
    \pagestyle{empty}
    \includepdf[pages=-]{coverpage}
    \pagestyle{headings}
    }
\else
%    \ifmaster
%        \ifus
%            \def\doctype{Master's Thesis in Computer Science}
%        \else
%            \def\doctype{Masteroppgave i Informatikk}   
%        \fi
%    \else
%        \ifus
%            \def\doctype{Bachelor's Thesis in Computer Science} 
%        \else
%            \def\doctype{Bacheloroppgave i Informatikk}      
%        \fi


\renewcommand{\maketitle}{
    
        % Smaller margins on titlepage
        \newgeometry{top=7mm,bottom=15mm,inner=15mm,outer=15mm}
        \pagestyle{empty}
        \begin{titlepage}
            %\includegraphics[width=0.5\textwidth,right]{hiof-logo}
            \includegraphics[width=0.5\textwidth,right]{hiof-logo-no}
            \mbox{
                \vtop{
                \vskip 5cm
                \begin{center}
                    \textsf{\fontseries{t}\selectfont \bfseries \Huge \@title\\ \smaller \vskip 1em \subt } \par

                \vskip 1cm
                    \textsf{\large \dtype} \par

                \vskip 2cm
                     \textsf{\LARGE \@author} \par

                \vskip 1cm
                    \textsf{\large \dep\\ \aff\\ \plc\\ \@date } \par
                \end{center}
            }%\mbox
        }
        
        \begin{figure}[!b]
        \includegraphics[width=0.99\textwidth]{hiof-footer}
        \end{figure}
        
        \null
        \end{titlepage}
        
        \pagestyle{headings}
        \newgeometry{inner=25mm,outer=35mm,top=30mm,bottom=40mm}
    }  

\fi %ifcover

\newcommand{\makehalftitle}{
    
    \newgeometry{inner=25mm,outer=35mm,top=70mm,bottom=40mm}
    \pagestyle{empty}
    \cleardoublepage
    \begin{center}
        \textsc{
            \Huge{\@title} \\
            \vskip .5cm
            \LARGE{\subt} 
        }\\
        \vskip 2cm
        \Large{\dtype} \\
        \vskip 5cm
        \LARGE{\@author} \\
        \vskip 2cm
        \large{\large \dep\\ \aff\\ \plc\\ \@date}
    \end{center}

    \cleardoublepage
    \newgeometry{inner=25mm,outer=35mm,top=30mm,bottom=40mm}
}  


%% Formatting paragraphs, must occur after maketitle
\ifword
  \setlength{\parindent}{0em}
  \setlength{\parskip}{1em}
\fi


%% Set main file
%!TEX root = main.tex


%%Common number levels in table of contents
\setcounter{tocdepth}{1}

%%Various new commands

% Redefine "\chapter*" to be added to table of contents

\let\oldchapter\chapter
\RenewDocumentCommand{\chapter}{s o m}{%
  \IfBooleanTF{#1}
    {% \chapter*
      \oldchapter*{#3}% Insert \chapter*{...}
      \addcontentsline{toc}{chapter}{\protect\numberline{}#3}% Add ToC entry
    }{% \chapter
      \IfNoValueTF{#2}
        {\oldchapter{#3}}% \chapter{...}
        {\oldchapter[#2]{#3}}% \chapter[..]{...}
    }%
}

% Prevent orphan and widow lines
\widowpenalty10000
\clubpenalty10000
\brokenpenalty10000
\hyphenpenalty10000

% Set headings and footers

\cleardoublepage
\setcounter{page}{1}

\newcommand{\theend}{
\newpage
\pagestyle{empty}
\mbox{}
\newpage
\mbox{}
\newpage
\mbox{}
\cleardoublepage
}

% Make some blank pages for sensor notes
\AtEndDocument{
    \newpage
    \pagestyle{empty}
    \mbox{}
    \newpage
    \mbox{}
    \newpage
    \mbox{}
    \cleardoublepage
}

%\RequirePackage{listings}
\endinput