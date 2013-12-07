# revision 22961
# category Package
# catalog-ctan /macros/latex/contrib/tkz/tkz-base
# catalog-date 2011-06-05 23:10:23 +0200
# catalog-license lppl
# catalog-version 1.16
Name:		texlive-tkz-base
Version:	1.16
Release:	6
Summary:	Tools for drawing with a cartesian coordinate system
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tkz/tkz-base
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-base.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-base.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is the base of a set of packages, designed to give
mathematics teachers (and students) easy access to programming
of drawings with TikZ.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tkz-base/tkz-base.cfg
%{_texmfdistdir}/tex/latex/tkz-base/tkz-base.sty
%{_texmfdistdir}/tex/latex/tkz-base/tkz-obj-marks.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-obj-points.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-obj-segments.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-tools-arith.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-tools-base.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-tools-math.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-tools-misc.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-tools-obsolete.tex
%{_texmfdistdir}/tex/latex/tkz-base/tkz-tools-utilities.tex
%doc %{_texmfdistdir}/doc/latex/tkz-base/README
%doc %{_texmfdistdir}/doc/latex/tkz-base/examples/Makefile
%doc %{_texmfdistdir}/doc/latex/tkz-base/examples/info_base_tex.txt
%doc %{_texmfdistdir}/doc/latex/tkz-base/examples/latex/tkzbase-tex.zip
%doc %{_texmfdistdir}/doc/latex/tkz-base/examples/tkzbasepreamble.ltx
%doc %{_texmfdistdir}/doc/latex/tkz-base/latex/TKZdoc.zip
%doc %{_texmfdistdir}/doc/latex/tkz-base/tkz-base-screen.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.16-2
+ Revision: 756926
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.16-1
+ Revision: 719760
- texlive-tkz-base
- texlive-tkz-base
- texlive-tkz-base

