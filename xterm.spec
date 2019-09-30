Name:		xterm
Version:	334
Release:        2
Summary:	It is a terminal emulator for the X Window System
License:	MIT
URL:		https://invisible-island.net/xterm
Source0:	ftp://ftp.invisible-island.net/xterm/xterm-334.tgz
Source1: 	ftp://ftp.invisible-island.net/xterm/16colors.txt
Patch0: 	xterm-defaults.patch
Patch1: 	xterm-desktop.patch
Patch2: 	xterm-man-paths.patch

BuildRequires: 	gcc git pkgconfig ncurses-devel libutempter-devel
BuildRequires: 	libXft-devel libXaw-devel libXext-devel desktop-file-utils
BuildRequires: 	libxkbfile-devel xorg-x11-apps

provides:	xterm-resize = 334-2
Obsoletes:	xterm-resize < 334-2

%bcond_with trace

%description
The xterm program is a terminal emulator for the X Window System.
It provides DEC VT102 and Tektronix 4014 compatible terminals.

%package	help
Summary: 	Doc files for xterm

%description 	help
The xterm-help package contains doc files for xterm.

%prep
%autosetup -n xterm-334 -p1 -S git

iconv -f iso8859-1 -t utf-8 < THANKS > TEMP
touch -r THANKS TEMP; mv TEMP THANKS

echo %{_datadir}/X11/app-defaults

%build
%configure --enable-meta-sends-esc --disable-backarrow-key --enable-256-color \
           --enable-exec-xterm --enable-luit --enable-warnings --enable-wide-chars \
	   --with-app-defaults=%{_datadir}/X11/app-defaults --with-icon-theme=hicolor \
	   --with-icondir=%{_datadir}/icons --with-utempter --with-tty-group=tty \
	   --disable-full-tgetent

%make_build

%install
%make_install

cp -fp %{SOURCE1} 16colors.txt
desktop-file-install --dir=%{buildroot}/%{_datadir}/applications xterm.desktop
mkdir -p %{buildroot}/%{_datadir}/appdata
install -m 644 -p xterm.appdata.xml %{buildroot}/%{_datadir}/appdata

%files
%doc 16colors.txt THANKS
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
* Wed Aug 28 2019 luhuaxin <luhuaxin@huawei.com> - 334-2
- Package init
