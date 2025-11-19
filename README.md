# PhysioNet ECG Image Digitization - Repo

**Project:** Robust digitization of 12-lead ECG images into time-series.

## Overview
This repository contains code, experiments, and documentation for reproducing the models and analyses described in our PhysioNet / Kaggle competition entry.

## Repo structure
- `notebooks/` - exploratory notebooks and baseline runs
- `scripts/` - helper scripts for data loading, preprocessing, and submission checks
- `models/` - saved model weights (git-ignored)
- `.github/` - issue and PR templates + CI workflows
- `Dockerfile`, `requirements.txt` - reproducibility and environment

## Quickstart (local)
1. Clone: `git clone https://github.com/AdilShamim8/Digitization-of-ECG-Images.git`
2. Create venv: `python -m venv venv && source venv/bin/activate`
3. Install: `pip install -r requirements.txt`
4. Run data check: `python scripts/check_submission.py --sample sample_submission.csv --preds my_submission.csv`

## Citation
If you use this work, please cite the PhysioNet challenge and the ECG-Image-Kit toolkit.
