# 알파벳의 자릿수 저장
dic = {}

# 단어의 개수
n = int(input())

# 알파벳에 따른 알파벳의 자릿수 저장
for _ in range(n):

    word = input()

    for i in range(len(word)):
        # 해당 알파벳의 자릿수가 이미 있다면 자릿수를 추가
        if (word[i] in dic):
            dic[word[i]] += 10**(len(word)-i-1)
        # 해당 알파벳의 자릿수가 없다면 자릿수를 새롭게 저장
        else:
            dic[word[i]] = 10**(len(word)-i-1)

# 사전의 모든 값들을 결과 리스트에 추가한 뒤, 내림차순 정렬
result = []
for value in dic.values():
    result.append(value)
result.sort(reverse=True)

# 결과 리스트의 첫 번째 자릿수부터 순서대로 확인하며 숫자를 곱해주고,
# 곱셈 결과를 최종 결과값에 덧셈
sum = 0 # 최종 결과값
num = 9 # 곱할 숫자
for value in result:
    sum += value * num
    num -= 1

# 결과값 출력
print(sum)