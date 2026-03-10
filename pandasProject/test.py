import random
import csv
from faker import Faker

# 初始化Faker(zh_CN用于生成中文城市名)
fake = Faker('zh_CN')
Faker.seed(42)  # 固定随机种子保证可复现
random.seed(42)

# 配置各字段枚举与分布
CITIES = ["北京", "上海", "广州", "深圳", "杭州", "成都", "重庆", "武汉", "南京", "西安"]
CHANNELS = ["网购", "自提", "门店购买"]
GENDERS = ["男", "女"]
AGE_GROUPS = ["青年", "中年", "老年"]
WEEKEND_IND = ["周末", "周间"]
PRODUCTS = ["电子产品", "服装鞋帽", "食品生鲜", "家居日用", "美妆护肤", "运动户外"]

# 定义列名
headers = [
    "store_id", "city", "channel", "gender_group", "age_group",
    "wkd_ind", "product", "customer", "revenue", "order", "quant", "unit_cost"
]


def generate_row():
    """生成单条模拟数据"""
    store_id = random.randint(10000, 99999)  # 门店随机ID
    city = random.choice(CITIES)
    channel = random.choice(CHANNELS)
    gender_group = random.choice(GENDERS)

    # 年龄段分布(青年70%、中年25%、老年5%)
    age_group = random.choices(AGE_GROUPS, weights=[0.7, 0.25, 0.05])[0]

    wkd_ind = random.choice(WEEKEND_IND)
    product = random.choice(PRODUCTS)

    # 客户数(1-500)
    customer = random.randint(1, 500)

    # 订单数(与客户数正相关)
    order = random.randint(1, min(customer, 200))

    # 购买数量(与订单数正相关)
    quant = random.randint(1, max(10, order * 2))

    # 销售额(结合客单价与数量，不同品类差异)
    price_map = {
        "电子产品": (1500, 8000), "服装鞋帽": (80, 500),
        "食品生鲜": (15, 80), "家居日用": (30, 200),
        "美妆护肤": (120, 600), "运动户外": (200, 1500)
    }
    min_price, max_price = price_map[product]
    revenue = round(quant * random.uniform(min_price, max_price), 2)

    # 单位成本(销售额的30%-60%)
    unit_cost = round(revenue / quant * random.uniform(0.3, 0.6), 2)

    return [
        store_id, city, channel, gender_group, age_group,
        wkd_ind, product, customer, revenue, order, quant, unit_cost
    ]


# 生成2000条数据并写入CSV
if __name__ == "__main__":
    with open("sales_data.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)  # 写入表头
        for _ in range(2000):
            writer.writerow(generate_row())
    print("✅ 2000条模拟数据已生成至 sales_data.csv")