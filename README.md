# ansible-test-runner

An extremely simple test runner for Ansible.

## Example

See the `functional_test` directory for a working example. `test_suite.yml` is a 
playbook defining the test suite and the `ansible_tests` directory contains a 
pair of test cases.

Run `ansible-playbook functional_test/test_suite.yml` to see the example run.

### test_suite.yml

`test_suite.yml` defines the tests to run. The test cases are passed to the
`run_tests` role as a list.

```yaml
- hosts: localhost
  gather_facts: no
  roles:
  - role: ../roles/run_tests
    test_cases:
    - ansible_tests/always_fails.yml
    - ansible_tests/always_passes.yml
```

### Test cases

Each test case is a simple task file.

```yaml
# always_fails.yml
- fail: msg="This test failed!"

# always_passes.yml
- debug: msg="This test passed!"
```

## Dependencies

* Ansible 2.8 or greater is recommended.
* Python 3.7 or above is required for the functional test.

## Setup

From the repo root:

```shell
python3.7 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
# check that the install is valid
python functional_test/test.py
```

## Testing

Run `python functional_test/test.py`.

## License

ansible-test-runner, a simple Ansible test runner.
Copyright (C) 2019 pushittoprod.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see https://www.gnu.org/licenses/.