"""
    案例:自定义代码模拟链表
        链表介绍:
        概述:
            它属于数据结构之 线性结构的一种，每个节点都只能有1个前驱 和1个后继节点.作用:
            用于优化顺序表的弊端(如果没有足够的连续的内存空间，会导致扩容失败)
            链表扩容时，有地儿就行，连不连续无所谓.
        组成:
            由节点组成，其中节点由 元素域(数值域)和链接域(地址域)组成.
        分类:
            根据 节点类型不同，链表主要分为:
            单向链表:节点由1个数值域 和1个地址域组成，前边节点的地址域存储的是后续节点的地址，最后1个节点的地址域为 None
            单向循环链表:
            双向链表:
            双向循环链表:
        自定义代码模拟链表，思路分析:
            1.自定义SingleNode类，表示 节点类.
                属性:
                    item数值域(元素域)
                    地址域(链接域)next
            2.自定义SingleLinkedList类,表示:链表
                属性：
                    head 头结点，指向第一个结点
                行为：
                    isEmpty() 判断是否为空
                    length()  长度
                    travel()  遍历链表
                    add()     链表头部加
                    append()  链表尾部加
                    insert()  指定位置插入
                    remove()  删除结点
                    search()  查找结点是否存在
            3.测试：

"""

# 1. 自定义StringLeMode类，表示节点类
class SingleNode:
    # 初始化属性
    def __init__(self, item):
        self.item = item # 数值域
        self.next = None # 地址域

# 2.自定义SingleLinkedList类,表示:链表
class SingleLinkedList:
    # 初始化属性
    def __init__(self,node=None): # node=None  默认参数
        self.head = node

     # 1.isEmpty() 判断是否为空
    def isEmpty(self):
        """
        思路：判断链表是否为空
        """
        # # 写法一： if else
        # if self.head is None:
        #     return True
        # else:
        #     return False

        # 写法二： 三元表达式
        # return True if self.head is None else False

        # 写法三： 最终版
        return self.head is None

     # 2.length()  长度
    def length(self):
        # 2.1计数器
        count = 0
        # 2.2 创建游标（表示当前节点），默认头结点
        cur = self.head
        # 2.3开始遍历，直到cur为None
        while cur != None:
            # 2.4 计数器+1，游标后移
            count += 1
            cur = cur.next
        return count
     # 3.travel()  遍历链表
    def travel(self):
        # 3.1 创建游标
        cur = self.head
        # 3.2 开始遍历
        while cur != None:
            # 3.3 打印当前节点的数值域元素
            print(f"数值域：{cur.item}")
            cur = cur.next
    # 4.add()     链表头部加
    def add(self,item):
        """
        思路：
        1.创建新节点
        2.将新节点的next指向头结点
        3.将新节点赋给头结点
        注意：顺序不能反，必须先让新节点指向头结点
        """
        new_node = SingleNode(item)
        new_node.next = self.head
        self.head = new_node

     # 5.append()  链表尾部加
    def append(self,item):
        # 5.1封装节点
        new_node = SingleNode(item)
        # 5.2 判断链表是否为空,如果为空，则将新节点赋给头结点
        if self.isEmpty():
            self.head = new_node
        # 5.3找到尾节点
        cur = self.head
        while cur.next != None:
            cur = cur.next
        # 5.4将尾节点的next指向新节点
        cur.next = new_node

    # 6.指定位置插入
    def insert(self,item,pos):
        # 6.1 判断索引索引是否越界
        # 6.2 长度小于0 直接从头结点插入
        if pos <= 0:
            self.add(item)
        # 6.3 pos大于长度，直接尾部添加
        elif pos >self.length():
            self.append(item)
        else:
            cur = self.head
            count = 0
            # 6.4 开始遍历，只要当前节点的位置 < pos 就一直循环
            while count< pos -1:
                cur = cur.next
                count += 1
            # 6.5 封装新节点
            new_node = SingleNode(item)
            new_node.next = cur.next
            cur.next = new_node
    # 7.删除节点
    def remove(self,item):
        # 7.1 创建游标
        cur = self.head
        # 7.2 定义变量，记录要删除节点的前驱节点
        pre = None
        # 7.2 开始遍历
        while cur != None:
            # 7.3 找到要删除的结点
            if cur.item == item:
                # 7.4 判断要删除的是否是头结点
                # 7.5 是头结点，则将头结点指向头结点的下一个节点
                if pre == None:
                    self.head = cur.next
                else:
                    # 7.6 不是头结点，则将当前节点的前驱节点的next指向当前节点的next
                    pre.next = cur.next
                    cur.next = None #  删除当前节点,这一步可有可无
                return
            else:
                pre = cur
                cur = cur.next

     # 8.search()  查找结点是否存在
    def search(self,item):
        # 1.创建游标
        cur = self.head
        # 2.开始遍历
        while cur != None:
            # 3.判断当前节点是目标节点
            if cur.item == item:
                return True
            # 4.当前节点不是目标节点,游标指向下一个节点
            cur = cur.next
        # 5.循环结束，没有找到目标结点，返回False
        return False
# 3.测试：在主方法中测试
if __name__ == '__main__':
    # 3.测试顺序表和单链表
    # 3.1 测试节点表
    # node = SingleNode(100)
    # print(f"顺序表的数值域元素为：{node.item}")
    # print(f"顺序表的地址域元素为：{node.next}")
    # print(f"node对象：{node}")
    # print(f"node类型：{type(node)}")
    #3.2测试链表
    # # sll = SingleLinkedList() # 不传参默认值：None
    # sll = SingleLinkedList(node)
    # print(f"链表的头结点为：{sll.head}")
    # print(f"头结点的地址域元素为：{sll.head.next}")  # 地址域元素为None
    # print(f"头结点的数值域元素为：{sll.head.item}")  # 数值域元素为100

    # 4.完整测试
    # 4.1 创建节点
    node = SingleNode("花椒油")
    # 4.2 创建链表
    my_sll = SingleLinkedList(node)
    # my_sll =  SingleLinkedList()
    # 4.3 打印头结点
    # print(f"链表的头结点为：{my_sll.head.item}")
    # 4.4 测试链表是否为空
    print(f"链表是否为空：{my_sll.isEmpty()}")
    print("-" * 66)

    # 4.7 测试链表头部加
    my_sll.add("悠悠")
    my_sll.add("灰灰")

    # 4.8 测试链表尾部加
    my_sll.append("春")
    my_sll.append("夏")

    # 4.9 测试指定位置插入
    my_sll.insert("郭靖",-3)
    my_sll.insert("黄蓉",8)
    my_sll.insert("小龙女",2)

    # 4.10 测试删除节点
    my_sll.remove("小龙女")


    # 4.5 测试链表长度
    print(f"链表的长度为：{my_sll.length()}")
    print("-" * 66)

    # 4.6 测试遍历链表
    my_sll.travel()
    print("-" * 66)


    # 4.11 测试查找结点是否存在
    print(f"链表是否包含“小龙女”：{my_sll.search('小龙女')}")
    print(f"链表是否包含“花椒油：”：{my_sll.search('花椒油')}")