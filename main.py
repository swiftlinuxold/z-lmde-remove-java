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

def message (string):
    os.system ('echo ' + string)

def purge_packages (packages):
    os.system ('echo PURGING ' + packages)
    os.system ('apt-get purge -qq ' + packages)

def package_add (name):
    os.system ('echo ADDING ' + name)
    os.system ('apt-get install -qq ' + name)

def purge_packages_file (filename):
    list_with_newlines = open(filename, 'r').read()
    list_with_spaces = list_with_newlines.replace ('\n', ' ')
    os.system ('apt-get purge -qq ' + list_with_spaces)

message ("========================================")
message ("BEGIN REMOVING SELECTED JAVA PACKAGES")
print ("NOTE: The screen output has been suppressed due to excessive volume.")

# STEP 1: PURGING LibreOffice packages other than Calc, Writer, and dependencies
# STEP 2: PURGING heavy Java packages (including those needed only for the above LibreOffice packages to be removed)

message ('REMOVING selected LibreOffice packages, keeping Calc and Writer')
purge_packages ('libreoffice')
purge_packages ('libreoffice-base libreoffice-report-builder-bin')
purge_packages ('libreoffice-draw libreoffice-impress')
purge_packages ('libreoffice-emailmerge')
purge_packages ('libreoffice-filter-mobiledev')
purge_packages ('libreoffice-gnome')
purge_packages ('libreoffice-gtk')
purge_packages ('libreoffice-java-common')
purge_packages ('libreoffice-math')
message ('PURGING openjdk-6-jre-headless and dependants')
purge_packages_file (dir_develop + '/remove-java/openjdk-6-jre-headless.txt')

message ("FINISHED REMOVING SELECTED JAVA PACKAGES")
message ("========================================")
