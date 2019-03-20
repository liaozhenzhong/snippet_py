class Solution:
    def is_judge(self, N, net, i):
        if any(net[i]):
            return False
        for j in range(i):
            if not net[j][i]:
                return False
        for j in range(i+1, N):
            if not net[j][i]:
                return False
        return True

    def findJudge(self, N, trust):
        net = [[False]*N for _ in range(N)]
        for i, j in trust:
            net[i-1][j-1] = True

        for i in range(N):
            if self.is_judge(N, net, i):
                return i + 1

        return -1

def test_find_judge_1():
    N = 2
    trust = [[1,2]]
    assert Solution().findJudge(N, trust) == 2

def test_find_judge_2():
    N = 3
    trust = [[1,3],[2,3]]
    assert Solution().findJudge(N, trust) == 3

def test_find_judge_3():
    N = 3
    trust = [[1,3],[2,3],[3,1]]
    assert Solution().findJudge(N, trust) == -1

def test_find_judge_4():
    N = 3
    trust = [[1,2],[2,3]]
    assert Solution().findJudge(N, trust) == -1

def test_find_judge_5():
    N = 4
    trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    assert Solution().findJudge(N, trust) == 3

test_find_judge_1()
