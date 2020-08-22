#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import unittest
import sys
"""
-------------------------------------------------
   Description :  基本数据结构一：栈和队列
   Author :       
   Date :         2020/8/11  1:10
   Software:      PyCharm
   Email:         @my.brisol.ac.uk  
-------------------------------------------------

"""

"""
Stack和queue是元素通过删除操作，从集合中移除的动态集合：
（1） 在Stack栈中，被删除的元素是最近插入的，即：后入，先出[LIFO]
（2） 在Queue队列中，元素总是删除那个进来最久的，即：先进，先出[FIFO]
"""

"""
Stack
(1) 插入操作，称为PUSH
(2) 删除操作，称为POP，无需输入元素的参数
(3) 将N个元素放入数组S[1,...,n]；
    数组拥有元素S.top,这是最近插入元素的索引；
    则：栈是由元素S[1,2,....,S.top]构成的；S[1]是栈的底部；S[S.top]是栈的顶部
    则：S.top = 0时，代表栈是空的，没有元素【STACK-EMPTY函数】:此时继续弹出元素，则stack underflows；若S.top > n,则Stack Overflows

伪码：STACK-EMPTY(S)
if S.top == 0 
    return TRUE
else return FALSE


伪码：PUSH(S,x)
S.top = S.top + 1
S[S.top] = x
即：[
If stack is full, throw exception
Else
    Increment stack pointer
    Get the absolute array index
    Insert the value to this index
]
操作复杂度：[Complexity:
Time: O(1)
Space: O(1)
]


伪码：POP(S)
if STACK-EMPTY(S)
    error "underflows"
else S.top = S.top - 1
    return S[S.top+1]
即：[
If stack is empty, throw exception
Else
    Store the value contained in the absolute array index
    Set the value in the absolute array index to None
    Decrement stack pointer
    return value
]
操作复杂度：[
Time: O(1)
Space: O(1)
]

"""


class Stacks1(object):
    """
    Challenge 1: 使用单数组实现n个栈
    """
    def __init__(self, num_stacks, stack_size):
        # 栈中已经存储的数据数量
        self.num_stacks = num_stacks
        # 栈的真容量大小
        self.stack_size = stack_size
        # 栈的指针[初始化为拥有数量大小的-1数组]
        self.stack_pointers = [-1] * self.num_stacks
        #
        self.stack_array = [None] * self.num_stacks * self.stack_size

    def abs_index(self, stack_index):
        """
        :param stack_index: 栈索引
        :return: 返回 栈大小 * 栈索引 + 栈指针
        """
        return stack_index * self.stack_size + self.stack_pointers[stack_index]

    def push(self, stack_index, data):
        """
        :param stack_index: 栈索引
        :param data:  数据
        :return: 栈插入数据【压入】
        """
        # 判断是否是满了
        if self.stack_pointers[stack_index] == self.stack_size - 1:
            raise Exception("Stack is full")
        # 栈指针+1
        self.stack_pointers[stack_index] += 1
        # 存储栈数据的数组指针指向新
        array_index = self.abs_index(stack_index)
        self.stack_array[array_index] = data

    def pop(self, stack_index):
        """
        :param stack_index: 栈索引
        :return: 删除元素后的栈
        """
        if self.stack_pointers[stack_index] < 0:
            raise Exception("Stack underflows and it is empty")
        array_index = self.abs_index(stack_index)
        data = self.stack_array[array_index]
        self.stack_array[array_index] = None
        self.stack_pointers[array_index] -= 1
        return data

# class TestStacks(object):
#     def test_pop_on_empty(self, num_stacks, stack_size):
#         print('Test: Pop on empty stack')
#         stacks = Stacks1(num_stacks, stack_size)
#         stacks.pop(0)
#
#     def test_push_on_full(self, num_stacks, stack_size):
#         print('Test: Push to full stack')
#         stacks = Stacks1(num_stacks, stack_size)
#         for i in range(0, stack_size):
#             stacks.push(2, i)
#         stacks.push(2, stack_size)
#
#     def test_stacks(self, num_stacks, stack_size):
#         print('Test: Push to non-full stack')
#         stacks = Stacks1(num_stacks, stack_size)
#         stacks.push(0, 1)
#         stacks.push(0, 2)
#         stacks.push(1, 3)
#         stacks.push(2, 4)
#         print('Success: test_stacks\n')


"""
限制：（1）从空栈中删除元素，返回None；（2）内存足够
各功能点：
push: 用值创建新节点；设置节点的下个为top；设置top为节点; 复杂度： O(1)
pOP : 若栈为空，则返回空；否则保存top的值，设置top.next为top并返回保存的值；复杂度：O(1)
PEEK: 若栈为空，则返回空；否则返回top的值；复杂度：O(1)
IS_EMPTY: 如果PEEK有值，则FALSE，否则为TUE; 复杂度：O(1)
"""


class Node(object):
    """
    链表基本节点
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class StackLinkedList(object):
    """
    基于链表实现栈
    """
    def __init__(self, top=None):
        """
        :param top: 传入顶点
        """
        self.top = top

    def push(self, data):
        """
        :param data: 压入值
        :return:
        """
        self.top = Node(data, self.top)

    def pop(self):
        """
        :return: 删除值
        """
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        return self.top.data if self.top is not None else None

    def is_empty(self):
        return self.peek() is None


"""
Problem: Implement SetOfStacks that wraps a list of stacks, where each stack is bound by a capacity.
限制：
（1）假设我们已经有栈的一个类
（2）每个栈都拥有相同容量边界
（3）栈满了，自动创建一个栈
（4）栈空了，返回None
（5）假设内存够用

则：
Push: 如果没有栈或最新的栈满了，则创建一个新栈；将数据添加在新栈
    时间复杂度：O(1)
    空间复杂度：O(m)， m是新栈的大小

Pop: 如果m没有栈，返回None；否则如果最新栈有一个元素则删除最新元素；删除现在的空栈；更新最新栈指针；否则删除最新元素数据并返回最新元素数据
    时间复杂度：O（1）
    空间复杂度：O（1） 
"""


# 基于已经实现的栈基类，实现带有容量的栈
class StackWithCapacity(StackLinkedList):
    def __init__(self, top=None, capacity=20):
        """ 初始化
        :param top: 用子类的顶部值初始化父类的顶部
        :param capacity: 栈容量
        """
        super(StackWithCapacity, self).__init__(top)
        self.capacity = capacity
        self.num_items = 0

    def push(self, data):
        if self.is_full():
            raise Exception("Stack Overflows")
        super(StackWithCapacity, self).push(data)
        self.num_items += 1

    def pop(self):
        self.num_items -= 1
        return super(StackWithCapacity, self).pop()

    def is_full(self):
        """
        :return: 判断容量是否于容纳值相等
        """
        return self.num_items == self.capacity

    def is_empty(self):
        """
        :return: 判断容纳值是否为0
        """
        return self.num_items == 0


# 定义栈集合
class SetOfStacks(object):
    """
    用途：当栈过大时，栈可能会坍塌，故而一般设定一个容量值，使得栈堆积的不要过高
    """
    def __init__(self, indiv_stack_capacity):
        self.indiv_stack_capacity = indiv_stack_capacity
        self.stacks = []
        self.last_stack = None

    def push(self, data):
        """
        若最新栈是否为空或者是否满，则最新栈更新为带容量栈，并将数据插入
        :param data:
        :return:
        """
        if self.last_stack is None or self.last_stack.is_full():
            self.last_stack = StackWithCapacity(None, self.indiv_stack_capacity)
            self.stacks.append(self.last_stack)
        self.last_stack.push(data)

    def pop(self):
        """
        (1)判断最新栈是否为空;(2) 保存最新栈值并最终返回值;(3) 最新栈为空则栈弹出此空栈，对剩余栈的最后一个栈作为最新栈
        :return:
        """
        if self.last_stack is None:
            return None
        data = self.last_stack.pop()
        if self.last_stack.is_empty():
            self.stacks.pop()
            self.last_stack = self.stacks[-1] if self.stacks else None
        return data


"""
Problem: Sort a stack. You can use another stack as a buffer
对栈排序

限制：
（1）排序时，最大元素在顶部还是在地底部？ 答：顶部
（2）是否能拥有重复的元素？ 答： 可以
（3）是否拥有基本的栈结构？ 答：有
（4）内存够用？ 答：够

算法规则：
（1）缓存反序保存已排序过的元素，最小的元素在顶部
（2）存储顶部元素在零食变量中
（3）当栈不为空时：
    [1] 当缓存不为空 或者 缓存的top是大于现在的temp, 则：将缓存的top放入栈
    [2] 将temp移动到缓存的top
（4）返回缓存

时间复杂度： O(n^2)
空间复杂度： O(n)
    
"""


# 实现栈排序_v1
class SortStackV1(StackLinkedList):
    def sort(self):
        buff = SortStackV1()
        while not self.is_empty():
            temp = self.pop()
            if buff.is_empty() or temp >= buff.peek():
                buff.push(temp)
            else:
                while not buff.is_empty() and temp < buff.peek():
                    self.push(buff.pop())
        return buff


# 实现栈排序_v2
class SortStackV2(StackLinkedList):
    def sort(self):
        buff = SortStackV2()
        while not self.is_empty():
            temp = self.pop()
            while not buff.is_empty() and temp < buff.peek():
                self.push(buff.pop())
            buff.push(temp)
        return buff


# def main_stack1():
#     """
#     单数组实现栈
#     :return:
#     """
#     num_stacks = 3
#     stack_size = 100
#     test = TestStacks()
#     test.test_stacks(num_stacks, stack_size)


def main_stack2():
    tp = Node(10)
    stack = StackLinkedList(tp)
    print(stack.pop())
    print(stack.peek())
    print('Test: More than one element')
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("stack.pop is {}\n stack.peek is {}\n stack.pop is {} \n stack.peek is {} \n {} \n {} \n {} \n {}".format(
        stack.pop(), stack.peek(), stack.pop(), stack.peek(), stack.is_empty(), stack.pop(), stack.peek(), stack.is_empty()))


# 实现栈集合，从而实现栈列表；每个栈是边界
def main_stack3():
    print('Test: Push on an empty stack')
    stacks = SetOfStacks(indiv_stack_capacity=2)
    stacks.push(3)
    print('Test: Push on a non-empty stack')
    stacks.push(5)
    print('Test: Push on a capacity stack to create a new one')
    stacks.push('a')
    print('Test: Pop on a stack to destroy it')
    print("stacks.pop is equal to a?{}".format(stacks.pop() == 'a'))
    print('Test: Pop general case')
    print("stacks.pop is equal to 5?{}".format(stacks.pop() == 5))
    print("stacks.pop is equal to 3?{}".format(stacks.pop() == 3))
    print('Test: Pop on no elements')
    print("stacks.pop is None?{}".format(stacks.pop() is None))
    print('Success: test_set_of_stacks')


# 实现栈排序
class TestSortStack():
    def __init__(self, stack, numbers):
        self.stack = stack
        self.numbers = numbers

    def get_sorted_stack(self):
        for x in self.numbers:
            self.stack.push(x)
        sorted_stack = self.stack.sort()
        return sorted_stack


# 测试：栈排序
def main_stack4():
    test1 = TestSortStack(SortStackV1,[])
    print('Test: Empty stack')
    test.get_sorted_stack()
    test.get_sorted_stack(SortStackV2)


"""
(1) 假设是整数栈
(2) 每次PUSH的值都是有效的
(3) 对空栈调用，返回最大栈大小
(4) 已经实现栈结构
(5) 内存充足
"""


# 实现最终版： 栈的PUSH\POP\MIN，使用O(1)时间操作
class StackMin(StackLinkedList):
    def __init__(self, top=None):
        super(StackMin, self).__init__(top)
        self.stack_of_mins = StackLinkedList()

    def minimum(self):
        if self.stack_of_mins.top is None:
            return sys.maxsize
        else:
            return self.stack_of_mins.peek()

    def push(self, data):
        super(StackMin, self).push(data)
        if data < self.minimum():
            self.stack_of_mins.push(data)

    def pop(self):
        data = super(StackMin, self).pop()
        if data == self.minimum():
            self.stack_of_mins.pop()
        return data


# 测试：PUSH POP MIN都为O(1)的栈操作
class main_stack4():
    def test_stack_min():
        print('Test: Push on empty stack, non-empty stack')
        print('CREATE STACNMIN DATASTRUCTURE:\n')
        stack = StackMin()
        print("PUSHING: 5")
        stack.push(5)
        print("stack.peek is equal to 5? [{}]".format(stack.peek() == 5))
        print("stack.minimum is equal to 5? [{}]".format(stack.minimum() == 5))
        print("PUSHING: 1")
        stack.push(1)
        print("stack.peek is equal to 1? [{}]".format(stack.peek() == 1))
        print("stack.minimum is equal to 1? [{}]".format(stack.minimum() == 1))
        print("PUSHING: 3")
        stack.push(3)
        print("stack.peek is equal to 3? [{}]".format(stack.peek() == 3))
        print("stack.minimum is equal to 3? [{}]".format(stack.minimum() == 3))
        print("PUSHING: 0")
        stack.push(0)
        print("stack.peek is equal to 0? [{}]".format(stack.peek() == 0))
        print("stack.minimum is equal to 0? [{}]".format(stack.minimum() == 0))

    @classmethod
    def fuck_it(cls):
        cls.test_stack_min()


if __name__ == '__main__':
    # # 1。使用单数组实现N栈
    # main_stack1()
    # # 2.使用链表实现栈[带有push \ pop \ peek \ is_empty]
    # main_stack2()
    # # 栈集合测试
    # main_stack3()
    fuckit = main_stack4()
    fuckit.fuck_it()

