.. _YAML: https://yaml.org

***************
Troubleshooting
***************

This page lists common problems when using Datavzrd and how to solve them.
The error messages shown here are examples based on the :doc:`tutorial <tutorial>`, so file, view and column names will differ in your case.

Installing Datavzrd
===================

The ``datavzrd`` command is not found
-------------------------------------

If you installed Pixi right before installing Datavzrd, restart your terminal so that the ``pixi`` command and all tools installed via ``pixi global install`` are found.
If you installed Datavzrd via Conda, make sure that the environment you installed it into is activated, e.g. via

.. code-block:: bash

    conda activate datavzrd

Running Datavzrd
================

The output directory is not empty
---------------------------------

.. code-block:: text

    Error: Given output directory "example-report" was not empty. If you wish to overwrite it please use the --overwrite-output option.

Datavzrd does not overwrite existing reports unless you explicitly allow it.
Add ``--overwrite-output`` (or its short form ``-x``) to your command:

.. code-block:: bash

    datavzrd config.datavzrd.yaml --output example-report -x

The configuration file cannot be found
--------------------------------------

.. code-block:: text

    Error: Could not find config file under given path "config.datavzrd.yml"

    Caused by:
        No such file or directory (os error 2)

Check that you run Datavzrd from the directory that contains your configuration file and that the given file name matches it exactly.
Running ``ls`` shows you which files are in your current directory.

Configuration file
==================

Errors in the configuration file point to the line and column where Datavzrd stumbled, which is a good place to start looking.

Unknown field
-------------

.. code-block:: text

    11 |     heatmap:
       |     ^ views.movies.render-table.columns.Rated: unknown field `heatmap`, expected one of `optional`, `precision`, `label`, `custom`, `custom-path`, `display-mode`, `link-to-url`, `plot`, `custom-plot`, `ellipsis`, `plot-view-legend`, `spell` at line 11 column 11

Either the entry is misspelled, or it is indented wrongly so that it ends up in the wrong place of the configuration.
In this example, ``heatmap`` has the same indentation as ``plot``, although it has to be nested below it:

.. code-block:: yaml

    # wrong
    Rated:
      plot:
      heatmap:
        scale: ordinal
        color-scheme: category20

    # correct
    Rated:
      plot:
        heatmap:
          scale: ordinal
          color-scheme: category20

The list after ``expected one of`` shows all entries that are allowed at this position.

Invalid type: unit value
------------------------

.. code-block:: text

     3 |   path: data/movies.csv
       |   ^ datasets.movies: invalid type: unit value, expected struct DatasetSpecs at line 3 column 3

Datavzrd expected entries nested below ``movies``, but found none.
This usually means that the following lines are not indented enough, or that they are indented with tab characters, which are not allowed in YAML_.
Always indent with spaces.

Mapping values are not allowed in this context
----------------------------------------------

.. code-block:: text

     7 |     desc: Note: this breaks
       |               ^ mapping values are not allowed in this context at line 7 column 15

A colon followed by a space has a special meaning in YAML_.
If a value contains one, put the value in quotes or write it as a multi-line text using ``|``:

.. code-block:: yaml

    desc: "Note: this works"

.. code-block:: yaml

    desc: |
      Note: this works too

Invalid separator
-----------------

.. code-block:: text

     4 |     separator: \t
       |                ^ datasets.movies.separator: invalid value: string "\\t", expected a character at line 4 column 16

Special characters like a tab have to be put in quotes:

.. code-block:: yaml

    separator: "\t"

Column cannot be found
----------------------

.. code-block:: text

    Error: Could not find column named 'rated' in the dataset that is used by view movies. Available columns are: Title, Year, Rated, Released, Runtime, Genre, Director, imdbRating, imdbID

Column names are case sensitive and have to match the header of your table exactly.
The list of available columns at the end of the message shows how they are spelled.

If this list contains only a single entry with all column names separated by semicolons (e.g. ``Available columns are: sample;value``), your table is separated by semicolons instead of commas.
This is often the case for CSV files exported from Excel.
Tell Datavzrd about it in the dataset definition:

.. code-block:: yaml

    datasets:
      samples:
        path: data/samples.csv
        separator: ";"

Data files
==========

The dataset cannot be read
--------------------------

.. code-block:: text

    Error: Failed to read dataset from path data/movies.csv

    Caused by:
        0: IO error: No such file or directory (os error 2)
        1: No such file or directory (os error 2)

Paths in the configuration file are interpreted relative to the directory from which you run Datavzrd, not relative to the configuration file.
Check that the file exists at the given path when looking from your current directory.

Unknown file format
-------------------

.. code-block:: text

    Error: Failed to read dataset from path data/samples.xlsx

    Caused by:
        Unknown file format

Datavzrd determines the format of a file from its ending, which has to be one of ``.csv``, ``.tsv``, ``.json`` or ``.parquet`` (CSV, TSV and JSON files may additionally be compressed, ending with e.g. ``.csv.gz``).
The ending is case sensitive, so ``.CSV`` is not recognized.
Excel files have to be exported as CSV first.

The file appears to be binary
-----------------------------

.. code-block:: text

    Error: Given file data/samples.csv appears to be binary, not plain text

Datavzrd expects text files to be encoded as UTF-8.
This error occurs if a file is saved in another encoding, e.g. when the column names contain special characters like umlauts in another encoding, or when the whole file is saved as UTF-16.
In Excel, export your table via "Save As" and choose "CSV UTF-8 (Comma delimited)" as file type.
Depending on the language settings of your system, Excel might still separate the columns by semicolons (see :ref:`Column cannot be found <column cannot be found>`).

No numeric values for a quantitative scale
------------------------------------------

.. code-block:: text

    Error: Column "value" in dataset at "data/samples.csv" is configured with a quantitative scale (e.g. a heatmap), but does not contain any numeric values to derive a domain from. Please provide numeric values for this column, set an explicit domain, or use an ordinal scale.

Scales like ``linear`` only work for columns with numbers.
Note that numbers with a decimal comma (e.g. ``3,14``) are not recognized as numbers, so they have to use a decimal point (e.g. ``3.14``).
For columns that contain categories instead of numbers, use an ``ordinal`` scale.

In the report
=============

Error when calling custom function
----------------------------------

If a Javascript function in your configuration (e.g. in ``custom`` or ``add-columns``) fails, the report shows a dialog like this:

.. code-block:: text

    Error when calling custom function for column Title (please fix the function definition in the datavzrd config):

    TypeError: Cannot read properties of undefined (reading 'toFixed')

The first line names the column whose function failed, followed by the error message of the browser.
In this example, the function accessed a column that does not exist (e.g. a misspelled ``row['imdbRatin']``), which yields ``undefined``.
Fix the function in your configuration file and run Datavzrd again.
