import sys
answer = -sys.maxsize
input = sys.stdin.readline

nums, op = [], []

def dfs(idx, sub_total):
    global answer

    if idx == len(op):
        answer = max(answer, int(sub_total))
        return

    # (3 + 8) * 7 - 9 * 2 부터 시작.
    first = str(eval(sub_total + op[idx] + nums[idx + 1]))
    dfs(idx + 1, first)

    if idx + 1 < len(op):
        # 3 + (8 * 7) - 9 * 2 부터 시작
        second = str(eval(nums[idx + 1] + op[idx + 1] + nums[idx + 2]))
        second = str(eval(sub_total + op[idx] + second))
        # op를 2개 소모했으므로 idx + 2
        dfs(idx + 2, second)


if __name__ == '__main__':
    n = int(input().rstrip())
    expression = input().rstrip()

    for index, char in enumerate(expression):

        if index % 2 == 0:
            nums.append(char)
        else:
            op.append(char)

    dfs(0, nums[0])
    print(answer)