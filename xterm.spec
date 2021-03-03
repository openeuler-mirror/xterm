Name:		xterm
Version:	363
Release:        2
Summary:	It is a terminal emulator for the X Window System
License:	MIT
URL:		http://invisible-island.net/xterm
Source0:	https://invisible-mirror.net/archives/xterm/xterm-%{version}.tgz

Patch6000:      backport-CVE-2021-27135.patch

BuildRequires: 	gcc git pkgconfig ncurses-devel libutempter-devel
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
%autosetup -n xterm-363 -p1 -S git

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
