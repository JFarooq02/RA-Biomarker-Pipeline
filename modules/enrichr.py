# modules/enrichr.py

import gseapy as gp
import os
import pandas as pd

def perform_enrichr_analysis(gene_list, gene_sets='GO_Biological_Process_2023', organism='human'):
    """Run Enrichr and return result DataFrame."""
    try:
        enr = gp.enrichr(gene_list=gene_list, gene_sets=gene_sets, organism=organism)
        return enr.results[['Term', 'Adjusted P-value', 'Genes']].head(20)
    except Exception as e:
        print(f"Error in Enrichr analysis: {e}")
        return pd.DataFrame()

def get_manual_terms():
    """Return manually curated list of GO terms."""
    return [
        'Canonical Wnt Signaling Pathway (GO:0060070)',
        'Positive Regulation Of Phosphatidylinositol 3-Kinase Signaling (GO:0014068)',
        'Wnt Signaling Pathway (GO:0016055)',
        'Regulation Of Phosphatidylinositol 3-Kinase Signaling (GO:0014066)',
        'Hemopoiesis (GO:0030097)',
        'Lymphoid Progenitor Cell Differentiation (GO:0002320)',
        'Negative Regulation Of Membrane Protein Ectodomain Proteolysis (GO:0051045)',
        'Positive Regulation Of Fibroblast Apoptotic Process (GO:2000271)',
        'Regulation Of Fibroblast Apoptotic Process (GO:2000269)',
        'Regulation Of Inflammatory Response To Wounding (GO:0106014)',
        'Regulation Of MAPK Cascade (GO:0043408)',
        'Regulation Of Histone Acetylation (GO:0035065)',
        'Dendritic Cell Differentiation (GO:0097028)',
        'Negative Regulation Of Epidermal Growth Factor Receptor Signaling Pathway (GO:0042059)',
        'Heparan Sulfate Proteoglycan Biosynthetic Process (GO:0015012)',
        'Mononuclear Cell Differentiation (GO:1903131)',
        'Negative Regulation Of Response To Wounding (GO:1903035)',
        'Positive Regulation Of Phosphatidylinositol 3-Kinase Activity (GO:0043552)',
        'Hematopoietic Progenitor Cell Differentiation (GO:0002244)',
        'Chondrocyte Differentiation (GO:0002062)',
        'Positive Regulation Of Lipid Kinase Activity (GO:0090218)',
        'Negative Chemotaxis (GO:0050919)',
        'Negative Regulation Of Chemotaxis (GO:0050922)',
        'Mesenchymal Cell Migration (GO:0090497)',
        'Proteoglycan Biosynthetic Process (GO:0030166)',
        'Membrane Protein Proteolysis (GO:0033619)',
        'Regulation Of Phosphatidylinositol 3-Kinase Activity (GO:0043551)',
        'Establishment Of Spindle Orientation (GO:0051294)',
        'Negative Regulation Of Protein Kinase B Signaling (GO:0051898)',
        'Lymphocyte Proliferation (GO:0046651)',
        'Negative Regulation Of Proteolysis (GO:0045861)',
        'Lysosome Organization (GO:0007040)',
        'Regulation Of Cell-Cell Adhesion (GO:0022407)',
        'Regulation Of Cell-Substrate Adhesion (GO:0010810)'
    ]
