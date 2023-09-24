G = int(input())

def getMyDivisor(n):
    # 약수 목록 구하는 함수

    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append((i, n // i)) 
            
    
    return divisorsList

divisorsList = getMyDivisor(G)

result = []
for c, d in divisorsList:
    # c : 작은 수
    # d : 큰수
    if (d+c) % 2 == 0 and (d != c): # 정수로 떨어지는 경우
        # c+d가 2로 나누어 떨어지면, d-c도 2로 나누어 떨어짐
        # 같은 수로 분해되는 경우 원래 알고 있는 무게가 0이므로 제외
        result.append((d+c)//2)

if len(result) == 0:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)