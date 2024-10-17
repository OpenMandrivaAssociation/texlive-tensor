Name:		texlive-tensor
Version:	15878
Release:	2
Summary:	Typeset tensors
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tensor
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tensor.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tensor.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tensor.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package which allows the user to set tensor-style super- and
subscripts with offsets between successive indices. It supports
the typesetting of tensors with mixed upper and lower indices
with spacing, also typset preposed indices. This is a complete
revision and extension of the original 'tensor' package by Mike
Piff.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tensor/tensor.sty
%doc %{_texmfdistdir}/doc/latex/tensor/README
%doc %{_texmfdistdir}/doc/latex/tensor/tensor.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tensor/tensor.dtx
%doc %{_texmfdistdir}/source/latex/tensor/tensor.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
