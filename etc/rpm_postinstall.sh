echo Installing 
pip3.9 install python-ldap
echo Fixing shebang
sed -i.bak 's|#!/usr/bin/python3|#!/usr/bin/python3.9|'  /usr/bin/slufld
