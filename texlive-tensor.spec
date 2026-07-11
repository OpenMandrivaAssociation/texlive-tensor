%global tl_name tensor
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2
Release:	%{tl_revision}.1
Summary:	Typeset tensors
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tensor
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tensor.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tensor.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tensor.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package which allows the user to set tensor-style super- and
subscripts with offsets between successive indices. It supports the
typesetting of tensors with mixed upper and lower indices with spacing,
also typeset preposed indices. This is a complete revision and extension
of the original 'tensor' package by Mike Piff.

