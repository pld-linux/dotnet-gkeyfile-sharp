#
%include	/usr/lib/rpm/macros.mono
#
Summary:	.NET bindings for GLib2's keyfile implementation
Summary(pl.UTF-8):	Wiązania implementacji GLib2 keyfile dla .NET
Name:		dotnet-gkeyfile-sharp
Version:	0.1
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	gkeyfile-sharp-%{version}.tar.gz
# Source0-md5:	52988c1293443b8cb536d1b971a14158
URL:		http://github.com/mono/gkeyfile-sharp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.12.9
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	mono-csharp >= 2.0.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(monoautodeps)
Requires:	glib2 >= 1:2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for .NET to GLib2's keyfile
implementation.

%description -l pl.UTF-8
Pakiet ten dostarcza wiązania dla .NET do implementacji GLib2 keyfile.

%package devel
Summary:	gkeyfile-sharp development files
Summary(pl.UTF-8):	Pliki programistyczne gkeyfile-sharp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dotnet-gtk-sharp2-devel >= 2.12.9

%description devel
gkeyfile-sharp development files.

%description devel -l pl.UTF-8
Pliki programistyczne gkeyfile-sharp.

%prep
%setup -q -n mono-gkeyfile-sharp-1a1adb8/

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_prefix}/lib/mono/gac/gkeyfile-sharp

%files devel
%defattr(644,root,root,755)
%dir %{_prefix}/lib/mono/gkeyfile-sharp
%{_prefix}/lib/mono/gkeyfile-sharp/gkeyfile-sharp.dll
%{_pkgconfigdir}/gkeyfile-sharp.pc
