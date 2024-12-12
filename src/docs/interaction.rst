***********
Interaction
***********

This section gives a short overview on how to interact with the generated datavzrd report and explains further options like URL parameters that can be used to integrate the report in various ways.

Understanding and Using the Output Report
------------------------------------------

When Datavzrd generates a report, it creates a folder containing:

- An `index.html` file, which serves as the entry point to the report.
- Subdirectories for each view defined in the configuration, such as `movies` and `oscars`.
- A subdirectory named `static` containing static resources needed for the report.

Opening `index.html` will redirect you to a specific view. The view to display is determined by either:

- Automatic selection.
- The `default_view` keyword specified in the configuration file.

Accessing Specific Views
------------------------

You can directly open a specific view by appending a `view` parameter to the `index.html` URL. For example:

.. code-block:: bash

   path/to/report/index.html?view=movies

This opens the `movies` view. Any additional URL parameters are passed through to the view for further use.

Highlighting Values in Views
----------------------------

To highlight specific values in table columns within a view, you can use the following URL parameters:

- `highlight_value`: The value to highlight.
- `highlight_column`: The column where the value should be highlighted.

For example:

.. code-block:: bash

   path/to/report/oscars/index_1.html?highlight_value=Jezebel&highlight_column=movie

This highlights the value `Jezebel` in the `movie` column of the `oscars` view.

Combining Parameters
--------------------

Highlighting parameters can be combined with the `index.html` URL, as all parameters are passed through to the specific view. For example:

.. code-block:: bash

   path/to/report/index.html?view=oscars&highlight_value=Jezebel&highlight_column=movie

This opens the `oscars` view and highlights the value `Jezebel` in the `movie` column.
