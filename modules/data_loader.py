# modules/data_loader.py

import pandas as pd

def read_gene_expression_data(file):
    """Read CSV into DataFrame."""
    return pd.read_csv(file)

def handle_gene_symbol_column(data):
    """Drop rows with missing GeneSymbol."""
    return data.dropna(subset=['GeneSymbol'])
