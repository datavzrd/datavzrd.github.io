********************************************
Integration with workflow management systems
********************************************

Snakemake
*********

Datavzrd integrates easily into any `Snakemake <https://snakemake.github.io>`__ workflow by using its own wrapper.

Snakemake's `datavzrd wrapper <https://snakemake-wrappers.readthedocs.io/en/latest/wrappers/datavzrd.html>`__ can be used in the following way:

.. code-block:: python

  rule datavzrd:
      input:
          # the config file may be a yte template, with access to input, params and wildcards
          # analogous to Snakemake's generic template support:
          # https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#template-rendering-integration
          # For template processing, __use_yte__: true has to be stated in the config file
          config="resources/{sample}.datavzrd.yaml",
          # optional files required for rendering the given config
          table="data/{sample}.tsv",
      params:
          extra="",
      output:
          report(
              directory("results/datavzrd-report/{sample}"),
              htmlindex="index.html",
              # see https://snakemake.readthedocs.io/en/stable/snakefiles/reporting.html
              # for additional options like caption, categories and labels
          ),
      log:
          "logs/datavzrd_report/{sample}.log",
      wrapper:
          "v3.13.4/utils/datavzrd"


Importantly, the ``report()`` marker instructs Snakemake to embed the Datavzrd report into the Snakemake report.
This way, Datavzrd's interative exploration capabilities are further enriched by the data provenance and reproducibility information as well as the result navigation features available in `Snakemake reports <https://snakemake.readthedocs.io/en/stable/snakefiles/reporting.html>`__.

Nextflow
********

Datavzrd is available as an `nf‑core module <https://nf-co.re/modules/datavzrd/>`__ for inclusion in Nextflow pipelines. It can be installed via:

.. code-block:: bash

  nf-core modules install datavzrd



