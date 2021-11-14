# Raspberry Pi

Ansible role to configure a Raspberry Pi via `raspi-config`.

## Role Variables

| Variable                        | Default value | Description                             |
| ------------------------------- | ------------- | --------------------------------------- |
| raspberry_locale                | en_US.UTF-8   | Locale configuration                    |
| raspberry_timezone              | Europe/Berlin | Timezone configuration                  |
| raspberry_keyboard_layout       | de            | Keyboard layout configuration           |
| raspberry_wlan_country          | DE            | WLAN country configuration              |
| raspberry_default_user          | pi            | Default user on a Raspberry Pi          |
| raspberry_default_user_password |               | Default user password on a Raspberry Pi |
| raspberry_new_user              |               | User to be added                        |
| raspberry_new_user_name         |               | Name of the new user                    |
| raspberry_new_user_password     |               | Password of the new user                |

## Tags

- `raspberry`
- `raspberry_raspi_config`
- `raspberry_user`
- `raspberry_password`
