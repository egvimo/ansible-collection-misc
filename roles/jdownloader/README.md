# Bash-it

Ansible role to install [JDownloader](https://my.jdownloader.org/) as Docker container.

## Role Variables

| Variable                            | Default value             | Description                                                  |
| ----------------------------------- | ------------------------- | ------------------------------------------------------------ |
| jdownloader_user_id                 | jd                        | User to run the container with                               |
| jdownloader_user_name               | JDownloader               | User to run the container with                               |
| jdownloader_cfg_path                | /opt/jdownloader/cfg      | Configuration directory                                      |
| jdownloader_download_path           | /opt/jdownloader/download | Download directory                                           |
| jdownloader_myjd_username           |                           | Username for My JDownloader                                  |
| jdownloader_myjd_password           |                           | Password for My JDownloader                                  |
| jdownloader_update_myjd_credentials | false                     | Defines if the My JDownloader credentials have to be updated |

See [user role](../user/README.md) for the user variables.
