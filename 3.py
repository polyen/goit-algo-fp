import heapq


def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def test_dijkstra():
    # Test case 1
    graph1 = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    assert dijkstra(graph1, 'A') == {'A': 0, 'B': 1, 'C': 3, 'D': 4}

    # Test case 2
    graph2 = {
        'A': {'B': 3, 'C': 6},
        'B': {'A': 3, 'C': 4, 'D': 7},
        'C': {'A': 6, 'B': 4, 'D': 8},
        'D': {'B': 7, 'C': 8}
    }
    assert dijkstra(graph2, 'A') == {'A': 0, 'B': 3, 'C': 6, 'D': 10}

    # Test case 3
    graph3 = {
        'A': {'B': 5, 'D': 9, 'E': 2},
        'B': {'A': 5, 'C': 2},
        'C': {'B': 2, 'D': 3},
        'D': {'A': 9, 'C': 3, 'F': 2},
        'E': {'A': 2, 'F': 3},
        'F': {'D': 2, 'E': 3}
    }
    assert dijkstra(graph3, 'A') == {'A': 0, 'B': 5, 'C': 7, 'D': 7, 'E': 2, 'F': 5}


if __name__ == "__main__":
    test_dijkstra()
