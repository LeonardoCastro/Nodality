# Who is driving the conversation?

This is the repository with all the publicly available* data and analysis scripts for the research paper: " Who is driving the conversation? Studying the nodality of British MPs and journalists in social networks".

This respository consists of three different main parts: The `classifier/` folder, the `data/` folder and the `notebooks/` folder. We also include a small installation guide to enable a local `conda` environment.

## Index
- 1. [Installation](#1-installation)
- 2. [Classifier](#2-classifier)
- 3. [Data](#3-data)
- 4. [Analysis](#4-analysis)
- 5. [Contact](#5-contact)

## 1. Installation

The package is written in Python (version: 3.8). We recommend that the installation is made inside a virtual environment and to do this, one can use `conda` (recommended in order to control the Python version).

### Using conda

The tool `conda`, which comes bundled with Anaconda has the advantage that it lets us specify the version of Python that we want to use. Python=3.8 is required.

After locating in the local github folder, like `cd $PATH$` e.g. `Documents/Local_Github/nodality`, a new environment can be created with

```bash
$ conda env create -f environment.yaml
```

The environment's name will be `nodality`. The environment must be activated before using it with

```bash
$ conda activate nodality
```

## 2. Classifier

We use a weak supervision classifier based on [(Ratner et al, 2019)](https://ojs.aaai.org/index.php/AAAI/article/view/4403). The classifier can be found in `classifier.py`, while the accompanying labeling functions can be reviewed in `labeling_functions.py`. A confusion matrix of the classifier can be reviews in [`confusion_matrix.csv`]

## 3. Data

The data presented in `data/` consists on the activity time series of journalists and MPs from January 14, 2022, to January 13, 2023. 

The labels used are:
- 1 for the Russia-Ukraine War
- 2 for the COVID-19 pandemic
- 5 for the Cost of Living Crisis
- 6 for Brexit

We also present the network measurements for all the different combinations of (out-degree centrality, in-degree centrality, eigenvector centrality, betweenness centrality, hubs, authority, funnel bandwidth, amplification bandwith) in `data/clusters/`. The latter two measurements are introduced in the paper.


## 4. Analysis

The `notebooks/` folder consists of different `jupyter notebooks` to obtain the different Figures and Tables of the paper. As such, each `notebook` is named as the Figure or Table that intends to reproduce. The `notebooks` make use of the two `python` scripts, `analysis_labels.py` and `helper_functions.py`


## 5. Contact

- Leonardo Castro-Gonzalez - lmcastrogonzalez@turing.ac.uk
- Sukankana Chakraborty - schakraborty@turing.ac.uk
- Helen Margetts - helen.margetts@oii.ox.ac.uk
- Hardik Rajpal - hrajpal@turing.ac.uk
- Daniele Guariso - dguariso@turing.ac.uk
- Jonathan Bright - jbright@turing.ac.uk


