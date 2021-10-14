# Installer

Ansible role to dynamically install different software from different sources.

This role contains the following custom install tasks:

- bat
- Brave Browser
- Google Chrome
- Docker
- Helm
- K3s
- kubectl
- Starship
- Syncthing
- Vagrant
- Visual Studio Code

If the package is not one of the above, then the `apt` package manager (`scoop` for Windows hosts) is used to install the package.

To dynamically pass the packages to the role (or override them) via command line, use the following command:

```shell
ansible-playbook playbook.yml -t installer -e "installer_packages=kubectl,starship"
```

## Role Variables

### K3s

| Variable                  | Default value | Description                 |
| ------------------------- | ------------- | --------------------------- |
| installer_k3s_server_args |               | Server arguments (optional) |
