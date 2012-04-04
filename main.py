#! /usr/bin/env python

# Check for root user login
import os, sys
if not os.geteuid()==0:
    sys.exit("\nOnly root can run this script\n")

# Get your username (not root)
import pwd
uname=pwd.getpwuid(1000)[0]

# The remastering process uses chroot mode.
# Check to see if this script is operating in chroot mode.
# /home/mint directory only exists in chroot mode
is_chroot = os.path.exists('/home/mint')
dir_develop=''
if (is_chroot):
	dir_develop='/usr/local/bin/develop'
	dir_user = '/home/mint'
else:
	dir_develop='/home/' + uname + '/develop'
	dir_user = '/home/' + uname

# Everything up to this point is common to all Python scripts called by shared-*.sh
# =================================================================================

os.system ("echo ========================================")
os.system ("echo BEGIN SWITCHING TO LIGHTER JAVA PACKAGES")
print ("NOTE: The screen output has been suppressed due to excessive volume.")

def purge_packages (packages):
    os.system ('echo PURGING ' + packages)
    os.system ('apt-get purge -qq ' + packages)

def package_add (name):
    os.system ('echo ADDING ' + name)
    os.system ('apt-get install -qq ' + name)

# Add gcj-jre as a lighter replacement for sun-java6-jre and sun-java6-bin (41.4MB).
os.system ('echo Installing gcj-jre and dependent packages.')
os.system ('echo This requires 12.0 MB of downloads and 41.4 MB of additional disk space.')
package_add ('gcj-jre')

# Now that gcj-jre is installed, sun-java6-jre and sun-java6-bin are no longer needed.
os.system ('echo Purging sun-java6-jre and sun-java6-bin.')
os.system ('echo This saves 104 MB of disk space.')
purge_packages ('sun-java6-jre sun-java6-bin')

# Removing selected LibreOffice packages
os.system ('echo Purging libreoffice libreoffice-emailmerge libreoffice-gnome python-uno')
os.system ('echo This saves 2449 kB of disk space.')
purge_packages ('libreoffice libreoffice-emailmerge libreoffice-gnome python-uno')

# Remove LibreOffice Base
os.system ('echo Purging libreoffice-base libreoffice-report-builder-bin')
os.system ('echo This saves 12.0 MB of disk space.)
purge_packages ('libreoffice-base libreoffice-report-builder-bin')

# Remove LibreOffice Draw and Impress
os.system ('echo Purging LibreOffice Draw and Impress')
os.system ('echo This saves 11.4 MB of disk space.')
purge_packages ('libreoffice-draw libreoffice-impress')

# Remove libreoffice-filter-mobiledev and libreoffice-java-common
os.system ('echo Purging libreoffice-filter-mobiledev libreoffice-java-common')
os.system ('echo This saves 9126 kB of disk space.')
purge_packages ('libreoffice-filter-mobiledev libreoffice-java-common')

# Remove libreoffice-gtk
os.system ('echo Purging libreoffice-gtk')
os.system ('echo This saves 1012 kB of disk space.')
purge_packages ('libreoffice-gtk')

# Remove LibreOffice Math
os.system ('echo Purging LibreOffice Math')
os.system ('echo This saves 1540 kB of disk space.')
purge_packages ('libreoffice-math')      

os.system ("echo FINISHED SWITCHING TO LIGHTER JAVA PACKAGES")
os.system ("echo ===========================================")
