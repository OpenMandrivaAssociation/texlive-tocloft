%global tl_name tocloft
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.3j
Release:	%{tl_revision}.1
Summary:	Control table of contents, figures, etc.
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tocloft
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tocloft.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tocloft.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tocloft.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides control over the typography of the Table of Contents, List of
Figures and List of Tables, and the ability to create new 'List of ...'.
The ToC \parskip may be changed.

