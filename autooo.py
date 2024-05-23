# step1.관련 패키지 및 모듈 import
import schedule
import time

# step2.실행할 함수 선언
def message1():
    print("6")
    print("스케쥴 실행중...")


print("1")
# step3.실행 주기 설정
schedule.every(3).seconds.do(message1)
print("2")
# step4.스캐쥴 시작
while True:
    print("3")
    schedule.run_pending()
    print("4")
    time.sleep(1)
    print("5")