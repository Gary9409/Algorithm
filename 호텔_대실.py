# https://school.programmers.co.kr/learn/courses/30/lessons/155651

def solution(book_time):
    answer = 0
    rooms = []
    
	# 시간 문자열을 정수로 변환
    def toSec(time):
        h, m = time.split(':')
        return int(h) * 60 + int(m)
    
	# 대실 시작 시각을 기준으로 소팅
    for start, end in sorted(book_time):
        start = toSec(start)
        end = toSec(end)
        
		# 사용중인 방이 하나도 없으면 방 추가
        if not rooms:
            rooms.append(end)
            answer = max(answer, len(rooms))
            continue
        
		# 사용하는 방 목록을 순회하며 이전 예약의 종료 시각 + 10분보다 현재 예약의 시작 시각이 큰 경우를 찾아 교체
        flag = 0
        for i in range(len(rooms)):
            if rooms[i] + 10 <= start:
                rooms[i], flag = end, 1
                break;
        
        if flag == 0:
            rooms.append(end)
            
        answer = max(answer, len(rooms))
            
    return answer


book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
# result = 3
print(f'#1\nbook_time = {book_time}\nresult = {solution(book_time)}\n')

book_time = [["09:10", "10:10"], ["10:20", "12:20"]]
# result = 1
print(f'#2\nbook_time = {book_time}\nresult = {solution(book_time)}\n')

book_time = [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]
# result = 3
print(f'#3\nbook_time = {book_time}\nresult = {solution(book_time)}')
