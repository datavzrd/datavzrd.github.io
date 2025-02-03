******************
Contribution Guide
******************

We welcome contributions to Datvazrd! Whether you're fixing bugs, adding new features, improving documentation, or writing tests, your help is appreciated. Please fork the repository and create a new branch for your fix or feature and create a PR for a review of your changes.

Getting started
===============

Before you can fully build Datvazrd make sure to install ``pnpm``. This is needed for the build script located in ``build.rs`` to install the necessary js dependencies. After succesfully compiling the binary with ``cargo build`` you can run Datavzrd with the example data and configuration with the following command:

.. code-block:: shell

    cargo run -- .examples/example-config.yaml -o out

This creates a directory named ``out`` where the generated report will be located. Open it by clicking on the file named ``index.html``.
.

Repository structure
====================

There are two directories that contain the essential source code of Datavzrd. 

- ``src`` contains all Rust related code that is used for the generation of the report.
- ``web`` contains Datavzrds own javascript library that is used when a generated report is openend in a browser.
