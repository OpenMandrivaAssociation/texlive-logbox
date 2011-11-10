# revision 24499
# category Package
# catalog-ctan /macros/latex/contrib/logbox
# catalog-date 2011-11-03 08:30:49 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-logbox
Version:	1.0
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The command \logbox does \showbox without stopping the
compilation. The package's main command is \viewbox*: the box
is typeset (copied) with its dimensions, and its contents are
logged in the .log file.

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
%{_texmfdistdir}/tex/latex/logbox/logbox.sty
%doc %{_texmfdistdir}/doc/latex/logbox/README
%doc %{_texmfdistdir}/doc/latex/logbox/logbox.pdf
%doc %{_texmfdistdir}/doc/latex/logbox/logbox.png
#- source
%doc %{_texmfdistdir}/source/latex/logbox/logbox.drv
%doc %{_texmfdistdir}/source/latex/logbox/logbox.dtx
%doc %{_texmfdistdir}/source/latex/logbox/logbox.ins
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
