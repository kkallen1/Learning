# n = 角色數量 w = 金幣數量
n, w = map(int, input().split())
data = []
x = 1
for i in range(n):
    # z = [ai, bi, ci]
    z = list(map(int, input().split()))
    data.append(z) 

# 判斷最優策略升級的角色
judgment = []
for i in range(n):
    judgment.append(round(data[i][1]/data[i][2]))
judgment_max_index = judgment.index(max(judgment))

ans = data[judgment_max_index][0]
while w > 0:
    ans += 4
    x += 1
    w -= data[judgment_max_index][2]

for i in range(n):
    if i != judgment_max_index:
        ans += data[i][0]

print(ans)