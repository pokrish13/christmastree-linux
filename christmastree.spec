Name:           christmastree
Version:        1.0.0
Release:        1%{?dist}
Summary:        Animated Christmas tree for terminal

License:        MIT
URL:            https://github.com/pokrish13/christmastree-linux
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

%description
Animated Christmas tree that runs in Linux terminal with colorful lights.
Perfect for holiday season! Brings festive mood to your terminal.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 Christmastree %{buildroot}%{_bindir}/

%files
%{_bindir}/Christmastree

%changelog
* Tue Nov 04 2025 Pokrish <kirashulgin@gmail.com> - 1.0.0-1
- Initial release of Christmastree
- Animated Christmas tree with colorful blinking lights
- Perfectly centered symmetric design
- Star on top and festive holiday messages
