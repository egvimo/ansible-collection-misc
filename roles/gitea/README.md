# Bash-it

Ansible role to install [Gitea](https://gitea.io/) as Docker container.

## Role Variables

| Variable        | Default value   | Description                        |
| --------------- | --------------- | ---------------------------------- |
| gitea_user_id   | gitea           | User to run the container with     |
| gitea_user_name | Gitea           | Username to run the container with |
| gitea_data_path | /opt/gitea/data | Data directory                     |

See [user role](../user/README.md) for the user variables.
