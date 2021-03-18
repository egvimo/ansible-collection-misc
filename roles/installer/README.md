# Installer

Ansible role to dynamically install different software from different sources.

This role contains the following custom install tasks:

- Brave Browser
- Google Chrome
- kubectl
- Starship
- Visual Studio Code

If the package is not one of the above, then the `apt` package manager (`scoop` for Windows hosts) is used to install the package.

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
