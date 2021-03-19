# programmers L3 : 광고 삽입
# solved by JY + hint
# DATE : 2021.03.19
# 문자열 처리
# 1초마다 시청자 수 저장 > 누적시간 구하기 > 광고시간만큼의 구간 중 누적시간 가장 많은 곳

def get_second(time):
    h, m, s = time.split(':')
    return int(h)*60*60 + int(m)*60 + int(s)

def get_time(second):
    h, m, s = second//(60*60), (second%(60*60))//60, (second%(60*60))%60
    # return "%02d:%02d:%02d"%(h,m,s)
    return f"{h:02d}:{m:02d}:{s:02d}"

def solution(play_time, adv_time, logs):
    pt, adt = get_second(play_time), get_second(adv_time)
    dic = [0] * (pt+1)

    for idx, log in enumerate(logs):    # 시작시간은 +1, 끝나는 시간은 -1로 처리
        s, e = log.split('-')
        s, e = get_second(s), get_second(e)
        dic[s] += 1
        dic[e] -= 1

    for idx in range(1, pt):    # 시청 구간 처리. dic[x] = x시각에 몇명이 보고있는가
        dic[idx] += dic[idx-1]

    for idx in range(1, pt):    # 누적 시간 처리. dic[x] = x시각까지 누적시간 저장
        dic[idx] += dic[idx-1]

    max_t, check = 0, 0
    for idx in range(adt - 1, pt):  # 광고시간(adt)만큼의 구간 기준 누적 시간 제일 많은 곳 구하기
        if max_t < dic[idx] - dic[idx-adt]:
            max_t = dic[idx] - dic[idx-adt]
            check = idx

    return get_time(check - adt + 1)

# run test
print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]), "01:30:59")
# print(solution())