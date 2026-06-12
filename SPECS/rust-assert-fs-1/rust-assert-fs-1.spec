%global crate_name assert_fs
%global full_version 1.1.3
%global pkgname assert-fs-1

Name:           rust-assert-fs-1
Version:        1.1.3
Release:        %autorelease
Summary:        Rust crate "assert_fs"
License:        MIT OR Apache-2.0
URL:            https://github.com/assert-rs/assert_fs
#!RemoteAsset:  sha256:a652f6cb1f516886fcfee5e7a5c078b9ade62cfcb889524efe5a64d682dd27a9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anstyle-1/default) >= 1.0.0
Requires:       crate(doc-comment-0.3/default) >= 0.3.0
Requires:       crate(globwalk-0.9/default) >= 0.9.0
Requires:       crate(predicates-3/diff) >= 3.0.1
Requires:       crate(predicates-core-1/default) >= 1.0.6
Requires:       crate(predicates-tree-1/default) >= 1.0.1
Requires:       crate(tempfile-3/default) >= 3.8.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "assert_fs"

%package     -n %{name}+color
Summary:        Filesystem fixtures and assertions for testing - feature "color" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(anstream-0.6/default) >= 0.6.7
Requires:       crate(predicates-3/color) >= 3.0.1
Requires:       crate(predicates-3/diff) >= 3.0.1
Provides:       crate(%{pkgname}/color) = %{version}
Provides:       crate(%{pkgname}/color-auto) = %{version}

%description -n %{name}+color
This metapackage enables feature "color" for the Rust assert_fs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "color-auto" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
