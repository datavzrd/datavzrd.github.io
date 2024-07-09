.. _YAML: https://yaml.org
.. _Markdown: https://en.wikipedia.org/wiki/Markdown

********
Tutorial
********

This tutorial introduces Datavzrd.
Datavzrd allows to generate interactive HTML based reports from tabular data (including multiple linked tables) without programming knowledge (depending on the use case even in a so-called zero-code or low-code manner).
The reports can be used to visualize and explore data, to communicate results, or to create interactive dashboards.
Datavzrd supports various rich visualizations out of the box and can be almost infinitely extended with custom visualizations, HTML and Javascript.
A key feature of Datavzrd reports is that they are portable, can be simply send around via mail or shared via cloud storage, without requiring a server infrastructure or any installed software on the viewing machine.

The examples used in this tutorial are based on an "Oscar winners" dataset, which has been chosen to demonstrate the capabilities of Datavzrd while being independent of any scientific domain.
In reality, Datavzrd can be used with any tabular data, e.g. from biomedicine, physics, social sciences, business, etc.

Setup
=====

There are two options for conducting this tutorial:

1. Install datavzrd on your own machine and conduct all steps there.
2. Use a Gitpod based environment, which allows you to conduct all exercises from within your web browser.

Run the tutorial via Gitpod
---------------------------

Gitpod enables performing the exercises via your browser—including all required software, for free and in the cloud.
In order to do this, simply open the predefined datavzrd-tutorial GitPod workspace in your browser.
GitPod provides you with a `Visual Studio Code <https://code.visualstudio.com>`_ development environment, which you can learn about in the linked documentation.

Run the tutorial on your own machine
------------------------------------

While datavzrd is platform independent, it is in general advisable to conduct such data analyses on a Unix-like system (`Linux <https://en.wikipedia.org/wiki/Linux>`_, `MacOS <https://www.apple.com/macos>`_).
In case you only have access to Microsoft Windows, note that Windows nowadays offers its own Linux subsystem (`WSL <https://learn.microsoft.com/en-us/windows/wsl/about>`_).
Check out the docs for installing WSL `here <https://learn.microsoft.com/en-us/windows/wsl/install>`_, enter WSL and proceed below as if you were on a plain Linux system.

First, install Datavzrd as instructed :ref:`here <installation>`.
Second, create a working directory for your tutorial excercises in some reasonable place of your file system and enter it.
In the following, we will always assume that you are in this working directory.
Create a subdirectory ``data`` and download the Oscar winners dataset via the following commands:

.. code-block:: bash

    mkdir data
    curl -L https://raw.githubusercontent.com/datavzrd/datavzrd/main/.examples/data/movies.csv > data/movies.csv
    curl -L https://raw.githubusercontent.com/datavzrd/datavzrd/main/.examples/data/oscars.csv > data/oscars.csv

The tutorial (and using Datavzrd in general) requires you to use a text editor for editing Datavzrd configuration files.
If you are an experienced developer and know all the formats and terms that are used here, you can of course use any editor you like and will have no issues.
If you are new to editing text files and using command line tools like Datavzrd, we recomment `Visual Studio Code (VSCode) <https://code.visualstudio.com>`_.
VSCode offers plugins which will help to write and edit such configuration files, in particular we recommend installing `indent-rainbow <https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow>`_, which simplifies getting the indentation in YAML_ files right.

Basic usage
===========

We will start with creating a simple report for a single table.
The table we will use is ``data/movies.csv``.
Datavzrd can be used via its `command line interface (CLI) <https://en.wikipedia.org/wiki/Command-line_interface>`_.
The basic structure of the datavzrd command is

.. code-block:: bash

    datavzrd config.yaml --output example-report

The first command line parameter (here ``config.yaml``) is a configuration file that specifies the data to be visualized and the visualizations to be used.
The second parameter (here ``--output myreport``) specifies the output directory for the generated report.
The output directory will contain the generated report as a main HTML file and a subdirectory with all required resources for displaying the report.

The configuration file is written in the so-called YAML_ format.
In this case, the format can be seen as a simple, structured, human readable way to specify how Datavzrd shall visualize the given tabular data.

.. note::

    Under the hood, Datavzrd delegates all of its visualization capabilities to the `Vega-Lite <https://vega.github.io/vega-lite>` library.
    This also means that often values passed to the configuration will stem from the vocabulary of Vega-Lite.
    Where this is the case, we will try to provide links to the respective Vega-Lite documentation.

Step 1: Create a minimal report
-------------------------------


We define a minimal configuration file as follows:

.. code-block:: yaml

    datasets:
      movies:
        path: data/movies.csv
    
    views:
      movies:
        dataset: movies
        render-table:
          columns:
            Rated:
              plot:
                heatmap:
                  scale: ordinal
                  color-scheme: category20

Save this configuration file as ``config.yaml`` in your working directory.
The file specifies that the table to be visualized is stored in the file ``data/movies.csv``.
There shall be a single view for this table, which renders the table while coloring the ``Rated`` column using a heatmap visualization.
We configure the heatmap to have an ordinal scale and to use the `category20 <https://vega.github.io/vega/docs/schemes/#categorical>`_ color scheme.

Next, we execute Datavzrd with this configuration file in order to generate our first report:

.. code-block:: bash

    datavzrd config.yaml --output example-report

The resulting report has the following structure:

.. code-block:: bash

    example-report/
    ├── index.html
    ├── movies
    │   ├── config.js
    │   ├── data
    │   │   └── data_1.js
    │   ├── functions.js
    │   ├── index_1.html
    │   └── plots
    │       └── plots.js
    └── static
        └── bundle.js

Open the main file, called ``index.html``, in your browser.
It contains a rendered version of the ``data/movies.csv`` table.
The ``Rated`` column is colored according to the heatmap configuration.
The report is interactive, meaning that you can, by clicking on corresponding icons on the column headers, sort the table, filter it, hide columns and show summary statistics.
Also note the "hamburger"-menu at the top right, which offers various view options.
Take your time to explore the interactive capabilities of this very minimal version of the report.

.. note::

    The report is self-contained and can be shared with others by simply compressing the output directory into a zip file and e.g. sending it around to sharing it via cloud storage.
    The report can be opened in any modern browser without requiring any additional software or server infrastructure.

Step 2: Add a report name and a description
-------------------------------------------

Reports become more transparent and understandable if they are self-descriptive.
For this purpose, Datavzrd offers the ability to provide a report-wide name (annotating the global topic of the report) and a description for each view.
We now extend our configuration from before (``config.yaml``) by defining a report name via adding the following to the top level of the configuration:

.. code-block:: yaml

    name: Oscars and movies

We also add a description by specifying the following as a child of the movies view, just below the dataset entry with the same indentation.
Description can make use of Markdown_ syntax for formatting text.

.. code-block:: yaml

    description: |
      Movies that won an **Oscar**.

Note the leading ``|`` in the description entry, which is a YAML_ operator that allows for multi-line text below (one indentation deeper).
Also note the ``**`` around the word "Oscar", which Markdown_ syntax for bold text.

The full configuration file now looks like this:

.. code-block:: yaml

    name: Oscars and movies

    datasets:
      movies:
        path: data/movies.csv
    
    views:
      movies:
        dataset: movies
        description: |
          Movies that won an **Oscar**.
        render-table:
          columns:
            Rated:
              plot:
                heatmap:
                  scale: ordinal
                  color-scheme: category20

Execute Datavzrd again with this updated configuration file:

.. code-block:: bash

    datavzrd config.yaml --output example-report

Open the main file, called ``index.html``, in your browser and check out the added name (top left) and description (above the table).
The description can also be hidden via the "x"-button at its top right, and opened again via the "hamburger"-menu.

.. note::

    In reality, descriptions should be as comprehensive as possible, allowing somebody viewing the report to understand the presented data without external help.
    This entails that one should consider explaining the content and interpretation of e.g. certain columns or the visualizations that have been applied.

Step 3: Add a second dataset
----------------------------

We now extend our report by adding the oscars table as a second dataset.

.. admonition:: Exercise

    1. Analogously to ``movies`` add a second entry to the ``datasets`` section of the configuration file.
    2. Add a second view to the ``views`` section that renders the oscars dataset as a table.
      Use the same heatmap configuration as for the ``Rated`` column of the movies table for the ``award`` column in the oscars table.
      Add a description to this view.

The full configuration file now looks like this:

.. code-block:: yaml

    name: Oscars and movies

    datasets:
      movies:
        path: data/movies.csv

      oscars:
        path: data/oscars.csv
    
    views:
      movies:
        dataset: movies
        description: |
          Movies that won an **Oscar**.
        render-table:
          columns:
            Rated:
              plot:
                heatmap:
                  scale: ordinal
                  color-scheme: category20

      oscars:
        dataset: oscars
        description: |
          This view shows **Oscar** awards.
        render-table:
          columns:
            award:
              plot:
                heatmap:
                  scale: ordinal
                  color-scheme: category20

Execute Datavzrd again with this updated configuration file:

.. code-block:: bash

    datavzrd config.yaml --output example-report

Open the main file, called ``index.html``, in your browser and check out the added oscars table.

Step 4: Link between movies and oscars
--------------------------------------

We now extend our report by adding a link between movies and oscars.
Datavzrd will automatically render link buttons into tables that are based on linked datasets, such that one can jump around between corresponding entries of the different tables.

Naturally, one can add a link between the ``movie`` column of the oscars dataset and the ``Title`` column of the movies dataset.
Add the following block to the oscars dataset, at the same indentation level as the path entry:

.. code-block:: yaml

    links:
      movie:
        column: movie
        table-row: movies/Title

Here, we express that any tabular view of the oscars dataset shall link each row to the corresponding row in the movies view based on the ``movie`` column in the oscars dataset and the matching ``Title`` column in the movies table view.

.. admonition:: Exercise

    Analogously, add a link between the ``Title`` column of the movies dataset and the ``movie`` column of the oscars table view to the movies dataset.

The full configuration file now looks like this:

.. code-block:: yaml

    name: Oscars and movies

    datasets:
      movies:
        path: data/movies.csv
        links:
          oscar:
            column: Title
            table-row: oscars/movie

      oscars:
        path: data/oscars.csv
        links:
          movie:
            column: movie
            table-row: movies/Title
    
    views:
      movies:
        dataset: movies
        description: |
          Movies that won an **Oscar**.
        render-table:
          columns:
            Rated:
              plot:
                heatmap:
                  scale: ordinal
                  color-scheme: category20

      oscars:
        dataset: oscars
        description: |
          This view shows **Oscar** awards.
        render-table:
          columns:
            award:
              plot:
                heatmap:
                  scale: ordinal
                  color-scheme: category20

Execute Datavzrd again with this updated configuration file:

.. code-block:: bash

    datavzrd config.yaml --output example-report

Open the main file, called ``index.html``, in your browser and check out the added link buttons that allow you to jump between corresponding entries of the tables.

Step 5: Add more column visualizations
--------------------------------------

We now extend our report by adding more visualizations for the columns of the tables.
