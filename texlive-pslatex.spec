Name:		texlive-pslatex
Version:	67469
Release:	1
Summary:	Use PostScript fonts by default
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pslatex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pslatex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pslatex.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A small package that makes LaTeX default to 'standard'
PostScript fonts. It is basically a merger of the times and the
(obsolete) mathptm packages from the psnfss suite. You must
have installed standard LaTeX and the psnfss PostScript fonts
to use this package. The main novel feature is that the pslatex
package tries to compensate for the visual differences between
the Adobe fonts by scaling Helvetica by 90%, and 'condensing'
Courier (i.e. scaling horizontally) by 85%. The package is
supplied with a (unix) shell file for a 'pslatex' command that
allows standard LaTeX documents to be processed, without
needing to edit the file. Note that current psnfss uses a
different technique for scaling Helvetica, and treats Courier
as a lost cause (there are better free fixed-width available
now, than there were when pslatex was designed). As a result,
pslatex is widely considered obsolete.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/pslatex/pcrr8rn.map
%{_texmfdistdir}/fonts/tfm/public/pslatex/pcrr7tn.tfm
%{_texmfdistdir}/fonts/tfm/public/pslatex/pcrr8rn.tfm
%{_texmfdistdir}/fonts/tfm/public/pslatex/pcrr8tn.tfm
%{_texmfdistdir}/fonts/vf/public/pslatex/pcrr7tn.vf
%{_texmfdistdir}/fonts/vf/public/pslatex/pcrr8tn.vf
%{_texmfdistdir}/tex/latex/pslatex/pslatex.sty
#- source
%doc %{_texmfdistdir}/source/latex/pslatex/fontinst/pslatex.tex
%doc %{_texmfdistdir}/source/latex/pslatex/shell/pslatex
%doc %{_texmfdistdir}/source/latex/pslatex/shell/pslatex.bat

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex source %{buildroot}%{_texmfdistdir}
