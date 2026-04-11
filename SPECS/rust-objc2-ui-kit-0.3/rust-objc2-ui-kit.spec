# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-ui-kit
%global full_version 0.3.2
%global pkgname objc2-ui-kit-0.3

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-objc2-ui-kit-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "objc2-ui-kit"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:d87d638e33c06f577498cbcc50491496a3ed4246998a7fbba7ccb98b1e7eab22
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(objc2-0.6/std) >= 0.6.4
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/documentmanager)
Provides:       crate(%{pkgname}/nsfileproviderextension)
Provides:       crate(%{pkgname}/nstext)
Provides:       crate(%{pkgname}/nstextviewportlayoutcontroller)
Provides:       crate(%{pkgname}/nstoolbar-uikitadditions)
Provides:       crate(%{pkgname}/nstouchbar-uikitadditions)
Provides:       crate(%{pkgname}/nsuseractivity-nsitemprovider)
Provides:       crate(%{pkgname}/printkitui)
Provides:       crate(%{pkgname}/sharesheet)
Provides:       crate(%{pkgname}/uiaccessibilitycontentsizecategoryimageadjusting)
Provides:       crate(%{pkgname}/uiaccessibilityzoom)
Provides:       crate(%{pkgname}/uialert)
Provides:       crate(%{pkgname}/uibandselectioninteraction)
Provides:       crate(%{pkgname}/uibarcommon)
Provides:       crate(%{pkgname}/uibehavioralstyle)
Provides:       crate(%{pkgname}/uicalendarselection)
Provides:       crate(%{pkgname}/uicalendarviewdecoration)
Provides:       crate(%{pkgname}/uicanvasfeedbackgenerator)
Provides:       crate(%{pkgname}/uiconfigurationcolortransformer)
Provides:       crate(%{pkgname}/uicontentsizecategoryadjusting)
Provides:       crate(%{pkgname}/uicontextmenusystem)
Provides:       crate(%{pkgname}/uifeedbackgenerator)
Provides:       crate(%{pkgname}/uifocusdebugger)
Provides:       crate(%{pkgname}/uifocusdefines)
Provides:       crate(%{pkgname}/uifocussystem)
Provides:       crate(%{pkgname}/uifocusupdatecontext-uikitadditions)
Provides:       crate(%{pkgname}/uifoundation)
Provides:       crate(%{pkgname}/uiguidedaccessrestrictions)
Provides:       crate(%{pkgname}/uiimpactfeedbackgenerator)
Provides:       crate(%{pkgname}/uiinputsuggestion)
Provides:       crate(%{pkgname}/uiinterface)
Provides:       crate(%{pkgname}/uikeyconstants)
Provides:       crate(%{pkgname}/uikitcore)
Provides:       crate(%{pkgname}/uikitdefines)
Provides:       crate(%{pkgname}/uiletterformawareadjusting)
Provides:       crate(%{pkgname}/uimenusystem)
Provides:       crate(%{pkgname}/uimessageconversationcontext)
Provides:       crate(%{pkgname}/uimessageconversationentry)
Provides:       crate(%{pkgname}/uinibdeclarations)
Provides:       crate(%{pkgname}/uinotificationfeedbackgenerator)
Provides:       crate(%{pkgname}/uipointerinteraction)
Provides:       crate(%{pkgname}/uipopoverpresentationcontrollersourceitem)
Provides:       crate(%{pkgname}/uipresentationcontroller)
Provides:       crate(%{pkgname}/uipreviewinteraction)
Provides:       crate(%{pkgname}/uiresponder-uiactivityitemsconfiguration)
Provides:       crate(%{pkgname}/uisceneenhancedstaterestoration)
Provides:       crate(%{pkgname}/uiscenesizerestrictions)
Provides:       crate(%{pkgname}/uiscenewindowingbehaviors)
Provides:       crate(%{pkgname}/uiscenewindowingcontrolstyle)
Provides:       crate(%{pkgname}/uiscene-avaudiosession)
Provides:       crate(%{pkgname}/uiscreenmode)
Provides:       crate(%{pkgname}/uiscribbleinteraction)
Provides:       crate(%{pkgname}/uiscrolledgeelementcontainerinteraction)
Provides:       crate(%{pkgname}/uiselectionfeedbackgenerator)
Provides:       crate(%{pkgname}/uisnapbehavior)
Provides:       crate(%{pkgname}/uisplitviewcontrollerlayoutenvironment)
Provides:       crate(%{pkgname}/uispringloadedinteraction)
Provides:       crate(%{pkgname}/uispringloadedinteractionsupporting)
Provides:       crate(%{pkgname}/uistatusbarmanager)
Provides:       crate(%{pkgname}/uisymboleffectcompletion)
Provides:       crate(%{pkgname}/uitabaccessory)
Provides:       crate(%{pkgname}/uitextcursordroppositionanimator)
Provides:       crate(%{pkgname}/uitextcursorview)
Provides:       crate(%{pkgname}/uitextinputcontext)
Provides:       crate(%{pkgname}/uitextiteminteraction)
Provides:       crate(%{pkgname}/uitextloupesession)
Provides:       crate(%{pkgname}/uitextpasteconfigurationsupporting)
Provides:       crate(%{pkgname}/uitextselectionhandleview)
Provides:       crate(%{pkgname}/uitraitlistenvironment)
Provides:       crate(%{pkgname}/uiupdateactionphase)
Provides:       crate(%{pkgname}/uiupdatelink)
Provides:       crate(%{pkgname}/uiviewcontrollertransition)
Provides:       crate(%{pkgname}/uiviewlayoutregion)
Provides:       crate(%{pkgname}/uiwindowsceneactivationrequestoptions)
Provides:       crate(%{pkgname}/uiwindowscenedraginteraction)
Provides:       crate(%{pkgname}/uiwindowscenegeometrypreferences)
Provides:       crate(%{pkgname}/uiwindowscenegeometrypreferencesios)
Provides:       crate(%{pkgname}/uiwindowscenegeometrypreferencesmac)
Provides:       crate(%{pkgname}/uiwindowscenegeometrypreferencesvision)
Provides:       crate(%{pkgname}/uiwritingtoolscoordinatoranimationparameters)
Provides:       crate(%{pkgname}/unnotificationresponse-uikitadditions)
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/unstable-darwin-objc)

%description
Source code for takopackized Rust crate "objc2-ui-kit"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
