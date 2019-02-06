#!/bin/bash

sudo ptf <<EOF
#intelligence gathering

use modules/intelligence-gathering/gobuster
run
use modules/intelligence-gathering/dnsrecon
run
use modules/intelligence-gathering/fierce
run
use modules/intelligence-gathering/dnsrecon
run
use modules/intelligence-gathering/recon-ng
run
use modules/intelligence-gathering/theHarvester
run
use modules/intelligence-gathering/subfinder
run
use modules/intelligence-gathering/sublist3r
run
use modules/intelligence-gathering/subjack
run
use modules/intelligence-gathering/subfinder
run
use modules/intelligence-gathering/wafw00f
run	
use modules/intelligence-gathering/smbmap
run
use modules/intelligence-gathering/spiderfoot
run

# vuln analyse

use modules/vulnerability-analysis/nmap
run
use modules/vulnerability-analysis/wfuzz
run
use modules/vulnerability-analysis/hydra
run
use modules/vulnerability-analysis/wpscan
run
use modules/vulnerability-analysis/arachni
run
use modules/vulnerability-analysis/testssl
run
use modules/vulnerability-analysis/nikto
run
use modules/vulnerability-analysis/lynis
run
use modules/vulnerability-analysis/openvas
run

# Exploitation

use modules/exploitation/msfdb
run
use modules/exploitation/burp
run
use modules/exploitation/sqlmap
run
use modules/exploitation/zaproxy
run
use modules/exploitation/nosqlmap
run
use modules/exploitation/metasploit
run
use modules/exploitation/msfdb
run
use modules/exploitation/exploit-db
run

# Post Exploitation


use modules/post-exploitation/linenum
run
use modules/post-exploitation/unicorn
run
use modules/webshells/install_update_all
run

# Pivoting

use modules/pivoting/iodine
run
use modules/pivoting/chisel
run

#else

use modules/password-recovery/seclist
run
use 

EOF
