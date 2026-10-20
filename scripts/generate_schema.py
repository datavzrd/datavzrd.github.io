import subprocess
from pathlib import Path

from site_config import load_config, save_config

SCHEMA_DIR = Path("src/schema")


def datavzrd(*args):
    return subprocess.run(
        ["datavzrd", *args], capture_output=True, text=True, check=True
    ).stdout


def update_assets():
    schemas = sorted(
        str(path.relative_to("src"))
        for path in SCHEMA_DIR.rglob("datavzrd.schema.json")
    )
    config = load_config()
    others = [asset for asset in config["assets"] if not asset.startswith("schema/")]
    config["assets"] = others + schemas
    save_config(config)


def generate_schema():
    try:
        schema = datavzrd("schema")
    except subprocess.CalledProcessError:
        print("Installed datavzrd does not provide the schema subcommand yet.")
        return

    version = datavzrd("--version").split()[-1]
    for directory in (SCHEMA_DIR / "latest", SCHEMA_DIR / f"v{version}"):
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "datavzrd.schema.json").write_text(schema)
    update_assets()

    print(f"Generated schema for datavzrd {version}")


if __name__ == "__main__":
    generate_schema()
