# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-foundation
%global full_version 0.3.2
%global pkgname objc2-foundation-0.3

%define _source_payload w9.xzdio
%define _binary_payload w9.xzdio
%global _local_file_attrs rustcrates_feature
%global __rustcrates_feature_path ^%{_datadir}/cargo/registry/%{crate_name}-%{version}/\.rpm/features/[^/]+\.rpmdeps$
%global __rustcrates_feature_protocol singlefile
%global __rustcrates_feature_requires %rustcrates_depgen_helper --requires
%global __rustcrates_feature_provides %rustcrates_depgen_helper --provides

Name:           rust-objc2-foundation-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "objc2-foundation"
License:        MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:e3e0adef53c21f888deb4fa59fc59f7eb17404926ee8a6f59f5df0fd7f9f3272
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  takopack

Requires:       crate(objc2-0.6/std) >= 0.6.4
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/foundationerrors)
Provides:       crate(%{pkgname}/foundationlegacyswiftcompatibility)
Provides:       crate(%{pkgname}/nsaffinetransform)
Provides:       crate(%{pkgname}/nsappleeventmanager)
Provides:       crate(%{pkgname}/nsapplescript)
Provides:       crate(%{pkgname}/nsarchiver)
Provides:       crate(%{pkgname}/nsautoreleasepool)
Provides:       crate(%{pkgname}/nsbackgroundactivityscheduler)
Provides:       crate(%{pkgname}/nsbundle)
Provides:       crate(%{pkgname}/nsbyteorder)
Provides:       crate(%{pkgname}/nscache)
Provides:       crate(%{pkgname}/nscalendardate)
Provides:       crate(%{pkgname}/nscharacterset)
Provides:       crate(%{pkgname}/nsclassdescription)
Provides:       crate(%{pkgname}/nscoder)
Provides:       crate(%{pkgname}/nscompoundpredicate)
Provides:       crate(%{pkgname}/nsconnection)
Provides:       crate(%{pkgname}/nsdate)
Provides:       crate(%{pkgname}/nsdateformatter)
Provides:       crate(%{pkgname}/nsdateinterval)
Provides:       crate(%{pkgname}/nsdateintervalformatter)
Provides:       crate(%{pkgname}/nsdebug)
Provides:       crate(%{pkgname}/nsdecimal)
Provides:       crate(%{pkgname}/nsdecimalnumber)
Provides:       crate(%{pkgname}/nsdictionary)
Provides:       crate(%{pkgname}/nsdistantobject)
Provides:       crate(%{pkgname}/nsdistributedlock)
Provides:       crate(%{pkgname}/nsenergyformatter)
Provides:       crate(%{pkgname}/nsenumerator)
Provides:       crate(%{pkgname}/nserror)
Provides:       crate(%{pkgname}/nsexception)
Provides:       crate(%{pkgname}/nsexpression)
Provides:       crate(%{pkgname}/nsextensioncontext)
Provides:       crate(%{pkgname}/nsextensionitem)
Provides:       crate(%{pkgname}/nsextensionrequesthandling)
Provides:       crate(%{pkgname}/nsfilehandle)
Provides:       crate(%{pkgname}/nsfilepresenter)
Provides:       crate(%{pkgname}/nsformatter)
Provides:       crate(%{pkgname}/nsgarbagecollector)
Provides:       crate(%{pkgname}/nshfsfiletypes)
Provides:       crate(%{pkgname}/nshttpcookie)
Provides:       crate(%{pkgname}/nshttpcookiestorage)
Provides:       crate(%{pkgname}/nshashtable)
Provides:       crate(%{pkgname}/nshost)
Provides:       crate(%{pkgname}/nsindexpath)
Provides:       crate(%{pkgname}/nsindexset)
Provides:       crate(%{pkgname}/nsinflectionrule)
Provides:       crate(%{pkgname}/nsinvocation)
Provides:       crate(%{pkgname}/nskeyvaluecoding)
Provides:       crate(%{pkgname}/nskeyvaluesharedobservers)
Provides:       crate(%{pkgname}/nskeyedarchiver)
Provides:       crate(%{pkgname}/nslengthformatter)
Provides:       crate(%{pkgname}/nslistformatter)
Provides:       crate(%{pkgname}/nslocale)
Provides:       crate(%{pkgname}/nslocalizednumberformatrule)
Provides:       crate(%{pkgname}/nslock)
Provides:       crate(%{pkgname}/nsmaptable)
Provides:       crate(%{pkgname}/nsmassformatter)
Provides:       crate(%{pkgname}/nsmeasurement)
Provides:       crate(%{pkgname}/nsmetadata)
Provides:       crate(%{pkgname}/nsmetadataattributes)
Provides:       crate(%{pkgname}/nsmethodsignature)
Provides:       crate(%{pkgname}/nsmorphology)
Provides:       crate(%{pkgname}/nsnotification)
Provides:       crate(%{pkgname}/nsnull)
Provides:       crate(%{pkgname}/nsnumberformatter)
Provides:       crate(%{pkgname}/nsobject)
Provides:       crate(%{pkgname}/nsobjectscripting)
Provides:       crate(%{pkgname}/nsoperation)
Provides:       crate(%{pkgname}/nsorderedcollectionchange)
Provides:       crate(%{pkgname}/nsorderedset)
Provides:       crate(%{pkgname}/nsorthography)
Provides:       crate(%{pkgname}/nspersonnamecomponents)
Provides:       crate(%{pkgname}/nspointerarray)
Provides:       crate(%{pkgname}/nsportcoder)
Provides:       crate(%{pkgname}/nsportmessage)
Provides:       crate(%{pkgname}/nsportnameserver)
Provides:       crate(%{pkgname}/nspredicate)
Provides:       crate(%{pkgname}/nsprogress)
Provides:       crate(%{pkgname}/nsprotocolchecker)
Provides:       crate(%{pkgname}/nsproxy)
Provides:       crate(%{pkgname}/nsrange)
Provides:       crate(%{pkgname}/nsrelativedatetimeformatter)
Provides:       crate(%{pkgname}/nsrunloop)
Provides:       crate(%{pkgname}/nsscanner)
Provides:       crate(%{pkgname}/nsscriptclassdescription)
Provides:       crate(%{pkgname}/nsscriptcoercionhandler)
Provides:       crate(%{pkgname}/nsscriptcommand)
Provides:       crate(%{pkgname}/nsscriptcommanddescription)
Provides:       crate(%{pkgname}/nsscriptexecutioncontext)
Provides:       crate(%{pkgname}/nsscriptkeyvaluecoding)
Provides:       crate(%{pkgname}/nsscriptobjectspecifiers)
Provides:       crate(%{pkgname}/nsscriptstandardsuitecommands)
Provides:       crate(%{pkgname}/nsscriptsuiteregistry)
Provides:       crate(%{pkgname}/nsscriptwhosetests)
Provides:       crate(%{pkgname}/nsset)
Provides:       crate(%{pkgname}/nssortdescriptor)
Provides:       crate(%{pkgname}/nsspellserver)
Provides:       crate(%{pkgname}/nstask)
Provides:       crate(%{pkgname}/nstermofaddress)
Provides:       crate(%{pkgname}/nsthread)
Provides:       crate(%{pkgname}/nstimezone)
Provides:       crate(%{pkgname}/nstimer)
Provides:       crate(%{pkgname}/nsurlauthenticationchallenge)
Provides:       crate(%{pkgname}/nsurlcache)
Provides:       crate(%{pkgname}/nsurlconnection)
Provides:       crate(%{pkgname}/nsurlcredential)
Provides:       crate(%{pkgname}/nsurlcredentialstorage)
Provides:       crate(%{pkgname}/nsurldownload)
Provides:       crate(%{pkgname}/nsurlerror)
Provides:       crate(%{pkgname}/nsurlhandle)
Provides:       crate(%{pkgname}/nsurlprotectionspace)
Provides:       crate(%{pkgname}/nsurlprotocol)
Provides:       crate(%{pkgname}/nsurlrequest)
Provides:       crate(%{pkgname}/nsurlresponse)
Provides:       crate(%{pkgname}/nsurlsession)
Provides:       crate(%{pkgname}/nsuuid)
Provides:       crate(%{pkgname}/nsubiquitouskeyvaluestore)
Provides:       crate(%{pkgname}/nsundomanager)
Provides:       crate(%{pkgname}/nsunit)
Provides:       crate(%{pkgname}/nsuseractivity)
Provides:       crate(%{pkgname}/nsuserdefaults)
Provides:       crate(%{pkgname}/nsusernotification)
Provides:       crate(%{pkgname}/nsuserscripttask)
Provides:       crate(%{pkgname}/nsvalue)
Provides:       crate(%{pkgname}/nsvaluetransformer)
Provides:       crate(%{pkgname}/nsxmldtd)
Provides:       crate(%{pkgname}/nsxmldtdnode)
Provides:       crate(%{pkgname}/nsxmldocument)
Provides:       crate(%{pkgname}/nsxmlelement)
Provides:       crate(%{pkgname}/nsxmlnode)
Provides:       crate(%{pkgname}/nsxmlparser)
Provides:       crate(%{pkgname}/nszone)
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/unstable-darwin-objc)
Provides:       crate(%{pkgname}/unstable-mutation-return-null)
Provides:       crate(%{pkgname}/unstable-static-nsstring)

%description
Source code for takopackized Rust crate "objc2-foundation"

%files
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/.rpm/features/*.rpmdeps
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
