class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = list(zip(difficulty, profit))
        jobs.sort()
        ans = i = best = 0
        for skill in sorted(worker):
            while i < len(jobs) and skill >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i += 1
            ans += best
        return ans


def test_max_profit():
    assert (Solution().maxProfitAssignment(
        [2, 4, 6, 8, 10],
        [10, 20, 30, 40, 50],
        [4, 5, 6, 7]
    ) == 100)


def test_max_profit_2():
    assert (Solution().maxProfitAssignment(
        [85, 47, 57],
        [24, 66, 99],
        [40, 25, 25],
    ) == 0)


def test_max_profit_3():
    assert (Solution().maxProfitAssignment(
        [68, 35, 52, 47, 86],
        [67, 17, 1, 81, 3],
        [92, 10, 85, 84, 82],
    ) == 324)
