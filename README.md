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
| Train  | Source 1 | Source 2 | Source 3 | Source 4 | Departure Time | Arrival Time |
|--------|----------|----------|----------|----------|----------------|--------------|
| Train1 | 10:00    | 10:05    | 10:10    | 10:20    | -              | -            |
| Train2 | -        | 10:00    | -        | 10:05    | -              | -            |
| Train3 | -        | 10:30    | 10:35    | 10:20    | -              | -            |

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
FUNCTION create_resource_graph(timetable)
    resource_graph = CREATE_EMPTY_GRAPH()
    FOR EACH train IN timetable
        FOR EACH resource IN train
            ADD_NODE(resource) TO resource_graph WITH time_interval ATTRIBUTE
            ADD_EDGES_BETWEEN_RESOURCES IF SHARED BY TRAINS
    RETURN resource_graph

FUNCTION find_resource_conflict_solution(graph)
    nodes_list = GET_NODES_OF(graph)
    GENERATE_ALL_COMBINATIONS_OF_NODES(nodes_list) INTO solutions_check
    is_found = False
    FOR EACH solution IN solutions_check
        temp_graph = COPY(graph)
        FOR EACH node IN solution
            REMOVE_NODE(node) FROM temp_graph
            IF NO_EDGES_LEFT_IN(temp_graph)
                is_found = True
                RECORD solution_nodes = solution
                BREAK
        IF is_found
            BREAK
    IF is_found
        PRINT solution_nodes
    ELSE
        PRINT " No solution found "

```

## Result
In a small network, we can generate graphs like this to be solved by different algorithms.

![image](https://github.com/dssdanial/Graph_Search_Brute_Force_algorithm/assets/32397445/eaa75e60-c63e-42f5-ab03-6a9400352774)


## Conclusion
However, while effective for smaller datasets, the brute force algorithm may become computationally intensive for larger graphs due to its exhaustive nature. Nonetheless, this approach ensures a comprehensive exploration of potential solutions, guaranteeing the identification of conflicts and providing valuable insights into resource utilization optimization.
