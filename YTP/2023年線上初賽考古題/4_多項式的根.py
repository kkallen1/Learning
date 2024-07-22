import math

# 判別式, 查看有幾個根
def Discriminant(a, b, c):
    if a == 0 and b == 0:
        return 4
    
    delta = b**2 - 4*a*c
    if delta > 0: # 2個不同實數根
        return 2
    elif delta == 0: # 2個相同實數根
        return 1
    else: # 方程沒有實數根,方程有兩個共軛虛根
        return 3 # 2個虛根

def solve_quadratic(a, b, c):
    if Discriminant(a, b, c) == 4:
        return "NOTHING"
    elif a==0: #一次方 or 零次方
        if b==0: #零次方
            return 0
        return round(-c/b, 4) #零次方
    elif c == 0:
        return [round(-b/a, 4), 0.0]
    else: #二次方
        delta = Discriminant(a, b, c)
        if delta == 2: # 2個不同實數根
            ans_1 = round((-b + math.sqrt(b*b-4*a*c)) / (2*a), 4)
            ans_2 = round((-b - math.sqrt(b*b-4*a*c)) / (2*a), 4)
            return [ans_1, ans_2]
        elif delta == 1: # 2個相同實數根
            return round((-b / 2*a), 4)
        elif delta == 3: # 2個虛根
            ans_1 = round((-b + math.sqrt(-(b*b-4*a*c))) / (2*a), 4)
            ans_2 = round((-b - math.sqrt(-(b*b-4*a*c))) / (2*a), 4)
            return [ans_1, ans_2]

# main
# T組測試資料
T = int(input())
ans = [] # 存放答案
for k in range(T):
    # N組子測試資料
    N = int(input())
    data = [] #存放每組測試資料 
    roots = [] # 存放多項式的根

    for i in range(N):
        a, b, c = map(int, input().split())
        data.append([a, b, c])

        # 計算多項式的根並加入roots中
        roots.append(solve_quadratic(a, b, c))
    
    # 去除陣列中的陣列
    for k in range(len(roots)):
        for i in roots:
            z = roots.index(i)
            if type(i) == list:
                for j in roots[z]:
                    roots.append(j)
                roots.remove(roots[z])
            if i == "NOTHING":
                roots.remove(roots[z])

    # 去除重複的根
    roots.sort()
    Len = len(roots)
    for i in range(Len):
        if i != Len-1 and i < Len:
            if roots[i] == roots[i+1]:
                roots.remove(roots[i])
                Len -= 1
    ans.append(len(roots))

for i in ans:
    print(i)