*************
Configuration
*************

Datavzrd allows the user to easily customize it's interactive HTML report via a config file.
When generating large reports, templating yaml files can be a bit tricky. We advise using `yte <https://github.com/yte-template-engine/yte>`_ for easy yaml templating with python expressions.

name
====

``name`` allows the user to optionally set a name for the generated report that will be heading all resulting tables and plots.

default-view
============

``default-view`` allows the user to optionally specify a view for the generated report that will be shown when opening the index file.

max-in-memory-rows
==================

``max-in-memory-rows`` defines the threshold for the maximum number of rows in memory. If the given dataset exceeds the threshold the data will be split across multiple pages and their html files. Defaults to 1000 rows.

aux-libraries
=============

``aux-libraries`` allows to add one or more js libraries via cdn links for usage in :ref:`render-html`. The keyword expects a list of urls that link to the js libraries.

webview-controls
================

``webview-controls`` allows to turn on sharing individual rows via a link with the data encoded into a url pointing to a webview that hosts a static version of datavzrd at https://datavzrd.github.io. Note that when using the link the row data can temporarily occur (in base64-encoded form) in the server logs of the given webview host. Defaults to ``false``.

datasets
========

``datasets`` defines the different datasets of the report. This is also the place to define links between your individual datasets.

.. list-table::
   :header-rows: 1

   * - keyword
     - explanation
     - default
   * - path
     - The path of the CSV/TSV file
     - 
   * - separator
     - The delimiter of the file
     - ,
   * - headers
     - Number of header rows in the file
     - 1
   * - `links <#links>`_
     - Configuration linking between items
     - 
   * - offer-excel
     - Whether to offer the dataset as an excel worksheet.
     - false


views
=====

``views`` consists of all different CSV/TSV views (table or plot) that should be included in the resulting report. If neither ``render-table`` nor ``render-plot`` is present, datavzrd will render the given file as a table. Each item definition can contain these values:

.. list-table::
   :header-rows: 1

   * - keyword
     - explanation
     - default
   * - desc
     - A description that will be shown in the report. `Markdown <https://github.github.com/gfm/>`_ is allowed and will be rendered to proper HTML. It is also possible to add latex formulas with ```latex ... ```.
     - 
   * - dataset
     - The name of the corresponding dataset to this view defined in `datasets <#datasets>`_
     - 
   * - datasets
     - Key-value pairs to include multiple datasets into a `render-plot <#render-plot>`_ configuration. Key must be the name of the dataset in the given vega-lite specswhile the value needs to be the name of a dataset defined in `datasets <#datasets>`_.
     - 
   * - page-size
     - Number of rows per page
     - 20
   * - `render-table <#render-table>`_
     - Configuration of individual column rendering
     - 
   * - `render-plot <#render-plot>`_
     - Configuration of a single plot
     - 
   * - `render-html <#render-html>`_
     - Configuration of a custom html view
     - 
   * - hidden
     - Whether or not the view is shown in the menu navigation
     - false
   * - max-in-memory-rows
     - Overwrites the global settings for `max-in-memory-rows <#max-in-memory-rows>`_


render-table
============

``render-table`` contains definitions for a table view

.. list-table::
   :header-rows: 1

   * - keyword
     - explanation
   * - `columns <#columns>`_
     - Configuration of columns
   * - `add-columns <#add-columns>`_
     - Configuration of additionally generated columns
   * - `headers <#headers>`_
     - Configuration of the additional headers


columns
=======

``columns`` contains individual configurations for each column that can either be adressed by its name defined in the header of the CSV/TSV file, its 0-based index (e.g. ``index(5)`` for the 6th column), a range expression (e.g. ``range(5, 10)`` for the 5th column to 9th column) or a regular expression (e.g. ``"regex('prob:.+')"`` for matching all columns starting with ``prob:``\ ):

.. list-table::
   :header-rows: 1

   * - keyword
     - explanation
     - default
     - possible values
   * - `link-to-url <#link-to-url>`_
     - You can either specify only a single url or key value pairs with a name as the key and the url as the value that will then be accessible via a dropdown. Use the special keyword ``custom-content`` to change the title of the link or the dropdown with a javascript function looking like this: ``function my_link_title(value, row) { return 'Open link to ' + value }``
     - 
     - 
   * - custom
     - Applies the given js function to render column content. The parameters of the function are similar to the ones defined `here <https://bootstrap-table.com/docs/api/column-options/#formatter>`_
     - 
     - 
   * - label
     - Allows to specify a label that will be used in the table header instead of the column title in the given dataset.
     - 
     - 
   * - custom-path
     - Allows to specify a path to a file that contains a js function similar to custom. The file should only contain one js function (the name of the function shouldn't matter) and should look like `this <https://github.com/koesterlab/datavzrd/blob/main/.examples/specs/time-formatter.js>`_. The given path is relative to the directory you are currently in and running datavzrd from.
     - 
     - 
   * - `custom-plot <#custom-plot>`_
     - Renders a custom vega-lite plot to the corresponding table cell
     - 
     - 
   * - `plot <#plot>`_
     - Renders a vega-lite plot defined with `plot <#plot>`_ to the corresponding table cell
     - 
     - 
   * - ellipsis
     - Shortens values to the first *n* given characters with the rest hidden behind a popover. With *n = 0* the cell will be empty and the value will only be shown in a popover.
     - 
     - 
   * - optional
     - Allows to have a column specified in render-table that is actually not present.
     - false
     - true, false
   * - display-mode
     - Allows to hide columns from views by setting this to ``hidden`` or have a column only in `detail view <https://examples.bootstrap-table.com/#options/detail-view.html#view-source>`_ by setting this to ``detail``.
     - normal
     - detail, normal, hidden
   * - precision
     - Allows to specify the precision of floats. It expects an integer specifying the decimal places that will be shown. Values smaller than $1 / (10^{precision})$ will be displayed in scientific notation with the same number of decimal places.
     - 2
     - 
   * - plot-view-legend
     - Specifies whether the column in the plot-view should include a legend or not.
     - false
     - true, false


add-columns
===========

``add-columns`` allows to generate new columns out of the existing dataset.

.. list-table::
   :header-rows: 1

   * - keyword
     - explanation
     - default
     - possible values
   * - value
     - A javascript function taking a row of the dataset as the parameter that returns the value for the newly generated column. A value named ``age`` may be accessed in the function via ``function my_new_col(row) { return row.age * 2 }`` for example.
     - 
     - 
   * - `link-to-url <#link-to-url>`_
     - You can either specify only a single url or key value pairs with a name as the key and the url as the value that will then be accessible via a dropdown. Use the special keyword ``custom-content`` to change the title of the link or the dropdown with a javascript function looking like this: ``function my_link_title(value, row) { return 'Open link to ' + value }``
     - 
     - 
   * - `custom-plot <#custom-plot>`_
     - Renders a custom vega-lite plot to the corresponding table cell
     - 
     - 
   * - display-mode
     - Allows to hide columns from views by setting this to ``hidden`` or have a column only in `detail view <https://examples.bootstrap-table.com/#options/detail-view.html#view-source>`_ by setting this to ``detail``.
     - normal
     - detail, normal, hidden


headers
=======

``headers`` contains definitions for additional header rows. Each row can be accessed with its index starting at ``1`` (\ ``0`` is the first header row that can't be customized).

.. list-table::
   :header-rows: 1

   * - keyword
     - explanation
   * - label
     - Allows to add an additional label to the corresponding header
   * - `plot <#plot>`_
     - Renders a vega-lite plot defined with `plot <#plot>`_ to the corresponding table cell (currently only the `heatmap <#heatmap>`_ type is supported in header rows)
   * - display-mode
     - Allows to hide the header row by setting this to ``hidden``.
   * - ellipsis
     - Shortens values to the first *n* given characters with the rest hidden behind a popover. With *n = 0* the cell will be empty and the value will only be shown in a popover.


render-plot
===========

``render-plot`` contains individual configurations for generating a single plot from the given CSV/TSV file.

.. list-table::
   :header-rows: 1

   * - keyword
     - explanation
   * - spec
     - A schema for a vega lite plot that will be rendered to a single view
   * - spec-path
     - The path to a file containing a schema for a vega lite plot that will be rendered to a single view. The given path is relative to the directory you are currently in and running datavzrd from.

.. _render-html:

render-html
===========

``render-html`` contains individual configurations for generating a single custom view where a global variable ``data`` with the dataset in json format can be accessed in the given js file. The rendered view contains a ``<div id="canvas">`` that can then be manipulated with the given script. By default, the div uses the full width and centers its contents. Of course, the divs CSS can be overwritten via Javascript. jQuery is already available, any other necessary Javascript libraries can be loaded via `aux-libraries <#aux-libraries>`_.

.. list-table::
   :header-rows: 1

   * - keyword
     - explanation
   * - script-path
     - A path to a js file that has access to the dataset and can manipulate the given canvas of the rendered view


links
=====

``links`` can configure linkouts between multiple items.

.. list-table::
   :header-rows: 1

   * - keyword
     - explanation
     - default
   * - column
     - The column that contains the value used for the linkout
     - 
   * - table-row
     - Renders as a linkout to the other table highlighting the row in which the gene column has the same value as here
     - 
   * - view
     - Renders as a link to the given view
     - 
   * - optional
     - Allows missing values in linked tables
     - false


custom-plot
===========

``custom-plot`` allows the rendering of customized vega-lite plots per cell.

.. list-table::
   :header-rows: 1

   * - keyword
     - explanation
     - default
   * - data
     - A function to return the data needed for the schema (see below) from the content of the column cell
     - 
   * - spec
     - The vega-lite spec for a vega plot that is rendered into each cell of this column
     - 
   * - spec-path
     - The path to a file containing a schema for a vega-lite plot that is rendered into each cell of this column
     - 
   * - vega-controls
     - Whether or not the resulting vega-lite plot is supposed to have action-links in the embedded view
     - false


link-to-url
===========

``link-to-url`` allows rendering a link to a given url with {value} replaced by the value of the table.

.. list-table::
   :header-rows: 1

   * - keyword
     - explanation
     - default
   * - url
     - The url where {value} is replaced by the value of the table. Other values of the same row can be accessed by their column header (e.g. {age} for a column named age).
     - 
   * - new-window
     - Whether or not the rendered link will be opened in a new window or not
     - true


plot
====

``plot`` allows the rendering of either a `tick-plot <https://vega.github.io/vega-lite/docs/tick.html>`_ for numeric values or a heatmap for nominal values.

.. list-table::
   :header-rows: 1

   * - keyword
     - explanation
   * - `ticks <#ticks>`_
     - Defines a `tick-plot <https://vega.github.io/vega-lite/docs/tick.html>`_ for numeric values
   * - `heatmap <#heatmap>`_
     - Defines a heatmap for numeric or nominal values
   * - `bars <#bars>`_
     - Defines a `bar-plot <https://vega.github.io/vega-lite/docs/bar.html>`_ for numeric values


ticks
=====

``ticks`` defines the attributes of a `tick-plot <https://vega.github.io/vega-lite/docs/tick.html>`_ for numeric values.

.. list-table::
   :header-rows: 1

   * - keyword
     - explanation
   * - scale
     - Defines the `scale <https://vega.github.io/vega-lite/docs/scale.html>`_ of the tick plot
   * - domain
     - Defines the domain of the tick plot. If not present datavzrd will automatically use the minimum and maximum values for the domain
   * - aux-domain-columns
     - Allows to specify a list of other columns that will be additionally used to determine the domain of the tick plot. Regular expression (e.g. ``"regex('prob:.+')"`` for matching all columns starting with ``prob:``\ ) are also supported as well as range expressions (e.g. ``range(5, 10)`` for the 5th column to 9th column).
   * - `color <#color>`_
     - Defines the color of the tick plot


heatmap
=======

``heatmap`` defines the attributes of a heatmap for numeric or nominal values.

.. list-table::
   :header-rows: 1

   * - keyword
     - explanation
     - default
   * - type
     - Corresponds to the `type <https://vega.github.io/vega-lite/docs/type.html>`_ definition of vega-lite. Either ``nominal``\ , ``ordinal`` or ``quantitative``. This overrides any given scale and color-scheme/range configuration and provides a quick way to setup any heatmap configuration. Using ``nominal`` or ``ordinal`` results in an ordinal scale with the color-scheme ``category20`` while ``quantitative`` results in a linear scale using the ``blues`` scheme.
     - 
   * - scale
     - Defines the `scale <https://vega.github.io/vega-lite/docs/scale.html>`_ of the heatmap
     - 
   * - color-scheme
     - Defines the `color-scheme <https://vega.github.io/vega/docs/schemes/#categorical>`_ of the heatmap for nominal values
     - 
   * - range
     - Defines the color range of the heatmap as a list
     - 
   * - domain
     - Defines the domain of the heatmap as a list
     - 
   * - domain-mid
     - Allows defining the mid point of a given numeric domain. If a domain is specified it must be of length 2, otherwise datavzrd will automatically set the outer domain from the given column of the dataset. The given color range array must be of length 3 where the middle entry corresponds to the domain-mid value.
     - 
   * - clamp
     - Defines whether values exceeding the given domain for continuous scales will be clamped to the minimum or maximum value.
     - true
   * - aux-domain-columns
     - Allows to specify a list of other columns that will be additionally used to determine the domain of the heatmap. Regular expression (e.g. ``"regex('prob:.+')"`` for matching all columns starting with ``prob:``\ ) are also supported.
     - 
   * - custom-content
     - Allows to render custom content into any heatmap cell (while using the actual cell content for the heatmap color). Requires a ``function(value, row)`` that returns the text value that will be displayed in the cell.
     -


bars
====

``bars`` defines the attributes of a `bar-plot <https://vega.github.io/vega-lite/docs/bar.html>`_ for numeric values.

.. list-table::
   :header-rows: 1

   * - keyword
     - explanation
   * - scale
     - Defines the `scale <https://vega.github.io/vega-lite/docs/scale.html>`_ of the bar plot
   * - domain
     - Defines the domain of the bar plot. If not present datavzrd will automatically use the minimum and maximum values for the domain
   * - aux-domain-columns
     - Allows to specify a list of other columns that will be additionally used to determine the domain of the bar plot. Regular expression (e.g. ``"regex('prob:.+')"`` for matching all columns starting with ``prob:``\ ) are also supported.
   * - `color <#color>`_
     - Defines the color of the bar plot


color
=====

``color`` defines the attributes of a color scale definition for tick and bar plots

.. list-table::
   :header-rows: 1

   * - keyword
     - explanation
   * - scale
     - Defines the `scale <https://vega.github.io/vega-lite/docs/scale.html>`_ of the tick or bar plot
   * - domain
     - Defines the domain of the color scale of the tick or bar plot. If not present datavzrd will automatically use the minimum and maximum values for the domain
   * - domain-mid
     - Defines a mid point of the domain. The argument is passed on straight to the `vega-lite domain defintion <https://vega.github.io/vega-lite/docs/scale.html#domain>`_
   * - range
     - Defines the color range of the tick or bar plot as a list

