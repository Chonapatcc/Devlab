n_town,n_path = map(int,input().split())

path_list = {}
for i in range(n_path):
    start,end,dist = map(int,input().split())

    if start in path_list:
        if end in path_list[start]:
            if path_list[start][end] > dist:
                path_list[start][end] = dist
        else:
            path_list[start][end] = dist
    else:
        path_list[start] = {end: dist}
    # one way only

min_dist = -1 
path_use_global = []
def shortest_path(t1,t2,sum_dist,path_used):
    
    path_used = path_used + [t2]
    path_used = path_used.copy()

    new_dist = sum_dist + path_list[t1][t2]
    if t2 == n_town:
        global min_dist
        global path_use_global
        if new_dist > min_dist and min_dist != -1:
            return 
        if min_dist == -1 or new_dist < min_dist:
            min_dist = new_dist
            path_use_global = path_used
        return

    if t2 not in path_list:
        return
    for i in list(path_list[t2].keys()):
        shortest_path(t2,i,new_dist,path_used)


for i in list(path_list[1].keys()):
    shortest_path(1,i,0,[1])

if min_dist == -1:
    print("-1")
else:
    print(" ".join(map(str,path_use_global)))
    print(min_dist)






