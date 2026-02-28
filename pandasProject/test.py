import pandas as pd
import numpy as np
import random

# 设置随机种子，保证每次生成的数据一致
np.random.seed(42)
random.seed(42)

# 定义基础数据列表
countries = ["France", "Italy", "Spain", "US", "Chile", "Argentina", "Australia", "Germany", "Portugal", "New Zealand"]
provinces = ["California", "Bordeaux", "Tuscany", "Catalonia", "Mendoza", "Barossa Valley", "Mosel", "Douro", "Marlborough", "Rioja"]
varieties = ["Cabernet Sauvignon", "Chardonnay", "Pinot Noir", "Merlot", "Syrah", "Sauvignon Blanc", "Riesling", "Zinfandel", "Malbec", "Sangiovese"]
wineries = ["Domaine de la Romanée-Conti", "Penfolds", "Vega Sicilia", "Opus One", "Catena Zapata", "Cloudy Bay", "Torres", "Antinori", "Caymus", "Henschke"]

# 生成100条模拟数据
data = {
    "country": [random.choice(countries) for _ in range(100)],
    "description": [f"This is a sample wine description {i+1} with rich flavors and a long finish." for i in range(100)],
    "designation": [f"Vineyard {random.choice(['A', 'B', 'C', 'D', 'E'])} {random.randint(1, 10)}" for _ in range(100)],
    "points": np.random.randint(80, 100, 100),  # 分数在80-100之间
    "price": np.round(np.random.uniform(10, 2000, 100), 2),  # 价格在10-2000之间，保留两位小数
    "province": [random.choice(provinces) for _ in range(100)],
    "region_1": [f"Region {random.randint(1, 5)}" for _ in range(100)],
    "region_2": [f"Sub-region {random.randint(1, 3)}" for _ in range(100)],
    "variety": [random.choice(varieties) for _ in range(100)],
    "winery": [random.choice(wineries) for _ in range(100)]
}

# 创建DataFrame
df = pd.DataFrame(data)

# 保存为CSV文件，使用utf-8-sig编码避免中文乱码
df.to_csv("winemag-data_first100k.csv", index=False, encoding="utf-8-sig")

# 打印前5行数据，验证生成结果
print("生成的CSV文件前5行数据：")
print(df.head())

print("\n✅ CSV文件已成功生成，文件名为：winemag-data_first100k.csv")