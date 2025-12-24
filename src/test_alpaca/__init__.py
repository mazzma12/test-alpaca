"""
test_alpaca - A fun CLI tool that displays messages with ASCII alpacas - like cowsay but with alpacas!

Like cowsay, but with alpacas!
"""
from test_alpaca.alpacas import ALPACAS, AlpacaType
from test_alpaca.cli import app
from test_alpaca.formatter import format_message

__all__ = ["ALPACAS", "AlpacaType", "format_message", "app"]
