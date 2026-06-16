Name:           rust-a-0.9
Version:        0.9.0
Release:        1
Summary:        Dummy provider for crate(a-0.9)
License:        MIT
BuildArch:      noarch

Provides:       crate(a-0.9) = %{version}
Provides:       crate(a-0.9/default) = %{version}

%description
Dummy package to test virtual Rust crate provides.

%install
mkdir -p %{buildroot}%{_datadir}/dummy-crates/a-0.9
echo "a 0.9" > %{buildroot}%{_datadir}/dummy-crates/a-0.9/provider.txt

%files
%{_datadir}/dummy-crates/a-0.9/provider.txt

%changelog
