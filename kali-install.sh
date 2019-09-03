#!/bin/bash

./ptf <<EOF
#intelligence gathering

use modules/exploitation/mitm6
run

# Post Exploitation

use modules/post-exploitation/SILENTTRINTY
run
use modules/post-exploitation/linenum
run

use modules/webshells/install_update_all
run
use modules/powershell/install_update_all
run 

# Pivoting

use modules/pivoting/iodine
run
use modules/pivoting/chisel
run

#else

use modules/password-recovery/seclist
run
use modules/ip4sure/extra
install

EOF
