"""
A minimalist acceptance test for ansible-test-runner. Executes tests via the
shell for simplicity.
"""
import logging
import os
import subprocess
import sys
import unittest


def get_logger(default_level='WARNING'):
    log_level = getattr(logging, os.environ.get('LOG_LEVEL', default_level))

    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    ch.setFormatter(formatter)

    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)
    logger.addHandler(ch)

    return logger
logger = get_logger()


assert sys.version_info[0] == 3 and sys.version_info[1] >= 7, \
    "This test requires Python 3.7 or above."


TEST_PATH = os.path.dirname(__file__)
ROLE_PATH = os.path.join(TEST_PATH, '..', 'roles', 'run_tests')


class AnsibleTestRunnerAcceptanceTests(unittest.TestCase):
    def setUp(self):
        test_suite = os.path.join(TEST_PATH, "test_suite.yml")
        logger.debug("Running Ansible test suite: %s", test_suite)

        self.r = subprocess.run(
            ["ansible-playbook", test_suite, 
             "-e", f"run_tests_role_path={ROLE_PATH}"],
            capture_output=True, text=True)
        logger.debug("Test return code: %s", self.r.returncode)
        logger.debug("Test stdout: %s", self.r.stdout)
        logger.debug("Test stderr: %s", self.r.stderr)

    def test_it_runs(self):
        self.assertEqual(self.r.returncode, 0)
    
    def test_summary_gets_printed(self):
        self.assertIn("Ran 2 tests and 1 failed.", self.r.stdout)
    
    def test_the_tests_actually_ran(self):
        self.assertIn("This test failed!", self.r.stdout)
        self.assertIn("This test passed!", self.r.stdout)


if __name__ == "__main__":
    unittest.main()