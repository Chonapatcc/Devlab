n, num_path = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(num_path):
    x,y,dist = map(int, input().split())
    graph[x][y] = dist
    graph[y][x] = dist



def dijkstra(start):
    visited = [False] * (n+1)
    distance = [float('inf')] * (n+1)
    distance[start] = 0

    for _ in range(n):
        min_dist = float('inf')
        min_index = -1
        for i in range(1, n+1):
            if not visited[i] and distance[i] < min_dist:
                min_dist = distance[i]
                min_index = i

        if min_index == -1:
            break

        visited[min_index] = True

        for j in range(1, n+1):
            if graph[min_index][j] != 0 and not visited[j]:
                new_dist = distance[min_index] + graph[min_index][j]
                if new_dist < distance[j]:
                    distance[j] = new_dist

    return distance

dijkstra_result = dijkstra(1)
print(dijkstra_result[-1])