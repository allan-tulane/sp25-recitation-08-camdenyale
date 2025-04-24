# CMPS 2200 Recitation 08

## Answers

**Name:**   Camden Yale

**Name:**   Emily Aymond


Place all written answers from `recitation-08.md` here for easier grading.



- **1b)**
  
The work is O((V + E)Log V)   

The span is O(log V * D)


- **2b)**

graph = get_sample_graph()
parents = bfs_path(graph, 's')
paths = get_path(parents, 'd')
print(paths)
Output: sbc
