#!/usr/bin/env python
#####################################
# Installation module for Gobuster
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Zawadi Done" 

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module wil install/update GoBuster" 

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/OJ/gobuster" 

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="gobuster"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="golang" 

<<<<<<< HEAD
=======
# COMMANDS TO RUN AFTER
>>>>>>> 6fd39ebe7c910ae7724850fda3b1549e5c4f79e3
AFTER_COMMANDS='go get github.com/OJ/gobuster,cp /home/root/go/bin/gobuster /usr/local/bin'

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER=""
