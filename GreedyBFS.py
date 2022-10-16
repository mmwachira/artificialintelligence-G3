import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
nodes = ["StrathmoreSportsComplex", "Siwaka", "Phase1Ent.A", "Phase1Ent.B", "Phase2", "J1", "Mada", "STC", "Phase3",
         "Parking Lot"]

g.add_node("StrathmoreSportsComplex")
g.add_node("Siwaka")
g.add_node("Phase1Ent.A")
g.add_node("Phase1Ent.B")
g.add_node("Phase2")
g.add_node("J1")
g.add_node("Mada")
g.add_node("STC")
g.add_node("Phase3")
g.add_node("Parking Lot")

g.add_edge("StrathmoreSportsComplex", "Siwaka", weight="450")
g.add_edge("Siwaka", "Phase1Ent.A", weight="10")
g.add_edge("Siwaka", "Phase1Ent.B", weight="230")
g.add_edge("Phase1Ent.A", "Phase1Ent.B", weight="100")
g.add_edge("Phase1Ent.B", "STC", weight="50")
g.add_edge("Phase1Ent.A", "Mada", weight="850")
g.add_edge("Phase1Ent.B", "Phase2", weight="112")
g.add_edge("STC", "Phase2", weight="50")
g.add_edge("STC", "Parking Lot", weight="250")
g.add_edge("Phase2", "Phase3", weight="500")
g.add_edge("Phase2", "J1", weight="600")
g.add_edge("J1", "Mada", weight="200")
g.add_edge("Phase3", "Parking Lot", weight="350")
g.add_edge("Mada", "Parking Lot", weight="700")

nx.draw(g, node_size=8000, with_labels=True, )
plt.savefig("filename.png")
