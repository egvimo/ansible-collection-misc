# Bash-it

Ansible role to install the [Starship](https://starship.rs/) shell prompt.

## Role Variables

| Variable           | Default value             | Description                  |
| ------------------ | ------------------------- | ---------------------------- |
| starship_user      | {{ ansible_user }}        | User to install Starship for |
| starship_user_home | /home/{{ starship_user }} | Home directory of the user   |
