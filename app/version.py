from pathlib import Path
import tomllib


_PROJECT_FILE = Path(__file__).resolve().parent.parent / "pyproject.toml"

with _PROJECT_FILE.open("rb") as project_file:
    APP_VERSION = tomllib.load(project_file)["project"]["version"]
