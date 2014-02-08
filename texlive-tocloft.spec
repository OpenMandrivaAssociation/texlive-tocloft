# revision 20084
# category Package
# catalog-ctan /macros/latex/contrib/tocloft
# catalog-date 2010-10-13 11:41:41 +0200
# catalog-license lppl1.3
# catalog-version 2.3e
Name:		texlive-tocloft
Version:	2.3e
Release:	3
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


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.3e-2
+ Revision: 757001
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.3e-1
+ Revision: 719772
- texlive-tocloft
- texlive-tocloft
- texlive-tocloft

