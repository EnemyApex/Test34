import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import io
from fpdf import FPDF
from pagerank import pagerank
from utils import generate_graph, get_adjacency_matrix, plot_graph_plotly

# ... garde tout le code d'avant ...

def create_pdf_report(df, n_nodes, n_edges, n_iter, damping, graph_type):
    pdf = FPDF()
    pdf.add_page()
    
    # Header
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Rapport d'Experimentation - PAKERANK", 0, 1, 'C')
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, "Ecole Superieure Polytechnique d'Antsiranana", 0, 1, 'C')
    pdf.ln(5)

    # Paramètres
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "1. Parametres", 0, 1)
    pdf.set_font("Arial", '', 11)
    pdf.cell(0, 8, f"Type de Graphe: {graph_type}", 0, 1)
    pdf.cell(0, 8, f"Nombre de Noeuds: {n_nodes}", 0, 1)
    pdf.cell(0, 8, f"Nombre d'Aretess: {n_edges}", 0, 1)
    pdf.cell(0, 8, f"Facteur de Damping: {damping}", 0, 1)
    pdf.cell(0, 8, f"Iterations pour convergence: {n_iter}", 0, 1)
    pdf.ln(5)

    # Top 10
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "2. Top 10 Noeuds PageRank", 0, 1)
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(40, 8, "Rang", 1)
    pdf.cell(40, 8, "Noeud", 1)
    pdf.cell(60, 8, "Score", 1)
    pdf.ln()
    pdf.set_font("Arial", '', 10)
    for i, row in df.head(10).iterrows():
        pdf.cell(40, 8, str(row['Rang']), 1)
        pdf.cell(40, 8, str(row['Noeud']), 1)
        pdf.cell(60, 8, f"{row['Notre Implementation']:.6f}", 1)
        pdf.ln()
    
    pdf.ln(5)
    pdf.set_font("Arial", 'I', 9)
    pdf.cell(0, 10, f"Erreur moyenne vs NetworkX: {df['Erreur Absolue'].mean():.2e}", 0, 1)

    return pdf.output(dest='S').encode('latin1')

# ... dans ton if run: ...
if run:
    # ... tout ton code de calcul ...

    with tab4:
        st.subheader("Matrice d'Adjacence")
        st.dataframe(pd.DataFrame(A.astype(int)), height=400)
        
        col_dl1, col_dl2 = st.columns(2)
        with col_dl1:
            st.download_button("📥 Télécharger Résultats CSV", df_scores.to_csv(index=False), "pagerank_espa_results.csv")
        with col_dl2:
            # Générer PDF
            pdf_bytes = create_pdf_report(df_scores, G.number_of_nodes(), G.number_of_edges(), n_iter, damping, graph_type)
            st.download_button("📄 Générer Rapport PDF", pdf_bytes, "rapport_pagerank_espa.pdf", "application/pdf")
