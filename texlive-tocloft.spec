# revision 30209
# category Package
# catalog-ctan /macros/latex/contrib/tocloft
# catalog-date 2013-05-02 18:21:19 +0200
# catalog-license lppl1.3
# catalog-version 2.3f
Name:		texlive-tocloft
Version:	2.3f
Release:	7
Summary:	Control table of contents, figures, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tocloft
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tocloft.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tocloft.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tocloft.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
