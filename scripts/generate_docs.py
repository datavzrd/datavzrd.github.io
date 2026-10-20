import re
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

Column spells configure a single column, while view spells configure an entire view, e.g. for the output of a specific tool.

Below is a list of all the available spells in the `datavzrd-spells repository <https://github.com/datavzrd/datavzrd-spells>`__.
For adding new spells, please see the instructions in the `datavzrd-spells repository <https://github.com/datavzrd/datavzrd-spells>`__.
"""

def parse_meta_yaml(file_path):
    """Parses a meta.yaml file and returns a dictionary with the relevant data."""
    with open(file_path, "r") as file:
        return yaml.safe_load(file)
    
def rst_description(text):
    """Turns markdown style code blocks, `code` and [links](url) into rst and escapes underscores elsewhere."""
    def convert(part):
        if block := re.fullmatch(r"```(\w*)\n(.*?)```\n?", part, re.DOTALL):
            code = "".join(f"   {line}" if line.strip() else line for line in block[2].splitlines(keepends=True))
            return f"\n.. code-block:: {block[1] or 'text'}\n\n{code}\n"
        if part.startswith("`"):
            return f"`{part}`"
        if link := re.fullmatch(r"\[([^\]]+)\]\(([^)]+)\)", part):
            return f"`{link[1]} <{link[2]}>`__"
        return part.replace("_", "\\_")

    parts = re.split(r"(```\w*\n.*?```\n?|`[^`]+`|\[[^\]]+\]\([^)]+\))", text, flags=re.DOTALL)
    return "".join(convert(part) for part in parts)


def header(title, level, rst_content):
    """Adds a header to the .rst content."""
    rst_content.append("\n" + title)
    rst_content.append((level * len(title)) + "\n")


def format_rst(spell_meta, spell_url, spell_path):
    """Converts the spell meta.yaml information into an .rst formatted string."""
    rst_content = []
    
    # Spell Name
    header(spell_meta['name'], "-", rst_content)

    rst_content.append(f".. image:: https://img.shields.io/badge/code-github-blue")
    rst_content.append(f"  :target: https://github.com/datavzrd/datavzrd-spells/tree/{spell_url}\n")
    rst_content.append(f".. image:: https://img.shields.io/badge/example-report-green")
    rst_content.append(f"  :target: https://datavzrd.github.io/datavzrd-spells/{spell_path}/index.html\n")
    
    # Description
    description = rst_description(spell_meta.get('description', 'No description available.'))
    rst_content.append(description)

    # Example
    example = spell_meta['example']["code"]
    example = example.replace("<url>", spell_url)
    header("Example", "^", rst_content)
    rst_content.append(".. code-block:: yaml\n")
    rst_content.append("\n")
    for line in example.splitlines():
        rst_content.append(f"  {line}")
    
    # Authors
    header("Authors", "^", rst_content)
    rst_content.append(", ".join(spell_meta['authors']))

    rst_content.append("\n\n")
    
    return rst_content

def generate_docs():
    """Iterates through the spells repository, parses meta.yaml files, and writes the output to the spells.rst file."""
    rst_content = [HEADER_CONTENT]

    spells = {"column": [], "view": []}
    for meta_file_path in sorted(Path(SPELLS_REPO_PATH).glob("**/meta.yaml")):
        spell_meta = parse_meta_yaml(meta_file_path)
        spells[spell_meta["type"]].append((spell_meta, meta_file_path.parent.relative_to(SPELLS_REPO_PATH)))

    for spell_type, title in [("column", "Column spells"), ("view", "View spells")]:
        if not spells[spell_type]:
            continue
        header(title, "=", rst_content)
        for spell_meta, spell_path in spells[spell_type]:
            spell_url = f"{TAG.name}/{spell_path}"
            rst_content.extend(format_rst(spell_meta, spell_url, spell_path))
    
    # Write the content to spells.rst
    with open(OUTPUT_FILE, "w") as rst_file:
        rst_file.write("\n".join(rst_content))

if __name__ == "__main__":
    generate_docs()
