#!/usr/bin/env python3
"""Check submission format against sample_submission.csv"""
import argparse
import pandas as pd
import sys

def main(sample_path, preds_path):
    sample = pd.read_csv(sample_path)
    preds = pd.read_csv(preds_path)
    # Check columns
    if list(sample.columns) != list(preds.columns):
        print("ERROR: Column mismatch.")
        print("Sample cols:", sample.columns.tolist())
        print("Preds cols:", preds.columns.tolist())
        sys.exit(2)
    # Check row count
    if len(sample) != len(preds):
        print(f"ERROR: Row count mismatch. sample={len(sample)} pred={len(preds)}")
        sys.exit(2)
    # Check ids and types
    if not sample['id'].equals(preds['id']):
        print("ERROR: id column does not match sample order/values.")
        # Show first mismatches
        mismatches = sample['id'] != preds['id']
        print(preds.loc[mismatches].head())
        sys.exit(2)
    if preds.isnull().any().any():
        print("ERROR: Found NaNs in predictions.")
        sys.exit(2)
    print("Submission format looks OK (columns, rows, ids, no NaNs).")

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--sample', required=True)
    p.add_argument('--preds', required=True)
    args = p.parse_args()
    main(args.sample, args.preds)
