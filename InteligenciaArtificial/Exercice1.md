# Exercice 1

By: Higor Ferreira Alves Santos

---

Consider the state space graph shown above. A is the start state and G is the goal state. The costs for each edge are shown on the graph. Each edge can be traversed in both directions. Note that the heuristic h1 is consistent but the heuristic h2​ is not consistent.

**(a) Possible paths returned**

For each of the following graph search strategies (_do not answer for tree search_), mark which, if any, of the listed paths it could return. Note that for some search strategies the specific path returned might depend on tie-breaking behavior. In any such cases, make sure to mark _all_ paths that could be returned under some tie-breaking scheme.

| Search Algorithm                 | A-B-D-G | A-C-D-G | A-B-C-D-F-G |
| -------------------------------- | ------- | ------- | ----------- |
| Depth first search               |         |         | X           |
| Breadth first search             |         | X       |             |
| Uniform cost search              |         |         | X           |
| A\* search with heuristic \(h1\) |         | X       |             |
| A\* search with heuristic \(h2\) |         | X       |             |

### Nós de árvore

```mermaid
flowchart TB
A((A)) -- 1 --> B((B))
A((A)) -- 4 --> C((C))
B2((B)) -- 1 --> A2((A))
B2((B)) -- 1 --> C2((C))
B2((B)) -- 5 --> D((D))
C3((C)) -- 4 --> A3((A))
C3((C)) -- 1 --> B3((B))
C3((C)) -- 3 --> D3((D))
```

```mermaid
flowchart TB
D4((D)) -- 5 --> B4((B))
D4((D)) -- 3 --> C4((C))
D4((D)) -- 8 --> E4((E))
D4((D)) -- 3 --> F4((F))
D4((D)) -- 9 --> G4((G))
E5((E)) -- 8 --> D5((D))
E5((E)) -- 2 --> G5((G))
F6((F)) -- 3 --> D6((D))
F6((F)) -- 5 --> G6((G))
```

```mermaid
flowchart TB
G7((G)) -- 9 --> D7((D))
G7((G)) -- 2 --> E7((E))
G7((G)) -- 5 --> F7((F))

```
