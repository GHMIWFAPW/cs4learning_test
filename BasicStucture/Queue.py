#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('/Users/msb/Downloads/weiweiHe_work/JupyterScript_ipy/program_works/model_try/ds')
# sys.path.append('C:\\Users\\\\Downloads\\coding\\ProjectAll\\test\\DataStructure')
import random
from BasicStucture.StackAndQueue import StackLinkedList

"""
-------------------------------------------------
   Description :  实现队列
   Author :       
   Date :         2020-08-19 21:13
   Email:         @my.bristol.ac.uk
   Mobile:         
-------------------------------------------------

"""

"""
1. 使用两个栈实现队列
(1) 实现进队和出队
(2) 已经实现基本的栈
(3) 不能拿将none值压入栈
(4) 内存足够
注： 使用两个栈，左栈和右栈：左栈用于进队，右栈用于出队

进队：enqueue
(1) 如果右栈不为空，则shift Stack右侧元素，再插入左侧
(2) 时间复杂度\空间复杂度：O(n)

出队：dequeue
(1) 如果左栈不为空，则shift Stack左侧元素；再从右侧删除并返回值
(2) 时间复杂度\空间复杂度：O(n)

shift Stack:
(1) 当源栈中有元素时：从源栈中删除元素并将其压入目标栈

"""


# 实现: 使用两个栈实现先进先出的队列
class QueueFromStacks(object):
    def __init__(self):
        self.left_stack = StackLinkedList()
        self.right_stack = StackLinkedList()

    def shift_stacks(self, source, destination):
        while source.peek() is not None:
            destination.push(source.pop())

    def enqueue(self, data):
        self.shift_stacks(self.right_stack, self.left_stack)
        self.left_stack.push(data)

    def dequeue(self):
        self.shift_stacks(self.left_stack, self.right_stack)
        return self.right_stack.pop()


# 测试
class api_QueueFromStacks(object):
    def __init__(self, num_items=3):
        self.num_items = num_items

    def test_queue_from_stacks(self):
        print('Test: Dequeue on empty stack')
        queue = QueueFromStacks()
        print("queue.dequeue()  == None ? [{}]".format(queue.dequeue() is None))
        print('Test: Enqueue on empty stack')
        print('Test: Enqueue on non-empty stack')
        print('Test: Multiple enqueue in a row')
        for i in range(0, self.num_items):
            print("Enqueue data:{}".format(i))
            # queue.enqueue(random.random)
            queue.enqueue(i)
        print('Test: Dequeue on non-empty stack')
        print('Test: Dequeue after an enqueue')
        print("queue.dequeue()  == 0 ? [{}]\n".format(queue.dequeue() == 0))

        print('Test: Multiple dequeue in a row')
        print("queue.dequeue()  == 1 ? [{}]".format(queue.dequeue() == 1))
        print("queue.dequeue()  == 2 ? [{}]".format(queue.dequeue() == 2))

        print('Test: Enqueue after a dequeue')
        print("enqueue 5~\n")
        queue.enqueue(5)
        print("queue.dequeue()  == 5 ? [{}]".format(queue.dequeue() == 5))
        print('Success: test_queue_from_stacks')

    # # @classmethod
    # def run(cls):
    #     cls.test_queue_from_stacks()


"""
2. 使用链表实现队列的进队与出队
(1) 若列表中有一个元素，是否让头与尾指针都指向它？ 答：是
(2) 若列表中没有元素，头与尾指正为空？答：是
(3) 对空队列出站，是否返回空？答：是
(4) 内存足够
"""


# 定义链表的节点
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueFromLinkList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        若为空列表，则头尾都指向当前node；否则将尾部全部指向node
        :param data: 进队数据
        :return: 插入数据并改变指针；时间&空间复杂度：O(1)
        """
        node = Node(data)
        # 空列表
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        """
        若为空，则返回空；
        若有一个节点，则：（1）保存头节点的值；（2）设置头和尾为空；（3）返回保存的值；
        否则：(1) 保存头节点的值；（2）设置头到下一个节点；（3）返回保存的值
        :return:出队并改变指正；时间&空间复杂度：O(1)
        """
        # 空
        if self.head is None and self.tail is None:
            return None
        data = self.head.data
        # 从一个元素列表中移除元素
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return data


class api_QueueFromLinkedList(object):
    def __init__(self, num_items=3):
        self.num_items = num_items

    def test_queue_from_stacks(self):
        print('Test: Dequeue on empty stack')
        queue = QueueFromLinkList()
        print("queue.dequeue()  == None ? [{}]".format(queue.dequeue() is None))
        print('Test: Enqueue on empty stack')
        print('Test: Enqueue on non-empty stack')
        print('Test: Multiple enqueue in a row')
        for i in range(0, self.num_items):
            print("Enqueue data:{}".format(i))
            # queue.enqueue(random.random)
            queue.enqueue(i)
        print('Test: Dequeue on non-empty stack')
        print('Test: Dequeue after an enqueue')
        print("queue.dequeue()  == 0 ? [{}]\n".format(queue.dequeue() == 0))

        print('Test: Multiple dequeue in a row')
        print("queue.dequeue()  == 1 ? [{}]".format(queue.dequeue() == 1))
        print("queue.dequeue()  == 2 ? [{}]".format(queue.dequeue() == 2))

        print('Test: Enqueue after a dequeue')
        print("enqueue 5~\n")
        queue.enqueue(5)
        print("queue.dequeue()  == 5 ? [{}]".format(queue.dequeue() == 5))
        print('Success: test_queue_from_stacks')


def mainv1():
    x = api_QueueFromStacks(5)
    x.test_queue_from_stacks()


def mainv2():
    x = api_QueueFromLinkedList(5)
    x.test_queue_from_stacks()


if __name__ == '__main__':
    # mainv1()
    mainv2()

