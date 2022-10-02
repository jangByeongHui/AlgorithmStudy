

# 테스트 케이스 회수 입력
T = int(input())

directions = [(0,1),(0,-1),(1,0),(-1,0)]

# 문자열 계산

def dfs(matrix,x,y,count,result,set_result):

    if count == 7:
        set_result.add(result)
        return

    for dx, dy in directions:
        tx = x + dx
        ty = y + dy

        if 0 <= tx < 4 and 0 <= ty < 4:
            dfs(matrix,tx,ty,count+1,result+matrix[tx][ty],set_result)

# 매 횟수 마다 실행 함수
def solution(index):

    board = []
    set_result = set()

    for _ in range(4):
        board.append(list(input().split()))

    for i in range(4):
        for j in range(4):
            dfs(board,i,j,0,"",set_result)

    print(f"#{index+1} {len(set_result)}")


# 테스트 케이스 별 실행
for index in range(T):
    solution(index)


