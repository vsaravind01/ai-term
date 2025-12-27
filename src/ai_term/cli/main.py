"""CLI Chat Application Entry Point."""

import os

from ai_term.cli.ui.app import ChatApp


def force_exit():
    """Force exit on interpreter shutdown."""
    os._exit(0)


def main():
    """Entry point for the CLI app."""
    app = ChatApp()

    try:
        app.run()
    except KeyboardInterrupt:
        pass
    finally:
        force_exit()


if __name__ == "__main__":
    main()
