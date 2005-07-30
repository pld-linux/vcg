Summary:	The VCG visualization tool for compiler graphs
Summary(pl):	Narzêdzie do wizualizacji grafów kompilacji
Name:		vcg
Version:	1.30
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.cs.uni-sb.de/pub/graphics/vcg/%{name}.tgz
# Source0-md5:	283faf1a2cc163d5c0e4977b8ec1f658
Patch0:		%{name}-LINUX.patch
URL:		http://www.cs.uni-sb.de/RW/users/sander/html/gsvcg1.html
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
Narzêdzie VCG odczytuje tekstow± i czyteln± specyfikacjê grafu i
wy¶wietla go. Je¿eli nie wszystkie pozycje li¶ci s± ustalone,
narzêdzie tworzy graf korzystaj±c z kilku heurystyk redukuj±c liczbê
przeciêæ, minimalizuj±c wielko¶æ krawêdzi, centruj±c li¶cie.
Specyfikacja jêzyka wykorzystywanego przez VCG jest niemal
kompatybilna z GRL, jêzykiem narzêdzi krawêdzi, ale zawiera kilka
rozszerzeñ. VCG pozwala na trzymanie dynamicznie i statycznie
ustalonych regionów grafu. U¿ywa kolorów i dzia³a pod X11.

%prep
%setup -q -n %{name}.%{version}
%patch0 -p1 -z .pix

%build
%{__make} xvcg_gcc_noxmkmf xvcg \
	CFLAGS="-c %{rpmcflags}" \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1 \
	LIBPATH="-L%{_prefix}/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	SED=sed \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

cp -f demo/demo.csh expl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README expl
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
