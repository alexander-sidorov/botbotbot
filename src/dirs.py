from pathlib import Path

_this_file = Path(__file__).resolve()

DIR_REPO = _this_file.parent.parent.resolve()

DIR_SRC = DIR_REPO / "src"
DIR_TEMPLATES = DIR_SRC / "templates"
