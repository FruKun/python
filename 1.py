f = open("1.txt", "r")
a = f.read()
f.close()
words = a.split()
graph={}
for word in range(0,len(words)-1):
    graph[words[word]] = [words.count(words[word]), [words[word-1],words[word+1]]]

visited = [] 
queue = []   
def bfs(visited, graph, node):
    global queue
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print (s, end = " ")
        for neighbour in graph[s][1]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

bfs(visited, graph, 'abba')