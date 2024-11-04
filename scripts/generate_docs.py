import os
from pathlib import Path
import yaml
import git

# Paths
SPELLS_REPO_PATH = "datavzrd-spells"
OUTPUT_FILE = "src/docs/spells.rst"
repo = git.Repo("datavzrd-spells")
# get latest tag
TAG = repo.tags[-1]

# Header content to be added at the top of spells.rst
HEADER_CONTENT = """
******
Spells
******

Spells provide reusable configuration snippets for **datavzrd**.
These spells simplify the process of creating reports by allowing users to define common configurations in a modular way. Users can easily pull spells from local files or remote URLs, facilitating consistency and efficiency in data visualization workflows.

Below is a list of all the available spells in the `datavzrd-spells repository <https://github.com/datavzrd/datavzrd-spells>`__.
For adding new spells, please see the instructions in the `datavzrd-spells repository <https://github.com/datavzrd/datavzrd-spells>`__.
"""

def parse_meta_yaml(file_path):
    """Parses a meta.yaml file and returns a dictionary with the relevant data."""
    with open(file_path, "r") as file:
        return yaml.safe_load(file)
    
def header(title, level, rst_content):
    """Adds a header to the .rst content."""
    rst_content.append("\n" + title)
    rst_content.append((level * len(title)) + "\n")


def format_rst(spell_meta, spell_url):
    """Converts the spell meta.yaml information into an .rst formatted string."""
    rst_content = []
    
    # Spell Name
    header(spell_meta['name'], "=", rst_content)

    rst_content.append(f".. image:: https://img.shields.io/badge/code-github-blue")
    rst_content.append(f"  :target: https://github.com/datavzrd/datavzrd-spells/tree/{spell_url}\n")
    
    # Description
    rst_content.append(spell_meta.get('description', 'No description available.'))

    # Example
    example = spell_meta['example']["code"]
    example = example.replace("<url>", spell_url)
    header("Example", "-", rst_content)
    rst_content.append(".. code-block:: yaml\n")
    rst_content.append("\n")
    for line in example.splitlines():
        rst_content.append(f"  {line}")
    
    # Authors
    header("Authors", "-", rst_content)
    rst_content.append(", ".join(spell_meta['authors']))

    rst_content.append("\n\n")
    
    return rst_content

def generate_docs():
    """Iterates through the spells repository, parses meta.yaml files, and writes the output to the spells.rst file."""
    rst_content = [HEADER_CONTENT]
    
    # Walk through the directory structure
    for root, dirs, files in os.walk(SPELLS_REPO_PATH):
        if "meta.yaml" in files:
            meta_file_path = os.path.join(root, "meta.yaml")
            spell_meta = parse_meta_yaml(meta_file_path)
            spell_url = f"{TAG.name}/{Path(root).relative_to(SPELLS_REPO_PATH)}"
            rst_content.extend(format_rst(spell_meta, spell_url))
    
    # Write the content to spells.rst
    with open(OUTPUT_FILE, "w") as rst_file:
        rst_file.write("\n".join(rst_content))

if __name__ == "__main__":
    generate_docs()
