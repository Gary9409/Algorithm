import sys
import time

class WordSort:
    def _compare(self, val1, val2):
        i, j = len(val1), len(val2)
        if i == j:
            for n, m in zip(val1, val2):
                if ord(n) != ord(m):
                    return ord(n) - ord(m)
        return i - j

    def merge(self, arr1, arr2):
        ret = []
        i = j = 0
        while i < len(arr1) and j < len(arr2):
            if self._compare(arr1[i], arr2[j]) < 0:
                ret.append(arr1[i])
                i += 1
            else:
                ret.append(arr2[j])
                j += 1
        if i < len(arr1):
            ret.extend(arr1[i:])
        if j < len(arr2):
            ret.extend(arr2[j:])
        return ret

    def merge_sort(self, lst):
        if len(lst) <= 1:
            return lst
        return self.merge(self.merge_sort(lst[:len(lst) // 2]), self.merge_sort(lst[len(lst) // 2:]))

    def quick_sort(self, lst, start, end):
        def partition(part, ps, pe):
            i = ps - 1
            for j in range(ps, pe):
                if self._compare(part[j], part[pe]) < 0:
                    i += 1
                    part[i], part[j] = part[j], part[i]
            part[i + 1], part[pe] = part[pe], part[i + 1]
            return i + 1

        if start >= end:
            return None

        p = partition(lst, start, end)
        self.quick_sort(lst, start, p - 1)
        self.quick_sort(lst, p + 1, end)
        return lst

words = set()
for _ in range(int(sys.stdin.readline())):
    words.add(sys.stdin.readline().strip())

sol = WordSort()
print(f'1. Merge Sort({len(words)}words): ')
start = time.time()
print(sol.merge_sort(list(words))[:10])
end = time.time()
print(f'{end - start} sec')
print('----------')
print(f'2. Quick Sort({len(words)}words):')
start = time.time()
print(sol.quick_sort(list(words), 0, len(words) - 1)[:10])
end = time.time()
print(f'{end - start} sec')
print('----------')
print(f'3. Tim Sort({len(words)}words):')
start = time.time()
print(sorted(list(words), key=lambda x: (len(x), x))[:10])
end = time.time()
print(f'{end - start} sec')