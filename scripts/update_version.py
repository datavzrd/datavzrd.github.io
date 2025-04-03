import git
import yaml

repo_url = "https://github.com/datavzrd/datavzrd.git"
repo = git.Repo.clone_from(repo_url, ".")
tag = repo.tags[-1]

config_path = "src/config.yaml"

with open(config_path) as f:
    config = yaml.safe_load(f)

config["version"] = str(tag)

with open(config_path, "w") as f:
    yaml.dump(config, f, default_flow_style=False)

print(f"Updated {config_path} to version {tag}")
