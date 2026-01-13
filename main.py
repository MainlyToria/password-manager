"""Entry point for running the SecurePass desktop application.

This module constructs and runs the Tkinter `SecurePassApp` when
executed as a script.
"""

from securepass.app import SecurePassApp


def main():
    """Create and run the desktop SecurePass application."""
    app = SecurePassApp()
    app.run()


if __name__ == "__main__":
    main()
