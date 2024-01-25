import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime

# Your timetable data
timetable = {
    "Train1": {
        "source1": (datetime.strptime("10:00", "%H:%M").time(), datetime.strptime("10:05", "%H:%M").time()),
        "source3": (datetime.strptime("10:05", "%H:%M").time(), datetime.strptime("10:10", "%H:%M").time()),
        "source4": (datetime.strptime("10:10", "%H:%M").time(), datetime.strptime("10:20", "%H:%M").time()),
        "source7": (datetime.strptime("10:20", "%H:%M").time(), datetime.strptime("10:25", "%H:%M").time()),
    },
    "Train2": {
        "source2": (datetime.strptime("10:00", "%H:%M").time(), datetime.strptime("10:05", "%H:%M").time()),
        "source4": (datetime.strptime("10:05", "%H:%M").time(), datetime.strptime("10:15", "%H:%M").time()),
        "source7": (datetime.strptime("10:15", "%H:%M").time(), datetime.strptime("10:20", "%H:%M").time()),
    },
    "Train3": {
        "source6": (datetime.strptime("10:10", "%H:%M").time(), datetime.strptime("10:15", "%H:%M").time()),
        "source5": (datetime.strptime("10:15", "%H:%M").time(), datetime.strptime("10:20", "%H:%M").time()),
        "source4": (datetime.strptime("10:10", "%H:%M").time(), datetime.strptime("10:30", "%H:%M").time()),
        "source2": (datetime.strptime("10:30", "%H:%M").time(), datetime.strptime("10:35", "%H:%M").time()),
    },
}

# Create a graph to represent resource occupancy during specific time intervals
occupancy_graph = nx.DiGraph()

# Add nodes for resources with their occupancy time intervals as attributes
for train, resources in timetable.items():
    for resource, (start_time, end_time) in resources.items():
        occupancy_graph.add_node(resource, start_time=start_time, end_time=end_time)

# Add edges to represent connections between resources
for train, resources in timetable.items():
    resource_list = list(resources.keys())
    for i in range(len(resource_list)):
        for j in range(i + 1, len(resource_list)):
            occupancy_graph.add_edge(resource_list[i], resource_list[j], train=train)

# Check for conflicts
conflict_edges = []

for edge in occupancy_graph.edges:
    train1 = occupancy_graph[edge[0]][edge[1]]['train']
    start_time1 = occupancy_graph.nodes[edge[0]]['start_time']
    end_time1 = occupancy_graph.nodes[edge[0]]['end_time']

    train2 = occupancy_graph[edge[0]][edge[1]]['train']
    start_time2 = occupancy_graph.nodes[edge[1]]['start_time']
    end_time2 = occupancy_graph.nodes[edge[1]]['end_time']

    # Check for conflicts
    if start_time1 < end_time2 and start_time2 < end_time1:
        conflict_edges.append(edge)

# Visualize conflicts
pos = nx.spring_layout(occupancy_graph)
nx.draw(occupancy_graph, pos, with_labels=True, font_weight='bold', node_size=2000, node_color='skyblue', font_size=8)

# Highlight conflict edges
nx.draw_networkx_edges(occupancy_graph, pos, edgelist=conflict_edges, edge_color='red', width=2)

plt.show()

# Print details of conflicts
for edge in conflict_edges:
    print(f"Conflict between {edge[0]} and {edge[1]} with trains {occupancy_graph[edge[0]][edge[1]]['train']} and {occupancy_graph[edge[0]][edge[1]]['train']}")

