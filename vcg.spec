Summary:	The VCG visualization tool for compiler graphs
Summary(pl):	Narz�dzie do wizualizacji graf�w kompilacji
Name:		vcg
Version:	1.30
Release:	1
License:	GPL
Group:		Applications/Graphics
URL:		http://www.cs.uni-sb.de/RW/users/sander/html/gsvcg1.html
Source0:	ftp://ftp.cs.uni-sb.de/pub/graphics/vcg/%{name}.tgz
Patch0:		%{name}-LINUX.patch
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The VCG tool reads a textual and readable specification of a graph and
visualizes the graph. If not all positions of nodes are fixed, the
tool layouts the graph using several heuristics as reducing the number
of crossings, minimizing the size of edges, centering of nodes. The
specification language of the VCG tool is nearly compatible to GRL,
the language of the edge tool, but contains many extensions. The VCG
tool allows folding of dynamically or statically specified regions of
the graph. It uses colors and runs on X11.


%description -l pl
Narz�dzie VCG odrzytuje tekstowa i czyteln� specyfikacj� grafi i
wy�wietla go. Je�eli nie wszystkie pozycje li�ci s� ustalone,
narz�dzie tworzy graf korzystaj�c z kilku heurestyk redukuj�c liczb�
przeci��, minimalizuj�c wielko�� kraw�dzi, centruj�c li�cie.
Specyfikacja j�zyka wykorzystywanego przez VCG jest niemal
kompatybilna z GRL, j�zykiem narz�dzi krawd�dzi, ale zawiera kilka
rozszerze�. VCG pozwala na trzymanie dynamicznie i statycznie
ustalonych region�w grafu. Wykorzystuje kolorki i dzia�a pod X11.

%prep
%setup -q -n %{name}.%{version}
%patch0 -p1 -z .pix

%build
%{__make} xvcg_gcc_noxmkmf xvcg CFLAGS="-c %{rpmcflags}" BINDIR=%{_bindir} MANDIR=%{_mandir}/man1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1}
%{__make} SED=sed BINDIR=$RPM_BUILD_ROOT/%{_bindir} MANDIR=$RPM_BUILD_ROOT/%{_mandir}/man1 install

cp -f demo/demo.csh expl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README expl
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
