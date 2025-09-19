import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import heapq

st.set_page_config(page_title="Kolkata Metro Sarathi", layout="wide")
st.title("Kolkata Metro Sarathi")
st.write("Find the shortest metro route and view full metro map.")

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


def find_min_switch_path(G, station_lines, src, dest):
    """
    Returns (path_list, num_switches, num_stations) or (None, None, None) if no path.
    """
    # PQ entries are (switches, stations, current_station, current_line, parent)
    pq = []
    visited = {}  
    # visited[(station, line)] = (best_switches, best_stations)

    # Initialize one entry per line that src belongs to
    for line in station_lines[src]:
        entry = (0, 1, src, line, None)
        heapq.heappush(pq, entry)
        visited[(src, line)] = (0, 1)

    best_final = None

    while pq:
        switches, stations_count, curr_station, curr_line, parent = heapq.heappop(pq)

        # If we've already seen a strictly better cost for (curr_station, curr_line), skip
        if visited.get((curr_station, curr_line), (float('inf'), float('inf'))) < (switches, stations_count):
            continue

        # Stop as soon as we pop a state at the destination
        if curr_station == dest:
            best_final = (switches, stations_count, curr_station, curr_line, parent)
            break

        # Explore each neighbor
        for nbr in G.neighbors(curr_station):
            edge_line = G[curr_station][nbr]['color']
            new_switches = switches + (edge_line != curr_line)
            new_stations = stations_count + 1

            state_key = (nbr, edge_line)
            best_seen = visited.get(state_key, (float('inf'), float('inf')))

            if (new_switches, new_stations) < best_seen:
                visited[state_key] = (new_switches, new_stations)
                heapq.heappush(pq, (new_switches, new_stations, nbr, edge_line,
                                     (switches, stations_count, curr_station, curr_line, parent)))

    if best_final is None:
        return None, None, None

    # Reconstruct path
    switches, stations_count, station, line, parent = best_final
    rev_path = [station]
    ptr = parent
    while ptr is not None:
        _, _, prev_station, _, prev_parent = ptr
        rev_path.append(prev_station)
        ptr = prev_parent

    rev_path.reverse()
    return rev_path, switches, stations_count


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
all_stations = list(G.nodes())
all_stations.sort()
src_input = st.sidebar.selectbox("Select the source station:", all_stations, index=all_stations.index("HOWRAH MAIDAN") if "HOWRAH MAIDAN" in all_stations else 0)
dest_input = st.sidebar.selectbox("Select the destination station:", all_stations, index=all_stations.index("SALT LAKE SECTOR V") if "SALT LAKE SECTOR V" in all_stations else 0)

# Button to find the route (subgraph)
if st.sidebar.button("Find Route"):
    src = src_input.upper()
    dest = dest_input.upper()

    # 1) Validate source/destination
    if src not in G.nodes():
        st.error(f"Source station '{src}' not found. Please check your input.")
        #return
    if dest not in G.nodes():
        st.error(f"Destination station '{dest}' not found. Please check your input.")
        #return

    # 2) Build station_lines for every station in G
    station_lines = {}
    for station in G.nodes():
        lines = set()
        if station in {s[0] for s in green_line}:      
            lines.add("green")
        if station in {s[0] for s in blue_line}:       
            lines.add("blue")
        if station in {s[0] for s in purple_line}:     
            lines.add("purple")
        if station in {s[0] for s in orange_line}:     
            lines.add("orange")
        if station in {s[0] for s in purple_line_ext}: 
            lines.add("silver")
        if station in {s[0] for s in yellow_line}:     
            lines.add("yellow")
        if station in {s[0] for s in orange_line_ext}: 
            lines.add("gold")
        station_lines[station] = lines

    # 3) Compute the minimum‐switch path instead of nx.shortest_path
    path, min_switches, min_stations = find_min_switch_path(G, station_lines, src, dest)

    if path is None:
        st.error(f"No path exists between {src} and {dest}")
        #return

    # 4) Compute exactly where each switch occurs
    edge_colors = [G[path[i]][path[i+1]]["color"] for i in range(len(path) - 1)]
    transitions = []
    prev_color = edge_colors[0]
    for i in range(1, len(path) - 1):
        curr_color = edge_colors[i]
        if curr_color != prev_color:
            transitions.append((path[i], prev_color, curr_color))
            prev_color = curr_color

    st.header("Track‐Switch Locations")
    if transitions:
        for station, from_line, to_line in transitions:
            st.subheader(f"🔄 Change from {from_line.title()} to {to_line.title()} at {station}")
    else:
        st.write("No transitions required.")

    # 5) Show routing summary
    st.header("Route Summary")
    st.write(f"🔄 Minimum line‐switches: **{min_switches}**")
    st.write(f"🚉 Stations traversed: **{min_stations}**")
    st.write("Route: " + " → ".join(path))

    # ──────────────────────────────────────────────────────────────
    # 6) Build subgraph nodes/edges and define subgraph_pos BEFORE any labeling loop
    subgraph_nodes = set(path)
    subgraph_edges = [
        (u, v)
        for u, v in G.edges()
        if u in subgraph_nodes and v in subgraph_nodes
    ]
    subgraph = G.edge_subgraph(subgraph_edges)
    subgraph_pos = {node: pos[node] for node in subgraph_nodes}

    # 7) Draw the subgraph
    fig_sub, ax_sub = plt.subplots(figsize=(12, 8))
    edge_colors = [subgraph[u][v]["color"] for u, v in subgraph.edges()]
    nx.draw_networkx_nodes(subgraph, subgraph_pos, node_size=50, node_color="lightblue", ax=ax_sub)
    nx.draw_networkx_edges(subgraph, subgraph_pos, edge_color=edge_colors, width=2, ax=ax_sub)

    # 8) Labeling loop: now it’s safe to reference subgraph_pos
    cg = 1; cb = 0; cp = 1; cpe = 0; co = 1; cy = 0
    done = set()
    for node in path:
        x, y = subgraph_pos[node]     # <— subgraph_pos is already defined
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

    ax_sub.axis("off")
    ax_sub.set_xlim(-10, 53)
    ax_sub.set_ylim(-41, 66)
    st.subheader("Shortest Path")
    st.pyplot(fig_sub)


# Button to display the full metro map (placed outside the "Find Route" block)
if st.sidebar.button("Show Full Map"):
    fig_full, ax_full = plt.subplots(figsize=(12, 8))
    nx.draw_networkx_nodes(G, pos, node_size=50, ax=ax_full)
    full_edge_colors = [G[u][v]['color'] for u, v in G.edges()]
    nx.draw_networkx_edges(G, pos, edge_color=full_edge_colors, width=2, ax=ax_full)
    
    # Conditional labeling for the full map
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
