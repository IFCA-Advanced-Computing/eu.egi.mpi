#
# Copyright (c) 2013 Instituto de Física de Cantabria,
#                    CSIC - UC. All rights reserved.
#

Summary: A MPI Nagios monitoring probe.
Name: eu.egi.mpi
Version: 1.0.0
Vendor: EGI 
Release: 1%{?dist}
License: ASL 2.0
Group: System Environment/Daemons 
Source: %{name}.src.tar.gz
URL: https://wiki.egi.eu/wiki/VT_MPI_within_EGI:Nagios
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#Requires: python
#Requires: emi-cream-nagios
BuildArch: noarch

%description
This package contains the probes for testing MPI support in the EGI.eu infrastructure.
Full description of probes is available at https://wiki.egi.eu/wiki/VT_MPI_within_EGI:Nagios.

%prep
%setup -q -n %{name}

%build
cd $RPM_BUILD_DIR/eu.egi.mpi
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
cd $RPM_BUILD_DIR/eu.egi.mpi
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root)
/usr/libexec/grid-monitoring/probes/eu.egi.mpi
%{_sysconfdir}/ncg-metric-config.d/eu.egi.mpi.conf
%doc README

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Mar 04 2013 <enolfc _AT_ ifca.unican.es> - 1.0.0-1%{?dist}
- Initial packaging of the probes. 
