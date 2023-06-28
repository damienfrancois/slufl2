echo "Installing python-ldap (pip)"
pip3.11 install python-ldap

echo Fixing shebang
sed -i.bak 's|#!/usr/libexec/platform-python|#!/usr/bin/python3.11|'  /usr/bin/slufld
