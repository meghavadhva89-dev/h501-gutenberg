# h501-gutenberg

Exercise 3: Project Gutenberg

This repository contains code and a notebook for Exercise 3. Key points:

- `tt_gutenberg` is a small Python package with helpers to list Project Gutenberg author aliases.
- `gutenberg.ipynb` demonstrates reading the TidyTuesday Gutenberg dataset and plotting top aliases using pandas and seaborn.

How to run

1. Create and activate the conda environment (example):

```powershell
conda create -n h501-env python=3.11 -y
conda activate h501-env
pip install -r requirements.txt
```

2. Download the full dataset locally (optional, recommended):

```powershell
mkdir data
$csvUrl = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv'
Invoke-WebRequest -Uri $csvUrl -OutFile .\data\gutenberg_authors.csv
```

3. Open `gutenberg.ipynb` in VS Code or Jupyter, select the `Python (h501-gutenberg)` kernel and run the cells. The notebook will prefer `data/gutenberg_authors.csv` if present and otherwise fall back to `data/sample_gutenberg.csv` included here.

Style and checks

- Code follows PEP8 style. Run flake8 to verify:

```powershell
pip install flake8
flake8 tt_gutenberg --max-line-length=88
```

- Run tests with pytest:

```powershell
pytest -q
```
