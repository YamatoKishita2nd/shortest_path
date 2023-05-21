# 淵野辺駅から渋谷駅までの経路の内、最短乗車時間、及び、その経路を求める

points = ["淵野辺", "町田", "橋本", "長津田", "菊名", "調布", "明大前", "下北沢", "渋谷"]

routes = {
    ((points[points.index("淵野辺")], points[points.index("町田")]), 6), ((points[points.index("淵野辺")], points[points.index("橋本")]), 8), ((points[points.index("淵野辺")], points[points.index("長津田")]), 13), ((points[points.index("淵野辺")], points[points.index("菊名")]), 30),  # 淵野辺から
    ((points[points.index("町田")], points[points.index("下北沢")]), 26), ((points[points.index("町田")], points[points.index("渋谷")]), 30),  # 町田から
    ((points[points.index("橋本")], points[points.index("調布")]), 27), ((points[points.index("橋本")], points[points.index("明大前")]), 45), # 橋本から
    ((points[points.index("長津田")], points[points.index("渋谷")]), 34),  # 長津田から
    ((points[points.index("菊名")], points[points.index("渋谷")]), 20),  # 菊名から
    ((points[points.index("調布")], points[points.index("明大前")]), 10),  # 調布から
    ((points[points.index("明大前")], points[points.index("渋谷")]), 7),  # 明大前から
    ((points[points.index("下北沢")], points[points.index("渋谷")]), 4),  # 下北沢から
}

# ひとつ前の駅と、そこからの距離を求めるデータ構造にする
def get_reverse_graph(routes):
    graph = {}
    for route in routes:
        from_point = route[0][0]
        to_point = route[0][1]
        dist = route[1]
        if not to_point in graph:
            graph[to_point] = []
        graph[to_point].append((from_point, dist))
    return graph

def get_min_path(graph, start_point, end_point):
    # 最短乗車時間を求める
    determined = {start_point: 0}
    undetermined = set(graph.keys())

    while not end_point in determined:
        for point in undetermined:
            check = 0
            for i in range(len(graph[point])):
                if graph[point][i][0] in determined:
                    check += 1

            if check == len(graph[point]):
                min_dist = determined[graph[point][0][0]] + graph[point][0][1]
                for i in range(1, len(graph[point])):
                    if determined[graph[point][i][0]] + graph[point][i][1] <= min_dist:
                        min_dist = determined[graph[point][i][0]] + graph[point][i][1]
                determined[point] = min_dist
                undetermined.remove(point)
                break
    
    # 最短乗車時間の経路を求める
    min_path = [end_point]
    curt_point = end_point
    
    while True:
        cur_dist = determined[curt_point] - graph[curt_point][0][1]
        next_point = graph[curt_point][0][0]
        
        for i in range(1, len(graph[curt_point])):
            if determined[curt_point] - graph[curt_point][i][1] > cur_dist:
                cur_dist = determined[curt_point] - graph[curt_point][i][1]
                next_point = graph[curt_point][i][0]

        curt_point = next_point
        min_path.append(curt_point)

        if start_point in min_path:
            break

    return determined[end_point], ' → '.join(list(reversed(min_path)))

graph = get_reverse_graph(routes)

start_point = points[0]
end_point = points[len(points) - 1]

result = get_min_path(graph, start_point, end_point)
print(f"{start_point}から{end_point}の最短乗車時間は{result[0]}分で、その経路は{result[1]}です。")