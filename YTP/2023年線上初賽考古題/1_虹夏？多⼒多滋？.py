import math

def distance(p1, p2):
    return round(math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2))

def are_triangles_congruent(t1, t2):
    #T1 = d or n
    #T2 = user_input
    T1 = [
        int(distance(t1[0], t1[1])),
        int(distance(t1[1], t1[2])),
        int(distance(t1[2], t1[0]))
    ]
    T2 = [
        int(distance(t2[0], t2[1])),
        int(distance(t2[1], t2[2])),
        int(distance(t2[2], t2[0]))
    ]
    T1.sort()
    T2.sort()
    if T1 == T2:
        return True
    return False

# main program
# 輸入 "判斷用" 三角形的三點座標
n = list(map(int, input().split())) #Nijika
d = list(map(int, input().split())) #Doritos
# 分割成一個座標為一組的list
n = [[n[i], n[i+1]] for i in range(0, 6, 2)]
d = [[d[i], d[i+1]] for i in range(0, 6, 2)]

run = int(input())
for i in range(run):
    # print(user_input)
    user_input = list(map(int, input().split()))
    # 分割成一個座標為一組的list
    user_input = [[user_input[i], user_input[i+1]] for i in range(0, 6, 2)]
    
    #判斷
    if are_triangles_congruent(n, user_input):
        print("Nijika")
    elif are_triangles_congruent(d, user_input):
        print("Doritos")
    else:
        print("None")