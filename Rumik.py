def combination_sum2(candidates, target):
    def backtrack(start, path, target):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            backtrack(i + 1, path + [candidates[i]], target - candidates[i])

    candidates.sort()
    result = []
    backtrack(0, [], target)
    return result
candidates1 = [2, 5, 2, 1, 2]
target1 = 5
print(combination_sum2(candidates1, target1))  # [[1, 2, 2], [5]]

candidates2 = [10, 1, 2, 7, 6, 1, 5]
target2 = 8
print(combination_sum2(candidates2, target2))  # [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
