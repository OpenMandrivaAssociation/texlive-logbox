Name:		texlive-logbox
Version:	24499
Release:	2
Summary:	e-TeX showbox facilities for exploration purposes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/logbox
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logbox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logbox.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logbox.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
