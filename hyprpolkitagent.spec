Name:		hyprpolkitagent
Version:	0.1.3
Release:	1
Summary:	A polkit authentication agent written in QT/QML
Group:		Hyprland
License:	BSD-3-Clause
URL:		https://github.com/hyprwm/%{name}
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	pkgconfig(hyprutils)
BuildRequires:	pkgconfig(polkit-agent-1)
BuildRequires:	pkgconfig(polkit-qt6-1)

Requires: hyprland-qt-support

BuildSystem: cmake

%description
%{summary}

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%files
%license LICENSE
%doc README.md
%{_datadir}/dbus-1/services/org.hyprland.%{name}.service
%{_libexecdir}/%{name}
%{_userunitdir}/%{name}.service
