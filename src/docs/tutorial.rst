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

The configuration file is written in the so-called `YAML <https://yaml.org>`_ format.
In this case, the format can be seen as a simple, structured, human readable way to specify how Datavzrd shall visualize the given tabular data.

.. note::

    Under the hood, Datavzrd delegates all of its visualization capabilities to the `Vega-Lite <https://vega.github.io/vega-lite>` library.
    This also means that often values passed to the configuration will stem from the vocabulary of Vega-Lite.
    Where this is the case, we will try to provide links to the respective Vega-Lite documentation.

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

Next we execute Datavzrd with this configuration file in order to generate our first report:

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