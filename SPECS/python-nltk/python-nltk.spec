%global srcname nltk

Name:           python-%{srcname}
Version:        3.9.4
Release:        %autorelease
Summary:        Natural Language Toolkit
License:        Apache-2.0
URL:            https://github.com/nltk/nltk
#!RemoteAsset:  sha256:ed03bc098a40481310320808b2db712d95d13ca65b27372f8a403949c8b523d0
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
BuildOption(check):  -e "nltk.app.chartparser_app"
BuildOption(check):  -e "nltk.app.chunkparser_app"
BuildOption(check):  -e "nltk.app.collocations_app"
BuildOption(check):  -e "nltk.app.concordance_app"
BuildOption(check):  -e "nltk.app.nemo_app"
BuildOption(check):  -e "nltk.app.rdparser_app"
BuildOption(check):  -e "nltk.app.srparser_app"
BuildOption(check):  -e "nltk.app.wordfreq_app"
BuildOption(check):  -e "nltk.book"
BuildOption(check):  -e "nltk.draw.cfg"
BuildOption(check):  -e "nltk.draw.table"
BuildOption(check):  -e "nltk.draw.tree"
BuildOption(check):  -e "nltk.draw.util"
BuildOption(check):  -e "nltk.langnames"
BuildOption(check):  -e "nltk.test.conftest"
BuildOption(check):  -e "nltk.test.test_filestring_sandbox"
BuildOption(check):  -e "nltk.test.unit.lm.test_counter"
BuildOption(check):  -e "nltk.test.unit.lm.test_models"
BuildOption(check):  -e "nltk.test.unit.test_bllip"
BuildOption(check):  -e "nltk.test.unit.test_cfd_mutation"
BuildOption(check):  -e "nltk.test.unit.test_classify"
BuildOption(check):  -e "nltk.test.unit.test_corenlp"
BuildOption(check):  -e "nltk.test.unit.test_corpora"
BuildOption(check):  -e "nltk.test.unit.test_corpus_reader"
BuildOption(check):  -e "nltk.test.unit.test_corpus_util"
BuildOption(check):  -e "nltk.test.unit.test_data"
BuildOption(check):  -e "nltk.test.unit.test_data_security"
BuildOption(check):  -e "nltk.test.unit.test_distance"
BuildOption(check):  -e "nltk.test.unit.test_downloader_unzip"
BuildOption(check):  -e "nltk.test.unit.test_hmm"
BuildOption(check):  -e "nltk.test.unit.test_json2csv_corpus"
BuildOption(check):  -e "nltk.test.unit.test_nombank"
BuildOption(check):  -e "nltk.test.unit.test_pathsec"
BuildOption(check):  -e "nltk.test.unit.test_pickle_load_warnings"
BuildOption(check):  -e "nltk.test.unit.test_rte_classify"
BuildOption(check):  -e "nltk.test.unit.test_seekable_unicode_stream_reader"
BuildOption(check):  -e "nltk.test.unit.test_segmentation"
BuildOption(check):  -e "nltk.test.unit.test_tgrep"
BuildOption(check):  -e "nltk.test.unit.test_tokenize"
BuildOption(check):  -e "nltk.test.unit.test_twitter_auth"
BuildOption(check):  -e "nltk.test.unit.test_util"
BuildOption(check):  -e "nltk.test.unit.test_verbnet"
BuildOption(check):  -e "nltk.test.unit.test_wordnet"
BuildOption(check):  -e "nltk.test.unit.translate.test_bleu"
BuildOption(check):  -e "nltk.tokenize.nist"
BuildOption(check):  -e "nltk.twitter.twitter_demo"
BuildOption(check):  -e "nltk.twitter.twitterclient"
BuildOption(check):  -e "nltk.twitter.util"
BuildOption(check):  -e "nltk.*"

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(joblib)
BuildRequires:  python3dist(regex)
BuildRequires:  python3dist(tqdm)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The Natural Language Toolkit (NLTK) is a Python package for
natural language processing. NLTK requires Python 3.10, 3.11, 3.12, 3.13, or 3.14.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%{_bindir}/nltk

%changelog
%autochangelog
