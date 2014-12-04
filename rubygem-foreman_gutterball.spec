%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from foreman_gutterball-0.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gemname foreman_gutterball

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: Gutterball plugin for Foreman and Katello
Name: %{?scl_prefix}rubygem-%{gemname}
Version: 0.0.1
Release: 1%{?dist}
Group: Development/Languages
License: GPLv3
URL: http://katello.org
Source0: %{gemname}-%{version}.gem

Requires: gutterball
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}ruby(release)
BuildRequires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}ruby(release)
BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Gutterball plugin for Foreman and Katello.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{?scl_prefix}%{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gemdir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gemdir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -pa .%{gemdir}/* \
        %{buildroot}%{gemdir}/


%files
%dir %{geminstdir}
%{geminstdir}/lib
%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}


%changelog
* Wed Dec 03 2014  <komidore64@gmail.com> - 0.0.1-1
- Initial package
