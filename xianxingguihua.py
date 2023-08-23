import pulp

# 目标函数系数
z = [25, 30]
# 约束条件
a = [[20, 30], [5, 4]]
b = [690, 120]
m = pulp.LpProblem(sense=pulp.LpMaximize)
x = [pulp.LpVariable(f'x{i}', lowBound=0) for i in range(len(z))]
m += pulp.lpDot(z, x)
for i in range(len(a)):
    m += (pulp.lpDot(a[i], x) <= b[i])
m.solve()
print(f'优化结果:{pulp.value(m.objective)}')
print(f'参数结果:{[pulp.value(var) for var in x]}')
