import git
import yaml
import os

def update_version():
    repo_url = "https://github.com/datavzrd/datavzrd.git"
    
    repo = git.Repo.clone_from(repo_url, "datavzrd")
    tags = sorted(repo.tags, key=lambda t: [int(i) for i in t.name.lstrip('v').split('.')], reverse=True)
    tag = tags[0] if tags else None
    
    config_path = "src/config.yaml"
    
    with open(config_path) as f:
        config = yaml.safe_load(f)
    
    config["project"]["version"] = str(tag)
    
    with open(config_path, "w") as f:
        yaml.dump(config, f, default_flow_style=False, indent=2)

    print(f"Found the following tags: {', '.join([str(tag) for tag in repo.tags])}")
    print(f"Updated {config_path} to latest tagged version {tag}")

if __name__ == "__main__":
    update_version()
