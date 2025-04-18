def merge(intervals):
    answer = []
    answer_interval = intervals[0]
    index = 1
    while index < len(intervals):
        current_interval = intervals[index]

        if current_interval[0] <= answer_interval[1]:
            if answer_interval[1] < current_interval[1]:
                answer_interval[1] = current_interval[1]
        else:
            answer.append(answer_interval)
            answer_interval = current_interval
        
        if index == len(intervals) - 1:
            answer.append(answer_interval)

        index += 1

    return answer

print(merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))
print(merge(intervals = [[1,4],[4,5]]))

print(merge(intervals = [[1,4],[0,0]]))
print(merge(intervals = [[1,3], [2,6] ,[8,10] ,[8,9], [9,11],[15,18], [2,4] ,[16,17]]))

"""
[[1,3],[2,6],[8,10],[15,18]]
[[1,4],[4,5]]
[[1,4],[0,0]]
[[1,3], [2,6] ,[8,10] ,[8,9], [9,11],[15,18], [2,4] ,[16,17]]
"""