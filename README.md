# octamaze
Python code for finding all assembly permutations of Pavel's Puzzles' Octamaze puzzle pieces. (Note that there is only one unique assembly configuration, but this is repeated due to the algorithm used to solve puzzle assembly)

## Prerequisites
1. Install mambaforge (this installs Anaconda Prompt with mamba as a package manager, and defaults the install repo to conda-forge): https://github.com/conda-forge/miniforge#mambaforge
    * Install as user in default directory
    * Create start menu shortcuts
    * Add to PATH
    * Register as default Python
    * Clear package cache upon completion
2. clone this repository locally

## Usage (CPython Interpreter [slower])
- Launch Anaconda Prompt and cd to repo directory
- Create a new conda environment from yml using: `mamba env create -f environment.yml` or `conda env create -f environment-pypy.yml`
- Activate the ensuing environment: `conda activate octamaze`
- Run the script with: `python octamaze.py`

## Usage (PyPy Interpreter [faster])
- Launch Anaconda Prompt and cd to repo directory
- Create a new conda environment from yml using: `conda env create -f environment-pypy.yml`
- Activate the ensuing environment: `conda activate octamaze-pypy`
- Run the script with: `pypy octamaze.py`

## Parallelized Code (Fastest)
- Repeat the steps above and substitute `octamaze-par.py` when using the interpreter to call the script
- E.g. `python ocatmaze-par.py` or `python octamaze-par.py`
- The PyPy interpreter is still faster