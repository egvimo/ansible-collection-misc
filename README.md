# Ansible collection of miscellaneous roles

[![Ansible Lint & Molecule Test](https://github.com/egvimo/ansible-collection-misc/actions/workflows/lint-test.yml/badge.svg)](https://github.com/egvimo/ansible-collection-misc/actions/workflows/lint-test.yml)

> This collection includes roles to setup my personal systems and is designed according to my preferences. It's not meant to be a universal tool, but you can use it as inspiration for your own playbooks.

## Roles

This collection contains the following roles.

### Installer

Ansible role to dynamically install different software from different sources (see [Readme](roles/installer/README.md)).

### Miscellaneous

| Role         | Name        | Documentation                         |
| ------------ | ----------- | ------------------------------------- |
| JDownloader  | jdownloader | [Readme](roles/jdownloader/README.md) |
| Raspberry Pi | raspberry   | [Readme](roles/raspberry/README.md)   |
| System       | system      | [Readme](roles/system/README.md)      |

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
