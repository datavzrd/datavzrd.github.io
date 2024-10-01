import os
import yaml

# Paths
SPELLS_REPO_PATH = "datavzrd-spells"
OUTPUT_FILE = "src/docs/spells.rst"

# Header content to be added at the top of spells.rst
HEADER_CONTENT = """
******
Spells
******

Spells provide reusable configuration snippets for **datavzrd**.
These spells simplify the process of creating reports by allowing users to define common configurations in a modular way. Users can easily pull spells from local files or remote URLs, facilitating consistency and efficiency in data visualization workflows.

Below is a list of all the available spells in the **datavzrd-spells** repository:
"""

def parse_meta_yaml(file_path):
    """Parses a meta.yaml file and returns a dictionary with the relevant data."""
    with open(file_path, "r") as file:
        return yaml.safe_load(file)

def format_rst(spell_meta):
    """Converts the spell meta.yaml information into an .rst formatted string."""
    rst_content = []
    
    # Spell Name
    rst_content.append(f"{spell_meta['name']}")
    rst_content.append("-" * len(spell_meta['name']))  # Underline
    
    # Description
    rst_content.append("\n")
    rst_content.append(spell_meta.get('description', 'No description available.'))

    # Example
    if 'example' in spell_meta:
        rst_content.append("\n\nExample:\n")
        rst_content.append(".. code-block:: yaml\n")
        rst_content.append("\n")
        for line in spell_meta['example'].splitlines():
            rst_content.append(f"  {line}")
    
    # Authors
    if 'authors' in spell_meta:
        rst_content.append("\n\nAuthors:\n")
        rst_content.append(", ".join(spell_meta['authors']))

    rst_content.append("\n\n")
    
    return "\n".join(rst_content)

def generate_docs():
    """Iterates through the spells repository, parses meta.yaml files, and writes the output to the spells.rst file."""
    rst_content = [HEADER_CONTENT]
    
    # Walk through the directory structure
    for root, dirs, files in os.walk(SPELLS_REPO_PATH):
        if "meta.yaml" in files:
            meta_file_path = os.path.join(root, "meta.yaml")
            spell_meta = parse_meta_yaml(meta_file_path)
            rst_content.append(format_rst(spell_meta))
    
    # Write the content to spells.rst
    with open(OUTPUT_FILE, "w") as rst_file:
        rst_file.write("\n".join(rst_content))

if __name__ == "__main__":
    generate_docs()
