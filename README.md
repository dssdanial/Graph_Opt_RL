# Graph Search Using Brute Force algorithm for exploring Train Conflictions
Finding possible solutions for a train's resources used in conflict avoidance based on Graph theory and Brute Force algorithm.

## Brute Force Algorithm 
The brute force algorithm is a straightforward approach to problem-solving that exhaustively checks all possible solutions to find the best or desired outcome. In our context of resolving resource conflicts, the algorithm systematically evaluates every combination of removing resources from a graph to identify a solution where no conflicts exist.
### Understanding Resource Usage by Trains:
In the graph representation, each node (resource) has edges connecting it to other nodes. These edges represent conflicts when multiple trains use the same resource. You can associate trains with resources by observing the connections (edges) in the graph. If two resources have an edge between them, it indicates that the corresponding trains are using those resources. For instance, if there's an edge between source4 and source7, it means Train1 and Train2 are both using source4 and source7.

### Finding a Solution to Resource Conflict:
The solution to the resource conflict is to identify a subset of resources (nodes) in the graph where no two nodes in that subset share an edge (i.e., no conflict between resources in that subset). Using a brute force approach, you can iterate through all possible subsets of resources and check if removing those resources resolves all conflicts. If a subset is found where no nodes share an edge, it represents a solution that resolves resource conflicts among trains.

## TimeTable 
```
| Train | Source1            | Source2            | Source3            | Source4            | Source5            | Source6            | Source7            |
|-------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|
| Train1| 10:00 - 10:05      | -                  | 10:05 - 10:10      | 10:10 - 10:20      | -                  | -                  | 10:20 - 10:25      |
| Train2| -                  | 10:00 - 10:05      | -                  | 10:05 - 10:15      | -                  | -                  | 10:15 - 10:20      |
| Train3| -                  | 10:30 - 10:35      | 10:10 - 10:15      | 10:15 - 10:20      | 10:20 - 10:30      | 10:15 - 10:20      | -                  |

```


## Important Libraries Used
- NetworkX: A powerful Python library for creating, manipulating, and studying complex networks or graphs.
- Itertools: A Python module providing functions for creating iterators for efficient looping and combination generation.

## Solution and Explanation:
Solution Finding Process:
- **Graph Creation**:
  Utilizes NetworkX library to generate a graph based on resource occupancy during specific time intervals.
  Adds nodes for resources with time intervals and connects resources shared by trains. 
- **Conflict Solution Search (Brute Force)**:
  Enumerates all combinations of resource removal (combinatorial brute force).
  Iterates through each combination to remove nodes and checks for conflicts.
  If a combination resolves conflicts (no edges remain), record the solution nodes.

```Latex
# Resource Hierarchy Conflict Detection

## Define Resource Hierarchy

- Create an empty directed graph `resource_hierarchy`.

## Add Resources to the Hierarchy

For each train in the timetable:
    For each resource in the train's schedule:
        Add a node for the resource in `resource_hierarchy` with the train as an attribute.

## Connect Resources in the Hierarchy

For each train in the timetable:
    For each pair of connected resources in the train's schedule:
        Add a directed edge between the two resources in `resource_hierarchy` with the train as an attribute.

## Detect Conflicts

- Initialize an empty list `conflict_edges` to store edges with conflicts.

For each edge in `resource_hierarchy.edges`:
    Get the trains associated with the connected resources.
    If the trains are different:
        Add the edge to `conflict_edges` as a conflict.

## Visualize the Resource Hierarchy

- Visualize the resource hierarchy using a tree graph.
- Highlight conflict edges in a different color.

## Output Conflicts

For each edge in `conflict_edges`:
    Print details of the conflict, including the connected resources and associated trains.


```

## Result
In a small network, we can generate graphs like this to be solved by different algorithms.

![Screenshot 2024-01-25 164417](https://github.com/dssdanial/Graph_Opt_RL/assets/32397445/d4488039-9b85-4e4a-ac62-04f62a3b1f2f)


## Conclusion
However, while effective for smaller datasets, the brute force algorithm may become computationally intensive for larger graphs due to its exhaustive nature. Nonetheless, this approach ensures a comprehensive exploration of potential solutions, guaranteeing the identification of conflicts and providing valuable insights into resource utilization optimization.


## Future Work
Future work could involve scalability for larger graphs using techniques like **graph embeddings** and **Reinforcement Learning** Algorithms, handling dynamic graph changes, incorporating transfer learning, advanced conflict resolution strategies, and domain-specific RL models. Interactive visualization tools, benchmarking datasets, and human-in-the-loop RL approaches are crucial for effective evaluation and real-world applicability
