# Installer

Ansible role to dynamically install different software from different sources.

This role contains the following custom install tasks:

- bat
- Brave Browser
- Google Chrome
- Docker
- Helm
- kubectl
- Starship
- Syncthing
- Vagrant
- Visual Studio Code

If the package is not one of the above, then the `apt` package manager (`scoop` for Windows hosts) is used to install the package.

If the role is defined in the playbook it is also possible to pass the packages (or override them) via command line:

```shell
ansible-playbook playbook.yml -t installer -e "installer_packages=kubectl,starship"
```
