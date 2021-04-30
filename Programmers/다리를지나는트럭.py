def solution(bridge_length, weight, truck_weights):
    queue = []
    idx = 0
    bridge = []
    cnt = 1
    while (idx) < len(truck_weights):
        if len(queue) >= 1:
            if bridge[0] >= bridge_length:
                queue.pop(0)
                bridge.pop(0)
        if len(queue) >= 1:
            for j in range(len(bridge)):
                bridge[j] += 1
        if sum(queue) + truck_weights[idx] <= weight:
            queue.append(truck_weights[idx])
            bridge.append(1)
            idx += 1
        cnt += 1
    cnt += bridge_length - bridge[0]
    return cnt

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
solution(bridge_length, weight, truck_weights)