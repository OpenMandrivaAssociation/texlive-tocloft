# revision 20084
# category Package
# catalog-ctan /macros/latex/contrib/tocloft
# catalog-date 2010-10-13 11:41:41 +0200
# catalog-license lppl1.3
# catalog-version 2.3e
Name:		texlive-tocloft
Version:	2.3e
Release:	1
Summary:	Control table of contents, figures, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tocloft
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tocloft.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tocloft.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tocloft.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Provides control over the typography of the Table of Contents,
List of Figures and List of Tables, and the ability to create
new `List of ...'. The ToC \parskip can be changed.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tocloft/tocloft.sty
%doc %{_texmfdistdir}/doc/latex/tocloft/README
%doc %{_texmfdistdir}/doc/latex/tocloft/tocloft.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tocloft/tocloft.dtx
%doc %{_texmfdistdir}/source/latex/tocloft/tocloft.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
