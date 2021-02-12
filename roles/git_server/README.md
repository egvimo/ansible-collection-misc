# Git Server

Ansible role to install and configure a Git server.

## Role Variables

| Variable                        | Default value               | Description                    |
| ------------------------------- | --------------------------- | ------------------------------ |
| git_server_user                 | git                         | User to install Git Server for |
| git_server_user_home            | /home/{{ git_server_user }} | Home directory of the user     |
| git_server_repository_directory | /srv/git                    | Directory of the repositories  |
