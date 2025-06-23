import streamlit as st
import pandas as pd
import modules.data_loader as data_loader
import modules.filtering as filtering
import modules.plots as plots
import modules.enrichr as enrichr
import modules.network as network
import streamlit.components.v1 as components

# Page Config 
st.set_page_config(page_title="RA Biomarker Identifier", layout="wide")

# Styling 
st.markdown("""
    <style>
    body {
        background-color: #003366;
        color: white;
    }
    .reportview-container {
        background: #003366;
        color: white;
    }
    .stApp {
        background-color: #003366;
        color: white;
    }
    .section-header {
        background-color: #004080;
        padding: 10px;
        border-radius: 6px;
        font-size: 18px;
        font-weight: bold;
        color: white;
        margin-bottom: 10px;
    }
    .dataframe th, .dataframe td {
        border: 1px solid white;
        padding: 5px;
    }
    .warning-text {
        background-color: #ffcc00;
        color: black;
        padding: 10px;
        border-radius: 5px;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    button:hover {
        background-color: #3366cc !important;
        color: white !important;
    }
    .stButton > button {
        background-color: white !important;
        color: black !important;
        font-weight: bold;
        border-radius: 5px;
        padding: 8px 16px;
    }
    .stButton > button:hover {
        background-color: #3366cc !important;
        color: white !important;
    }
    div[data-testid="stNotificationContent"] {
        color: white;
    }
    div.stAlert {
        color: white !important;
        background-color: #FFFFFF !important;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Title 
st.title("Biomarker Identification for Rheumatoid Arthritis")

# STEP 1: Data Upload 
uploaded_file = st.file_uploader("Upload your Gene Expression CSV file", type=["csv"])

if uploaded_file:
    df = data_loader.read_gene_expression_data(uploaded_file)
    df = data_loader.handle_gene_symbol_column(df)
    st.markdown('<div class="section-header">Loaded and Cleaned Data</div>', unsafe_allow_html=True)
    st.dataframe(df)

    # STEP 2: Filtering 
    filtered = filtering.filter_data_by_condition(df)
    filtered = filtering.copy_filtered_data(filtered)
    logfc_filtered = filtering.filter_data_by_logFC(filtered)
    st.markdown('<div class="section-header">Filtered Data (logFC & p-value)</div>', unsafe_allow_html=True)
    st.dataframe(logfc_filtered)

    # STEP 3: Volcano Plot
    st.markdown('<div class="section-header">Volcano Plot</div>', unsafe_allow_html=True)
    volcano_fig = plots.create_volcano_plot(filtered)
    st.pyplot(volcano_fig)

    # STEP 4: Gene Ranking 
    ranked = filtering.add_rank_column(logfc_filtered)
    sorted_genes = filtering.sort_and_extract_ranking(ranked)
    gene_list = filtering.extract_gene_symbols(sorted_genes)
    st.markdown('<div class="section-header">Top Genes</div>', unsafe_allow_html=True)
    st.dataframe(sorted_genes)

    # STEP 5: Enrichment 
    st.markdown('<div class="section-header">GO Term Enrichment (Enrichr)</div>', unsafe_allow_html=True)
    enrichr_result = enrichr.perform_enrichr_analysis(gene_list)
    st.dataframe(enrichr_result)

    # STEP 6: Gene Network 
    st.markdown('<div class="section-header">Gene Interaction Network (IntAct API)</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="warning-text">
        ⚠ Interactions are based on <b>IntAct</b>, which may be incomplete or biased towards well-studied genes.<br>
        ⚠ Some genes may show no interactions if not available in IntAct.<br>
        ⚠ Raw interaction data; biological significance is not filtered.<br>
        ⚠ This visualization is exploratory and not definitive proof of interactions.
        </div>
        """, unsafe_allow_html=True
    )

    st.markdown('<p style="color:white; font-weight:bold;">Select number of top genes for network</p>', unsafe_allow_html=True)
    num_genes = st.slider("", min_value=3, max_value=len(gene_list), value=5)

    if st.button("Show Gene Network"):
        net = network.visualize_gene_network(gene_list[:num_genes])
        net.save_graph('gene_network.html')
        components.html(open('gene_network.html', 'r', encoding='utf-8').read(), height=550)

    #STEP 7: Enrichment Bar Plot 
    
    st.markdown('<div class="section-header">Upload RA(Relevant).csv for Enrichment Bar Plot</div>', unsafe_allow_html=True)

    st.markdown('<p style="color:white; font-weight:bold;">Upload \'RA(Relevant).csv\' to generate the bar plot for significant genes relevant to the disease</p>', unsafe_allow_html=True)
    ra_file = st.file_uploader("", type=["csv"])

    if ra_file:
        ra_df = pd.read_csv(ra_file)
        extracted = filtering.extract_columns(ra_df)
        terms_list = enrichr.get_manual_terms()
        bar_fig = plots.plot_bar_from_dataframe(extracted, terms_list)
        st.pyplot(bar_fig)
    else:
        st.info("ℹ Please upload 'RA(Relevant).csv' to generate the bar plot.")
