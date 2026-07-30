"""The one thing this zed-sourced package exports."""

__all__ = ["greet"]


def greet(who: str) -> str:
    """Name the immutable Zed package namespace.

    A consumer asserts on this string so its test proves *which* package it
    resolved, not merely that something importable was on the path.
    """
    return f"hello {who} from zed-pkg-test/python-lib"
