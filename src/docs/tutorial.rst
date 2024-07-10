.. _YAML: https://yaml.org
.. _Markdown: https://en.wikipedia.org/wiki/Markdown
.. _Javascript: https://en.wikipedia.org/wiki/JavaScript
.. _Vega-Lite: https://vega.github.io/vega-lite

***************
Getting started
***************

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

    desc: |
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
        desc: |
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
        desc: |
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
        desc: |
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
        desc: |
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
        desc: |
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

Step 5: Add Links to external resources
---------------------------------------

We now extend our report by adding more visualizations for the columns of the tables.
First, we add a Wikipedia and a Letterboxd link to every movie title in the movies table by adding an entry ``Title`` of the following form to the ``columns`` section of the movies table view:

.. code-block::yaml

    Title:
      link-to-url:
        Wikipedia:
          url: https://en.wikipedia.org/wiki/{value}
        Letterboxd:
          url: https://letterboxd.com/search/{value}

As can be seen, the ``link-to-url`` entry takes a map of keys and values, where the keys are the descriptive names of the links that shall be rendered and the values are URL patterns.
The URL patterns may contain a placeholder ``{value}``, which will be replaced by the actual value of the respective column entry.
Moreover, it is possible to refer to any other column value of the same row by using the column name as a placeholder.

In total, the updated configuration looks like this:

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
        desc: |
          Movies that won an **Oscar**.
        render-table:
          columns:
            Title:
              link-to-url:
                Wikipedia:
                  url: https://en.wikipedia.org/wiki/{value}
                Letterboxd:
                  url: https://letterboxd.com/search/{value}
            Rated:
              plot:
                heatmap:
                  scale: ordinal
                  color-scheme: category20

      oscars:
        dataset: oscars
        desc: |
          This view shows **Oscar** awards.
        render-table:
          columns:
            award:
              plot:
                heatmap:
                  scale: ordinal
                  color-scheme: category20

Execute Datavzrd again with this updated configuration file and see how the links are added to the Title column of the movies table view in the form of a dropdown menu.

.. node::

  If there would be only a single link, it would be rendered as a simple link on each column entry instead of a dropdown menu.

.. admonition:: Exercise

    1. Add a link to the oscars table that links the ``name`` column to the corresponding imDB search (use the URL pattern ``https://www.imdb.com/find/?q={value}``) page of the respective award.
    2. Modify the link to Wikipedia in the movies table such that it opens the page in a new tab. For this purpose, Datavzrd offers the possibility to add an entry ``new-window: true`` next to the ``url:`` entry of the ``link-to-url`` structure.

Step 6: Add a tick plot
-----------------------

In order to display numerical values in the context of their observed range, Datavzrd offers tick plots.
We will now add a tick plot for the ``age`` column of the oscars table, by adding an entry ``age`` of the following form to the ``columns`` section:

.. code-block::yaml

    age:
      plot:
        ticks:
          scale: linear

The ``scale`` of the tick plot can be chosen from the available `Vega-Lite continuous scales <https://vega.github.io/vega-lite/docs/scale.html#continuous-scales>`_.
In this case, we choose a linear scale, meaning that the distance between any two ticks in the plots is proportional to the distance between their underlying values.

The updated configuration looks like this:

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
        desc: |
          Movies that won an **Oscar**.
        render-table:
          columns:
            Title:
              link-to-url:
                Wikipedia:
                  url: https://en.wikipedia.org/wiki/{value}
                Letterboxd:
                  url: https://letterboxd.com/search/{value}
            Rated:
              plot:
                heatmap:
                  scale: ordinal
                  color-scheme: category20

      oscars:
        dataset: oscars
        desc: |
          This view shows **Oscar** awards.
        render-table:
          columns:
            award:
              plot:
                heatmap:
                  scale: ordinal
                  color-scheme: category20
            age:
              plot:
                ticks:
                  scale: linear

Execute Datavzrd again with this updated configuration file and see how the tick plot is added to the age column of the oscars table view.

.. admonition:: Exercise

    Analogously to tick plots, Datavzrd offers bar plots for numerical values.
    Add a bar plot for the ``imdbRating`` column of the movies table (the syntax is the same, just use ``bars`` instead of ``ticks``).

Step 7: Adding derived columns and hiding columns
-------------------------------------------------

Sometimes, tabular data might contain information that should rather be visualized in a different way.
In the oscars table, there are columns ``birth_d``, ``birth_mo``, and ``birth_y``, denoting the birthdate of the actress or actor.
We will now add a derived column ``birth_season`` that displays the birtdate as an icon that represents the season.
For such tasks, Datavzrd offers the possibility do use custom functions (written in Javascript_).
We add a new section ``add-columns`` with the following content to the ``render-table`` section of the oscars table view:

.. code-block::yaml

    add-columns:
      birth_season:
        value: |
          function(row) {
            const month = row['birth_mo'];
            if (month >= 3 && month <= 5) {
              return '🌷';
            } else if (month >= 6 && month <= 8) {
              return '🌞';
            } else if (month >= 9 && month <= 11) {
              return '🍂';
            } else {
              return '❄️';
            }
          }

In other words, we add a column named ``birth_season`` that calculates its value via a Javascript_ function that accesses the column ``birht_mo`` from the same row, and returns a season-representing icon (which here are in fact a special unicode/font characters) depending on the month.

Let us assume that only the season is relevant in this context.
Datavzrd offers the ability to hide irrelevant columns in two ways: not displaying them completely, or displaying them upon request.
We will now hide the columns ``birth_d`` and ``birth_mo`` in the oscars table view and display the year upon request.
For this purpose, we add entries for the three columns to the ``columns`` section of the oscars table view:

.. code-block::yaml
    columns: 
      birth_d:
        display-mode: hidden
      birth_mo:
        display-mode: hidden
      birth_y:
        display-mode: detail

For the former two, ``display-mode: hidden`` is used, which means that the columns are not displayed at all.
For the latter, ``display-mode: detail`` is used, which means that the value appears with all others of the same dsiplay mode when a ``+`` button at the beginning of the row is clicked.

The updated configuration looks like this:

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
        desc: |
          Movies that won an **Oscar**.
        render-table:
          columns:
            Title:
              link-to-url:
                Wikipedia:
                  url: https://en.wikipedia.org/wiki/{value}
                Letterboxd:
                  url: https://letterboxd.com/search/{value}
            Rated:
              plot:
                heatmap:
                  scale: ordinal
                  color-scheme: category20

      oscars:
        dataset: oscars
        desc: |
          This view shows **Oscar** awards.
        render-table:
          columns:
            award:
              plot:
                heatmap:
                  scale: ordinal
                  color-scheme: category20
            age:
              plot:
                ticks:
                  scale: linear
            birth_d:
              display-mode: hidden
            birth_mo:
              display-mode: hidden
            birth_y:
              display-mode: detail
          add-columns:
            birth_season:
              value: |
                function(row) {
                  const month = row['birth_mo'];
                  if (month >= 3 && month <= 5) {
                    return '🌷';
                  } else if (month >= 6 && month <= 8) {
                    return '🌞';
                  } else if (month >= 9 && month <= 11) {
                    return '🍂';
                  } else {
                    return '❄️';
                  }
                }

Execute Datavzrd again with this updated configuration file and explore the introduced changes.

Step 8: Adding a custom plot to render cells of a column
--------------------------------------------------------

Beyond the offered built-ins like tick and bar plots, Datavzrd offers the ability to specify custom Vega-Lite_ plots.
For learning how to write Vega-Lite_, we refer to the `Vega-Lite tutorial <https://vega.github.io/vega-lite/tutorials/getting_started.html>`_.
Here, we simply assume that this knowledge is already present, and aim to display wins and nominations of each actor and actress as a pie chart.
Note that this information is present in the column ``overall_wins_and_overall_nominations`` (in the form ``m/n`` with ``m`` being the wins and ``n`` being the nominations), see the rendered Datavzrd report from any previous step.
For this purpose, we add an entry ``overall_wins_and_overall_nominations`` of the following form to the ``columns`` section of the oscars table view:

.. code-block::yaml

    overall_wins_and_overall_nominations:
      custom-plot:
        data: |
          function(value, row) {
            const [wins, nominations] = value.split("/");
            return [
              {"category": "wins", "amount": wins},
              {"category": "nominations", "amount": nominations},
            ]
          }
        spec: |
          {
            "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
            "height": 25,
            "width": 25,
            "mark": {"type": "arc", "tooltip": true},
            "encoding": {
              "theta": {"field": "amount", "type": "quantitative"},
              "color": {"field": "category", "type": "nominal"}
            },
            "config": {
              "legend": {"disable": true}
            }
          }

This definition does two things.
First, it uses the column value to construct a data representation that is suitable for Vega-Lite_.
Similar to the previous step, this works again by specifying a Javascript_ function.
Second, it defines a Vega-Lite_ plot which maps the categories (wins and nominations) to colors and the amount to arcs in the pie chart.

The updated configuration looks like this:

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
        desc: |
          Movies that won an **Oscar**.
        render-table:
          columns:
            Title:
              link-to-url:
                Wikipedia:
                  url: https://en.wikipedia.org/wiki/{value}
                Letterboxd:
                  url: https://letterboxd.com/search/{value}
            Rated:
              plot:
                heatmap:
                  scale: ordinal
                  color-scheme: category20

      oscars:
        dataset: oscars
        desc: |
          This view shows **Oscar** awards.
        render-table:
          columns:
            award:
              plot:
                heatmap:
                  scale: ordinal
                  color-scheme: category20
            age:
              plot:
                ticks:
                  scale: linear
            birth_d:
              display-mode: hidden
            birth_mo:
              display-mode: hidden
            birth_y:
              display-mode: detail
            overall_wins_and_overall_nominations:
              custom-plot:
                data: |
                  function(value, row) {
                    const [wins, nominations] = value.split("/");
                    return [
                      {"category": "wins", "amount": wins},
                      {"category": "nominations", "amount": nominations},
                    ]
                  }
                spec: |
                  {
                    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
                    "height": 25,
                    "width": 25,
                    "mark": {"type": "arc", "tooltip": true},
                    "encoding": {
                      "theta": {"field": "amount", "type": "quantitative"},
                      "color": {"field": "category", "type": "nominal"}
                    },
                    "config": {
                      "legend": {"disable": true}
                    }
                  }
          add-columns:
            birth_season:
              value: |
                function(row) {
                  const month = row['birth_mo'];
                  if (month >= 3 && month <= 5) {
                    return '🌷';
                  } else if (month >= 6 && month <= 8) {
                    return '🌞';
                  } else if (month >= 9 && month <= 11) {
                    return '🍂';
                  } else {
                    return '❄️';
                  }
                }

Execute Datavzrd again with this updated configuration file and explore the introduced changes.

Step 9: Add a plot view
-----------------------

Apart from displaying table views, Datavzrd offers the ability to define so-called plot views, which only contain a custom plot instead of a table.
Again, plots can be defined using Vega-Lite_.
To illustrate this feature, let us specify a view that displays the relation between the year of the Oscar award (column ``oscar_yr``) and the age of the actress or actor (column ``age``).
We add the following entry as a new view below the oscars table view in the configuration file (of course at the same indentation level).

.. code-block:: yaml

    year_vs_age:
      dataset: oscars
      desc: |
        Relationship between year of the Oscar award and the age of the actress/actor.
      render-plot:
        spec: |
          {
            "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
            "mark": {"type": "circle", "tooltip": true},
            "encoding": {
              "x": {"field": "oscar_yr", "type": "temporal"},
              "y": {"field": "age", "type": "quantitative"},
              "color": {"field": "award", "type": "nominal"}
            }
          }

The updated configuration file looks like this:

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
        desc: |
          Movies that won an **Oscar**.
        render-table:
          columns:
            Title:
              link-to-url:
                Wikipedia:
                  url: https://en.wikipedia.org/wiki/{value}
                Letterboxd:
                  url: https://letterboxd.com/search/{value}
            Rated:
              plot:
                heatmap:
                  scale: ordinal
                  color-scheme: category20

      oscars:
        dataset: oscars
        desc: |
          This view shows **Oscar** awards.
        render-table:
          columns:
            award:
              plot:
                heatmap:
                  scale: ordinal
                  color-scheme: category20
            age:
              plot:
                ticks:
                  scale: linear
            birth_d:
              display-mode: hidden
            birth_mo:
              display-mode: hidden
            birth_y:
              display-mode: detail
            overall_wins_and_overall_nominations:
              custom-plot:
                data: |
                  function(value, row) {
                    const [wins, nominations] = value.split("/");
                    return [
                      {"category": "wins", "amount": wins},
                      {"category": "nominations", "amount": nominations},
                    ]
                  }
                spec: |
                  {
                    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
                    "height": 25,
                    "width": 25,
                    "mark": {"type": "arc", "tooltip": true},
                    "encoding": {
                      "theta": {"field": "amount", "type": "quantitative"},
                      "color": {"field": "category", "type": "nominal"}
                    },
                    "config": {
                      "legend": {"disable": true}
                    }
                  }
          add-columns:
            birth_season:
              value: |
                function(row) {
                  const month = row['birth_mo'];
                  if (month >= 3 && month <= 5) {
                    return '🌷';
                  } else if (month >= 6 && month <= 8) {
                    return '🌞';
                  } else if (month >= 9 && month <= 11) {
                    return '🍂';
                  } else {
                    return '❄️';
                  }
                }
      year_vs_age:
          dataset: oscars
          desc: |
            Relationship between year of the Oscar award and the age of the actress/actor.
          render-plot:
            spec: |
              {
                "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
                "mark": {"type": "circle", "tooltip": true},
                "encoding": {
                  "x": {"field": "oscar_yr", "type": "temporal"},
                  "y": {"field": "age", "type": "quantitative"},
                  "color": {"field": "award", "type": "nominal"}
                }
              }

As always run datavzrd on this configuration to obtain an updated report.
Investigate the resulting new view, and be suprised (or not) about the systematic age difference between actors and actresses and how that reflects some of the issues we have in the society.

With this, we are at the end of the Datavzrd tutorial.
Naturally, there are numerous options and features that we did not cover here.
For a comprehensive overview, we refer to the `Datavzrd homepage <https://datavzrd.github.io>`_ and the documentation that can be reached from there.