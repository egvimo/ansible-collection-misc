# Ansible collection of miscellaneous roles

![Molecule Test](https://github.com/egvimo/ansible-collection-general/workflows/Molecule%20Test/badge.svg)

This collection contains the following roles:

| Role               | Name        | Documentation                         |
| ------------------ | ----------- | ------------------------------------- |
| Bash-it            | bash_it     | [Readme](roles/bash_it/README.md)     |
| Docker             | docker      | [Readme](roles/docker/README.md)      |
| JDownloader        | jdownloader | [Readme](roles/jdownloader/README.md) |
| Pi-hole            | pi_hole     | [Readme](roles/pi_hole/README.md)     |
| Raspberry Pi       | raspberry   | [Readme](roles/raspberry/README.md)   |
| ReadyMedia         | minidlna    | [Readme](roles/minidlna/README.md)    |
| User               | user        | [Readme](roles/user/README.md)        |
| Visual Studio Code | vs_code     | [Readme](roles/vs_code/README.md)     |

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

## Usage

The usage of the roles includes explained based on the Bash-it role. Use the role with default settings:

```yml
- hosts: servers
  roles:
    - role: egvimo.general.bash_it
```

Customize usage:

```yml
- hosts: servers
  roles:
    - role: egvimo.general.bash_it
      bash_it_user: bob
      bash_it_theme: atomic
```

## License

Copyright © 2020 egvimo.

Licensed under the MIT License. See [LICENSE](LICENSE).
