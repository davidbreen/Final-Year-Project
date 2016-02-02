import networkx as nx
import gexf
G=nx.Graph()
G.add_node("spam")
G.add_node(2)
G.add_node(3)
G.add_edge(2,3)
nx.write_gexf(G, "C:/Users/David/Desktop/fyp/test.gexf")

#C:\Program Files (x86)\ActiveState Komodo Edit 9\example6.db