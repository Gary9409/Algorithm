import bisect


class BinarySearch:
    def my_binary_search(self, lst, target, start, end):
        if start > end:
            return -1

        # 오버플로우 방지
        # p = (start + end) // 2
        p = start + (end - start) // 2

        # 가운데 값이 타겟보다 작으면 앞 절반을 제외
        if lst[p] < target:
            return self.my_binary_search(lst, target, p + 1, end)
        # 가운데 값이 타겟보다 크면 뒤 절반을 제외
        elif lst[p] > target:
            return self.my_binary_search(lst, target, start, p - 1)
        # 가운데 값이 타겟일 경우 리턴
        else:
            return p

    def binary_search(self, lst, target, start, end):
        # bisect 모듈 이용
        idx = bisect.bisect_left(lst, target, start, end)

        if idx < len(lst) and lst[idx] == target:
            return idx
        else:
            return -1