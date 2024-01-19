.. _usage:

*****
Usage
*****

To use **Datavzrd**, run the following command in your terminal:

.. code-block:: bash

   $ datavzrd [FLAGS] [OPTIONS] <CONFIG> --output <output>

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
