"""
Learn CLI package containing Typer and Click example applications.
"""

from .click_app import cli as click_cli
from .typer_app import app as typer_app

__all__ = ["click_cli", "typer_app"]
