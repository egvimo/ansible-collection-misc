# Raspberry Pi

Ansible role to configure a Raspberry Pi via `raspi-config`.

## Role Variables

| Variable                  | Default value | Description                    |
| ------------------------- | ------------- | ------------------------------ |
| ansible_user              | pi            | Default user on a Raspberry Pi |
| ansible_password          | raspberry     | Default password for user pi   |
| raspberry_locale          | en_US.UTF-8   | Locale configuration           |
| raspberry_timezone        | Europe/Berlin | Timezone configuration         |
| raspberry_keyboard_layout | de            | Keyboard layout configuration  |
| raspberry_wlan_country    | DE            | WLAN country configuration     |
| raspberry_user            |               | User to be added               |
| raspberry_username        |               | Name of the new user           |
| raspberry_password        |               | Password of the new user       |

## Tags

- `raspberry`
- `raspberry_raspi_config`
- `raspberry_user`
