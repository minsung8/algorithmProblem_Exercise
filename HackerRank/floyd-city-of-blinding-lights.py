n, m = tuple(int(x) for x in input().strip().split())
edges = {}

for i in range(1, n + 1):
    edges[i] = []


for _ in range(m):
    f, t, r = tuple(int(x) for x in input().strip().split())
    try:
        idx = next(i for i,(to,_) in enumerate(edges[f]) if to == t)
        edges[f][idx] = [t, r]
    except StopIteration:
        edges[f].append([t, r])

question = [
    tuple(int(x) for x in input().strip().split())
        for _ in range(int(input()))
]

questions_dict = {}

for xy_list in question:
    if xy_list[0] not in questions_dict:
        questions_dict[xy_list[0]] = [xy_list[1]]
    else:
        questions_dict[xy_list[0]].append(xy_list[1])

answer = {}
for start, ends in questions_dict.items():

    visited = [start]
    dist = {node: -1 for node in range(1, n+1)}
    dist[start] = 0

    while visited:

        next_visited = set()

        for node in visited:

            cur_cost = dist[node]

            for node_cost in edges[node]:

                next_cost = cur_cost + node_cost[1]

                if dist[node_cost[0]] == -1 or next_cost < dist[node_cost[0]]:
                    dist[node_cost[0]] = next_cost
                    next_visited.add(node_cost[0])

        visited = next_visited

    for end in ends:
        answer[(start, end)] = dist[end]

for start, end in question:
    print(answer[(start, end)])
