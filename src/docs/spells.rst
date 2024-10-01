
******
Spells
******

Spells provide reusable configuration snippets for **datavzrd**.
These spells simplify the process of creating reports by allowing users to define common configurations in a modular way. Users can easily pull spells from local files or remote URLs, facilitating consistency and efficiency in data visualization workflows.

Below is a list of all the available spells in the **datavzrd-spells** repository:

p-value
-------


This spell generates a heatmap visualization to represent the distribution of p-values or statistical significance in data.
The heatmap uses a linear color scale to map values to a gradient from green over white to organge.
The significance_threshold (e.g., p = 0.05) - a boundary between statistical significance and non-significance - can be adjusted dynamically based on the context or dataset.



Example:

.. code-block:: yaml



  render-table:
  columns:
    p-value:
      spell:
        url: v1.0.0/stats/p-value
        with:
          significance_threshold: 0.05


Authors:

Johannes Köster, Felix Wiegand


