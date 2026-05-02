%global srcname authlib

Name:           python-%{srcname}
Version:        1.7.0
Release:        %autorelease
Summary:        The ultimate Python library in building OAuth and OpenID Connect servers and clients.
License:        BSD-3-Clause
URL:            https://github.com/authlib/authlib
#!RemoteAsset:  sha256:b3e326c9aa9cc3ea95fe7d89fd880722d3608da4d00e8a27e061e64b48d801d5
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
BuildOption(check):  -e "authlib.integrations.django_client"
BuildOption(check):  -e "authlib.integrations.django_client.apps"
BuildOption(check):  -e "authlib.integrations.django_client.integration"
BuildOption(check):  -e "authlib.integrations.django_oauth1"
BuildOption(check):  -e "authlib.integrations.django_oauth1.authorization_server"
BuildOption(check):  -e "authlib.integrations.django_oauth1.nonce"
BuildOption(check):  -e "authlib.integrations.django_oauth1.resource_protector"
BuildOption(check):  -e "authlib.integrations.django_oauth2"
BuildOption(check):  -e "authlib.integrations.django_oauth2.authorization_server"
BuildOption(check):  -e "authlib.integrations.django_oauth2.endpoints"
BuildOption(check):  -e "authlib.integrations.django_oauth2.requests"
BuildOption(check):  -e "authlib.integrations.django_oauth2.resource_protector"
BuildOption(check):  -e "authlib.integrations.django_oauth2.signals"
BuildOption(check):  -e "authlib.integrations.flask_client"
BuildOption(check):  -e "authlib.integrations.flask_client.apps"
BuildOption(check):  -e "authlib.integrations.flask_client.integration"
BuildOption(check):  -e "authlib.integrations.flask_oauth1"
BuildOption(check):  -e "authlib.integrations.flask_oauth1.authorization_server"
BuildOption(check):  -e "authlib.integrations.flask_oauth1.cache"
BuildOption(check):  -e "authlib.integrations.flask_oauth1.resource_protector"
BuildOption(check):  -e "authlib.integrations.flask_oauth2"
BuildOption(check):  -e "authlib.integrations.flask_oauth2.authorization_server"
BuildOption(check):  -e "authlib.integrations.flask_oauth2.errors"
BuildOption(check):  -e "authlib.integrations.flask_oauth2.requests"
BuildOption(check):  -e "authlib.integrations.flask_oauth2.resource_protector"
BuildOption(check):  -e "authlib.integrations.flask_oauth2.signals"
BuildOption(check):  -e "authlib.integrations.httpx_client"
BuildOption(check):  -e "authlib.integrations.httpx_client.assertion_client"
BuildOption(check):  -e "authlib.integrations.httpx_client.oauth1_client"
BuildOption(check):  -e "authlib.integrations.httpx_client.oauth2_client"
BuildOption(check):  -e "authlib.integrations.httpx_client.utils"
BuildOption(check):  -e "authlib.integrations.requests_client"
BuildOption(check):  -e "authlib.integrations.requests_client.assertion_session"
BuildOption(check):  -e "authlib.integrations.requests_client.oauth1_session"
BuildOption(check):  -e "authlib.integrations.requests_client.oauth2_session"
BuildOption(check):  -e "authlib.integrations.requests_client.utils"
BuildOption(check):  -e "authlib.integrations.sqla_oauth2"
BuildOption(check):  -e "authlib.integrations.sqla_oauth2.client_mixin"
BuildOption(check):  -e "authlib.integrations.sqla_oauth2.functions"
BuildOption(check):  -e "authlib.integrations.sqla_oauth2.tokens_mixins"
BuildOption(check):  -e "authlib.integrations.starlette_client"
BuildOption(check):  -e "authlib.integrations.starlette_client.apps"
BuildOption(check):  -e "authlib.integrations.starlette_client.integration"

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The ultimate Python library in building OAuth and OpenID Connect servers.
JWS, JWK, JWA, JWT are included.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog
