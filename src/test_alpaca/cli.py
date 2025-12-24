"""CLI interface for test_alpaca."""

import sys
from pathlib import Path
from typing import Annotated, Optional

import typer


app = typer.Typer(
    name="test_alpaca",
    help="test-alpaca - Display messages with ASCII alpacas!",
    add_completion=False,
)


def version_callback(value: bool) -> None:
    """Show version and exit."""
    if value:
        typer.echo("test_alpaca version 0.1.0")
        raise typer.Exit()


@app.command()
def main(
    message: Annotated[str, typer.Argument(help="Message to display")] = "World!",
) -> None:
    typer.echo(f"Hello, {message.capitalize()}")


if __name__ == "__main__":
    app()
