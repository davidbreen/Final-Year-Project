import sqlite3
import gexf
import networkx as nx
G=nx.Graph()
conn = sqlite3.connect('C:/Users/David/Desktop/fyp/presidents.db')
c = conn.cursor()
select=c.execute("SELECT Name FROM info")
every_name = select.fetchall()
select2=c.execute("SELECT Friend FROM info")
every_friend = select2.fetchall()
select3=c.execute("SELECT * FROM info")
every= select3.fetchall()
newlist=[]
for i in every_name:
  if i[0] not in newlist:
    newlist.append(i[0])   
i=0
p=0
for each in newlist:
    G.add_node(each, )
    for item in every:
        if each == item[0]:
            if item[1] in newlist:
                G.add_edge(item[1], each)

nx.write_gexf(G, "C:/Users/David/Desktop/fyp/nodes.gexf")         
    
    
