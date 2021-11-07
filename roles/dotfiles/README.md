# Dotfiles

Ansible role to dynamically configure various dotfiles.

This role contains the following dotfiles:

- inputrc
- starship

## Usage

```yml
- hosts: servers
  roles:
    - role: egvimo.misc.dotfiles
      vars:
        dotfiles:
          - inputrc
          - starship
        dotfiles_starship_screen: true
```

## Role Variables

| Variable                    | Default value | Description          |
| --------------------------- | ------------- | -------------------- |
| dotfiles_starship_cpu_temp  | false         | Enable custom module |
| dotfiles_starship_git_email | false         | Enable custom module |
| dotfiles_starship_screen    | false         | Enable custom module |
