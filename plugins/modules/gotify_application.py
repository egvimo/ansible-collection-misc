#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: gotify_application

short_description: Manage Gotify applications

version_added: "0.11.0"

description: Manage Gotify applications.

options:
    url:
        description: Gotify server URL.
        required: true
        type: str
    validate_certs:
        description: If C(false), SSL certificates will not be validated.
        required: false
        default: 'true'
        choices: ['true', 'false']
    username:
        description: A username for the module to use for authentication.
        required: true
        type: str
    password:
        description: A password for the module to use for authentication.
        required: true
        type: str
    name:
        description: Name of the Gotify application.
        required: true
        type: str
    description:
        description: Application description.
        required: false
        type: str
    image:
        description: Application image.
        required: false
        type: str

author:
    - egvimo (@egvimo)
'''

EXAMPLES = r'''
# Create an application
- name: Create application
  egvimo.misc.gotify_application:
    url: http://localhost:8080
    username: admin
    password: admin
    name: My App
'''

RETURN = r'''
token:
    description: The token for the application.
    type: str
    returned: always
    sample: 'AWH0wZ5r0Mbac.r'
'''

from ansible.module_utils.basic import AnsibleModule, json
from ansible.module_utils.urls import open_url


class Gotify():
    headers = {'Content-Type': 'application/json'}

    def __init__(self, module):
        self.module = module
        self.url = module.params['url']
        self.username = module.params['username']
        self.password = module.params['password']
        self.validate_certs = module.params['validate_certs']
        self.application_url = f"{self.url.rstrip('/')}/application"

    def _send_request(self, url, method='get', data=None):
        response = open_url(
            url,
            method=method,
            headers=self.headers,
            url_username=self.username,
            url_password=self.password,
            validate_certs=self.validate_certs,
            force_basic_auth=True,
            data=data
        )

        if response.code != 200:
            self.module.fail_json(msg=f"Request to Gotify failed with HTTP {response.code}")

        return json.loads(response.read())

    def get_applications(self):
        return self._send_request(self.application_url)

    def create_application(self, name, description=None, image=None):
        application = {
            'name': name,
            'description': description
        }
        result = self._send_request(self.application_url, method='post', data=json.dumps(application))

        # TODO Image

        return result

    def update_application(self, application_id, name, description=None):
        application = {
            'name': name,
            'description': description
        }
        return self._send_request(f"{self.application_url}/{application_id}", method='put', data=json.dumps(application))

    def set_application_image(self, application_id, image):
        return self._send_request(f"{self.application_url}/{application_id}/image", method='post', data=image)


def main():
    module_args = dict(
        url=dict(type='str', required=True),
        validate_certs=dict(type='bool', required=False, default=True),
        username=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
        name=dict(type='str', required=True),
        description=dict(type='str', required=False),
        image=dict(type='str', required=False)
    )
    required_together = (
        ['username', 'password'],
    )

    result = dict(
        changed=False,
        token=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        required_together=required_together,
        supports_check_mode=True
    )

    name = module.params['name']
    description = module.params['description']
    image = module.params['image']

    gotify = Gotify(module)
    applications = gotify.get_applications()

    for app in applications:
        if app['name'] == name:
            # TODO Full check
            result['token'] = app['token']
            module.exit_json(**result)

    if not module.check_mode:
        app = gotify.create_application(name, description, image)
        result['token'] = app['token']
        result['changed'] = True

    module.exit_json(**result)


if __name__ == '__main__':
    main()
