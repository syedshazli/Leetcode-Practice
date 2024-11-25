# How I think it should go
# INITIALIZATION
# keep a list of visited nodes, initially empty
# keep a stack, do store which items to go thru next
# a list of neighbors
# TRAVERSING THROUGH 
def dfs(Graph, vertice):
    marked = [False] * len(Graph)
    stack = []
    while len(stack) >0:
      v = stack.pop()
      
      if not marked[v]:
        marked[v] = True
        for v in vertice.neighbors():
          if not marked[v]:
            stack.append(v)
