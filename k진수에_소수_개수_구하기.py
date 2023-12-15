# https://school.programmers.co.kr/learn/courses/30/lessons/92335

def solution(n, k):
    def baseX(n, k):
        ret = ''
        while n:
            n, r = divmod(n, k)
            ret = str(r) + ret
        return ret

    def isPrime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False

        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6

        return True

    answer = 0
    for num in [int(seg) for seg in baseX(n, k).split('0') if seg != '']:
        answer += isPrime(num)

    return answer


n, k = 437674, 3
print (f"#1\nn = {n}\nk = {k}\nanswer = {solution(n, k)}\n")
n, k = 110011, 10
print (f"#2\nn = {n}\nk = {k}\nanswer = {solution(n, k)}")