SLUFL is a daemon that triggers Ansible playbook when entries in an LDAP directory change.

The slufld daemon polls the LDAP directory at regular intervals for changes in entries matching a given filter. When updated entries appear, slufld triggers a set of Ansible playbooks and feed them with the information from the LDAP entries.

It can be used for instance to setup a proper environment for new users that are registered to an LDAP directory. It was first developed within the [CÉCI](http://www.ceci-hpc.be) to setup new users (for instance create home directory, set user quota, register to Slurm resource manager, etc.)


Quick start
===========

Prerequisites:

  - Python 2.7
  - LDAP Python binding (python-ldap) with your operating system's package manager or Pip
  - Ansible (version 2 or above; for the 2.4 and 2.9 versions, see the dedicated branches)

Copy the `slufld.conf.template` file to `/etc/slufld.conf` and update its contents, especially the part that refers to the LDAP server configuration. Copy the `etc/slufld.conf.d` directory to `/etc`.

You can then test slufl by running it interactively on the entries corresponding to the LDAP filter "uid=*".

    ./slufld --debug --run-once --foreground "uid=*"


