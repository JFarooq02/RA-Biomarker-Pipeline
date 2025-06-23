# modulesRA/plots.py

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import networkx as nx

def create_volcano_plot(data, logFC_threshold=0.7, title="Volcano Plot"):
    """Create a matplotlib volcano plot and return the figure."""
    fig, ax = plt.subplots(figsize=(10, 6))

    data['Color'] = np.where(data['logFC'] < -logFC_threshold, 'blue',
                      np.where(data['logFC'] > logFC_threshold, 'red', 'black'))

    ax.scatter(data['logFC'], data['-log10(p-value)'], c=data['Color'], alpha=0.6)

    for _, row in data.iterrows():
        if row['Color'] in ['red', 'blue']:
            ax.annotate(row['GeneSymbol'], (row['logFC'], row['-log10(p-value)']),
                        textcoords="offset points", xytext=(5, 5), ha='center', fontsize=6)

    ax.set_title(title)
    ax.set_xlabel("logFC")
    ax.set_ylabel("-log10(p-value)")

    red_patch = mpatches.Patch(color='red', label='Up-regulated')
    blue_patch = mpatches.Patch(color='blue', label='Down-regulated')
    black_patch = mpatches.Patch(color='black', label='Not Significant')

    ax.legend(handles=[red_patch, blue_patch, black_patch])

    return fig

def plot_bar_from_dataframe(df, terms_list):
    """Create bar plot of adjusted p-values with gene labels."""
    fig, ax = plt.subplots(figsize=(10, 8))
    bars = ax.barh(range(len(df)), df['Adjusted_P_value'], color='orange')

    for bar, gene_label in zip(bars, df['Genes']):
        yval = bar.get_y() + bar.get_height() / 2
        ax.text(bar.get_width(), yval, gene_label, va='center', ha='left', fontsize=8)

    ax.set_yticks(range(len(df)))
    ax.set_yticklabels(terms_list)
    ax.set_xlabel('Adjusted P-value')
    ax.set_title('GO Term Enrichment Bar Plot')

    return fig

def plot_gene_network(gene_list):
    """Visualizes a simple gene interaction network."""
    G = nx.Graph()

    # Add nodes (genes)
    for gene in gene_list:
        G.add_node(gene)

    # Dummy edges for illustration (replace with real data later)
    for i in range(len(gene_list)):
        for j in range(i + 1, len(gene_list)):
            if i % 2 == 0 and j % 3 == 0:
                G.add_edge(gene_list[i], gene_list[j])

    # Draw network
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='orange', edge_color='gray', node_size=700, font_size=10)
    plt.title("Gene Interaction Network")
    plt.tight_layout()

    return plt.gcf()
