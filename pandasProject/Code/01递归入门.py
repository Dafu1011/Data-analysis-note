"""
案例：递归入门。
递归介绍：
    概述：
        自己调用自己的情况就叫递归
    经典案例：
        1.求阶乘
        2.不死神兔，斐波那契数列
        3.文件夹的拷贝、删除
        4.服务器文件整理
    核心要点：
        1.递归必须有出口，容易造成死递归
        2.递归调用次数不能过多，否则容易造死递归
        3.递归必须有规律
    要搞定递归，掌握两点：
        1.分析出口
        2，找规律
    案例：求阶乘
        公式：n！ = n * (n - 1)!
"""
# 场景1 ：入门案例：
# def show():
#     global count
#     count += 1
#     if count > 66:
#         return
#     print(f"递归第{count}次")
#     show()
# if __name__ == '__main__':
#     count = 0
#     show()

def funa(n):
    return 1 if n == 1 else n * funa(n - 1)
if __name__ == '__main__':
    print(funa(5))