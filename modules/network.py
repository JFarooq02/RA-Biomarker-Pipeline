import requests
from pyvis.network import Network

def fetch_intact_interactions(gene_symbol):
 
 
    url = f"https://www.ebi.ac.uk/intact/ws/search/interactor/{gene_symbol}?format=tab25"
    response = requests.get(url)

    if response.status_code != 200:
        return []

    interactions = set()

    for line in response.text.splitlines()[1:]: 
        columns = line.split("\t")
        if len(columns) >= 2:
            try:
                gene_a = columns[0].split(":")[1]
                gene_b = columns[1].split(":")[1]
                interactions.add((gene_a, gene_b))
            except IndexError:
                continue  

    return list(interactions)


def visualize_gene_network(gene_list):
    """
    Builds and visualizes a gene interaction network using PyVis and IntAct API.

    Args:
        gene_list (list): List of gene symbols to visualize.

    Returns:
        pyvis.network.Network: Interactive network graph.
    """
    net = Network(height="500px", width="100%", bgcolor="#ffffff", font_color="black")
    added_nodes = set(gene_list)  

    for gene in gene_list:
        net.add_node(gene, label=gene, color='orange', title=f"Seed Gene: {gene}")
        interactions = fetch_intact_interactions(gene)

        for gene_a, gene_b in interactions:
            for g in (gene_a, gene_b):
                if g not in added_nodes:
                    net.add_node(g, label=g, title=f"Interactor: {g}")
                    added_nodes.add(g)
            net.add_edge(gene_a, gene_b)

    net.repulsion(node_distance=150)
    return net
