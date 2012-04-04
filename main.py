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

# Add gcj-jre (41.4 MB) as a lighter replacement for sun-java6-jre and sun-java6-bin (41.4MB).
#os.system('apt-get install -y gcj-jre')
#purge_packages ('gcj-jre')

# Now that gcj-jre is installed, sun-java6-jre and sun-java6-jre are no longer needed.
# Remove sun-java6-jre and sun-java6-bin.
#os.system('apt-get purge -y sun-java6-jre sun-java6-bin')
#purge_packages ('sun-java6-jre sun-java6-bin')

# Removing selected LibreOffice packages
#os.system('apt-get purge -y libreoffice libreoffice-emailmerge libreoffice-gnome python-uno')
#purge_packages ('libreoffice libreoffice-emailmerge libreoffice-gnome python-uno')

# Remove LibreOffice Base
#os.system('apt-get purge -y libreoffice-base libreoffice-report-builder-bin')
#purge_packages ('libreoffice-base libreoffice-report-builder-bin')

# Remove LibreOffice Draw and Impress
#os.system('apt-get purge -y libreoffice-draw libreoffice-impress')
#purge_packages ('libreoffice-draw libreoffice-impress')

# Remove libreoffice-filter-mobiledev and libreoffice-java-common
#os.system('apt-get purge -y libreoffice-filter-mobiledev libreoffice-java-common')
#purge_packages ('libreoffice-filter-mobiledev libreoffice-java-common')

# Remove libreoffice-gtk
#os.system('apt-get purge -y libreoffice-gtk')
#purge_packages ('libreoffice-gtk')

# Remove LibreOffice Math
#os.system('apt-get purge -y libreoffice-math')
#purge_packages ('libreoffice-math')





      
      


os.system ("echo FINISHED SWITCHING TO LIGHTER JAVA PACKAGES")
os.system ("echo ===========================================")
