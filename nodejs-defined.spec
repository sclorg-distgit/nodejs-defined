# spec file for package nodejs-nodejs-defined
%{?scl:%scl_package nodejs-defined}
%{!?scl:%global pkg_name %{name}}

%global npm_name defined
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-defined
Version:	1.0.0
Release:	3%{?dist}
Summary:	Return the first argument that is `!== undefined`
Url:		https://github.com/substack/defined
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch
ExclusiveArch:	%{ix86} x86_64 %{arm} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel
#BuildRequires:	nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:	npm(tape)
%endif

%description
Return the first argument that is `!== undefined`

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
tape test/*.js
%endif

%files
%{nodejs_sitelib}/defined

%doc readme.markdown
%license LICENSE

%changelog
* Wed Aug 05 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-3
- Fix ExclusiveArch

* Thu Jul 30 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-2
- Fix typo

* Wed Jul 29 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-1
- Initial build
