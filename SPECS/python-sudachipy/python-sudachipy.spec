# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sudachipy

Name:           python-sudachipy
Version:        0.6.11
Release:        %autorelease
Summary:        A Japanese morphological analyzer
License:        Apache-2.0
URL:            https://github.com/WorksApplications/sudachi.rs/
#!RemoteAsset:  sha256:b8910a4610de98b2c3cb6dc3362fea93e3ba5059f1eb445a68baa9585278f31b
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
#!RemoteAsset:  sha256:c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4
Source1:        https://raw.githubusercontent.com/WorksApplications/sudachi.rs/v%{version}/LICENSE
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  rust-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-rust)
BuildRequires:  python3dist(wheel)
BuildRequires:  crate(aho-corasick-1) >= 1.1.4
BuildRequires:  crate(anes-0.1) >= 0.1.6
BuildRequires:  crate(anstream-1) >= 1.0.0
BuildRequires:  crate(anstyle-1) >= 1.0.14
BuildRequires:  crate(anstyle-parse-1) >= 1.0.0
BuildRequires:  crate(anstyle-query-1) >= 1.1.5
BuildRequires:  crate(anstyle-wincon-3) >= 3.0.11
BuildRequires:  crate(arbitrary-1) >= 1.4.2
BuildRequires:  crate(autocfg-1) >= 1.5.0
BuildRequires:  crate(bitflags-2) >= 2.13.0
BuildRequires:  crate(bit-set-0.5) >= 0.5.3
BuildRequires:  crate(bit-vec-0.6) >= 0.6.3
BuildRequires:  crate(bumpalo-3) >= 3.20.2
BuildRequires:  crate(cast-0.3) >= 0.3.0
BuildRequires:  crate(cfg-if-1) >= 1.0.4
BuildRequires:  crate(ciborium-0.2) >= 0.2.2
BuildRequires:  crate(ciborium-io-0.2) >= 0.2.2
BuildRequires:  crate(ciborium-ll-0.2) >= 0.2.2
BuildRequires:  crate(clap-4) >= 4.6.1
BuildRequires:  crate(clap-builder-4) >= 4.6.0
BuildRequires:  crate(clap-derive-4) >= 4.6.1
BuildRequires:  crate(clap-lex-1) >= 1.1.0
BuildRequires:  crate(colorchoice-1) >= 1.0.5
BuildRequires:  crate(criterion-0.5) >= 0.5.1
BuildRequires:  crate(criterion-plot-0.5) >= 0.5.0
BuildRequires:  crate(crossbeam-deque-0.8) >= 0.8.6
BuildRequires:  crate(crossbeam-epoch-0.9) >= 0.9.18
BuildRequires:  crate(crossbeam-utils-0.8) >= 0.8.21
BuildRequires:  crate(crunchy-0.2) >= 0.2.4
BuildRequires:  crate(csv-1) >= 1.4.0
BuildRequires:  crate(csv-core-0.1) >= 0.1.13
BuildRequires:  crate(either-1) >= 1.16.0
BuildRequires:  crate(equivalent-1) >= 1.0.2
BuildRequires:  crate(fancy-regex-0.13) >= 0.13.0
BuildRequires:  crate(futures-core-0.3) >= 0.3.32
BuildRequires:  crate(futures-task-0.3) >= 0.3.32
BuildRequires:  crate(futures-util-0.3) >= 0.3.32
BuildRequires:  crate(half-2) >= 2.7.1
BuildRequires:  crate(hashbrown-0.17) >= 0.17.0
BuildRequires:  crate(heck-0.5) >= 0.5.0
BuildRequires:  crate(hermit-abi-0.5) >= 0.5.2
BuildRequires:  crate(honggfuzz-0.5) >= 0.5.60
BuildRequires:  crate(indexmap-2) >= 2.14.0
BuildRequires:  crate(indoc-2) >= 2.0.7
BuildRequires:  crate(is-terminal-0.4) >= 0.4.17
BuildRequires:  crate(is-terminal-polyfill-1) >= 1.70.2
BuildRequires:  crate(itertools-0.10) >= 0.10.5
BuildRequires:  crate(itertools-0.13) >= 0.13.0
BuildRequires:  crate(itoa-1) >= 1.0.18
BuildRequires:  crate(js-sys-0.3) >= 0.3.98
BuildRequires:  crate(lazy-static-1) >= 1.5.0
BuildRequires:  crate(libc-0.2) >= 0.2.186
BuildRequires:  crate(libloading-0.8) >= 0.8.9
BuildRequires:  crate(memchr-2) >= 2.8.1
BuildRequires:  crate(memmap2-0.9) >= 0.9.10
BuildRequires:  crate(memoffset-0.9) >= 0.9.1
BuildRequires:  crate(minimal-lexical-0.2) >= 0.2.1
BuildRequires:  crate(nom-7) >= 7.1.3
BuildRequires:  crate(num-traits-0.2) >= 0.2.19
BuildRequires:  crate(once-cell-1) >= 1.21.4
BuildRequires:  crate(once-cell-polyfill-1) >= 1.70.2
BuildRequires:  crate(oorandom-11) >= 11.1.5
BuildRequires:  crate(pin-project-lite-0.2) >= 0.2.17
BuildRequires:  crate(plotters-0.3) >= 0.3.7
BuildRequires:  crate(plotters-backend-0.3) >= 0.3.7
BuildRequires:  crate(plotters-svg-0.3) >= 0.3.7
BuildRequires:  crate(portable-atomic-1) >= 1.13.1
BuildRequires:  crate(proc-macro2-1) >= 1.0.106
BuildRequires:  crate(pyo3-0.27) >= 0.27.2
BuildRequires:  crate(pyo3-build-config-0.27) >= 0.27.2
BuildRequires:  crate(pyo3-ffi-0.27) >= 0.27.2
BuildRequires:  crate(pyo3-macros-0.27) >= 0.27.2
BuildRequires:  crate(pyo3-macros-backend-0.27) >= 0.27.2
BuildRequires:  crate(quote-1) >= 1.0.45
BuildRequires:  crate(rayon-1) >= 1.12.0
BuildRequires:  crate(rayon-core-1) >= 1.13.0
BuildRequires:  crate(regex-1) >= 1.12.3
BuildRequires:  crate(regex-automata-0.4) >= 0.4.14
BuildRequires:  crate(regex-syntax-0.8) >= 0.8.10
BuildRequires:  crate(rustc-version-0.4) >= 0.4.1
BuildRequires:  crate(rustversion-1) >= 1.0.22
BuildRequires:  crate(ryu-1) >= 1.0.23
BuildRequires:  crate(same-file-1) >= 1.0.6
BuildRequires:  crate(scopeguard-1) >= 1.2.0
BuildRequires:  crate(semver-1) >= 1.0.28
BuildRequires:  crate(serde-1) >= 1.0.228
BuildRequires:  crate(serde-core-1) >= 1.0.228
BuildRequires:  crate(serde-derive-1) >= 1.0.228
BuildRequires:  crate(serde-json-1) >= 1.0.150
BuildRequires:  crate(slab-0.4) >= 0.4.12
BuildRequires:  crate(strsim-0.11) >= 0.11.1
BuildRequires:  crate(syn-2) >= 2.0.117
BuildRequires:  crate(target-lexicon-0.13) >= 0.13.5
BuildRequires:  crate(thiserror-1) >= 1.0.69
BuildRequires:  crate(thiserror-impl-1) >= 1.0.69
BuildRequires:  crate(thread-local-1) >= 1.1.9
BuildRequires:  crate(tinytemplate-1) >= 1.2.1
BuildRequires:  crate(tinyvec-1) >= 1.11.0
BuildRequires:  crate(tinyvec-macros-0.1) >= 0.1.1
BuildRequires:  crate(unicode-ident-1) >= 1.0.24
BuildRequires:  crate(unicode-normalization-0.1) >= 0.1.25
BuildRequires:  crate(unindent-0.2) >= 0.2.4
BuildRequires:  crate(utf8parse-0.2) >= 0.2.2
BuildRequires:  crate(walkdir-2) >= 2.5.0
BuildRequires:  crate(wasm-bindgen-0.2) >= 0.2.121
BuildRequires:  crate(wasm-bindgen-macro-0.2) >= 0.2.121
BuildRequires:  crate(wasm-bindgen-macro-support-0.2) >= 0.2.121
BuildRequires:  crate(wasm-bindgen-shared-0.2) >= 0.2.121
BuildRequires:  crate(web-sys-0.3) >= 0.3.98
BuildRequires:  crate(winapi-util-0.1) >= 0.1.11
BuildRequires:  crate(windows-link-0.2) >= 0.2.1
BuildRequires:  crate(windows-sys-0.61) >= 0.61.2
BuildRequires:  crate(yada-0.5) >= 0.5.1
BuildRequires:  crate(zerocopy-0.8) >= 0.8.50
BuildRequires:  crate(zerocopy-derive-0.8) >= 0.8.50
BuildRequires:  crate(zmij-1) >= 1.0.21

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
SudachiPy is a Python implementation of Sudachi, a Japanese morphological
analyzer. It provides robust word segmentation and part-of-speech tagging,
designed for high-performance natural language processing.

%generate_buildrequires
%pyproject_buildrequires

%prep -a
cp %{SOURCE1} .

rm -f Cargo.lock
mkdir -p .cargo ~/.cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "system-registry"

[source.system-registry]
directory = "/usr/share/cargo/registry"
EOF
cp .cargo/config.toml ~/.cargo/config.toml

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/sudachipy

%changelog
%autochangelog
