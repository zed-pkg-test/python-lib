import unittest

from python_lib import greet


class GreetTest(unittest.TestCase):
    def test_greet_identifies_the_immutable_zed_package_namespace(self) -> None:
        self.assertEqual(
            greet("consumer"),
            "hello consumer from zed-pkg-test/python-lib",
        )


if __name__ == "__main__":
    unittest.main()
