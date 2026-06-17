# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global cairo_version 1.18.0

Name:           librsvg
Version:        2.62.3
Release:        %autorelease
Summary:        An SVG library based on cairo
License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/LibRsvg
#!RemoteAsset:  sha256:7eb449b2722a768021356f66dfee3202c229b54ed4e6a70ce40c090e97ff16f2
Source0:        https://download.gnome.org/sources/librsvg/2.62/librsvg-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Ddocs=disabled
BuildOption(conf):  -Dtests=false
BuildOption(conf):  -Dpixbuf-loader=disabled
BuildOption(conf):  -Ddocs=enabled
BuildOption(conf):  -Dtests=true

BuildRequires:  python3dist(docutils)
BuildRequires:  crate(adler2-2) >= 2.0.1
BuildRequires:  crate(ahash-0.8) >= 0.8.12
BuildRequires:  crate(aho-corasick-1) >= 1.1.4
BuildRequires:  crate(android-system-properties-0.1) >= 0.1.5
BuildRequires:  crate(anstream-1) >= 1.0.0
BuildRequires:  crate(anstyle-1) >= 1.0.14
BuildRequires:  crate(anstyle-parse-1) >= 1.0.0
BuildRequires:  crate(anstyle-query-1) >= 1.1.5
BuildRequires:  crate(anstyle-wincon-3) >= 3.0.11
BuildRequires:  crate(approx-0.5) >= 0.5.1
BuildRequires:  crate(autocfg-1) >= 1.5.0
BuildRequires:  crate(av-data-0.4) >= 0.4.4
BuildRequires:  crate(bitflags-2) >= 2.13.0
BuildRequires:  crate(bitreader-0.3) >= 0.3.11
BuildRequires:  crate(block-0.1) >= 0.1.6
BuildRequires:  crate(bumpalo-3) >= 3.20.2
BuildRequires:  crate(bytemuck-1) >= 1.25.0
BuildRequires:  crate(byteorder-1) >= 1.5.0
BuildRequires:  crate(byteorder-lite-0.1) >= 0.1.0
BuildRequires:  crate(bytes-1) >= 1.11.1
BuildRequires:  crate(byte-slice-cast-1) >= 1.2.3
BuildRequires:  crate(cairo-rs-0.22) >= 0.22.0
BuildRequires:  crate(cairo-sys-rs-0.22) >= 0.22.0
BuildRequires:  crate(cast-0.3) >= 0.3.0
BuildRequires:  crate(cc-1) >= 1.2.63
BuildRequires:  crate(cfg-expr-0.20) >= 0.20.8
BuildRequires:  crate(cfg-if-1) >= 1.0.4
BuildRequires:  crate(chrono-0.4) >= 0.4.44
BuildRequires:  crate(clap-4) >= 4.6.1
BuildRequires:  crate(clap-builder-4) >= 4.6.0
BuildRequires:  crate(clap-complete-4) >= 4.6.3
BuildRequires:  crate(clap-derive-4) >= 4.6.1
BuildRequires:  crate(clap-lex-1) >= 1.1.0
BuildRequires:  crate(colorchoice-1) >= 1.0.5
BuildRequires:  crate(color-quant-1) >= 1.1.0
BuildRequires:  crate(core-foundation-sys-0.8) >= 0.8.7
BuildRequires:  crate(crc32fast-1) >= 1.5.0
BuildRequires:  crate(crossbeam-deque-0.8) >= 0.8.6
BuildRequires:  crate(crossbeam-epoch-0.9) >= 0.9.18
BuildRequires:  crate(crossbeam-utils-0.8) >= 0.8.21
BuildRequires:  crate(cssparser-0.35) >= 0.35.0
BuildRequires:  crate(cssparser-color-0.3) >= 0.3.0
BuildRequires:  crate(cssparser-macros-0.6) >= 0.6.1
BuildRequires:  crate(data-url-0.3) >= 0.3.2
BuildRequires:  crate(dav1d-0.11) >= 0.11.1
BuildRequires:  crate(dav1d-sys-0.8) >= 0.8.3
BuildRequires:  crate(derive-more-2) >= 2.1.1
BuildRequires:  crate(derive-more-impl-2) >= 2.1.1
BuildRequires:  crate(displaydoc-0.2) >= 0.2.5
BuildRequires:  crate(dlib-0.5) >= 0.5.3
BuildRequires:  crate(dtoa-1) >= 1.0.11
BuildRequires:  crate(dtoa-short-0.3) >= 0.3.5
BuildRequires:  crate(either-1) >= 1.16.0
BuildRequires:  crate(encoding-rs-0.8) >= 0.8.35
BuildRequires:  crate(equivalent-1) >= 1.0.2
BuildRequires:  crate(fallible-collections-0.4) >= 0.4.9
BuildRequires:  crate(fdeflate-0.3) >= 0.3.7
BuildRequires:  crate(find-msvc-tools-0.1) >= 0.1.9
BuildRequires:  crate(flate2-1) >= 1.1.9
BuildRequires:  crate(float-cmp-0.10) >= 0.10.0
BuildRequires:  crate(form-urlencoded-1) >= 1.2.2
BuildRequires:  crate(futf-0.1) >= 0.1.5
BuildRequires:  crate(futures-channel-0.3) >= 0.3.32
BuildRequires:  crate(futures-core-0.3) >= 0.3.32
BuildRequires:  crate(futures-executor-0.3) >= 0.3.32
BuildRequires:  crate(futures-io-0.3) >= 0.3.32
BuildRequires:  crate(futures-macro-0.3) >= 0.3.32
BuildRequires:  crate(futures-task-0.3) >= 0.3.32
BuildRequires:  crate(futures-util-0.3) >= 0.3.32
BuildRequires:  crate(fxhash-0.2) >= 0.2.1
BuildRequires:  crate(gdk-pixbuf-0.22) >= 0.22.0
BuildRequires:  crate(gdk-pixbuf-sys-0.22) >= 0.22.0
BuildRequires:  crate(gif-0.14) >= 0.14.2
BuildRequires:  crate(gio-0.22) >= 0.22.6
BuildRequires:  crate(gio-sys-0.22) >= 0.22.0
BuildRequires:  crate(gio-unix-0.22) >= 0.22.6
BuildRequires:  crate(gio-unix-sys-0.22) >= 0.22.0
BuildRequires:  crate(gio-win32-0.22) >= 0.22.6
BuildRequires:  crate(gio-win32-sys-0.22) >= 0.22.0
BuildRequires:  crate(glam-0.14) >= 0.14.0
BuildRequires:  crate(glam-0.15) >= 0.15.2
BuildRequires:  crate(glam-0.16) >= 0.16.0
BuildRequires:  crate(glam-0.17) >= 0.17.3
BuildRequires:  crate(glam-0.18) >= 0.18.0
BuildRequires:  crate(glam-0.19) >= 0.19.0
BuildRequires:  crate(glam-0.20) >= 0.20.5
BuildRequires:  crate(glam-0.21) >= 0.21.3
BuildRequires:  crate(glam-0.22) >= 0.22.0
BuildRequires:  crate(glam-0.23) >= 0.23.0
BuildRequires:  crate(glam-0.24) >= 0.24.2
BuildRequires:  crate(glam-0.25) >= 0.25.0
BuildRequires:  crate(glam-0.27) >= 0.27.0
BuildRequires:  crate(glam-0.28) >= 0.28.0
BuildRequires:  crate(glam-0.29) >= 0.29.3
BuildRequires:  crate(glam-0.30) >= 0.30.10
BuildRequires:  crate(glam-0.31) >= 0.31.1
BuildRequires:  crate(glam-0.32) >= 0.32.1
BuildRequires:  crate(glib-0.22) >= 0.22.7
BuildRequires:  crate(glib-macros-0.22) >= 0.22.6
BuildRequires:  crate(glib-sys-0.22) >= 0.22.6
BuildRequires:  crate(gobject-sys-0.22) >= 0.22.6
BuildRequires:  crate(hashbrown-0.13) >= 0.13.2
BuildRequires:  crate(hashbrown-0.17) >= 0.17.0
BuildRequires:  crate(heck-0.5) >= 0.5.0
BuildRequires:  crate(iana-time-zone-0.1) >= 0.1.65
BuildRequires:  crate(iana-time-zone-haiku-0.1) >= 0.1.2
BuildRequires:  crate(icu-collections-2) >= 2.2.0
BuildRequires:  crate(icu-locale-core-2) >= 2.2.0
BuildRequires:  crate(icu-normalizer-2) >= 2.2.0
BuildRequires:  crate(icu-normalizer-data-2) >= 2.2.0
BuildRequires:  crate(icu-properties-2) >= 2.2.0
BuildRequires:  crate(icu-properties-data-2) >= 2.2.0
BuildRequires:  crate(icu-provider-2) >= 2.2.0
BuildRequires:  crate(idna-1) >= 1.1.0
BuildRequires:  crate(idna-adapter-1) >= 1.2.1
BuildRequires:  crate(image-0.25) >= 0.25.10
BuildRequires:  crate(image-webp-0.2) >= 0.2.4
BuildRequires:  crate(indexmap-2) >= 2.14.0
BuildRequires:  crate(is-terminal-polyfill-1) >= 1.70.2
BuildRequires:  crate(itertools-0.14) >= 0.14.0
BuildRequires:  crate(itoa-1) >= 1.0.18
BuildRequires:  crate(js-sys-0.3) >= 0.3.98
BuildRequires:  crate(language-tags-0.3) >= 0.3.2
BuildRequires:  crate(lazy-static-1) >= 1.5.0
BuildRequires:  crate(libc-0.2) >= 0.2.186
BuildRequires:  crate(libloading-0.8) >= 0.8.9
BuildRequires:  crate(litemap-0.8) >= 0.8.2
BuildRequires:  crate(locale-config-0.3) >= 0.3.0
BuildRequires:  crate(lock-api-0.4) >= 0.4.14
BuildRequires:  crate(log-0.4) >= 0.4.30
BuildRequires:  crate(mac-0.1) >= 0.1.1
BuildRequires:  crate(malloc-buf-0.0.6) >= 0.0.6
BuildRequires:  crate(markup5ever-0.35) >= 0.35.0
BuildRequires:  crate(matrixmultiply-0.3) >= 0.3.10
BuildRequires:  crate(memchr-2) >= 2.8.1
BuildRequires:  crate(miniz-oxide-0.8) >= 0.8.9
BuildRequires:  crate(moxcms-0.8) >= 0.8.1
BuildRequires:  crate(mp4parse-0.17) >= 0.17.0
BuildRequires:  crate(mutants-0.0.3) >= 0.0.3
BuildRequires:  crate(nalgebra-0.34) >= 0.34.2
BuildRequires:  crate(nalgebra-macros-0.3) >= 0.3.0
BuildRequires:  crate(new-debug-unreachable-1) >= 1.0.6
BuildRequires:  crate(num-bigint-0.4) >= 0.4.6
BuildRequires:  crate(num-complex-0.4) >= 0.4.6
BuildRequires:  crate(num-derive-0.4) >= 0.4.2
BuildRequires:  crate(num-integer-0.1) >= 0.1.46
BuildRequires:  crate(num-rational-0.4) >= 0.4.2
BuildRequires:  crate(num-traits-0.2) >= 0.2.19
BuildRequires:  crate(objc-0.2) >= 0.2.7
BuildRequires:  crate(objc-foundation-0.1) >= 0.1.1
BuildRequires:  crate(objc-id-0.1) >= 0.1.1
BuildRequires:  crate(once-cell-1) >= 1.21.4
BuildRequires:  crate(once-cell-polyfill-1) >= 1.70.2
BuildRequires:  crate(pango-0.22) >= 0.22.6
BuildRequires:  crate(pangocairo-0.22) >= 0.22.0
BuildRequires:  crate(pangocairo-sys-0.22) >= 0.22.0
BuildRequires:  crate(pango-sys-0.22) >= 0.22.0
BuildRequires:  crate(parking-lot-0.12) >= 0.12.5
BuildRequires:  crate(parking-lot-core-0.9) >= 0.9.12
BuildRequires:  crate(paste-1) >= 1.0.15
BuildRequires:  crate(percent-encoding-2) >= 2.3.2
BuildRequires:  crate(phf-0.11) >= 0.11.3
BuildRequires:  crate(phf-codegen-0.11) >= 0.11.3
BuildRequires:  crate(phf-generator-0.11) >= 0.11.3
BuildRequires:  crate(phf-macros-0.11) >= 0.11.3
BuildRequires:  crate(phf-shared-0.11) >= 0.11.3
BuildRequires:  crate(phf-shared-0.13) >= 0.13.1
BuildRequires:  crate(pin-project-lite-0.2) >= 0.2.17
BuildRequires:  crate(pkg-config-0.3) >= 0.3.33
BuildRequires:  crate(png-0.18) >= 0.18.1
BuildRequires:  crate(potential-utf-0.1) >= 0.1.5
BuildRequires:  crate(precomputed-hash-0.1) >= 0.1.1
BuildRequires:  crate(proc-macro2-1) >= 1.0.106
BuildRequires:  crate(pxfm-0.1) >= 0.1.29
BuildRequires:  crate(quick-error-2) >= 2.0.1
BuildRequires:  crate(quote-1) >= 1.0.45
BuildRequires:  crate(rand-0.8) >= 0.8.6
BuildRequires:  crate(rand-core-0.6) >= 0.6.4
BuildRequires:  crate(rawpointer-0.2) >= 0.2.1
BuildRequires:  crate(rayon-1) >= 1.12.0
BuildRequires:  crate(rayon-core-1) >= 1.13.0
BuildRequires:  crate(rctree-0.6) >= 0.6.0
BuildRequires:  crate(redox-syscall-0.5) >= 0.5.18
BuildRequires:  crate(regex-1) >= 1.12.3
BuildRequires:  crate(regex-automata-0.4) >= 0.4.14
BuildRequires:  crate(regex-syntax-0.8) >= 0.8.10
BuildRequires:  crate(rgb-0.8) >= 0.8.53
BuildRequires:  crate(rustc-version-0.4) >= 0.4.1
BuildRequires:  crate(rustversion-1) >= 1.0.22
BuildRequires:  crate(safe-arch-0.7) >= 0.7.4
BuildRequires:  crate(scopeguard-1) >= 1.2.0
BuildRequires:  crate(selectors-0.31) >= 0.31.0
BuildRequires:  crate(semver-1) >= 1.0.28
BuildRequires:  crate(serde-1) >= 1.0.228
BuildRequires:  crate(serde-core-1) >= 1.0.228
BuildRequires:  crate(serde-derive-1) >= 1.0.228
BuildRequires:  crate(serde-spanned-1) >= 1.1.1
BuildRequires:  crate(servo-arc-0.4) >= 0.4.3
BuildRequires:  crate(shlex-2) >= 2.0.1
BuildRequires:  crate(simba-0.9) >= 0.9.1
BuildRequires:  crate(simd-adler32-0.3) >= 0.3.9
BuildRequires:  crate(siphasher-1) >= 1.0.3
BuildRequires:  crate(slab-0.4) >= 0.4.12
BuildRequires:  crate(smallvec-1) >= 1.15.1
BuildRequires:  crate(stable-deref-trait-1) >= 1.2.1
BuildRequires:  crate(static-assertions-1) >= 1.1.0
BuildRequires:  crate(string-cache-0.8) >= 0.8.9
BuildRequires:  crate(string-cache-0.9) >= 0.9.0
BuildRequires:  crate(string-cache-codegen-0.5) >= 0.5.4
BuildRequires:  crate(strsim-0.11) >= 0.11.1
BuildRequires:  crate(syn-2) >= 2.0.117
BuildRequires:  crate(synstructure-0.13) >= 0.13.2
BuildRequires:  crate(system-deps-7) >= 7.0.8
BuildRequires:  crate(target-lexicon-0.13) >= 0.13.5
BuildRequires:  crate(tendril-0.4) >= 0.4.3
BuildRequires:  crate(tinystr-0.8) >= 0.8.3
BuildRequires:  crate(tinyvec-1) >= 1.11.0
BuildRequires:  crate(tinyvec-macros-0.1) >= 0.1.1
BuildRequires:  crate(toml-1) >= 1.1.2
BuildRequires:  crate(toml-datetime-1) >= 1.1.1
BuildRequires:  crate(toml-parser-1) >= 1.1.2
BuildRequires:  crate(toml-writer-1) >= 1.1.1
BuildRequires:  crate(typenum-1) >= 1.20.1
BuildRequires:  crate(unicode-ident-1) >= 1.0.24
BuildRequires:  crate(url-2) >= 2.5.8
BuildRequires:  crate(utf-8-0.7) >= 0.7.6
BuildRequires:  crate(utf8-iter-1) >= 1.0.4
BuildRequires:  crate(utf8parse-0.2) >= 0.2.2
BuildRequires:  crate(version-check-0.9) >= 0.9.5
BuildRequires:  crate(version-compare-0.2) >= 0.2.1
BuildRequires:  crate(wasm-bindgen-0.2) >= 0.2.121
BuildRequires:  crate(wasm-bindgen-macro-0.2) >= 0.2.121
BuildRequires:  crate(wasm-bindgen-macro-support-0.2) >= 0.2.121
BuildRequires:  crate(wasm-bindgen-shared-0.2) >= 0.2.121
BuildRequires:  crate(web-atoms-0.1) >= 0.1.3
BuildRequires:  crate(weezl-0.1) >= 0.1.12
BuildRequires:  crate(wide-0.7) >= 0.7.33
BuildRequires:  crate(winapi-0.3) >= 0.3.9
BuildRequires:  crate(winapi-i686-pc-windows-gnu-0.4) >= 0.4.0
BuildRequires:  crate(winapi-x86-64-pc-windows-gnu-0.4) >= 0.4.0
BuildRequires:  crate(windows-core-0.62) >= 0.62.2
BuildRequires:  crate(windows-implement-0.60) >= 0.60.2
BuildRequires:  crate(windows-interface-0.59) >= 0.59.3
BuildRequires:  crate(windows-link-0.2) >= 0.2.1
BuildRequires:  crate(windows-result-0.4) >= 0.4.1
BuildRequires:  crate(windows-strings-0.5) >= 0.5.1
BuildRequires:  crate(windows-sys-0.61) >= 0.61.2
BuildRequires:  crate(winnow-1) >= 1.0.3
BuildRequires:  crate(writeable-0.6) >= 0.6.2
BuildRequires:  crate(xml5ever-0.35) >= 0.35.0
BuildRequires:  crate(yeslogic-fontconfig-sys-6) >= 6.0.1
BuildRequires:  crate(yoke-0.8) >= 0.8.2
BuildRequires:  crate(yoke-derive-0.8) >= 0.8.2
BuildRequires:  crate(zerocopy-0.8) >= 0.8.50
BuildRequires:  crate(zerocopy-derive-0.8) >= 0.8.50
BuildRequires:  crate(zerofrom-0.1) >= 0.1.7
BuildRequires:  crate(zerofrom-derive-0.1) >= 0.1.7
BuildRequires:  crate(zerotrie-0.2) >= 0.2.4
BuildRequires:  crate(zerovec-0.11) >= 0.11.6
BuildRequires:  crate(zerovec-derive-0.11) >= 0.11.3
BuildRequires:  crate(zune-core-0.5) >= 0.5.1
BuildRequires:  crate(zune-jpeg-0.5) >= 0.5.15
BuildRequires:  crate(aes-0.8) >= 0.8.4
BuildRequires:  crate(anes-0.1) >= 0.1.6
BuildRequires:  crate(anyhow-1) >= 1.0.102
BuildRequires:  crate(assert-cmd-2) >= 2.2.2
BuildRequires:  crate(bitflags-1) >= 1.3.2
BuildRequires:  crate(bit-set-0.5) >= 0.5.3
BuildRequires:  crate(bit-vec-0.6) >= 0.6.3
BuildRequires:  crate(block-buffer-0.10) >= 0.10.4
BuildRequires:  crate(block-padding-0.3) >= 0.3.3
BuildRequires:  crate(bstr-1) >= 1.12.1
BuildRequires:  crate(bytecount-0.6) >= 0.6.9
BuildRequires:  crate(cbc-0.1) >= 0.1.2
BuildRequires:  crate(ciborium-0.2) >= 0.2.2
BuildRequires:  crate(ciborium-io-0.2) >= 0.2.2
BuildRequires:  crate(ciborium-ll-0.2) >= 0.2.2
BuildRequires:  crate(cipher-0.4) >= 0.4.4
BuildRequires:  crate(cpufeatures-0.2) >= 0.2.17
BuildRequires:  crate(criterion-0.7) >= 0.7.0
BuildRequires:  crate(criterion-plot-0.6) >= 0.6.0
BuildRequires:  crate(crunchy-0.2) >= 0.2.4
BuildRequires:  crate(crypto-common-0.1) >= 0.1.6
BuildRequires:  crate(deranged-0.5) >= 0.5.8
BuildRequires:  crate(diff-0.1) >= 0.1.13
BuildRequires:  crate(difflib-0.4) >= 0.4.0
BuildRequires:  crate(digest-0.10) >= 0.10.7
BuildRequires:  crate(ecb-0.1) >= 0.1.2
BuildRequires:  crate(errno-0.3) >= 0.3.14
BuildRequires:  crate(fastrand-2) >= 2.4.1
BuildRequires:  crate(fnv-1) >= 1.0.7
BuildRequires:  crate(foldhash-0.1) >= 0.1.5
BuildRequires:  crate(generic-array-0.14) >= 0.14.9
BuildRequires:  crate(getrandom-0.2) >= 0.2.17
BuildRequires:  crate(getrandom-0.3) >= 0.3.4
BuildRequires:  crate(getrandom-0.4) >= 0.4.2
BuildRequires:  crate(half-2) >= 2.7.1
BuildRequires:  crate(hashbrown-0.15) >= 0.15.5
BuildRequires:  crate(id-arena-2) >= 2.3.0
BuildRequires:  crate(inout-0.1) >= 0.1.4
BuildRequires:  crate(itertools-0.13) >= 0.13.0
BuildRequires:  crate(jiff-0.2) >= 0.2.24
BuildRequires:  crate(jiff-static-0.2) >= 0.2.24
BuildRequires:  crate(jiff-tzdb-0.1) >= 0.1.6
BuildRequires:  crate(jiff-tzdb-platform-0.1) >= 0.1.3
BuildRequires:  crate(leb128fmt-0.1) >= 0.1.0
BuildRequires:  crate(linux-raw-sys-0.12) >= 0.12.1
BuildRequires:  crate(lopdf-0.38) >= 0.38.0
BuildRequires:  crate(matches-0.1) >= 0.1.10
BuildRequires:  crate(md-5-0.10) >= 0.10.6
BuildRequires:  crate(nom-8) >= 8.0.0
BuildRequires:  crate(nom-locate-5) >= 5.0.0
BuildRequires:  crate(normalize-line-endings-0.3) >= 0.3.0
BuildRequires:  crate(num-conv-0.2) >= 0.2.1
BuildRequires:  crate(oorandom-11) >= 11.1.5
BuildRequires:  crate(plotters-0.3) >= 0.3.7
BuildRequires:  crate(plotters-backend-0.3) >= 0.3.7
BuildRequires:  crate(plotters-svg-0.3) >= 0.3.7
BuildRequires:  crate(portable-atomic-1) >= 1.13.1
BuildRequires:  crate(portable-atomic-util-0.2) >= 0.2.7
BuildRequires:  crate(powerfmt-0.2) >= 0.2.0
BuildRequires:  crate(ppv-lite86-0.2) >= 0.2.21
BuildRequires:  crate(predicates-3) >= 3.1.4
BuildRequires:  crate(predicates-core-1) >= 1.0.10
BuildRequires:  crate(predicates-tree-1) >= 1.0.13
BuildRequires:  crate(pretty-assertions-1) >= 1.4.1
BuildRequires:  crate(prettyplease-0.2) >= 0.2.37
BuildRequires:  crate(proptest-1) >= 1.0.0
BuildRequires:  crate(quick-error-1) >= 1.2.0
BuildRequires:  crate(rand-0.9) >= 0.9.4
BuildRequires:  crate(rand-chacha-0.3) >= 0.3.1
BuildRequires:  crate(rand-chacha-0.9) >= 0.9.0
BuildRequires:  crate(rand-core-0.9) >= 0.9.5
BuildRequires:  crate(rand-xorshift-0.3) >= 0.3.0
BuildRequires:  crate(rangemap-1) >= 1.7.1
BuildRequires:  crate(r-efi-5) >= 5.3.0
BuildRequires:  crate(r-efi-6) >= 6.0.0
BuildRequires:  crate(regex-syntax-0.6) >= 0.6.0
BuildRequires:  crate(rustix-1) >= 1.1.4
BuildRequires:  crate(rusty-fork-0.3) >= 0.3.0
BuildRequires:  crate(same-file-1) >= 1.0.6
BuildRequires:  crate(serde-json-1) >= 1.0.150
BuildRequires:  crate(sha2-0.10) >= 0.10.9
BuildRequires:  crate(shell-words-1) >= 1.1.1
BuildRequires:  crate(stringprep-0.1) >= 0.1.5
BuildRequires:  crate(tempfile-3) >= 3.27.0
BuildRequires:  crate(termtree-0.5) >= 0.5.1
BuildRequires:  crate(thiserror-2) >= 2.0.18
BuildRequires:  crate(thiserror-impl-2) >= 2.0.18
BuildRequires:  crate(time-0.3) >= 0.3.47
BuildRequires:  crate(time-core-0.1) >= 0.1.8
BuildRequires:  crate(time-macros-0.2) >= 0.2.27
BuildRequires:  crate(tinytemplate-1) >= 1.2.1
BuildRequires:  crate(ttf-parser-0.25) >= 0.25.1
BuildRequires:  crate(ucd-util-0.1) >= 0.1.0
BuildRequires:  crate(unicode-bidi-0.3) >= 0.3.18
BuildRequires:  crate(unicode-normalization-0.1) >= 0.1.25
BuildRequires:  crate(unicode-properties-0.1) >= 0.1.4
BuildRequires:  crate(unicode-xid-0.2) >= 0.2.6
BuildRequires:  crate(wait-timeout-0.2) >= 0.2.1
BuildRequires:  crate(walkdir-2) >= 2.5.0
BuildRequires:  crate(wasi-0.11) >= 0.11.1
BuildRequires:  crate(wasip2-1) >= 1.0.3
BuildRequires:  crate(wasip3-0.4) >= 0.4.0
BuildRequires:  crate(wasm-encoder-0.244) >= 0.244.0
BuildRequires:  crate(wasm-metadata-0.244) >= 0.244.0
BuildRequires:  crate(wasmparser-0.244) >= 0.244.0
BuildRequires:  crate(web-sys-0.3) >= 0.3.98
BuildRequires:  crate(winapi-util-0.1) >= 0.1.11
BuildRequires:  crate(wit-bindgen-0.51) >= 0.51.0
BuildRequires:  crate(wit-bindgen-0.57) >= 0.57.1
BuildRequires:  crate(wit-bindgen-core-0.51) >= 0.51.0
BuildRequires:  crate(wit-bindgen-rust-0.51) >= 0.51.0
BuildRequires:  crate(wit-bindgen-rust-macro-0.51) >= 0.51.0
BuildRequires:  crate(wit-component-0.244) >= 0.244.0
BuildRequires:  crate(wit-parser-0.244) >= 0.244.0
BuildRequires:  crate(yansi-1) >= 1.0.1
BuildRequires:  crate(zmij-1) >= 1.0.21
BuildRequires:  meson >= 1.2.0
BuildRequires:  gcc
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  cargo-c
BuildRequires:  python3-docutils
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(cairo) >= %{cairo_version}
BuildRequires:  pkgconfig(cairo-gobject) >= %{cairo_version}
BuildRequires:  pkgconfig(cairo-png) >= %{cairo_version}
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  vala
BuildRequires:  pkgconfig(gi-docgen)

Requires:       cairo%{?_isa} >= %{cairo_version}
Requires:       cairo-gobject%{?_isa} >= %{cairo_version}

%description
An SVG library based on cairo.

%package        devel
Summary:        Libraries and include files for developing with librsvg
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for librsvg.

%prep -a
mkdir -p ~/.cargo
cat > ~/.cargo/config.toml <<EOF
[source.crates-io]
replace-with = "system-registry"

[source.system-registry]
directory = "/usr/share/cargo/registry"
EOF

sed -i 's/, "--locked"//g' meson/cargo_wrapper.py

%build -p
rm -rf Cargo.lock

%install -a
rm -f %{buildroot}%{_docdir}/librsvg*/COMPILING.md

%files
%license COPYING.LIB
%doc NEWS README.md
%{_libdir}/librsvg-2.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Rsvg-2.0.typelib
%{_bindir}/rsvg-convert
%{_mandir}/man1/rsvg-convert.1*

%files devel
%{_libdir}/librsvg-2.so
%{_includedir}/librsvg-2.0/
%{_libdir}/pkgconfig/librsvg-2.0.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Rsvg-2.0.gir
%{_datadir}/vala/vapi/librsvg-2.0.vapi
%{_datadir}/vala/vapi/librsvg-2.0.deps
%{_docdir}/Rsvg-2.0

%changelog
%autochangelog
