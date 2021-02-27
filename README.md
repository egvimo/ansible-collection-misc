# Ansible collection of miscellaneous roles

![Molecule Test](https://github.com/egvimo/ansible-collection-misc/workflows/Molecule%20Test/badge.svg)

This collection contains the following roles:

| Role               | Name        | Documentation                         |
| ------------------ | ----------- | ------------------------------------- |
| Bash-it            | bash_it     | [Readme](roles/bash_it/README.md)     |
| Google Chrome      | chrome      | [Readme](roles/chrome/README.md)      |
| Docker             | docker      | [Readme](roles/docker/README.md)      |
| Git Server         | git_server  | [Readme](roles/git_server/README.md)  |
| Gitea              | gitea       | [Readme](roles/gitea/README.md)       |
| JDownloader        | jdownloader | [Readme](roles/jdownloader/README.md) |
| K3s                | k3s         | [Readme](roles/k3s/README.md)         |
| ReadyMedia         | minidlna    | [Readme](roles/minidlna/README.md)    |
| Pi-hole            | pi_hole     | [Readme](roles/pi_hole/README.md)     |
| Raspberry Pi       | raspberry   | [Readme](roles/raspberry/README.md)   |
| System             | system      | [Readme](roles/system/README.md)      |
| User               | user        | [Readme](roles/user/README.md)        |
| Visual Studio Code | vs_code     | [Readme](roles/vs_code/README.md)     |

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

The usage of the roles includes explained based on the Bash-it role. Use the role with default settings:

```yml
- hosts: servers
  roles:
    - role: egvimo.misc.bash_it
```

Customize usage:

```yml
- hosts: servers
  roles:
    - role: egvimo.misc.bash_it
      bash_it_user: bob
      bash_it_theme: atomic
```

## Tags

Every role has tags, which can be used to control the role. The default tag of each role is the role name itself, so within a large playbook the role can be run separately. Some roles have more tags to allow finer control over it. If this is the case, the tags are described in the particular readme.

## License

Copyright © 2020 egvimo.

Licensed under the MIT License. See [LICENSE](LICENSE).
