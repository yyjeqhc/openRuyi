# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cargo
%global full_version 0.95.0
%global pkgname cargo-0.95

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-cargo-0.95
Version:        0.95.0
Release:        %autorelease
Summary:        Rust crate "cargo"
License:        MIT OR Apache-2.0
URL:            https://doc.rust-lang.org/cargo/index.html
#!RemoteAsset:  sha256:0af45a75a5265a587a8d9e4098cd2b12a07b34bcbd9eb7952ae6a62ea6d65c4d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(annotate-snippets-0.12/default) >= 0.12.15
Requires:       crate(annotate-snippets-0.12/simd) >= 0.12.15
Requires:       crate(anstream-0.6/default) >= 0.6.21
Requires:       crate(anstyle-1.0/default) >= 1.0.14
Requires:       crate(anyhow-1.0/default) >= 1.0.102
Requires:       crate(base64-0.22/default) >= 0.22.1
Requires:       crate(blake3-1.0/default) >= 1.8.4
Requires:       crate(cargo-credential-0.4/default) >= 0.4.9
Requires:       crate(cargo-credential-libsecret-0.5/default) >= 0.5.5
Requires:       crate(cargo-credential-macos-keychain-0.4/default) >= 0.4.20
Requires:       crate(cargo-credential-wincred-0.4/default) >= 0.4.20
Requires:       crate(cargo-platform-0.3/default) >= 0.3.2
Requires:       crate(cargo-util-0.2/default) >= 0.2.27
Requires:       crate(cargo-util-schemas-0.12/default) >= 0.12.0
Requires:       crate(clap-4.0/default) >= 4.6.0
Requires:       crate(clap-4.0/wrap-help) >= 4.6.0
Requires:       crate(clap-complete-4.0/default) >= 4.6.1
Requires:       crate(clap-complete-4.0/unstable-dynamic) >= 4.6.1
Requires:       crate(color-print-0.3/default) >= 0.3.7
Requires:       crate(crates-io-0.40/default) >= 0.40.17
Requires:       crate(curl-0.4/default) >= 0.4.49
Requires:       crate(curl-0.4/http2) >= 0.4.49
Requires:       crate(curl-sys-0.4/default) >= 0.4.87
Requires:       crate(filetime-0.2/default) >= 0.2.27
Requires:       crate(flate2-1.0/zlib-rs) >= 1.1.9
Requires:       crate(git2-0.20/default) >= 0.20.4
Requires:       crate(git2-curl-0.21/default) >= 0.21.0
Requires:       crate(gix-0.77/dirwalk) >= 0.77.0
Requires:       crate(gix-0.77/parallel) >= 0.77.0
Requires:       crate(gix-0.77/progress-tree) >= 0.77.0
Requires:       crate(gix-0.77/status) >= 0.77.0
Requires:       crate(glob-0.3/default) >= 0.3.3
Requires:       crate(hex-0.4/default) >= 0.4.3
Requires:       crate(hmac-0.12/default) >= 0.12.1
Requires:       crate(home-0.5/default) >= 0.5.12
Requires:       crate(http-auth-0.1) >= 0.1.10
Requires:       crate(ignore-0.4/default) >= 0.4.25
Requires:       crate(im-rc-15.0/default) >= 15.1.0
Requires:       crate(indexmap-2.0/default) >= 2.14.0
Requires:       crate(itertools-0.14/default) >= 0.14.0
Requires:       crate(jiff-0.2/serde) >= 0.2.23
Requires:       crate(jiff-0.2/std) >= 0.2.23
Requires:       crate(jobserver-0.1/default) >= 0.1.34
Requires:       crate(libc-0.2/default) >= 0.2.184
Requires:       crate(libgit2-sys-0.18/default) >= 0.18.3
Requires:       crate(memchr-2.0/default) >= 2.8.0
Requires:       crate(opener-0.8/default) >= 0.8.4
Requires:       crate(os-info-3.0) >= 3.14.0
Requires:       crate(pasetors-0.7/default) >= 0.7.8
Requires:       crate(pasetors-0.7/paserk) >= 0.7.8
Requires:       crate(pasetors-0.7/serde) >= 0.7.8
Requires:       crate(pasetors-0.7/std) >= 0.7.8
Requires:       crate(pasetors-0.7/v3) >= 0.7.8
Requires:       crate(pathdiff-0.2/default) >= 0.2.3
Requires:       crate(rand-0.9/default) >= 0.9.2
Requires:       crate(regex-1.0/default) >= 1.12.3
Requires:       crate(rusqlite-0.38/bundled) >= 0.38.0
Requires:       crate(rusqlite-0.38/default) >= 0.38.0
Requires:       crate(rusqlite-0.38/fallible-uint) >= 0.38.0
Requires:       crate(rustc-hash-2.0/default) >= 2.1.2
Requires:       crate(rustc-stable-hash-0.1/default) >= 0.1.2
Requires:       crate(rustfix-0.9/default) >= 0.9.4
Requires:       crate(same-file-1.0/default) >= 1.0.6
Requires:       crate(semver-1.0/default) >= 1.0.28
Requires:       crate(semver-1.0/serde) >= 1.0.28
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-1.0/derive) >= 1.0.228
Requires:       crate(serde-ignored-0.1/default) >= 0.1.14
Requires:       crate(serde-json-1.0/default) >= 1.0.149
Requires:       crate(serde-json-1.0/raw-value) >= 1.0.149
Requires:       crate(serde-untagged-0.1/default) >= 0.1.9
Requires:       crate(sha1-0.10/default) >= 0.10.6
Requires:       crate(shell-escape-0.1/default) >= 0.1.5
Requires:       crate(supports-hyperlinks-3.0/default) >= 3.2.0
Requires:       crate(supports-unicode-3.0/default) >= 3.0.0
Requires:       crate(tar-0.4) >= 0.4.45
Requires:       crate(tempfile-3.0/default) >= 3.27.0
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Requires:       crate(time-0.3/default) >= 0.3.47
Requires:       crate(time-0.3/formatting) >= 0.3.47
Requires:       crate(time-0.3/parsing) >= 0.3.47
Requires:       crate(time-0.3/serde) >= 0.3.47
Requires:       crate(toml-0.9/display) >= 0.9.12
Requires:       crate(toml-0.9/parse) >= 0.9.12
Requires:       crate(toml-0.9/preserve-order) >= 0.9.12
Requires:       crate(toml-0.9/serde) >= 0.9.12
Requires:       crate(toml-0.9/std) >= 0.9.12
Requires:       crate(toml-edit-0.24/default) >= 0.24.1
Requires:       crate(toml-edit-0.24/serde) >= 0.24.1
Requires:       crate(tracing-0.1/attributes) >= 0.1.44
Requires:       crate(tracing-0.1/std) >= 0.1.44
Requires:       crate(tracing-chrome-0.7/default) >= 0.7.2
Requires:       crate(tracing-subscriber-0.3/default) >= 0.3.23
Requires:       crate(tracing-subscriber-0.3/env-filter) >= 0.3.23
Requires:       crate(unicase-2.0/default) >= 2.9.0
Requires:       crate(unicode-ident-1.0/default) >= 1.0.24
Requires:       crate(unicode-width-0.2/default) >= 0.2.2
Requires:       crate(url-2.0/default) >= 2.5.8
Requires:       crate(walkdir-2.0/default) >= 2.5.0
Requires:       crate(windows-sys-0.61/default) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-security) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-storage-filesystem) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-console) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-io) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-jobobjects) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-threading) >= 0.61.2
Requires:       crate(winnow-0.7/default) >= 0.7.15
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "cargo"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
