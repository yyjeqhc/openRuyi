Name:           test-a-or
Version:        1
Release:        1
Summary:        Test OR dependency on crate(a-0.8) or crate(a-0.9)
License:        MIT
BuildArch:      noarch

BuildRequires:  (crate(a-0.8) or crate(a-0.9))

%description
Dummy package to test RPM rich dependency with crate virtual provides.

%install
mkdir -p %{buildroot}%{_datadir}/dummy-crates/test-a-or
echo "ok" > %{buildroot}%{_datadir}/dummy-crates/test-a-or/result.txt

%files
%{_datadir}/dummy-crates/test-a-or/result.txt

%changelog
