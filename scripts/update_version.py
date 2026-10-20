import git

from site_config import CONFIG_PATH, load_config, save_config

def update_version():
    repo_url = "https://github.com/datavzrd/datavzrd.git"
    
    repo = git.Repo.clone_from(repo_url, "datavzrd")
    tags = sorted(repo.tags, key=lambda t: [int(i) for i in t.name.lstrip('v').split('.')], reverse=True)
    tag = tags[0] if tags else None
    
    config = load_config()
    config["project"]["version"] = str(tag)
    save_config(config)

    print(f"Found the following tags: {', '.join([str(tag) for tag in repo.tags])}")
    print(f"Updated {CONFIG_PATH} to latest tagged version {tag}")

if __name__ == "__main__":
    update_version()
