# Docker

Ansible role to configure a Raspberry Pi via `raspi-config`.

## Role Variables

| Variable                  | Default value | Description                   |
| ------------------------- | ------------- | ----------------------------- |
| raspberry_locale          | en_US.UTF-8   | Locale configuration          |
| raspberry_timezone        | Europe/London | Timezone configuration        |
| raspberry_keyboard_layout | de            | Keyboard layout configuration |
| raspberry_wlan_country    | DE            | WLAN country configuration    |

## Example Playbook

Use the role with default settings:

```yml
- hosts: servers
  roles:
    - role: egvimo.general.raspberry
```

Customize usage:

```yml
- hosts: servers
  roles:
    - role: egvimo.general.raspberry
      raspberry_locale: en_GB.UTF-8
```
