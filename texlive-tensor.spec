# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/tensor
# catalog-date 2006-11-03 07:18:50 +0100
# catalog-license lppl
# catalog-version 2.1
Name:		texlive-tensor
Version:	2.1
Release:	6
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.1-2
+ Revision: 756582
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.1-1
+ Revision: 719668
- texlive-tensor
- texlive-tensor
- texlive-tensor

