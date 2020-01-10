Name:           kcm_touchpad
Version:        0.3.1
Release:        9%{?dist}
Summary:        Synaptics driver based touchpads kcontrol module

Group:          User Interfaces/Desktops
License:        GPLv2
URL:            http://kde-apps.org/content/show.php/kcm_touchpad?content=113335
Source0:        http://download.github.com/mishaaq-kcm_touchpad-00370b5.tar.gz
Patch0:         kcm_touchpad-0.3.1-scrollbar.patch
# Kubuntu patches:
Patch1:         kcm_touchpad-0.3.1-disable-smart-mode-settings.patch
Patch2:         kcm_touchpad-0.3.1-load-error-checking.patch
Patch3:         kcm_touchpad-0.3.1-fix-high-sensitivity.patch
Patch4:         kcm_touchpad-0.3.1-fix-circular-scrolling.patch
# This one is basically the same as Kubuntu's patch 05:
Patch5:         kcm_touchpad-0.3.1-new-systemsettings-layout.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  kdelibs4-devel gettext

# need kcmshell4 from kdebase-runtime at least
Requires: kdebase-runtime%{?_kde4_version: >= %{_kde4_version}}


%description
A KDE System Settings module to to configure synaptics based touchpads.


%prep
%setup -q -n mishaaq-kcm_touchpad-00370b5
%patch0 -p1 -b .scrollbar
%patch1 -p1 -b .disable-smart-mode-settings
%patch2 -p1 -b .load-error-checking
%patch3 -p1 -b .fix-high-sensitivity
%patch4 -p1 -b .fix-circular-scrolling
%patch5 -p1 -b .new-systemsettings-layout


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags}  -C %{_target_platform}


%install
rm -rf %{buildroot}
make install/fast DESTDIR=%{buildroot}  -C %{_target_platform}

rm -rf %{buildroot}%{_kde4_docdir}/%{name}/

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS LICENSE README
%{_kde4_libdir}/kde4/kcm_touchpad.so
%{_kde4_datadir}/kde4/services/touchpad.desktop


%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.3.1-6
- Merge bugfixes from Kubuntu, fixes circular scrolling and more (#633353)
- Drop default kcmtouchpadrc, use driver defaults (#611611)
- Make the Scrolling tab use a vertical scrollbar if needed (#600121)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 28 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.3.1-4
- Requires: kdebase-runtime
- cmake cosmetics

* Tue Sep 7  2010 Ryan Rix <ry@n.rix.si> - 0.3.1-3
- Update the category to adhere to new SC 4.5 systemsettings layout. Will now
  appear under the "input devices" section.

* Sat Jun 5  2010 Ryan Rix <ry@n.rix.si> - 0.3.1-2
- Ship a default config file For Greater Justice

* Sat Feb 20 2010 Ryan Rix <ry@n.rix.si> - 0.3.1-1
- New source

* Tue Nov 24 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.3.0-6
- Rebuild for Qt 4.6.0 RC1 in F13 (was built against Beta 1 with unstable ABI)

* Thu Nov 12 2009 Ryan Rix < phrkonaleash [AT] gmail dot com > - 0.3.0-5
- I'm just going to remove that BR.

* Thu Nov 12 2009 Ryan Rix < phrkonaleash [AT] gmail dot com > - 0.3.0-4
- Bumpint spec, fixing that build require :9

* Thu Nov 12 2009 Ryan Rix < phrkonaleash [AT] gmail dot com > - 0.3.0-3
- Added specific build require for libXi-devel because it was dying in dist-f10.

* Wed Nov 4 2009 Ryan Rix < phrkonaleash [AT] gmail dot com > - 0.3.0-2
- Update source URL and category

* Tue Nov 3 2009 Ryan Rix < phrkonaleash [AT] gmail dot com > - 0.3.0-1
- Updated source.
- Updated BR
- Removed now unnecessary Patch0

* Fri Oct 16 2009 Ryan Rix < phrkonaleash [AT] gmail dot com > - 0.2.1-1
- initial package
