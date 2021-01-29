# Bash-it

Ansible role to install ReadyMedia (formerly known as MiniDLNA) as Docker container.

## Role Variables

| Variable            | Default value | Description                    |
| ------------------- | ------------- | ------------------------------ |
| minidlna_user_id    | minidlna      | User to run the container with |
| minidlna_user_name  | ReadyMedia    | User to run the container with |
| minidlna_media_path |               | Media directory                |

See [user role](../user/README.md) for the user variables.

## Example Playbook

Use the role with default settings:

```yml
- hosts: servers
  roles:
    - role: egvimo.general.minidlna
```

Customize usage:

```yml
- hosts: servers
  roles:
    - role: egvimo.general.minidlna
      bash_it_user: bob
      bash_it_theme: atomic
```
