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
  Node(id="Tableu", label="Tableu", color="#28b463")
]


edges = [
  Edge (source="Data Science Tools", target="Collection"),
  Edge (source="Data Science Tools", target="Cleaning"),
  Edge (source="Data Science Tools", target="EDA"),
  Edge (source="Data Science Tools", target="Model Building"),
  Edge (source="Data Science Tools", target="Model Deployment"),
  Edge (source="Collection", target="SQL"),
  Edge (source="", target="Scrapy"),
  Edge (source="", target="Python"),
  Edge (source="Cleaning", target="OpenRefine"),
  Edge (source="EDA", target="Pandas"),
  Edge (source="Model Building", target="StatsModels"),
  Edge (source="Model Deployment", target="Power BI"),
  Edge (source="Model Deployment", target="Tableu")
]

config = Config(
  width=900,
  height=900,
  directed=True,
  nodeHightlightBehaviour=True,
  hightlightColor="#b70b3d",
  collapsible=False,
  node={'labelProperty': 'label'},
  link={'labelProperty': 'label', 'renderLabel': False},
  hierarchical=True,
  layout={
    "hierarchical": {
      "enabled": True,
      "levelSeparation": 150,
      "nodeSpacing": 100,
      "treeSpacing": 200,
      "direction": "UD", # UD for top to bottom
      "sortMethod": "directed"
    }
  }
  zoom=1.2 # Adjust as needed
)
