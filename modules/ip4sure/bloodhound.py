#!/usr/bin/env python
#####################################
# Installation module for Bloodhound
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="David Kennedy (ReL1K), Stan"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Bloodhound - a post exploitation tool"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/adaptivethreat/BloodHound"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="bloodhound"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git gconf2 jq curl"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}, wget https://github.com/$(wget https://github.com/BloodHoundAD/BloodHound/releases/latest -O - | egrep -m4 '/.*/.*/.*zip' -o| tail -n1) -O BloodHound-linux-x64.zip, unzip -o BloodHound-linux-x64.zip"
