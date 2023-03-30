%define name slufl3
%define version 3.0.0
%define unmangled_version 3.0.0
%define release 1

Summary: Run Ansible playbooks when LDAP entries change.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Damien François <damien.francois@uclouvain.be>
Provides: slufl3
Requires: ansible python39-devel openldap-devel
Url: https://github.com/damienfrancois/slufl3

%description
slufl is a damon that monitors an LDAP server and
                  triggers Ansible playbook upon changes.

%prep
%setup -n %{name}-%{unmangled_version}

%build
python3 setup.py build

%install
python3 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo Installing 
pip3.9 install python-ldap
echo Fixing shebang
sed -i.bak 's|#!/usr/bin/python3|#!/usr/bin/python3.9|'  /usr/bin/slufld


%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README.md
