.. _YAML: https://yaml.org
.. _YTE: https://github.com/yte-template-engine/yte
.. _Python: https://www.python.org

********
Overview
********

This advanced tutorial builds directly on the :doc:`basic tutorial <tutorial>` and continues from the code produced in its final step.
If you have not yet completed the basic tutorial, we recommend doing so first, as all examples here assume familiarity with the foundations introduced there.

The focus of this tutorial is on advanced usage, in particular templating your configuration via the YTE_ template engine, and extending your specifications with more powerful customization options.

Setup
=====

We will extend our datasets with more information about each oscar winning movie. In particular we will add one full table per movie containing information about the companies involved in producing this movie.
This means we will end up with quite a few tables.
To fetch all these we will run the following curl command that downloads and extracts the compressed data:

.. code-block:: bash

    curl -L https://raw.githubusercontent.com/datavzrd/datavzrd.github.io/main/resources/companies.zip | unzip -d data -

Our data directory should now include a directory named ``companies`` with one csv file per movie named based on its imdbID.

Step 1: Adding the tables to the report
=======================================

Since our movies dataset contain more than 180 movies, adding one table per movie will result in a lot of manual typing and makes the configuration file large and difficult to maintain.
To avoid this, we will use the YTE_ template engine to generate the configuration file dynamically.
YTE_ allows us to use Python_ expressions within a YAML_ file while still maintaining a valid YAML syntax.
As our configuration now becomes a template, we should rename it to clearly indicate its purpose.
We can do that using our IDE with right-clicking on the file and renaming it to `config.yte.yaml` or running the following command:

.. code-block:: bash

    mv config.yaml config.yte.yaml

Before we can start using YTE_ we need to install it. We can do this by running the following command:

.. code-block:: bash

    conda install -c conda-forge yte

Next up we can add the new tables to the report. We will do that by adding the following section to or config file `config.yte.yaml`:

.. code-block:: yaml

    __definitions__:
    - import re, pathlib
    - tt_numbers = [re.match(r"(tt\d+)_", f.name).group(1) for f in pathlib.Path("data/companies").glob("tt*_companies.csv")]

    name: Oscars and movies

    default-view: oscars

    datasets:
    ?for movie in tt_numbers:
        ?f"{movie}":
        path: ?f"data/companies/{movie}_companies.csv"

    views:
      ?for movie in tt_numbers:
        ?f"{movie}":
          dataset: ?movie
          desc: ?f"All companies involved in the making of {movie}"


To break these changes down let us start with ``__definitions__:``. This special YTE_ keyword allows us to define variables that can be used within the template. In this case we are importing the ``re`` and ``pathlib`` modules and defining a list of movie IDs we parse from the file names located in the `data/companies` directory.
Within our ``datasets`` definition we can now use the ``tt_numbers`` variable to generate the table names and paths dynamically for each movie.

To render the template we simply have to call YTE_ via the command line:

.. code-block:: bash

    yte < config.yte.yaml > config.yaml


Now look into the generated `config.yaml` file we can see that the table names and paths have been generated dynamically for each movie.
The configuration is now ready to be used with datavzrd to generate the report:

.. code-block:: bash

    datavzrd config.yaml --output example-report --overwrite-output


Have a look at the generated report to see how very few lines added that many datasets and views to the report.


Step 2: Adding a heatmap with a custom color palette and legend
===============================================================

Let us now bring some color into our report by adding a heatmap with a custom color palette. This can be done by explicitly specifying a domain and a range of colors for a column.
Using the ``legend`` keyword, we can also add a legend for the column to the description of our view.
Add the following ``heatmap`` definition to the ``company_type`` column:

.. code-block:: yaml

    views:
      ?for movie in tt_numbers:
        ?f"{movie}":
          dataset: ?movie
          desc: ?f"All companies involved in the making of {movie}"
          render-table:
            columns:
              company_type:
                plot:
                  heatmap:
                    scale: ordinal
                    domain: ["distribution", "sales", "production", "specialEffects", "miscellaneous"]
                    range: ["blue", "green", "red", "yellow", "cyan"]
                    legend:
                      title: "Company Type"


Re-render the template using YTE_ as well as the report using the previous commands and inspect the changes.


Step 3: Linking the detailed views to the main table
====================================================

Since each movie has its own detailed view about the involved companies it makes sense to link them to the main table. This can be done by adding a ``links`` keyword to dataset definition of our ``movies`` table:

.. code-block:: yaml

    datasets:
    movies:
        path: data/movies.csv
        links:
        oscar:
            column: Title
            table-row: oscars/movie
        companies:
            column: imdbID
            view: "{value}"


After re-runnning YTE_ and Datvazrd open the movies view in the report and use the linkout in the most right column to jump to the corresponding company view for a movie of your choice.

Step 4: Hiding the company view from the main menu
===================================================

If you havent already, have a look into the view menu of the report and see how our company views take up a lot of space in the menu. We can actually hide them by adding a ``hidden`` keyword to the view definition:

.. code-block:: yaml

  views:
    ?for movie in tt_numbers:
      ?f"{movie}":
        dataset: ?movie
        desc: ?f"All companies involved in the making of {movie}"
        hidden: true
        render-table:
          columns:
            company_type:
              plot:
                heatmap:
                  scale: ordinal
                  domain: ["distribution", "sales", "production", "specialEffects", "miscellaneous"]
                  range: ["blue", "green", "red", "yellow", "cyan"]
                  legend:
                    title: "Company Type"


Re-render the temaplte and report using the previous command and inspect the changes.
