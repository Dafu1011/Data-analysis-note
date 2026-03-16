import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# ---------------------- 配置参数 ----------------------
np.random.seed(42)  # 固定随机种子，保证结果可复现
years = [2015, 2016, 2017, 2018]
# 各年份数据记录数
record_counts = {2015: 30774, 2016: 41278, 2017: 50839, 2018: 81349}
# 生成基础会员ID池（保证跨年份可重复下单）
total_members = 20000  # 总会员数
member_ids = [f"{random.randint(10 ** 10, 10 ** 11 - 1)}" for _ in range(total_members)]

# ---------------------- 1. 生成各年份订单数据 ----------------------
year_dfs = {}
for year in years:
    n = record_counts[year]
    data = []
    for _ in range(n):
        member_id = random.choice(member_ids)
        order_id = f"{random.randint(10 ** 10, 10 ** 11 - 1)}"  # 11位纯数字订单号
        # 生成该年份随机日期
        start_date = datetime(year, 1, 1)
        end_date = datetime(year, 12, 31)
        days_diff = (end_date - start_date).days
        random_days = random.randint(0, days_diff)
        submit_date = (start_date + timedelta(days=random_days)).strftime("%Y/%m/%d")

        # 生成订单金额：包含正常金额、NA值、异常值（<1元）
        rand = random.random()
        if rand < 0.02:  # 2% 概率为NA
            order_amount = np.nan
        elif rand < 0.05:  # 3% 概率为异常值（<1元）
            order_amount = round(random.uniform(0.01, 0.99), 8)
        else:  # 95% 概率为正常金额（参考示例金额范围）
            order_amount = round(random.choice([
                99, 199, 299, 399, 599, 899, 1299, 1999, 2599, 3599, 3646, 3999
            ]) + random.uniform(0, 0.99999999), 8)

        data.append([member_id, order_id, submit_date, order_amount])

    # 构造DataFrame
    df = pd.DataFrame(data, columns=["会员ID", "订单号", "提交日期", "订单金额"])
    year_dfs[year] = df
    print(
        f"✅ {year}年数据生成完成，共{len(df)}条记录，NA值数量：{df['订单金额'].isna().sum()}，异常值数量：{(df['订单金额'] < 1).sum()}")

# ---------------------- 2. 生成会员等级表 ----------------------
member_level_data = []
for member_id in member_ids:
    # 会员等级：1-4级，数字越大等级越高，按权重分布
    level = np.random.choice([1, 2, 3, 4], p=[0.5, 0.3, 0.15, 0.05])
    member_level_data.append([member_id, level])
member_level_df = pd.DataFrame(member_level_data, columns=["会员ID", "会员等级"])
print(f"✅ 会员等级表生成完成，共{len(member_level_df)}条记录")

# ---------------------- 3. 写入Excel文件 ----------------------
with pd.ExcelWriter("Data/rfm_data.xlsx", engine="openpyxl") as writer:
    for year in years:
        year_dfs[year].to_excel(writer, sheet_name=str(year), index=False)
    member_level_df.to_excel(writer, sheet_name="会员等级", index=False)

print("\n🎉 完整数据文件 rfm_model_full_data.xlsx 已生成完成！")