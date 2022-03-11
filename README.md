# Ansible collection of miscellaneous roles

[![Ansible Lint & Molecule Test](https://github.com/egvimo/ansible-collection-misc/actions/workflows/lint-test.yml/badge.svg)](https://github.com/egvimo/ansible-collection-misc/actions/workflows/lint-test.yml)

> This collection includes roles to setup my personal systems and is designed according to my preferences. It's not meant to be a universal tool, but you can use it as inspiration for your own playbooks.

## Roles

This collection contains the following roles.

| Name                                     | Description                                                      |
| ---------------------------------------- | ---------------------------------------------------------------- |
| [docker_wsl](roles/docker_wsl/README.md) | Install and configure Docker inside WSL2 to use it under Windows |
| [dotfiles](roles/dotfiles/README.md)     | Dynamically install various dotfiles                             |
| [gnome](roles/gnome/README.md)           | Configure Gnome                                                  |
| [installer](roles/installer/README.md)   | Dynamically install different software from different sources    |
| [raspberry](roles/raspberry/README.md)   | Configure a Raspberry Pi via `raspi-config`                      |
| [system](roles/system/README.md)         | Perform general system related tasks                             |

## Installation

The latest version of the collection can be installed via Ansible Galaxy:

```shell
ansible-galaxy collection install egvimo.misc
```

Or directly from the repository via `requirements.yml`:

```yml
collections:
  - name: https://github.com/egvimo/ansible-collection-misc.git
    type: git
    version: main # Or any other Git branch, tag or commit
```

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

## Tags

Every role has tags, which can be used to control the role. The default tag of each role is the role name itself, so within a large playbook the role can be run separately. Some roles have more tags to allow finer control over it. If this is the case, the tags are described in the particular readme.

## License

Copyright © 2020 egvimo.

Licensed under the MIT License. See [LICENSE](LICENSE).
