Summary:        Flatpak host extension with asahi OpenGL driver Fedora Asahi Remix
Name:           flatpak-mesa-asahi
# Use the time of the last metadata update as version
Version:        2023.08.20240228
Release:        1%{?dist}
License:        MIT
URL:            https://fedora-asahi-remix.org/
Source1:        org.freedesktop.Platform.GL.asahi.yml
Source2:        org.freedesktop.Platform.GL.asahi.metainfo.xml
BuildArch:      aarch64

BuildRequires: flatpak
BuildRequires: flatpak-builder

%description
Flatpak host extension for Asahi Mesa drivers

%prep
cp -p %SOURCE1 %SOURCE2 .
flatpak remote-add --user --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install --assumeyes --user flathub org.freedesktop.Sdk//23.08 org.freedesktop.Platform//23.08 org.freedesktop.Sdk.Extension.llvm17//23.08

%build
flatpak-builder --user --install --force-clean build-dir org.freedesktop.Platform.GL.asahi.yml

%install

%files
%license LICENSE

%changelog
* Sat May 11 2024 Janne Grunau <janne-fdr@jananu.net> - 2023.08.20240228-1
- Initial package
