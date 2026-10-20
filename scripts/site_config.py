from ruamel.yaml import YAML

CONFIG_PATH = "src/config.yaml"

# Round-trip mode keeps the formatting of the hand-written config intact.
yaml = YAML()
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.width = 4096


def load_config():
    with open(CONFIG_PATH) as f:
        return yaml.load(f)


def save_config(config):
    with open(CONFIG_PATH, "w") as f:
        yaml.dump(config, f)
