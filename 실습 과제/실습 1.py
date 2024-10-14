import time

# 하노이 타워 함수
def hanoi_tower(n, fr, tmp, to, call_count):
    if n == 1:
        call_count[0] += 1
        print("원판 1: %s --> %s" % (fr, to))
    else:
        hanoi_tower(n - 1, fr, to, tmp, call_count)
        call_count[0] += 1
        print("원판 %d: %s --> %s" % (n, fr, to))
        hanoi_tower(n - 1, tmp, fr, to, call_count)

# 사용자 입력 받기
n = int(input("하노이 타워의 높이(최대 층 수)를 입력하세요: "))

# 호출 횟수 저장 변수
call_count = [0]

# 실행 시간 측정 시작
start_time = time.time()

# 하노이 타워 함수 호출
hanoi_tower(n, 'A', 'B', 'C', call_count)

# 실행 시간 측정 종료
end_time = time.time()

# 결과 출력
print("\n호출 횟수: %d" % call_count[0])
print("실행 시간: %.6f 초" % (end_time - start_time))
