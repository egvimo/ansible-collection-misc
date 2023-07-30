# Installer

Ansible role to dynamically install different software from different sources.

This role contains the following custom install tasks:

- bat
- Brave Browser
- Gotify CLI
- Helm
- K9s
- kubectl
- lsd
- Rclone
- Restic
- Starship
- Syncthing
- Visual Studio Code

If the package is not one of the above, then the `apt` or `dnf` package manager (`scoop` for Windows hosts) is used to install the package.

## Usage

```yml
- hosts: servers
  roles:
    - role: egvimo.misc.installer
      vars:
        installer_packages:
          - kubectl
          - screen
          - starship
```

To dynamically pass the packages to the role (or override them) via command line, use the following command:

```shell
ansible-playbook playbook.yml -t installer -e "installer_packages=kubectl,starship"
```
