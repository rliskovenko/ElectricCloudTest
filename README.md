### NB. Installer fails with `Install Error: Failed to initialize Agent's keystore`. Needs more knowledge of installer internals to fix that(missing requirements?).

### Packages on Google Drive: https://drive.google.com/folderview?id=0B7Hpe8i8z8GycjdBQ1ZhaVZVVnc&usp=sharing

# Easy way 
  * Using pre-installed files in `/opt/electriccloud/electriccommander` assuming they are here
  * _Startup script from:_ `/opt/electriccloud/electriccommander/startup/commanderAgent`
  * _Relocatable_, but startup script would be broken(some `sed` can help though).
  * Should be built from `root` because of permission problems copying wrapper files
  * **RPM:** `ElectricFlowAgent-FromPreInstalled-6.1.0.98785-0.x86_64.rpm`

# A bit better way 
  * pack binary installer into RPM and run it
  * crudely assumes installation directory and user/group for the service
  * _Relocatable_, by default uses /tmp to unpack installer but this could be altered with `--prefix` option for `rpm`
  * Installation directory should be empty
  * _Startup script from:_ `/opt/electriccloud/electriccommander/startup/commanderAgent`
  * **RPM:** `ElectricFlowAgent-FromInstaller-6.1.0.98785-0.x86_64.rpm`

# Debian packages
  * Using debbuild to build from RPM .spec
  * **Was not tested.** Looks working for the `FromPreInstalled` version.
  * _Wouldn't add service to autostart in Debian-based distro_

