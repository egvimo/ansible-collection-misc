# Docker

Ansible role to install the Docker via package manager.

## Role Variables

| Variable    | Default value      | Description                   |
| ----------- | ------------------ | ----------------------------- |
| docker_user | {{ ansible_user }} | User to add to `docker` group |

## Example Playbook

Use the role with default settings:

```yml
- hosts: servers
  roles:
    - role: egvimo.general.docker
```

Customize usage:

```yml
- hosts: servers
  roles:
    - role: egvimo.general.docker
      docker_user: bob
```
