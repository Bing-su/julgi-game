from importlib.metadata import version

from .__main__ import game

__version__ = version("julgi-game")

__all__ = ["__version__", "game"]
