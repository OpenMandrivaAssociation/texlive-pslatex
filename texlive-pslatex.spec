%global tl_name pslatex
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Use PostScript fonts by default
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pslatex
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pslatex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pslatex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A small package that makes LaTeX default to 'standard' PostScript fonts.
It is basically a merger of the times and the (obsolete) mathptm
packages from the psnfss suite. You must have installed standard LaTeX
and the psnfss PostScript fonts to use this package. The main novel
feature is that the pslatex package tries to compensate for the visual
differences between the Adobe fonts by scaling Helvetica by 90%, and
'condensing' Courier (i.e. scaling horizontally) by 85%. The package is
supplied with a (unix) shell file for a 'pslatex' command that allows
standard LaTeX documents to be processed, without needing to edit the
file. Note that current psnfss uses a different technique for scaling
Helvetica, and treats Courier as a lost cause (there are better free
fixed-width available now, than there were when pslatex was designed).
As a result, pslatex is widely considered obsolete.

