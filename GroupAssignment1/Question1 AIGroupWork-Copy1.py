#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx
import matplotlib.pyplot as plt

# In[2]:


g = nx.Graph()

g.add_edge("SportsComplex", "Siwaka", weight="450")
g.add_edge("Siwaka", "Ph1A", weight="10")
g.add_edge("Ph1A", "Mada", weight="850")
g.add_edge("Mada", "ParkingLot", weight="700")
g.add_edge("Siwaka", "Ph1B", weight="230")
g.add_edge("Ph1A", "Ph1B", weight="100")
g.add_edge("Ph1B", "STC", weight="50")
g.add_edge("STC", "ParkingLot", weight="250")
g.add_edge("Ph1B", "Phase2", weight="112")
g.add_edge("Phase2", "J1", weight="600")
g.add_edge("J1", "Mada", weight="200")
g.add_edge("Mada", "ParkingLot", weight="700")
g.add_edge("Ph1B", "STC", weight="50")
g.add_edge("STC", "Phase2", weight="50")
g.add_edge("Phase2", "Phase3", weight="500")
g.add_edge("Phase3", "ParkingLot", weight="350")

# In[3]:


nx.draw(g, with_labels="true")

# In[ ]:
