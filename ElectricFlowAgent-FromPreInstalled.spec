Name: ElectricFlowAgent-FromPreInstalled
Version: 6.1.0.98785
Release: 0
Epoch: 0
License: Unknown
URL: http://downloads.electric-cloud.com/ElectricFlowAgent-x64-6.1.0.98785
Packager: Roman V. Liskovenko <rliskovenko@gmail.com>
Summary: An agent application for ElectricFlow installation
Prefix: /opt/electriccloud

AutoReqProv: no

%define __jar_repack %{nil}

%description
Better description for an agent application for ElectricFlow installation

%prep

%build

%install
mkdir -p ${RPM_BUILD_ROOT}/opt/electriccloud
cp -R /opt/electriccloud/electriccommander ${RPM_BUILD_ROOT}/opt/electriccloud

%clean

%files
%defattr(-,root,root)
%doc
/opt/electriccloud/electriccommander

%post
# Remove old link if it is exists ignoring errors
unlink /etc/init.d/ElectricFlowAgent >/dev/null 2> /dev/null || true
# Set a new link
ln -s /opt/electriccloud/electriccommander/startup/commanderAgent /etc/init.d/ElectricFlowAgent 
# Set up service to run on startup. On systemd distros chkconfig should still work in compatibility mode
chkconfig --add ElectricFlowAgent >/dev/null 2> /dev/null || true
chkconfig ElectricFlowAgent on >/dev/null 2> /dev/null || true

%postun
# Remove a link if it is exists ignoring errors
unlink /etc/init.d/ElectricFlowAgent >/dev/null 2> /dev/null || true
# Remove a service from automatic startup
chkconfig ElectricFlowAgent off >/dev/null 2> /dev/null || true
# Fails on CentOS 7.x
chkconfig --del ElectricFlowAgent >/dev/null 2> /dev/null || true

