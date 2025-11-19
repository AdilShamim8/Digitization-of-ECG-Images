"""Starter utilities to load Kaggle PhysioNet ECG competition files locally.

Note: Kaggle API or manual download required. This is a skeleton file to extend.
"""
import pandas as pd
import os

def load_sample_submission(path='sample_submission.csv'):
    return pd.read_csv(path)

def load_train_csv(path='train.csv'):
    return pd.read_csv(path)

if __name__ == '__main__':
    print('Available files in cwd:')
    print('\n'.join(os.listdir('.')))
