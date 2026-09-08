.. _usage:

*****
Usage
*****

To use **Datavzrd**, run the following command in your terminal:

.. code-block:: bash

   $ datavzrd [FLAGS] [OPTIONS] <CONFIG> --output <output>

Example:

.. code-block:: bash

   $ datavzrd path/to/my-config.yaml --output my-report

Command Line Arguments
======================

.. list-table:: Command Line Arguments
   :widths: 20 40 10 10 20
   :header-rows: 1

   * - Name
     - Description
     - Type
     - Required
     - Default Value
   * - ``--debug``
     - Activates debug mode. Javascript files are not minified.
     - Flag
     - No
     - N/A
   * - ``-n``, ``--dryrun``
     - Do not execute anything. Only validate the configuration and report what would be rendered, without writing any output.
     - Flag
     - No
     - N/A
   * - ``-h``, ``--help``
     - Prints help information.
     - Flag
     - No
     - N/A
   * - ``-x``, ``--overwrite-output``
     - Overwrites the contents of the given output directory if it is not empty.
     - Flag
     - No
     - N/A
   * - ``-V``, ``--version``
     - Prints version information.
     - Flag
     - No
     - N/A
   * - ``-v``, ``--verbose``
     - Verbose mode (-v, -vv, -vvv, etc.).
     - Flag
     - No
     - N/A
   * - ``-o``, ``--output``
     - Output file.
     - Option
     - Yes
     - N/A
   * - ``-w``, ``--webview-url``
     - Sets the URL of the webview host. Note that when using the link, the row data can temporarily occur (in base64-encoded form) in the server logs of the given webview host.
     - Option
     - No
     - ``https://datavzrd.github.io/view/``
   * - ``<CONFIG>``
     - Config file containing file paths and settings.
     - Argument
     - Yes
     - N/A

Subcommands
===========

Datavzrd also supports additional functionality through subcommands. Below are the available subcommands:

Publish
-------

The `publish` subcommand allows you to publish a generated report to GitHub Pages. This requires the user to have `gh` installed and authenticated.

.. code-block:: bash

   $ datavzrd publish --repo-name <repo_name> --report-path <report_path> [--org <organization>]

Command Line Arguments for `publish`:

.. list-table:: `publish` Subcommand Arguments
   :widths: 20 40 10 10 20
   :header-rows: 1

   * - Name
     - Description
     - Type
     - Required
     - Default Value
   * - ``--repo-name``
     - GitHub repository name to publish to.
     - Option
     - Yes
     - N/A
   * - ``--report-path``
     - Path to the report directory.
     - Option
     - Yes
     - N/A
   * - ``--org``
     - Optional: Specify the organization for the repository.
     - Option
     - No
     - N/A

Example:

.. code-block:: bash

    $ datavzrd publish --repo-name my-awesome-report --report-path ./output --org my-awesome-org --entry index.html

This command publishes the report located in ./output to the my-awesome-report repository of the organisation my-awesome-org on GitHub Pages, with index.html as the entry point. The repository will be created under https://my-awesome-org.github.io/my-awesome-report/ and can be accessed after GitHub pages is activated by the user. After successful publishing the user is provided with simple instructions on how to activate GitHub pages.

.. note::

    When publishing a Snakemake report, make sure it was generated with
    ``snakemake --report report.zip`` and properly unzipped afterwards. Do **not** use
    ``snakemake report report.html``. For details, see the `Snakemake reporting documentation <https://snakemake.readthedocs.io/en/stable/snakefiles/reporting.html>`_.


Suggest
-------

The `suggest` subcommand generates a configuration file based on the provided tabular input files. The suggested configuration is written to stdout. When an LLM endpoint is passed via ``--llm-url``, the configuration is drafted by that model instead of the built-in heuristic and validated against datavzrd before it is written.

.. code-block:: bash

   $ datavzrd suggest --files <file_paths> --separators <separators> [--name <report_name>]

Command Line Arguments for `suggest`:

.. list-table:: `suggest` Subcommand Arguments
   :widths: 20 40 10 10 20
   :header-rows: 1

   * - Name
     - Description
     - Type
     - Required
     - Default Value
   * - ``-f``, ``--files``
     - List of paths to input files.
     - Option
     - Yes
     - N/A
   * - ``-s``, ``--separators``
     - Separators for the corresponding input files (e.g., comma for CSV, tab for TSV).
     - Option
     - Yes
     - N/A
   * - ``--name``
     - Name of the report.
     - Option
     - No
     - ``Datavzrd Report``
   * - ``--llm-url``
     - Base URL of an OpenAI-compatible chat completions endpoint, including the API version (e.g. ``http://localhost:11434/v1`` for Ollama). When set, the configuration is drafted by the LLM.
     - Option
     - No
     - N/A
   * - ``--llm-model``
     - Model to request from the LLM endpoint.
     - Option
     - With ``--llm-url``
     - N/A
   * - ``--llm-token``
     - API token for the LLM endpoint, sent as a bearer token. Can also be set via the ``DATAVZRD_LLM_TOKEN`` environment variable.
     - Option
     - No
     - N/A
   * - ``-p``, ``--prompt``
     - Description of the desired report passed to the LLM. If omitted, it is requested interactively.
     - Option
     - No
     - N/A

Example:

.. code-block:: bash

    $ datavzrd suggest -f data1.csv -s , -f data2.tsv -s $'\t'

To let an LLM draft the configuration, point ``--llm-url`` at an OpenAI-compatible endpoint and pass a model and a prompt:

.. code-block:: bash

    $ datavzrd suggest -f data.csv -s , --llm-url http://localhost:11434/v1 --llm-model qwen2.5:1.5b --prompt "Hide id columns, pin the sample name, viridis heatmap for p-values"

If the endpoint requires a token, set ``DATAVZRD_LLM_TOKEN`` in your environment or pass it with ``--llm-token``.


Schema
------

The `schema` subcommand prints the JSON schema of the configuration file to stdout. It enables autocompletion and inline validation in editors that support JSON schema for YAML.

.. code-block:: bash

   $ datavzrd schema

Example:

.. code-block:: bash

    $ datavzrd schema > datavzrd.schema.json
