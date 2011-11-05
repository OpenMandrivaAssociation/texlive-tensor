# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/tensor
# catalog-date 2006-11-03 07:18:50 +0100
# catalog-license lppl
# catalog-version 2.1
Name:		texlive-tensor
Version:	2.1
Release:	1
Summary:	Typeset tensors
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tensor
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tensor.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tensor.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tensor.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A package which allows the user to set tensor-style super- and
subscripts with offsets between successive indices. It supports
the typesetting of tensors with mixed upper and lower indices
with spacing, also typset preposed indices. This is a complete
revision and extension of the original 'tensor' package by Mike
Piff.

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
%{_texmfdistdir}/tex/latex/tensor/tensor.sty
%doc %{_texmfdistdir}/doc/latex/tensor/README
%doc %{_texmfdistdir}/doc/latex/tensor/tensor.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tensor/tensor.dtx
%doc %{_texmfdistdir}/source/latex/tensor/tensor.ins
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
