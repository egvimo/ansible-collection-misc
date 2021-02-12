# Bash-it

Ansible role to install [Pi-hole](https://pi-hole.net/) as Docker container.

## Role Variables

| Variable                      | Default value | Description                           |
| ----------------------------- | ------------- | ------------------------------------- |
| pi_hole_user_id               | pihole        | User to run the container with        |
| pi_hole_user_name             | Pi-hole       | Username to run the container with    |
| pi_hole_base_path             | /opt/pihole   | Base directory                        |
| pi_hole_timezone              | Europe/Berlin | Timezone of the Pi-hole server        |
| pi_hole_additional_dns_server | 8.8.8.8       | Additional external DNS server IP     |
| pi_hole_server_ip             |               | Server IP of the Pi-hole installation |

See [user role](../user/README.md) for the user variables.
