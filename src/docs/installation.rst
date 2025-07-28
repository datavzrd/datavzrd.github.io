.. _installation:

******************
Installation Guide
******************

Datavzrd can be installed in several ways. We recommend **Conda** as the preferred method due to ease of setup and integration of dependencies. To install **Conda** check their `installation guide <https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html>__`.

Conda
=====

To install Datavzrd via Conda, use one of the following commands:

.. code-block:: bash

    conda install -c conda-forge datavzrd

or

.. code-block:: bash

    mamba install -c conda-forge datavzrd

or

.. code-block:: bash

    micromamba install -c conda-forge datavzrd

This installs Datavzrd along with all its dependencies.

.. tip::

  To isolate Datavzrd in its own environment, you can create and activate a dedicated Conda environment:

  .. code-block:: bash
  
      conda create -n datavzrd -c conda-forge datavzrd
      conda activate datavzrd


Cargo
=====

If you prefer using Rust's native package manager, you can install Datavzrd using Cargo. Please note that Datavzrd depends on Python packages via `pyo3` and [`yte`](https://github.com/yte-template-engine/yte) and also various JavaScript libraries via `pnpm`. Therefore you must have the following installed beforehand:

- `Rust <https://rustup.rs>`__
- `Python <https://www.python.org>`__
- `pnpm <https://pnpm.io>`__
- `yte <https://github.com/yte-template-engine/yte>`__

Then install Datavzrd via Cargo:

.. code-block:: bash

    cargo install datavzrd

----

Once installed, you can run `datavzrd` from the command line to generate interactive reports from tabular data.

From Source
===========

To build Datavzrd from source, first clone the repository:

.. code-block:: bash

    git clone https://github.com/datavzrd/datavzrd
    cd datavzrd

Ensure all prequisites listed in the above Cargo section are installed an then build via:

.. code-block:: bash

    cargo build

This will compile Datavzrd. To run it with the alredy included example material in the repository run:

.. code-block:: bash

    cargo run .examples/example-config.yaml -o report

