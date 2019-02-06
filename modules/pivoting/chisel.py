AUTHOR="Stan vdv"

DESCRIPTION="This module wil install/update chisel" 

INSTALL_TYPE="GIT"

REPOSITORY_LOCATION="https://github.com/jpillora/chisel.git" 

INSTALL_LOCATION="chisel"

DEBIAN="golang" 

AFTER_COMMANDS="go get github.com/jpillora/chisel,cp /root/go/bin/chisel /usr/local/bin,cd {INSTALL_LOCATION},go build -o chisel"

LAUNCHER=""
