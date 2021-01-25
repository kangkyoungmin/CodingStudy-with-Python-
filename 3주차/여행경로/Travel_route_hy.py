def solution(tickets):
    routes = {} # 딕셔너리 구성
    for t in tickets: # 출발지:도착지 dic만듦
        if t[0] not in routes.keys():
            routes[t[0]] = [t[1]]
        else:
            routes[t[0]] = [t[1]]
    for r in routes.keys(): # 딕셔너리 돌면서 항공권 리스트 역순 정렬/ pop()대비해 알파벳순서대로 뽑히도록
        routes[r].sort(reverse=True)
    stack = ['ICN']
    path = []
    while stack:
        top = stack[-1]
        if top in routes and routes[top]: # 갈 수 있는 항공권이 있으면 항공권의 리스트에서 선택하고 스택에 저장
            stack.append(routes[top].pop())
        else: # 갈 수 있는 항공권이 없으면 스택에서 빼 path에 추가
            path.append(stack.pop())

    return path[::-1] # path 거꾸로 돌림(스택은 선입후출이기때문)
