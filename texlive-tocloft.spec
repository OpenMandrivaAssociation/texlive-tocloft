Name:		texlive-tocloft
Version:	53364
Release:	1
Summary:	Control table of contents, figures, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tocloft
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tocloft.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tocloft.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tocloft.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides control over the typography of the Table of Contents,
List of Figures and List of Tables, and the ability to create
new `List of ...'. The ToC \parskip can be changed.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tocloft/tocloft.sty
%doc %{_texmfdistdir}/doc/latex/tocloft/README
%doc %{_texmfdistdir}/doc/latex/tocloft/tocloft.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tocloft/tocloft.dtx
%doc %{_texmfdistdir}/source/latex/tocloft/tocloft.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
