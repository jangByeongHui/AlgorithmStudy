from collections import defaultdict, deque

used_alpha = defaultdict(bool)

alpha_pos = dict()

board = [[]for _ in range(5)]

plain_text = input()
key = input()

key_queue = deque()

for c in key:
    key_queue.append(c)

# 암호화 판에 글자수 채워 넣기
col_count = 0
row_count = 0
alpha = deque(list("A B C D E F G H I K L M N O P Q R S T U V W X Y Z".split()))

while key_queue:

    char = key_queue.popleft()

    if used_alpha[char]:
        continue
    used_alpha[char] = True

    board[row_count].append(char)
    col_count += 1

    if col_count == 5:
        col_count = 0
        row_count += 1

while alpha:
    if row_count == 5:
        break
    char = alpha.popleft()

    if used_alpha[char]:
        continue
    used_alpha[char] = True

    board[row_count].append(char)
    col_count += 1

    if col_count == 5:
        col_count = 0
        row_count += 1

for i in range(5):
    for j in range(5):
        alpha_pos[board[i][j]] = (i,j)

# 두 글자씩 페어 이루기
two_pairs = []
while len(plain_text) > 0:
    if len(plain_text) > 1:
        temp_plain_text = plain_text[:2]

        if temp_plain_text[0] == temp_plain_text[1] and temp_plain_text[0] != "X":
            temp_plain_text += "X"
            temp_plain_text = temp_plain_text[1:]
            plain_text = plain_text[1:] # 페어가 안됨으로 1칸
        elif temp_plain_text[0] == temp_plain_text[1] and temp_plain_text[0] == "X":
            temp_plain_text += "Q"
            temp_plain_text = temp_plain_text[1:]
            plain_text = plain_text[1:] # 페어가 안됨으로 1칸
        else:
            plain_text = plain_text[2:] # 이미 페어이기 때문에 2칸
        two_pairs.append("".join(temp_plain_text)) # 페어된 두 글자 추가

    else:
        temp_plain_text = plain_text[-1]
        two_pairs.append(temp_plain_text +"X")
        plain_text = plain_text[1:]

# 암호화하기
result = ""
for pair in two_pairs:
    first_r, first_c = alpha_pos[pair[0]]
    second_r, second_c = alpha_pos[pair[1]]

    if first_r == second_r:
        first_c = (first_c+1)%5
        second_c = (second_c+1)%5
    elif first_c == second_c:
        first_r = (first_r+1)%5
        second_r = (second_r+1)%5
    else:
        first_c, second_c = second_c, first_c

    result += board[first_r][first_c]
    result += board[second_r][second_c]

print(result)