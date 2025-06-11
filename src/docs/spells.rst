
******
Spells
******

Spells provide reusable configuration snippets for **datavzrd**.
These spells simplify the process of creating reports by allowing users to define common configurations in a modular way. Users can easily pull spells from local files or remote URLs, facilitating consistency and efficiency in data visualization workflows.

Below is a list of all the available spells in the `datavzrd-spells repository <https://github.com/datavzrd/datavzrd-spells>`__.
For adding new spells, please see the instructions in the `datavzrd-spells repository <https://github.com/datavzrd/datavzrd-spells>`__.


p-value
=======

.. image:: https://img.shields.io/badge/code-github-blue
  :target: https://github.com/datavzrd/datavzrd-spells/tree/v1.3.0/stats/p-value

This spell generates a heatmap visualization to represent the distribution of p-values or statistical significance in data.
The heatmap uses a linear color scale to map values to a gradient from green over white to organge.
The significance\_threshold (e.g., p = 0.05) - a boundary between statistical significance and non-significance - can be adjusted dynamically based on the context or dataset.


Example
-------

.. code-block:: yaml



  render-table:
    columns:
      some p-value column:
        spell:
          url: v1.3.0/stats/p-value
          with:
            significance_threshold: 0.05

Authors
-------

Johannes Köster, Felix Wiegand




genomic-coordinates
===================

.. image:: https://img.shields.io/badge/code-github-blue
  :target: https://github.com/datavzrd/datavzrd-spells/tree/v1.3.0/med/genomic-coordinates

This spell visualizes genomic coordinates in a structured and visually enhanced way.
It formats the coordinates with color-coded pills for reference and alternate bases, making it easy to read and interpret genomic variant data.
The values should be given in a column with the format "<chromosome>\:<reference><coordinates><alternate>" (e.g., "6\:G29942560A").


Example
-------

.. code-block:: yaml



  render-table:
    columns: 
      some clinical column containing genomic coordinates:
        spell:
          url: v1.3.0/med/genomic-coordinates

Authors
-------

Felix Wiegand




clin-sig
========

.. image:: https://img.shields.io/badge/code-github-blue
  :target: https://github.com/datavzrd/datavzrd-spells/tree/v1.3.0/med/clin-sig

This spell visualizes the clinical significance, given in clinvar significance terms (https\://www.ncbi.nlm.nih.gov/clinvar/)
The values should be given in a column consisting of strings and separated by ','


Example
-------

.. code-block:: yaml



  render-table:
    columns: 
      some clinical significance column:
        spell:
          url: v1.3.0/med/clin-sig

Authors
-------

Benjamin Orlik




boolean
=======

.. image:: https://img.shields.io/badge/code-github-blue
  :target: https://github.com/datavzrd/datavzrd-spells/tree/v1.3.0/logic/boolean

This spell visualizes boolean values via colored +/- symbols.


Example
-------

.. code-block:: yaml



  render-table:
    columns:
      some boolean column:
        spell:
          url: v1.3.0/logic/boolean
          with:
            # specify which values should be interpreted as true or false
            true_value: "true"
            false_value: "false"

Authors
-------

Johannes Köster


