# Ansible collection of miscellaneous roles

[![Ansible Lint](https://github.com/egvimo/ansible-collection-misc/actions/workflows/ansible-lint.yml/badge.svg)](https://github.com/egvimo/ansible-collection-misc/actions/workflows/ansible-lint.yml)
[![Molecule Test](https://github.com/egvimo/ansible-collection-misc/actions/workflows/molecule-test.yml/badge.svg)](https://github.com/egvimo/ansible-collection-misc/actions/workflows/molecule-test.yml)

> This collection includes roles to setup my personal systems and is designed according to my preferences. It's not meant to be a universal tool, but you can use it as inspiration for your own playbooks.

This collection contains the following roles:

| Role              | Name        | Documentation                         |
| ----------------- | ----------- | ------------------------------------- |
| Git Server        | git_server  | [Readme](roles/git_server/README.md)  |
| Gitea             | gitea       | [Readme](roles/gitea/README.md)       |
| JDownloader       | jdownloader | [Readme](roles/jdownloader/README.md) |
| K3s               | k3s         | [Readme](roles/k3s/README.md)         |
| ReadyMedia        | minidlna    | [Readme](roles/minidlna/README.md)    |
| Pi-hole           | pi_hole     | [Readme](roles/pi_hole/README.md)     |
| Raspberry Pi      | raspberry   | [Readme](roles/raspberry/README.md)   |
| System            | system      | [Readme](roles/system/README.md)      |

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
    - role: egvimo.misc.k3s
      vars:
        k3s_server_args: '--docker'
```

## Tags

Every role has tags, which can be used to control the role. The default tag of each role is the role name itself, so within a large playbook the role can be run separately. Some roles have more tags to allow finer control over it. If this is the case, the tags are described in the particular readme.

## License

Copyright © 2020 egvimo.

Licensed under the MIT License. See [LICENSE](LICENSE).
