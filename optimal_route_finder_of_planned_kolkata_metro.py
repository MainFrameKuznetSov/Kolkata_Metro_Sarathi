# # -*- coding: utf-8 -*-
# """Optimal_Route_Finder_of_Planned_Kolkata_Metro.ipynb

# Automatically generated by Colab.

# Original file is located at
#     https://colab.research.google.com/drive/1VZBB2-N2Ytk90FCIVoJktCdNCWjnfqEl
# """

# from google.colab import files
# import pandas as pd
# from collections import defaultdict as dd

# green_line=[("Howrah Maidan",0),("Howrah Railway Station",1),("Mahakaran",2),("Esplanade",3),("Sealdah",4),
# ("Phoolbagan",5), ("Salt Lake Stadium",6),("Bengal Chemical",7),("City Centre I",8),("Central Park",9),
# ("Korunamoyee",70),("Salt Lake Sector V",10)]

# adj_list=dd(list)
# for i in range(len(green_line)-1):
#     stn1=green_line[i]
#     stn2=green_line[i+1]
#     adj_list[stn1].append(stn2)
#     adj_list[stn2].append(stn1)

# for i,j in adj_list.items():
#     print(f"{i}->{j}")

# data=[]
# for i,j in adj_list.items():
#   str=", ".join([f"{next[0]} ({next[1]})" for next in j])
#   data.append({"Station":f"{i[0]}({[i[1]]})","Connected Stations":str})

# temp=pd.DataFrame(data)
# temp.to_csv("Green_Line.csv",index=False)

# print(temp)

# #files.download("Green_Line.csv")

# from google.colab import files
# import pandas as pd
# from collections import defaultdict as dd

# blue_line=[("Dakshineshwar",11),("Baranagar",12),("Noapara",13),("Dum Dum",14),("Belgachhia",15),("Shyambazar",16),
# ("Sovabazar Sutanuti",17),("Girish Park",18),("Mahatma Gandhi Road",19),("Central",20),("Chandni Chowk",21),
# ("Esplanade",3),("Park Street",22),("Maidan",23),("Rabindra Sadan",24),("Netaji Bhavan",25),("Jatin Das Park",26),
# ("Kalighat",27),("Rabindra Sarovar",28),("Mahanayak Uttam Kumar",29),("Netaji",30),("Masterda Surya Sen",31),
# ("Gitanjali",32),("Kavi Nazrul",33),("Shahid Khudiram",34),("Kavi Subhas",35)]

# blue_line_set = set(blue_line)

# for i in range(len(blue_line)-1):
#     stn1=blue_line[i]
#     stn2=blue_line[i+1]
#     if stn2 in blue_line_set:
#         adj_list[stn1].append(stn2)
#     if stn1 in blue_line_set:
#         adj_list[stn2].append(stn1)

# #for i,j in adj_list.items():
#     #print(f"{i}->{j}")


# filtered_adj_list = dd(list)

# for station, connections in adj_list.items():
#     if station in blue_line_set:  # Only process stations in the blue line
#         for conn in connections:
#             if conn in blue_line_set and conn not in filtered_adj_list[station]:  # Ensure no duplicate in one direction
#                 filtered_adj_list[station].append(conn)
# data = []
# for station, connections in filtered_adj_list.items():
#     connection_str = ", ".join(f"{conn[0]} ({conn[1]})" for conn in connections)
#     data.append({"Station": f"{station[0]} ({station[1]})", "Connected Stations": connection_str})


# temp=pd.DataFrame(data)
# temp.to_csv("Blue_Line.csv",index=False)

# print(temp)

# #files.download("Blue_Line.csv")

# from google.colab import files
# import pandas as pd
# from collections import defaultdict as dd

# purple_line=[("Joka",36),("Thakurpukur",37),("Sakherbazar",38),("Behala Chowrasta",39),("Behala Bazar",40),("Taratala",41),
# ("Majerhat",42)]

# purple_line_set = set(purple_line)

# for i in range(len(purple_line)-1):
#     stn1=purple_line[i]
#     stn2=purple_line[i+1]
#     if stn2 in purple_line_set:
#         adj_list[stn1].append(stn2)
#     if stn1 in purple_line_set:
#         adj_list[stn2].append(stn1)

# # for i,j in adj_list.items():
# #     print(f"{i}->{j}")

# filtered_adj_list = dd(list)

# for station, connections in adj_list.items():
#     if station in purple_line_set:  # Only process stations in the blue line
#         for conn in connections:
#             if conn in purple_line_set and conn not in filtered_adj_list[station]:  # Ensure no duplicate in one direction
#                 filtered_adj_list[station].append(conn)
# data = []
# for station, connections in filtered_adj_list.items():
#     connection_str = ", ".join(f"{conn[0]} ({conn[1]})" for conn in connections)
#     data.append({"Station": f"{station[0]} ({station[1]})", "Connected Stations": connection_str})


# temp=pd.DataFrame(data)
# temp.to_csv("Purple_Line.csv",index=False)

# print(temp)

# # files.download("Purple_Line.csv")

# from google.colab import files
# import pandas as pd
# from collections import defaultdict as dd

# orange_line=[("Kavi Subhas",35),("Satyajit Ray",43),("Jyotirindra Nath Nandy",44),("Kavi Sukanta",45),
# ("Hemanta Mukherjee",46)]

# orange_line_set = set(orange_line)

# for i in range(len(orange_line)-1):
#     stn1=orange_line[i]
#     stn2=orange_line[i+1]
#     if stn2 in orange_line_set:
#         adj_list[stn1].append(stn2)
#     if stn1 in orange_line_set:
#         adj_list[stn2].append(stn1)

# # for i,j in adj_list.items():
# #     print(f"{i}->{j}")

# filtered_adj_list = dd(list)

# for station, connections in adj_list.items():
#     if station in orange_line_set:  # Only process stations in the blue line
#         for conn in connections:
#             if conn in orange_line_set and conn not in filtered_adj_list[station]:  # Ensure no duplicate in one direction
#                 filtered_adj_list[station].append(conn)
# data = []
# for station, connections in filtered_adj_list.items():
#     connection_str = ", ".join(f"{conn[0]} ({conn[1]})" for conn in connections)
#     data.append({"Station": f"{station[0]} ({station[1]})", "Connected Stations": connection_str})


# temp=pd.DataFrame(data)
# temp.to_csv("Orange_Line.csv",index=False)

# print(temp)

# # files.download("Orange_Line.csv")

# from collections import defaultdict as dd

# purple_line_ext=[("Majerhat",46),("Mominpur",47),("Khidderpore",48),("Victoria Memorial",49),("Park Street",22),
#                 ("Esplanade",3)]

# purple_ext_set=set(purple_line_ext)

# for i in range(len(purple_line_ext)-1):
#     stn1=purple_line_ext[i]
#     stn2=purple_line_ext[i+1]
#     if stn2 in purple_ext_set:
#         adj_list[stn1].append(stn2)
#     if stn1 in purple_ext_set:
#         adj_list[stn2].append(stn1)

# filtered_adj_list=dd(list)
# for station, connections in adj_list.items():
#     if station in purple_line_ext:
#         for conn in connections:
#             if conn in purple_line_ext and conn not in filtered_adj_list[station]:
#                 filtered_adj_list[station].append(conn)

# data=[]
# for station, connections in filtered_adj_list.items():
#     connection_str = ", ".join(f"{conn[0]} ({conn[1]})" for conn in connections)
#     data.append({"Station": f"{station[0]} ({station[1]})", "Connected Stations": connection_str})

# temp=pd.DataFrame(data)
# temp.to_csv("Purple_Line_Extended.csv",index=False)

# print(temp)

# #files.download("Purple_Line_Extended.csv")

# # for i,j in adj_list.items():
# #     print(f"{i}->{j}")

# from collections import defaultdict as dd

# yellow_line=[("Noapara",13),("Dum Dum Cantonment",50),("Jessore Road",51),("Biman Bandar",52),("Birati",71),("Michael Nagar",72),("New Barrackpore",73),("Madhyamgram",74),("Hridaypur",75),("Barasat",76)]

# yellow_line_set=set(yellow_line)

# for i in range(len(yellow_line)-1):
#     stn1=yellow_line[i]
#     stn2=yellow_line[i+1]
#     if stn2 in yellow_line_set:
#         adj_list[stn1].append(stn2)
#     if stn1 in yellow_line_set:
#         adj_list[stn2].append(stn1)

# filtered_adj_list=dd(list)
# for station, connections in adj_list.items():
#     if station in yellow_line_set:
#         for conn in connections:
#             if conn in yellow_line_set and conn not in filtered_adj_list:
#                 filtered_adj_list[station].append(conn)

# data=[]

# for station, connections in filtered_adj_list.items():
#     connection_str = ", ".join(f"{conn[0]} ({conn[1]})" for conn in connections)
#     data.append({"Station": f"{station[0]} ({station[1]})", "Connected Stations": connection_str})

# temp=pd.DataFrame(data)
# temp.to_csv("Yellow_Line.csv",index=False)

# print(temp)

# #files.download("Yellow_Line.csv")

# # for i,j in adj_list.items():
# #     print(f"{i}->{j}")

# from collections import defaultdict as dd

# orange_line_ext=[("Hemanta Mukherjee",46),("VIP Bazar",53),("Ritwik Ghatak",54),("Barun Sengupta",55),("Beliaghata",56),("Gour Kishore Ghosh",57),
# ("NICCO Park",58),("Salt Lake Sector V",10),("Technopolis",59),("Nazrul Tirtha",60),("Swapno Bhor",61),
# ("Biswa Bangla Convention Centre",62),("Kala Kshetra",63),("Mother's Wax Museum",64),("Eco Park",65),
# ("Siksha Tirtha",66),("City Centre II",67),("Chinar Park",68),("VIP Road",69),("Biman Bandar",52)]

# orange_ext_set=set(orange_line_ext)

# for i in range(len(orange_line_ext)-1):
#     stn1=orange_line_ext[i]
#     stn2=orange_line_ext[i+1]
#     if stn2 in orange_ext_set:
#         adj_list[stn1].append(stn2)
#     if stn1 in orange_ext_set:
#         adj_list[stn2].append(stn1)

# filtered_adj_list=dd(list)
# for station, connections in adj_list.items():
#     if station in orange_ext_set:
#         for conn in connections:
#             if conn in orange_ext_set and conn not in filtered_adj_list:
#                 filtered_adj_list[station].append(conn)

# data=[]

# for station, connections in filtered_adj_list.items():
#     connection_str = ", ".join(f"{conn[0]} ({conn[1]})" for conn in connections)
#     data.append({"Station": f"{station[0]} ({station[1]})", "Connected Stations": connection_str})

# temp=pd.DataFrame(data)
# temp.to_csv("Orange_Line_Extended.csv",index=False)

# print(temp)

# #files.download("Orange_Line_Extended.csv")

# # for i,j in adj_list.items():
# #     print(f"{i}->{j}")

# from google.colab import files
# import pandas as pd

# data=[]
# for i,j in adj_list.items():
#   str=", ".join([f"{next[0]} ({next[1]})" for next in j])
#   data.append({"Station":f"{i[0]}({[i[1]]})","Connected Stations":str})

# temp=pd.DataFrame(data)
# temp.to_csv("Kolkata_Metro_Adjacency_List.csv",index=False)

# print(temp)

# files.download("Kolkata_Metro_Adjacency_List.csv")

# !pip install adjustText

# from adjustText import adjust_text as at
# import networkx as nx
# import matplotlib.pyplot as plt

# def add_edges_with_color(line, color):
#     for i in range(len(line) - 1):
#         node1, node2 = line[i][0], line[i + 1][0]
#         if not G.has_edge(node1, node2):
#             G.add_edge(node1, node2, color=color)

# G=nx.Graph()

# color_map = {
#     'green': "green",
#     'blue': "blue",
#     'purple': "purple",
#     'silver': "silver",
#     'yellow': "yellow",
#     'orange': "orange",
#     'gold': "gold"
# }

# node_color = {}


# add_edges_with_color(blue_line, color_map['blue'])
# add_edges_with_color(green_line, color_map['green'])
# add_edges_with_color(purple_line, color_map['purple'])
# add_edges_with_color(purple_line_ext, color_map['silver'])
# add_edges_with_color(yellow_line, color_map['yellow'])
# add_edges_with_color(orange_line, color_map['orange'])
# add_edges_with_color(orange_line_ext, color_map['gold'])

# edge_colors = [G[u][v]['color'] for u, v in G.edges()]

# plt.figure(figsize=(15, 10))
# pos = nx.kamada_kawai_layout(G)
# nx.draw_networkx_nodes(G, pos, node_size=10)
# nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=2)
# #nx.draw_networkx_labels(G, pos, font_size=6)

# '''texts = []
# for i, node in enumerate(G.nodes()):
#     x, y = pos[node]
#     y_offset = 0.015 if i % 2 == 0 else -0.015
#     text = plt.text(x, y + y_offset, node, fontsize=6, ha='right', va='bottom') if i%2==0 else plt.text(x, y + y_offset, node, fontsize=6, ha='left', va='top')
#     texts.append(text)
# '''
# texts = []
# for i, node in enumerate(G.nodes()):
#     x, y = pos[node]
#     y_offset = 0.05 if i % 2 == 0 else -0.05
#     text = plt.text(x, y + y_offset, node, fontsize=6, ha='center', va='bottom' if i % 2 == 0 else 'top')
#     texts.append(text)



# plt.show()

import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(page_title="Metro Route Planner", layout="wide")
st.title("Metro Route Planner")
st.write("Find the shortest metro route and view the full metro map.")

# Define metro lines
green_line = [("HOWRAH MAIDAN", 0), ("HOWRAH STATION", 1), ("MAHAKARAN", 2),
              ("ESPLANADE", 3), ("SEALDAH", 4), ("PHOOLBAGAN", 5),
              ("SALT LAKE STADIUM", 6), ("BENGAL CHEMICAL", 7), ("CITY CENTRE I", 8),
              ("CENTRAL PARK", 9), ("KORUNAMOYEE", 10), ("SALT LAKE SECTOR V", 11)]

blue_line = [("DAKSHINESHWAR", 12), ("BARANAGAR", 13), ("NOAPARA", 14), ("DUM DUM", 15),
             ("BELGACHHIA", 16), ("SHYAMBAZAR", 17), ("SOVABAZAR SUTANUTI", 18),
             ("GIRISH PARK", 19), ("MAHATMA GANDHI ROAD", 20), ("CENTRAL", 21),
             ("CHANDNI CHOWK", 22), ("ESPLANADE", 3), ("PARK STREET", 23),
             ("MAIDAN", 24), ("RABINDRA SADAN", 25), ("NETAJI BHAVAN", 26),
             ("JATIN DAS PARK", 27), ("KALIGHAT", 28), ("RABINDRA SAROVAR", 29),
             ("MAHANAYAK UTTAM KUMAR", 30), ("NETAJI", 31), ("MASTERDA SURYA SEN", 32),
             ("GITANJALI", 33), ("KAVI NAZRUL", 34), ("SHAHID KHUDIRAM", 35),
             ("KAVI SUBHAS", 36)]

purple_line = [("JOKA", 37), ("THAKURPUKUR", 38), ("SAKHERBAZAR", 39), ("BEHALA CHOWRASTA", 40),
               ("BEHALA BAZAR", 41), ("TARATALA", 42), ("MAJERHAT", 43)]

orange_line = [("KAVI SUBHAS", 36), ("SATYAJIT RAY", 44), ("JYOTIRINDRA NATH NANDY", 45),
               ("KAVI SUKANTA", 46), ("HEMANTA MUKHERJEE", 47)]

purple_line_ext = [("MAJERHAT", 43), ("MOMINPUR", 48), ("KHIDDERPORE", 49),
                   ("VICTORIA MEMORIAL", 50), ("PARK STREET", 22), ("ESPLANADE", 3)]

yellow_line = [("NOAPARA", 14), ("DUM DUM CANTONMENT", 51), ("JESSORE ROAD", 52),
               ("BIMAN BANDAR", 53)]

orange_line_ext = [("HEMANTA MUKHERJEE", 47), ("VIP BAZAR", 54), ("RITWIK GHATAK", 55),
                   ("BARUN SENGUPTA", 56), ("BELIAGHATA", 57), ("GOUR KISHORE GHOSH", 58),
                   ("NICCO PARK", 59), ("SALT LAKE SECTOR V", 11), ("TECHNOPOLIS", 60),
                   ("NAZRUL TIRTHA", 61), ("SWAPNO BHOR", 62), ("BISWA BANGLA CONVENTION CENTRE", 63),
                   ("KALA KSHETRA", 64), ("MOTHER'S WAX MUSEUM", 65), ("ECO PARK", 66),
                   ("SIKSHA TIRTHA", 67), ("CITY CENTRE II", 68), ("CHINAR PARK", 69),
                   ("VIP ROAD", 70), ("BIMAN BANDAR", 53)]

color_priority = {"green": 7, "blue": 6, "purple": 5, "orange": 4,
                  "silver": 3, "yellow": 2, "gold": 1}

# Build the full metro graph
G = nx.Graph()
def add_edges(line, color):
    for i in range(len(line) - 1):
        node1, node2 = line[i][0], line[i+1][0]
        if not G.has_edge(node1, node2) or color_priority[color] > color_priority[G[node1][node2]['color']]:
            G.add_edge(node1, node2, color=color)

add_edges(green_line, "green")
add_edges(blue_line, "blue")
add_edges(purple_line, "purple")
add_edges(orange_line, "orange")
add_edges(purple_line_ext, "silver")
add_edges(yellow_line, "yellow")
add_edges(orange_line_ext, "gold")

# Define positions for each station
pos = {
    # Green line
    "HOWRAH MAIDAN": (-7, 6), "HOWRAH STATION": (-3, 6), "MAHAKARAN": (1, 6),
    "ESPLANADE": (5, 6), "SEALDAH": (9, 6), "PHOOLBAGAN": (13, 6),
    "SALT LAKE STADIUM": (17, 6), "BENGAL CHEMICAL": (21, 6), "CITY CENTRE I": (25, 6),
    "CENTRAL PARK": (29, 6), "KORUNAMOYEE": (33, 6), "SALT LAKE SECTOR V": (37, 6),

    # Blue line
    "DAKSHINESHWAR": (5, -38), "BARANAGAR": (5, -34), "NOAPARA": (5, -30),
    "DUM DUM": (5, -26), "BELGACHHIA": (5, -22), "SHYAMBAZAR": (5, -18),
    "SOVABAZAR SUTANUTI": (5, -14), "GIRISH PARK": (5, -10), "MAHATMA GANDHI ROAD": (5, -6),
    "CENTRAL": (5, -2), "CHANDNI CHOWK": (5, 2), "ESPLANADE": (5, 6), "PARK STREET": (5, 10),
    "MAIDAN": (5, 14), "RABINDRA SADAN": (5, 18), "NETAJI BHAVAN": (5, 22),
    "JATIN DAS PARK": (5, 26), "KALIGHAT": (5, 30), "RABINDRA SAROVAR": (5, 34),
    "MAHANAYAK UTTAM KUMAR": (5, 38), "NETAJI": (5, 42), "MASTERDA SURYA SEN": (5, 46),
    "GITANJALI": (5, 50), "KAVI NAZRUL": (5, 54), "SHAHID KHUDIRAM": (5, 58),

    # Purple line
    "JOKA": (46, 15), "THAKURPUKUR": (42, 15), "SAKHERBAZAR": (38, 15),
    "BEHALA CHOWRASTA": (34, 15), "BEHALA BAZAR": (30, 15), "TARATALA": (26, 15),
    "MAJERHAT": (22, 15),

    # Orange line
    "KAVI SUBHAS": (5, 62), "SATYAJIT RAY": (9, 62), "JYOTIRINDRA NATH NANDY": (13, 62),
    "KAVI SUKANTA": (17, 62), "HEMANTA MUKHERJEE": (21, 62),

    # Purple line Extended
    "MOMINPUR": (18, 15), "KHIDDERPORE": (14, 15), "VICTORIA MEMORIAL": (10, 15),

    # Yellow line
    "DUM DUM CANTONMENT": (9, -30), "JESSORE ROAD": (13, -30), "BIMAN BANDAR": (17, -30),

    # Orange line Extended
    "VIP BAZAR": (25, 55), "RITWIK GHATAK": (29, 48), "BARUN SENGUPTA": (33, 41),
    "BELIAGHATA": (37, 34), "GOUR KISHORE GHOSH": (50, 34), "NICCO PARK": (50, 6),
    "TECHNOPOLIS": (41, 0), "NAZRUL TIRTHA": (45, -6), "SWAPNO BHOR": (49, -12),
    "BISWA BANGLA CONVENTION CENTRE": (49, -18), "KALA KSHETRA": (49, -24),
    "MOTHER'S WAX MUSEUM": (49, -30), "ECO PARK": (43, -30), "SIKSHA TIRTHA": (37, -30),
    "CITY CENTRE II": (31, -30), "CHINAR PARK": (25, -30), "VIP ROAD": (21, -30)
}
pos['HEMANTA MUKHERJEE'] = (21, 62)

# Sidebar inputs for routing and map display
src = st.sidebar.text_input("Enter the source station:", "HOWRAH MAIDAN")
dest = st.sidebar.text_input("Enter the destination station:", "SALT LAKE SECTOR V")

# Button to find the route (subgraph)
if st.sidebar.button("Find Route"):
    src = src.upper()
    dest = dest.upper()
    # Define sets for quick membership testing
    n_green_line = {stn[0] for stn in green_line}
    n_blue_line = {stn[0] for stn in blue_line}
    n_purple_line = {stn[0] for stn in purple_line}
    n_orange_line = {stn[0] for stn in orange_line}
    n_purple_line_ext = {stn[0] for stn in purple_line_ext}
    n_yellow_line = {stn[0] for stn in yellow_line}
    n_orange_line_ext = {stn[0] for stn in orange_line_ext}

    try:
        path = nx.shortest_path(G, source=src, target=dest)

        # Build dictionary mapping station to available lines
        station_lines = {}
        for station in path:
            lines = set()
            if station in n_green_line: lines.add("Green Line")
            if station in n_blue_line: lines.add("Blue Line")
            if station in n_purple_line: lines.add("Purple Line")
            if station in n_orange_line: lines.add("Orange Line")
            if station in n_purple_line_ext: lines.add("Purple Line Extended")
            if station in n_yellow_line: lines.add("Yellow Line")
            if station in n_orange_line_ext: lines.add("Orange Line Extended")
            station_lines[station] = lines

        st.subheader("Dynamic Transitions (Lookahead):")
        transitions = []
        active_line = list(station_lines[path[0]])[0]
        st.write(f"Initial active line: {active_line}")

        for i in range(1, len(path)):
            current_station = path[i]
            current_avail = station_lines[current_station]
            if active_line in current_avail:
                j = i
                while j < len(path) and active_line in station_lines[path[j]]:
                    j += 1
                if j < len(path):
                    crit_avail = station_lines[path[j]]
                    candidate = None
                    for cand in current_avail:
                        if cand != active_line and cand in crit_avail:
                            candidate = cand
                            break
                    if candidate and candidate != active_line:
                        transitions.append((path[i-1], active_line, candidate))
                        active_line = candidate
            else:
                candidate = list(current_avail)[0]
                transitions.append((path[i-1], active_line, candidate))
                active_line = candidate

        if transitions:
            for t in transitions:
                st.write(f"🔄 Change from {t[1]} to {t[2]} at {t[0]}")
        else:
            st.write("No transitions required.")

        st.write(f"Final Active Line: {active_line}")
        st.write("Shortest Path: " + " -> ".join(path))

    except nx.NetworkXNoPath:
        st.error(f"No path exists between {src} and {dest}")
        path = None

    # If a valid path was found, plot the subgraph
    if path:
        subgraph_nodes = set(path)
        subgraph_edges = [(u, v) for u, v in G.edges() if u in subgraph_nodes and v in subgraph_nodes]
        subgraph = G.edge_subgraph(subgraph_edges)
        subgraph_pos = {node: pos[node] for node in subgraph_nodes}

        fig_sub, ax_sub = plt.subplots(figsize=(12, 8))
        edge_colors = [subgraph[u][v]['color'] for u, v in subgraph.edges()]
        nx.draw_networkx_nodes(subgraph, subgraph_pos, node_size=50, node_color="lightblue", ax=ax_sub)
        nx.draw_networkx_edges(subgraph, subgraph_pos, edge_color=edge_colors, width=2, ax=ax_sub)

        # Conditional labeling for the subgraph
        cg = 1; cb = 0; cp = 1; cpe = 0; co = 1; cy = 0
        done = set()
        for node in path:
            x, y = subgraph_pos[node]
            if node in done:
                continue
            if node == "KAVI SUBHAS":
                ax_sub.text(x, y+2, node, fontsize=6, ha='left', va='top')
                done.add(node)
                continue
            if node == "ESPLANADE":
                cg += 1
                ax_sub.text(x+0.1, y+0.5, node, fontsize=6, ha='left', va='bottom')
                done.add(node)
                continue
            if node == "PARK STREET":
                cb += 1
                ax_sub.text(x-0.3, y, node, fontsize=6, ha='right', va='center')
                done.add(node)
                continue
            if node == "NOAPARA":
                cy += 1
                ax_sub.text(x+0.1, y-1, node, fontsize=6, ha='left', va='top')
                done.add(node)
                continue
            if node == "HEMANTA MUKHERJEE":
                co += 1
                ax_sub.text(x+0.5, y-1, node, fontsize=6, ha='left', va='bottom')
                done.add(node)
                continue
            if node in [n[0] for n in green_line]:
                cg += 1
                if cg & 1:
                    ax_sub.text(x+0.1, y+0.7, node, fontsize=6, ha='left', va='bottom')
                else:
                    ax_sub.text(x+0.1, y-0.7, node, fontsize=6, ha='left', va='top')
            elif node in [n[0] for n in blue_line]:
                cb += 1
                if cb & 1:
                    ax_sub.text(x+0.3, y, node, fontsize=6, ha='left', va='center')
                else:
                    ax_sub.text(x-0.3, y, node, fontsize=6, ha='right', va='center')
            elif node in [n[0] for n in purple_line]:
                cp += 1
                if cp & 1:
                    ax_sub.text(x+0.3, y+1.5, node, fontsize=6, ha='left', va='center')
                else:
                    ax_sub.text(x-0.3, y-1.5, node, fontsize=6, ha='left', va='center')
            elif node in [n[0] for n in orange_line]:
                co += 1
                if co & 1:
                    ax_sub.text(x-0.3, y+1, node, fontsize=6, ha='left', va='bottom')
                else:
                    ax_sub.text(x-0.3, y-1, node, fontsize=6, ha='left', va='top')
            elif node in [n[0] for n in purple_line_ext]:
                cpe += 1
                if cpe & 1:
                    ax_sub.text(x-0.3, y+1, node, fontsize=6, ha='left', va='bottom')
                else:
                    ax_sub.text(x-0.3, y-1, node, fontsize=6, ha='left', va='top')
            elif node in [n[0] for n in yellow_line]:
                cy += 1
                if cy & 1:
                    ax_sub.text(x-0.3, y+1, node, fontsize=6, ha='left', va='bottom')
                else:
                    ax_sub.text(x-0.3, y-1, node, fontsize=6, ha='left', va='top')
            elif node in [n[0] for n in orange_line_ext]:
                ax_sub.text(x, y+0.3, node, fontsize=6, ha='left', va='bottom')
            done.add(node)

        ax_sub.axis('off')
        ax_sub.set_xlim(-10, 53)
        ax_sub.set_ylim(-41, 66)
        st.subheader("Shortest Path Subgraph")
        st.pyplot(fig_sub)

# Button to display the full metro map
if st.sidebar.button("Show Full Map"):
    fig_full, ax_full = plt.subplots(figsize=(12, 8))
    nx.draw_networkx_nodes(G, pos, node_size=50, ax=ax_full)
    full_edge_colors = [G[u][v]['color'] for u, v in G.edges()]
    nx.draw_networkx_edges(G, pos, edge_color=full_edge_colors, width=2, ax=ax_full)
    
    # Conditional labeling for the full map (similar to your logic)
    cg = 1; cb = 0; cp = 1; cpe = 0; co = 1; cy = 0
    done = set()
    for node, (x, y) in pos.items():
        if node in done:
            continue
        if node == "KAVI SUBHAS":
            ax_full.text(x, y+2, node, fontsize=6, ha='left', va='top')
            done.add(node)
            continue
        if node == "ESPLANADE":
            cg += 1
            ax_full.text(x+0.1, y+0.5, node, fontsize=6, ha='left', va='bottom')
            done.add(node)
            continue
        if node == "PARK STREET":
            cb += 1
            ax_full.text(x-0.3, y, node, fontsize=6, ha='right', va='center')
            done.add(node)
            continue
        if node == "NOAPARA":
            cy += 1
            ax_full.text(x+0.1, y-1, node, fontsize=6, ha='left', va='top')
            done.add(node)
            continue
        if node == "HEMANTA MUKHERJEE":
            co += 1
            ax_full.text(x+0.5, y-1, node, fontsize=6, ha='left', va='bottom')
            done.add(node)
            continue
        if node in [n[0] for n in green_line]:
            cg += 1
            if cg & 1:
                ax_full.text(x+0.1, y+0.7, node, fontsize=6, ha='left', va='bottom')
            else:
                ax_full.text(x+0.1, y-0.7, node, fontsize=6, ha='left', va='top')
        elif node in [n[0] for n in blue_line]:
            cb += 1
            if cb & 1:
                ax_full.text(x+0.3, y, node, fontsize=6, ha='left', va='center')
            else:
                ax_full.text(x-0.3, y, node, fontsize=6, ha='right', va='center')
        elif node in [n[0] for n in purple_line]:
            cp += 1
            if cp & 1:
                ax_full.text(x+0.3, y+1.5, node, fontsize=6, ha='left', va='center')
            else:
                ax_full.text(x-0.3, y-1.5, node, fontsize=6, ha='left', va='center')
        elif node in [n[0] for n in orange_line]:
            co += 1
            if co & 1:
                ax_full.text(x-0.3, y+1, node, fontsize=6, ha='left', va='bottom')
            else:
                ax_full.text(x-0.3, y-1, node, fontsize=6, ha='left', va='top')
        elif node in [n[0] for n in purple_line_ext]:
            cpe += 1
            if cpe & 1:
                ax_full.text(x-0.3, y+1, node, fontsize=6, ha='left', va='bottom')
            else:
                ax_full.text(x-0.3, y-1, node, fontsize=6, ha='left', va='top')
        elif node in [n[0] for n in yellow_line]:
            cy += 1
            if cy & 1:
                ax_full.text(x-0.3, y+1, node, fontsize=6, ha='left', va='bottom')
            else:
                ax_full.text(x-0.3, y-1, node, fontsize=6, ha='left', va='top')
        elif node in [n[0] for n in orange_line_ext]:
            ax_full.text(x, y+0.3, node, fontsize=6, ha='left', va='bottom')
        done.add(node)

    ax_full.axis('off')
    ax_full.set_xlim(-10, 53)
    ax_full.set_ylim(-41, 66)
    st.subheader("Full Metro Map")
    st.pyplot(fig_full)
