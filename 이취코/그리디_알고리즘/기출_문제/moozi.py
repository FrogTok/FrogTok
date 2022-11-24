import heapq

def solution(food_times, k):   
    if(sum(food_times) <= k):
        return -1
    answer = -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))
    
    sum_eated = 0
    remain_food_num = len(food_times)
    cycle = 0
    while sum_eated + (q[0][0] - cycle) * remain_food_num <= k:
        food_time = heapq.heappop(q)[0]
        sum_eated += (food_time - cycle) * remain_food_num
        cycle = food_time
        remain_food_num -= 1
        
    result = sorted(q, key = lambda x : x[1])
    return result[(k-sum_eated) % remain_food_num][1]