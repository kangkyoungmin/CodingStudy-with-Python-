def solution(play_time, adv_time, logs):
    play_time = str_to_int(play_time)        # 1
    adv_time = str_to_int(adv_time)               
    all_time = [0 for i in range(play_time + 1)]

    for l in logs:                           # 2
        start, end = l.split('-')
        start = str_to_int(start)
        end = str_to_int(end)
        all_time[start] += 1
        all_time[end] -= 1
    # print(all_time)
    

    for i in range(1, len(all_time)):       # 3
        all_time[i] = all_time[i] + all_time[i - 1]
    print(all_time) # 특정 시청자의 시작 시간이 되면 1이 할당되고 그대로 쭉 1이 더해진다. 이 때 또 다른 시청자가 있으면 1이 더해져 2가 된다

    for i in range(1, len(all_time)):       # 4 모든 구간의 시청자 누적 기록
        all_time[i] = all_time[i] + all_time[i - 1]
    # print(all_time)

    most_view = 0                           # 5 누적된 시간의 시청자수에서 누적된 시간의 시청자수를 빼면 pure한 시청자수가 나온다
    max_time = 0                          
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i - adv_time]:
                most_view = all_time[i] - all_time[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]
                max_time = i - adv_time + 1

    return int_to_str(max_time)


def str_to_int(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def int_to_str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s

print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
# print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
# print(solution("50:00:00","50:00:00",["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))