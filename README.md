# Ansible collection of miscellaneous roles

![Molecule Test](https://github.com/egvimo/ansible-collection-general/workflows/Molecule%20Test/badge.svg)

This collection contains the following roles:

- [Bash-it](#bash-it)

## Installation

```shell
ansible-galaxy collection install egvimo.general
```

## Bash-it

Ansible role to install the [Bash-it framework](https://github.com/Bash-it/bash-it).

### Role Variables

| Variable           | Default value                            | Description                 |
| ------------------ | ---------------------------------------- | --------------------------- |
| bash_it_user       | {{ ansible_user }}                       | User to install Bash-it for |
| bash_it_user_home  | /home/{{ bash_it_user }}                 | User to install Bash-it for |
| bash_it_repository | <https://github.com/Bash-it/bash-it.git> | Git repository of Bash-it   |
| bash_it_version    | master                                   | Git branch, tag or commit   |
| bash_it_theme      | bobby                                    | Theme to be used            |

### Example Playbook

Install Bash-it with default settings:

```yml
- hosts: servers
  roles:
    - role: egvimo.general.bash_it
```

Customize installation:

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
