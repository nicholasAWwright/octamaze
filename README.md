# octamaze
Python code for finding all assembly permutations of Pavel's Puzzles' Octamaze puzzle pieces. (Note that there is only one unique assembly configuration, but this is repeated due to the algorithm used to solve puzzle assembly)

## Usage
- Install conda3: https://docs.conda.io/en/latest/miniconda.html
- Launch Anaconda Prompt and cd to repo directory
- Create a new conda environment from yml using: `conda create -f environment.yml` or `conda create -f environment-pypy.yml` (note there are CPython and PyPy versions. PyPy runs much faster)
- Activate the ensuing environment: `conda activate octamaze` or `conda activate octamaze-pypy`
- Run the script with: `python ocatmaze.py` or `pypy pctamaze.py`, depending on the environment (note that using the former command in the PyPy environment seems to also invoke PyPy as the interpreter.)
