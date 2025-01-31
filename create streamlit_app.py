import streamlit as st
from stremlit_agraph import agraph, Note, Edge, Config

st.set_page_config(layout="wide")
st.title("Data Science Tools Hierarchical Graph")
col1, col2 = st.columns([3, 1]) 

nodes = [

  Node(id="Data Science Tools", label="Data Science Tools", color="#cb4335"),
  Node(id="Collection", label="Collection", color="#d2b4de"),
  Node(id="Cleaning", label="Cleaning", color="#eb984e"),
  Node(id="EDA", label="EDA", color="#2471a3"),
  Node(id="Model Building", label="Model Building", color="#28b463"),
  Node(id="Model Deployment", label="Model Deployment)", color="#b7950b"),
  Node(id="SQL", label="SQL", color="#d2b4de"),
  Node(id="Scrapy", label="Scrapy", color="#d2b4de"),
  Node(id="Python", label="Python", color="#d2b4de"),
  Node(id="OpenRefine", label="OpenRefine", color="#eb984e"),
  Node(id="Pandas", label="Pandas", color="#2471a3"),
  Node(id="StatsModels", label="StatsModels", color="#28b463"),
  Node(id="Power BI", label="Power BI", color="#b7950b"),
  Node(id="Tableu", label="Tableu", color="#28b463"),
  Node(id="StatsModels", label="StatsModels", color="#b7950b")
]
