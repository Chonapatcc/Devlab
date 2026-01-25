n , num_paths = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(num_paths):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1


def longest_path(start,path_used,counter):
    if counter not in mapper:
        mapper[counter] = [path_used]
    else:
        mapper[counter].append(path_used)
    for i in range(start+1, n+1):
        if graph[start][i] == 1:
            longest_path(i, path_used + [i], counter + 1)


mapper = {}
for i in range(1, n+1):
    longest_path(i, [i], 0)

max_length = max(mapper.keys())
result_paths = [[path[0], path[-1]] for path in mapper[max_length]]
result_paths = list(set(tuple(path) for path in result_paths))
result_paths = sorted(result_paths)
# print(result_paths)
print(max_length)

lst = [f"({path[0]},{path[-1]})" for path in result_paths]
print(" ".join(lst)) 



