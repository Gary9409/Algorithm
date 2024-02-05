# https://school.programmers.co.kr/learn/courses/30/lessons/92341

def solution(fees, records):
    answer, acc = [], dict()

    for r in records:

        # 레코드 가져와서 split()으로 분리
        time, num, status = r.split()
        h, m = map(int, time.split(':'))

        # 시간:분 형태를 분으로 변환
        mins = h * 60 + m

        # 딕셔너리에 번호가 없으면 추가
        if num not in acc:
            acc[num] = list()

        # IN이면 시간에 -1을 곱해서 추가
        if len(status) == 2:
            acc[num].append(-mins)
        else:
            acc[num].append(mins)

    for key in sorted(acc.keys()):

        # 시간 기록이 홀수개면 IN으로 끝난 것이므로 23:59 -> 1439분 추가
        if len(acc[key]) % 2 == 1:
            acc[key].append(1439)

        # IN은 음수, OUT은 양수이므로 모두 더해주면 총 누적 시간이 나옴
        total = sum(acc[key])

        # fees의 원소를 대입해서 요금 계산
        if total <= fees[0]:
            answer.append(fees[1])
        else:
            extra = ((total - fees[0]) // fees[2]) + ((total - fees[0]) % fees[2] != 0)
            answer.append(fees[1] + fees[3] * extra)

    return answer


fees, records = [180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
# result = [14600, 344400, 5000]
print(f'#1\nfees = {fees}\nrecords = {records}\nresult = {solution(fees, records)}\n\n')

fees, records = [120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
# result = [0, 591]
print(f'#2\nfees = {fees}\nrecords = {records}\nresult = {solution(fees, records)}\n\n')

fees, records = [1, 461, 1, 10], ["00:00 1234 IN"]
# result = [14841]
print(f'#3\nfees = {fees}\nrecords = {records}\nresult = {solution(fees, records)}')