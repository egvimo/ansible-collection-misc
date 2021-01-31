# User

Ansible role to create a user (and group). This is mainly a helper role for other roles.

## Role Variables

| Variable                       | Default value | Description                             |
| ------------------------------ | ------------- | --------------------------------------- |
| user_id                        |               | ID of user (and group) to be created    |
| user_name                      |               | Name of user to be created              |
| user_add_ansible_user_to_group | false         | Add `ansible_user` to the created group |
| user_uid                       |               | Will be set after user creation         |
| user_gid                       |               | Will be set after user creation         |
