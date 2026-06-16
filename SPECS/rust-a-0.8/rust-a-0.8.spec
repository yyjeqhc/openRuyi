Name:           rust-a-0.8
Version:        0.8.0
Release:        1
Summary:        Dummy provider for crate(a-0.8)
License:        MIT
BuildArch:      noarch

Provides:       crate(a-0.8) = %{version}
Provides:       crate(a-0.8/default) = %{version}

%description
Dummy package to test virtual Rust crate provides.

%install
mkdir -p %{buildroot}%{_datadir}/dummy-crates/a-0.8
echo "a 0.8" > %{buildroot}%{_datadir}/dummy-crates/a-0.8/provider.txt

%files
%{_datadir}/dummy-crates/a-0.8/provider.txt

%changelog
