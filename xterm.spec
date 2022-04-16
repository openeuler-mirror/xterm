Name:		xterm
Version:	372
Release:        1
Summary:	It is a terminal emulator for the X Window System
License:	MIT
URL:		http://invisible-island.net/xterm
Source0:	https://invisible-mirror.net/archives/xterm/xterm-%{version}.tgz

BuildRequires: 	gcc pkgconfig ncurses-devel libutempter-devel
BuildRequires: 	libXft-devel libXaw-devel libXext-devel desktop-file-utils
BuildRequires: 	libxkbfile-devel xorg-x11-apps

provides:	xterm-resize = %{version}-%{release}
Obsoletes:	xterm-resize < %{version}-%{release}

%bcond_with trace

%description
The xterm program is a terminal emulator for the X Window System.
It provides DEC VT102 and Tektronix 4014 compatible terminals.

%package	help
Summary: 	Doc files for xterm

%description 	help
The xterm-help package contains doc files for xterm.

%prep
%autosetup -n xterm-%{version} -p1

iconv -f iso8859-1 -t utf-8 < THANKS > TEMP
touch -r THANKS TEMP; mv TEMP THANKS

%build
%configure --enable-meta-sends-esc --disable-backarrow-key --enable-256-color \
           --enable-exec-xterm --enable-luit --enable-warnings --enable-wide-chars \
	   --with-app-defaults=%{_datadir}/X11/app-defaults --with-icon-theme=hicolor \
	   --with-icondir=%{_datadir}/icons --with-utempter --with-tty-group=tty \
	   --disable-full-tgetent

%make_build

%install
%make_install

desktop-file-install --dir=%{buildroot}/%{_datadir}/applications xterm.desktop
mkdir -p %{buildroot}/%{_datadir}/appdata
install -m 644 -p xterm.appdata.xml %{buildroot}/%{_datadir}/appdata

%files
%doc THANKS
%{_bindir}/*xterm
%{_datadir}/X11/app-defaults/*
%{_datadir}/appdata/xterm.appdata.xml
%{_datadir}/applications/xterm.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/pixmaps/*
%{_bindir}/resize

%files help
%doc README.i18n ctlseqs.txt xterm.log.html
%{_mandir}/man1/*

%changelog
* Sun Apr 17 2022 YukariChiba <i@0x7f.cc> - 372-1
- Upgrade version to 372

* Tue Feb 22 2022 xingxing <xingxing9@h-partners.com> - 363-4
- fix CVE-2022-24130

* Fri Jul 30 2021 chenyanpanHW <chenyanpan@huawei.com> - 363-3
- DESC: delete -S git from %autosetup, and delete BuildRequires git

* Wed Mar 03 2021 jinzhimin <jinzhimin2@huawei.com> - 363-2
- fix CVE-2021-27135

* Thu Jan 28 2021 jinzhimin <jinzhimin2@huawei.com> - 363-1
- Upgrade to 363

* Thu Sep 29 2020 hanhui <hanhui15@huawei.com> - 334-6
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:modify source url

* Thu Sep 10 2020 hanhui <hanhui15@huawei.com> - 334-5
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:modify source url

* Thu Jan 3 2020 openEuler Buildteam <buildteam@openeuler.org> - 334-4
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:optimization the spec

* Mon Sep 30 2019 luhuaxin <luhuaxin@huawei.com> - 334-3
- Type: enhancement
- ID: NA
- SUG: NA
- DESC: package rebuild

* Wed Aug 28 2019 luhuaxin <luhuaxin@huawei.com> - 334-2
- Package init
