import sys
import heapq

def solve():
    input = sys.stdin.read
    data = input().split()
    iterator = iter(data)

    try:
        time_num = int(next(iterator))
        path_num = int(next(iterator))
    except StopIteration:
        return

    # time_list[i] is the green/red duration for node i+1
    time_list = []
    for _ in range(time_num):
        time_list.append(int(next(iterator)))

    # Building the Adjacency List (Directed Graph)
    # Using a list of dicts for O(1) edge lookups
    adj = [{} for _ in range(time_num + 1)]
    
    for _ in range(path_num):
        u = int(next(iterator))
        v = int(next(iterator))
        w = int(next(iterator))
        
        # Store the minimum distance if multiple edges exist between same nodes
        if v in adj[u]:
            if w < adj[u][v]:
                adj[u][v] = w
        else:
            adj[u][v] = w

    # Get time_to_school (last input)
    try:
        time_to_school = int(next(iterator))
    except StopIteration:
        time_to_school = 0

    # Dijkstra's Algorithm
    # dists[i] = shortest time to reach node i AND finish waiting for its light
    dists = {i: float('inf') for i in range(1, time_num + 1)}
    dists[1] = 0
    
    # Priority Queue stores: (current_accumulated_time, current_node)
    pq = [(0, 1)]
    
    while pq:
        current_time, u = heapq.heappop(pq)
        
        # Optimization: If we found a shorter way to 'u' before, skip this outdated path
        if current_time > dists[u]:
            continue
        
        # If we reached the destination (node time_num)
        if u == time_num:
            print(current_time + time_to_school)
            return

        # Check neighbors
        for v, travel_time in adj[u].items():
            arrival_time = current_time + travel_time
            
            # --- Traffic Light Logic ---
            # Determine wait time at node v based on arrival_time
            green_duration = time_list[v-1]
            wait_time = 0
            
            # If duration is 0, we assume no light (or always green) to avoid div by zero
            if green_duration > 0:
                cycle_period = 2 * green_duration
                # Find position in the Green-Red cycle
                phase = arrival_time % cycle_period
                
                # Logic: [0 to G) is Green, [G to 2G) is Red
                if phase >= green_duration:
                    # It is Red, wait until cycle completes
                    wait_time = cycle_period - phase
            
            total_time_at_v = arrival_time + wait_time
            
            # If this path is faster than any previous path to v, push to PQ
            if total_time_at_v < dists[v]:
                dists[v] = total_time_at_v
                heapq.heappush(pq, (total_time_at_v, v))

    # If destination is unreachable
    print(-1)

if __name__ == "__main__":
    solve()