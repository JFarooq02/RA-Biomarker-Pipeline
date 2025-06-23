# modules/filtering.py

import numpy as np
import pandas as pd

def filter_data_by_condition(data, pval_threshold=0.01):
    """Filter rows where p-value < threshold."""
    return data[data['p.value'] < pval_threshold]

def copy_filtered_data(data):
    """Add -log10(p-value) column."""
    data = data.copy()
    data['-log10(p-value)'] = -np.log10(data['p.value'])
    return data

def filter_data_by_logFC(data, logFC_threshold=0.7):
    """Filter based on log fold change."""
    return data[np.abs(data['logFC']) > logFC_threshold]

def add_rank_column(df):
    """Create rank column using logFC and p-value."""
    df = df.copy()
    df['rank'] = df['logFC'] * -np.log10(df['p.value'])
    return df

def sort_and_extract_ranking(df):
    """Sort by rank and return Gene + Rank."""
    df = df.rename(columns={'GeneSymbol': 'Gene', 'rank': 'Rank'})
    sorted_df = df.sort_values(by='Rank', ascending=False)
    return sorted_df[['Gene', 'Rank']].reset_index(drop=True)

def extract_gene_symbols(df):
    """Extract gene names as list."""
    return df['Gene'].tolist()

def extract_columns(df):
    """Extract specific columns from enrichment CSV."""
    return df[['Adjusted_P_value', 'Genes']]
