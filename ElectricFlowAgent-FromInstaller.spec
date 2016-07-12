# We need this because otherwise installer file is stripped by rpmbuild 
%global __os_install_post %{nil}

Name: ElectricFlowAgent-FromInstaller
Version: 6.1.0.98785
Release: 0
Epoch: 0
License: Unknown
URL: http://downloads.electric-cloud.com/ElectricFlowAgent-x64-6.1.0.98785
Packager: Roman V. Liskovenko <rliskovenko@gmail.com>
Summary: An agent application for ElectricFlow installation
Prefix: /tmp

AutoReqProv: no

Source0: ElectricFlowAgent-x64-6.1.0.98785

%description
Better description for n agent application for ElectricFlow installation

%prep

%build

%install
mkdir ${RPM_BUILD_ROOT}/tmp
cp %{SOURCE0} ${RPM_BUILD_ROOT}/tmp/

%clean

%files
%defattr(-,root,root)
%doc

# Skip verification because of fake file
%verify(owner) /tmp/ElectricFlowAgent-x64-6.1.0.98785

%post
chmod u+x /tmp/ElectricFlowAgent-x64-6.1.0.98785
/tmp/ElectricFlowAgent-x64-6.1.0.98785 --mode silent \
	--installDirectory /opt/electriccloud/electriccommander \
	--unixAgentGroup nobody \
	--unixAgentUser nobody \
	--unixServerGroup nobody \
	--unixServerUser nobody

rm -f /tmp/ElectricFlowAgent-x64-6.1.0.98785

# Remove old link if it is exists ignoring errors
unlink /etc/init.d/ElectricFlowAgent >/dev/null 2> /dev/null || true
# Set a new link
ln -s /opt/electriccloud/electriccommander/startup/commanderAgent /etc/init.d/ElectricFlowAgent 
# Set up service to run on startup. On systemd distros chkconfig should still work in compatibility mode
chkconfig --add ElectricFlowAgent >/dev/null 2> /dev/null || true
chkconfig ElectricFlowAgent on >/dev/null 2> /dev/null || true

%preun
# Create a fake FS entry to be removed by uninstaller
touch /tmp/ElectricFlowAgent-x64-6.1.0.98785
# Run unistaller script provided with installation
/opt/electriccloud/electriccommander/uninstall --mode silent

%postun
# Remove a link if it is exists ignoring errors
unlink /etc/init.d/ElectricFlowAgent >/dev/null 2> /dev/null || true
# Remove a service from automatic startup
chkconfig ElectricFlowAgent off >/dev/null 2> /dev/null || true
# Fails on CentOS 7.x
chkconfig --del ElectricFlowAgent >/dev/null 2> /dev/null || true

