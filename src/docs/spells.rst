
******
Spells
******

Spells provide reusable configuration snippets for **datavzrd**.
These spells simplify the process of creating reports by allowing users to define common configurations in a modular way. Users can easily pull spells from local files or remote URLs, facilitating consistency and efficiency in data visualization workflows.

Column spells configure a single column, while view spells configure an entire view, e.g. for the output of a specific tool.

Below is a list of all the available spells in the `datavzrd-spells repository <https://github.com/datavzrd/datavzrd-spells>`__.
For adding new spells, please see the instructions in the `datavzrd-spells repository <https://github.com/datavzrd/datavzrd-spells>`__.


Column spells
=============


boolean
-------

.. image:: https://img.shields.io/badge/code-github-blue
  :target: https://github.com/datavzrd/datavzrd-spells/tree/v1.9.0/logic/boolean

.. image:: https://img.shields.io/badge/example-report-green
  :target: https://datavzrd.github.io/datavzrd-spells/logic/boolean/index.html

This spell visualizes boolean values via colored +/- symbols.


Example
^^^^^^^

.. code-block:: yaml



  render-table:
    columns:
      some boolean column:
        spell:
          url: v1.9.0/logic/boolean
          with:
            # specify which values should be interpreted as true or false
            true_value: "true"
            false_value: "false"

Authors
^^^^^^^

Johannes Köster




alleles
-------

.. image:: https://img.shields.io/badge/code-github-blue
  :target: https://github.com/datavzrd/datavzrd-spells/tree/v1.9.0/med/alleles

.. image:: https://img.shields.io/badge/example-report-green
  :target: https://datavzrd.github.io/datavzrd-spells/med/alleles/index.html

This spell visualizes alleles (e.g. A, T, G, C or any longer string composed out of these nucleotides) using merged pills with color-coded bases.
Coloring is based on the same color scheme used by alignoth.


Example
^^^^^^^

.. code-block:: yaml



  render-table:
    columns:
      some clinical column containing alleles:
        spell:
          url: v1.9.0/med/alleles

Authors
^^^^^^^

Felix Wiegand




clin-sig
--------

.. image:: https://img.shields.io/badge/code-github-blue
  :target: https://github.com/datavzrd/datavzrd-spells/tree/v1.9.0/med/clin-sig

.. image:: https://img.shields.io/badge/example-report-green
  :target: https://datavzrd.github.io/datavzrd-spells/med/clin-sig/index.html

This spell visualizes the clinical significance, given in clinvar significance terms (https://www.ncbi.nlm.nih.gov/clinvar/)
The values should be given in a column consisting of strings and separated by ','


Example
^^^^^^^

.. code-block:: yaml



  render-table:
    columns: 
      some clinical significance column:
        spell:
          url: v1.9.0/med/clin-sig

Authors
^^^^^^^

Benjamin Orlik




genomic-coordinates
-------------------

.. image:: https://img.shields.io/badge/code-github-blue
  :target: https://github.com/datavzrd/datavzrd-spells/tree/v1.9.0/med/genomic-coordinates

.. image:: https://img.shields.io/badge/example-report-green
  :target: https://datavzrd.github.io/datavzrd-spells/med/genomic-coordinates/index.html

This spell visualizes genomic coordinates in a structured and visually enhanced way.
It formats the coordinates with color-coded pills for reference and alternate bases, making it easy to read and interpret genomic variant data.
The values should be given in a column with the format "<chromosome>:<reference><coordinates><alternate>" (e.g., "6:G29942560A").


Example
^^^^^^^

.. code-block:: yaml



  render-table:
    columns: 
      some clinical column containing genomic coordinates:
        spell:
          url: v1.9.0/med/genomic-coordinates

Authors
^^^^^^^

Felix Wiegand




p-value
-------

.. image:: https://img.shields.io/badge/code-github-blue
  :target: https://github.com/datavzrd/datavzrd-spells/tree/v1.9.0/stats/p-value

.. image:: https://img.shields.io/badge/example-report-green
  :target: https://datavzrd.github.io/datavzrd-spells/stats/p-value/index.html

This spell generates a heatmap visualization to represent the distribution of p-values or statistical significance in data.
The heatmap uses a linear color scale to map values to a gradient from green over white to organge.
The significance\_threshold (e.g., p = 0.05) - a boundary between statistical significance and non-significance - can be adjusted dynamically based on the context or dataset.


Example
^^^^^^^

.. code-block:: yaml



  render-table:
    columns:
      some p-value column:
        spell:
          url: v1.9.0/stats/p-value
          with:
            significance_threshold: 0.05

Authors
^^^^^^^

Johannes Köster, Felix Wiegand




separated-links
---------------

.. image:: https://img.shields.io/badge/code-github-blue
  :target: https://github.com/datavzrd/datavzrd-spells/tree/v1.9.0/stats/separated-links

.. image:: https://img.shields.io/badge/example-report-green
  :target: https://datavzrd.github.io/datavzrd-spells/stats/separated-links/index.html

This spell separates a cell on a given separator (default: comma) and creates clickable links for each element. Each element can be formatted as a URL using a configurable URL template with ``${value}`` as a placeholder.
Perfect for lists of genes, proteins, or other entities that should link to external resources.


Example
^^^^^^^

.. code-block:: yaml



  render-table:
    columns:
      genes:
        spell:
          url: v1.9.0/stats/separated-links
          with:
            separator: ","
            url_template: "https://www.genecards.org/cgi-bin/carddisp.pl?gene=${value}"

Authors
^^^^^^^

Adrian Prinz




text
----

.. image:: https://img.shields.io/badge/code-github-blue
  :target: https://github.com/datavzrd/datavzrd-spells/tree/v1.9.0/utils/text

.. image:: https://img.shields.io/badge/example-report-green
  :target: https://datavzrd.github.io/datavzrd-spells/utils/text/index.html

This spell allows to split long text after a certain number of characters (always at whitespace).


Example
^^^^^^^

.. code-block:: yaml



  render-table:
    columns:
      text:
        spell:
          url: v1.9.0/utils/text
          with:
            # specify how many characters should be used per line
            chars_per_line: 50

Authors
^^^^^^^

Felix Wiegand




View spells
===========


clusterprofiler
---------------

.. image:: https://img.shields.io/badge/code-github-blue
  :target: https://github.com/datavzrd/datavzrd-spells/tree/v1.9.0/tools/clusterprofiler

.. image:: https://img.shields.io/badge/example-report-green
  :target: https://datavzrd.github.io/datavzrd-spells/tools/clusterprofiler/index.html

This spell renders the results of an over-representation analysis with `clusterProfiler <https://bioconductor.org/packages/clusterProfiler>`__ (e.g. ``enrichGO()``, ``enrichKEGG()``, ``enricher()`` or ``compareCluster()``) as a table.
Results of gene set enrichment analyses like ``gseGO()`` or ``gseKEGG()`` have different columns and are not supported.
GO, Reactome, KEGG and WikiPathways ids link to the respective databases, fold enrichment and gene counts are shown as bars and adjusted p-values are colored by ``significance_threshold``.
The genes of each term are shown in the detail view as pills linking to NCBI Gene, restricted to ``organism`` if given (e.g. ``Homo sapiens``).
These links need gene symbols as obtained with ``readable = TRUE`` or ``setReadable()``.
The spell expects the columns of ``as.data.frame()`` on the result.


Example
^^^^^^^

.. code-block:: yaml



  spell:
    url: v1.9.0/tools/clusterprofiler
    with:
      significance_threshold: 0.05
      organism: Homo sapiens

Authors
^^^^^^^

Felix Wiegand




deseq2
------

.. image:: https://img.shields.io/badge/code-github-blue
  :target: https://github.com/datavzrd/datavzrd-spells/tree/v1.9.0/tools/deseq2

.. image:: https://img.shields.io/badge/example-report-green
  :target: https://datavzrd.github.io/datavzrd-spells/tools/deseq2/index.html

This spell renders the results of a differential expression analysis with `DESeq2 <https://bioconductor.org/packages/DESeq2>`__ as a table.
Log2 fold changes are shown as a diverging heatmap that saturates at ``fold_change_color_limit`` (default 3, i.e. an 8-fold change), adjusted p-values are colored by ``significance_threshold`` and genes link to Ensembl.
The threshold should match the ``alpha`` used in ``results()``, which defaults to 0.1 in DESeq2.
DESeq2 itself does not write files, the spell expects the columns of ``results()`` or ``lfcShrink()`` as written by e.g. ``write.csv()``, with the Ensembl gene ids in the first column, named or not.
If the table also contains gene symbols, e.g. added with ``mapIds()`` of the ``AnnotationDbi`` package, their column can be given as ``symbol_column``.
``baseMean`` and ``log2FoldChange`` are required, ``lfcSE``, ``stat``, ``pvalue``, ``padj`` and ``svalue`` are shown if present, so shrunken fold changes from apeglm or ashr work as well.
A ``signed_pi_value`` column (``-log10(pvalue) * log2FoldChange``, see `Xiao et al. 2014 <https://doi.org/10.1093/bioinformatics/btr671>`__) is shown as a diverging heatmap if present.
Combine it with the volcano-plot spell in another view to get a clickable volcano plot linking to the rows of this table.
Such links need a named gene column, e.g. by writing ``data.frame(gene = rownames(res), res)``.


Example
^^^^^^^

.. code-block:: yaml



  spell:
    url: v1.9.0/tools/deseq2
    with:
      significance_threshold: 0.05
      fold_change_color_limit: 3
      symbol_column: symbol

Authors
^^^^^^^

Felix Wiegand




seurat-markers
--------------

.. image:: https://img.shields.io/badge/code-github-blue
  :target: https://github.com/datavzrd/datavzrd-spells/tree/v1.9.0/tools/seurat-markers

.. image:: https://img.shields.io/badge/example-report-green
  :target: https://datavzrd.github.io/datavzrd-spells/tools/seurat-markers/index.html

This spell renders marker genes found with ``FindAllMarkers()`` or ``FindMarkers()`` of `Seurat <https://satijalab.org/seurat>`__ (version 4 or later) as a table.
Average log2 fold changes are shown as a diverging heatmap that saturates at ``fold_change_color_limit`` (default 3), adjusted p-values are colored by ``significance_threshold``, clusters are colored and genes link to NCBI Gene, restricted to ``organism`` if given (e.g. ``Homo sapiens``).
An additional column shows the fraction of cells expressing the gene in the tested group (``pct.1``) next to the cells it is compared to (``pct.2``).
``FindMarkers()`` only stores genes as row names, so add them as a column before writing, e.g. ``markers$gene <- rownames(markers)``.


Example
^^^^^^^

.. code-block:: yaml



  spell:
    url: v1.9.0/tools/seurat-markers
    with:
      significance_threshold: 0.05
      fold_change_color_limit: 3
      organism: Homo sapiens

Authors
^^^^^^^

Felix Wiegand




volcano-plot
------------

.. image:: https://img.shields.io/badge/code-github-blue
  :target: https://github.com/datavzrd/datavzrd-spells/tree/v1.9.0/visualization/volcano-plot

.. image:: https://img.shields.io/badge/example-report-green
  :target: https://datavzrd.github.io/datavzrd-spells/visualization/volcano-plot/index.html

This spell renders a volcano plot of the results of a differential expression or abundance analysis, plotting the log2 fold change against the negative log10 p-value.
The columns holding them are given as ``fold_change_column`` and ``p_value_column``, an optional ``id_column`` is shown in the tooltip.
For `DESeq2 <https://bioconductor.org/packages/DESeq2>`__ these are e.g. ``log2FoldChange`` and ``padj``, for edgeR ``logFC`` and ``FDR`` and for limma ``logFC`` and ``adj.P.Val``.
Rows below ``significance_threshold`` and beyond ``fold_change_threshold`` (default 0, drawn as dashed lines if set) are colored by the direction of regulation.
The x-axis is centered at zero, the plot can be zoomed and panned and rows without a fold change or p-value are left out.
The ``label_top`` (default 10) rows with the highest π score (absolute fold change times negative log10 p-value) are labeled, as well as the comma separated ``label_genes``.
Instead of π, the rows can be ranked by the absolute value of a given ``rank_column``, e.g. a precomputed signed π value.
Labels are taken from ``label_column`` (e.g. gene symbols), falling back to ``id_column`` for empty values.
p-values of zero are drawn one order of magnitude above the smallest non-zero one, while the tooltip shows the actual value.
When plotting s-values from ``lfcShrink()`` with apeglm or ashr, a ``significance_threshold`` of 0.005 is common.
If the plot stays empty, check that the given column names exist in the dataset.
For DESeq2, plotting shrunken fold changes from ``lfcShrink()`` avoids that genes with low counts dominate the x-axis.
Points can link to the corresponding table row (e.g. of the deseq2 spell) via a link defined for the dataset, here pointing to the view ``results`` showing the table:


.. code-block:: yaml

   datasets:
     results:
       path: results.tsv
       links:
         gene details:
           column: gene_id
           table-row: results/gene_id


Passing ``link: gene details`` to the spell then makes the points clickable.


Example
^^^^^^^

.. code-block:: yaml



  spell:
    url: v1.9.0/visualization/volcano-plot
    with:
      id_column: gene_id
      label_column: symbol
      fold_change_column: log2FoldChange
      p_value_column: padj
      significance_threshold: 0.05
      fold_change_threshold: 1
      label_top: 10
      label_genes: FKBP5,ZBTB16

Authors
^^^^^^^

Felix Wiegand


