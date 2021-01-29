# Ansible collection of miscellaneous roles

![Molecule Test](https://github.com/egvimo/ansible-collection-general/workflows/Molecule%20Test/badge.svg)

This collection contains the following roles:

- [Bash-it](roles/bash_it/README.md)
- [Docker](roles/docker/README.md)
- [Raspberry Pi](roles/raspberry/README.md)
- [ReadyMedia (MiniDLNA)](roles/minidlna/README.md)
- [User](roles/user/README.md) (Helper)

## Installation

The latest version of the collection can be installed via Ansible Galaxy:

```shell
ansible-galaxy collection install egvimo.general
```

Or directly from the repository via `requirements.yml`:

```yml
collections:
  - name: https://github.com/egvimo/ansible-collection-general.git
    type: git
    version: main # Or any other Git branch, tag or commit
```

## License

Copyright © 2020 egvimo.

Licensed under the MIT License. See [LICENSE](LICENSE).
