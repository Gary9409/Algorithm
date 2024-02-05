import sys
import statistics as st

nums = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
mode_list = st.multimode(nums)
mode = mode_list[0] if len(mode_list) == 1 else sorted(mode_list)[1]
print(round(st.mean(nums)), st.median(nums), mode, max(nums) - min(nums))