import numpy as np
import matplotlib.pyplot as plt

time_heatmap_start = np.loadtxt('time_heatmap_start.csv', delimiter=',').reshape(-1, 50, 50)
time_heatmap_end = np.loadtxt('time_heatmap_end.csv', delimiter=',').reshape(-1, 50, 50)

# 初始状态每个地区的储量
store_amount = []
store_amount.append(np.ones((50, 50)) * 100)

import seaborn as sns
# 模拟自行车的迁移过程
for i, (start, end) in enumerate(zip(time_heatmap_start, time_heatmap_end)):
    store_amount.append(store_amount[i] - start + end)
    
# 计算不同时间的自行车利用率
sum_num = 50 * 50 * 100
used_rate = []
for i, (need, stored) in enumerate(zip(time_heatmap_start, store_amount)):
    # 去store_amount除负值
    stored[stored < 0] = 0
    
    # 取need和stored中的较小值
    used = np.minimum(need, stored)
    used_rate.append(np.sum(used) / sum_num)

for i in used_rate:
    print(i)

plt.plot(used_rate)
plt.xlabel('time')
plt.ylabel('used rate')
plt.show()    
    