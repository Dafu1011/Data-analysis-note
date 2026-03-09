import pandas as pd

# 创建数据
data = {
    'name': ['刘海柱', '赵金龙', '周立齐', '于谦'],
    'AKA': ['职业法师', '大力哥', '窃格瓦拉', '相声皇后']
}

# 生成DataFrame
df = pd.DataFrame(data)

# 保存为CSV文件
csv_filename = 'Data/people_aka.csv'
df.to_csv(csv_filename, index=False, encoding='utf-8-sig')

print(f"CSV文件 {csv_filename} 已生成完成！")