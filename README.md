# Landau Levels

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14568540.svg)](https://doi.org/10.5281/zenodo.14568540)

Numerical simulation in an *Advanced Quantum Mechanics* course of the *Engineering Physics* degree.

## Contents

This repository contains the code elaborated in December 2023 for an advanced quantum mechanics numerical laboratory. There are several scripts in this repository, all of which use the library `landau/simulator.py` to compute the wave function and the density function of the `n`-th Landau level.

The lab report, which shows and discusses the generated plots, is located at ```Documents/Lab Report.pdf```

## Clone

First, make sure you have installed ```git``` on your system (info on how to install [here](https://github.com/git-guides/install-git)). Then, run ```git clone https://github.com/bfrangi/landau-levels.git``` to clone this repository into your current working directory.

## Requirements

To run this code on your system you will need:

- Python 3.

- Python packages listed in `requirements.txt`. These can be installed by running `pip install -r requirements.txt` in the main project folder.

## Run

Run the simulations with:
```
python3 landau-levels.py
```

## Cite this repository

```
@software{bernat_frangi_2024_14568540,
  author       = {Bernat Frangi},
  title        = {bfrangi/landau-levels},
  month        = 12,
  year         = 2024,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.14568540},
  url          = {https://doi.org/10.5281/zenodo.14568540},
}
```
