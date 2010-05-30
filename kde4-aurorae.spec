#
# Conditional build:
#
%define		orgname		aurorae
%define		kdever		4.4.4

Summary:	Aurorae Theme Engine
Summary(pl.UTF-8):	Aurore Theme Engine
Name:		kde4-aurorae
Version:	0.2.1
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://kde-look.org/CONTENT/content-files/107158-%{orgname}-%{version}.tar.gz
# Source0-md5:	7b92f0d8d661aaafbb2c391a64907906
URL:		http://kde-look.org/content/show.php/Aurorae+Theme+Engine?content=107158
# leave only required ones
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	kde4-kdebase-workspace-devel >= %{kdever}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aurorae is a theme engine for KWin window decorations.
It was created with the idea of making KWin decorations as themeable
as the Plasma desktop shell. Decoration and buttons are SVG files.

%description -l pl.UTF-8

%prep
%setup -q -n %{orgname}

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kwin3_aurorae.so
%attr(755,root,root) %{_libdir}/kde4/kwin_aurorae_config.so
%{_datadir}/apps/aurorae
%{_datadir}/apps/kwin/aurorae.desktop
%{_datadir}/config/aurorae.knsrc
