class Solution:
    def findRestaurant(self, list1, list2):
        map1 = dict()
        for i in range(len(list1)):
            map1[list1[i]] = i

        min_index_sum = 2001
        for i in range(len(list2)):
            if list2[i] not in map1:
                continue
            index_sum = i + map1[list2[i]]
            if index_sum < min_index_sum:
                min_index_sum = index_sum

        res = []
        for i in range(len(list2)):
            if list2[i] not in map1:
                continue
            index_sum = i + map1[list2[i]]
            if index_sum == min_index_sum:
                res.append(list2[i])
        return res
