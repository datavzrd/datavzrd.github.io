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
   * - ``-h``, ``--help``
     - Prints help information.
     - Flag
     - No
     - N/A
   * - ``--overwrite-output``
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

Suggest
-------

The `suggest` subcommand generates a configuration file based on the provided tabular input files. The suggested configuration is written to stdout.

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
   * - ``--files``
     - List of paths to input files.
     - Option
     - Yes
     - N/A
   * - ``--separators``
     - Separators for the corresponding input files (e.g., comma for CSV, tab for TSV).
     - Option
     - Yes
     - N/A
   * - ``--name``
     - Name of the report.
     - Option
     - No
     - ``Datavzrd Report``

Example:

.. code-block:: bash

    $ datavzrd suggest -f data1.csv -s , -f data2.tsv -s $'\t'
