# revision 24499
# category Package
# catalog-ctan /macros/latex/contrib/logbox
# catalog-date 2011-11-03 08:30:49 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-logbox
Version:	1.0
Release:	8
Summary:	e-TeX showbox facilities for exploration purposes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/logbox
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logbox.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logbox.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The command \logbox does \showbox without stopping the
compilation. The package's main command is \viewbox*: the box
is typeset (copied) with its dimensions, and its contents are
logged in the .log file.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/logbox/logbox.sty
%doc %{_texmfdistdir}/doc/latex/logbox/README
%doc %{_texmfdistdir}/doc/latex/logbox/logbox.pdf
%doc %{_texmfdistdir}/doc/latex/logbox/logbox.png
#- source
%doc %{_texmfdistdir}/source/latex/logbox/logbox.drv
%doc %{_texmfdistdir}/source/latex/logbox/logbox.dtx
%doc %{_texmfdistdir}/source/latex/logbox/logbox.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 753411
- Rebuild to reduce used resources

* Thu Nov 10 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 729678
- texlive-logbox
- texlive-logbox

