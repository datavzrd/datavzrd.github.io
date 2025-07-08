#!/bin/bash
set -e

echo "Setting up Datavzrd tutorial environment..."

# Clean up workspace
find . -mindepth 1 -delete

# Create data directory and download example files
mkdir -p data
curl -L https://raw.githubusercontent.com/datavzrd/datavzrd/main/.examples/data/movies.csv -o data/movies.csv
curl -L https://raw.githubusercontent.com/datavzrd/datavzrd/main/.examples/data/oscars.csv -o data/oscars.csv

# Install micromamba
export MAMBA_ROOT_PREFIX="$HOME/micromamba"
curl -L micro.mamba.pm/install.sh | bash -s -- -b -p $MAMBA_ROOT_PREFIX
export PATH="$MAMBA_ROOT_PREFIX/bin:$PATH"

# Activate micromamba and install datavzrd
source ~/.bashrc
micromamba create -n datavzrd -c conda-forge datavzrd --yes
echo "micromamba activate datavzrd" >> ~/.bashrc

echo "alias show-report-url='echo https://0.0.0.0:8000/example-report'" >> ~/.bashrc

# Activate for current shell
source ~/.bashrc
micromamba activate datavzrd

echo "Setup complete!"
