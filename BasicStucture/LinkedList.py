#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   Description :  基本数据结构二：链表
   Author :       
   Date :         2020/8/11  1:11
   Change_Date:   2020-08-21 20:55
   Software:      PyCharm
   Email:         @my.brisol.ac.uk  
-------------------------------------------------

"""

"""
十大问题：
（1）移除重复元素
（2）找到第k个到最后一个元素
（3）中部删除一个节点
（4）围绕给定值分组链表
（5）两元素相加
（6）找到链表循环起始
（7）判断链表是否回文
（8）实现链表
（9）判断列表是否循环或者无环的
（10）其他挑战
"""

"""
1. 实现链表，附带功能：插入、增加、查找、删除、长度、打印
"""


# 实现节点
class Node(object):
    def __init__(self, data, next=None):
        """
        :param data: 节点值
        :param next: 节点指针
        """
        self.data = data
        self.next = next

    def __str__(self):
        return self.data


# 链表基本结构
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        """
        指向头部，若头部不为空，则创造计数器，每加一后，将指针指向节点的next指针，直到为空时
        :return: 返回计数器的结果
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        curr = self.head
        counter = 0
        while curr is not None:
            counter += 1
            curr = curr.next
        return counter

    def insert(self, data):
        """
        对指定数据插入到开头,即：将原先的头部指针变成现在插入数据的下一个指针;将头部指针指向现在的数据
        实现描述：
        (1) 若插入的数据是None,则返回None
        (2) 创建一个输入数据的节点，并把节点的尾指针指向现在的头
        (3) 将头指针指向现在的节点
        :param data: 需要插入的数据
        :return: 插入的当前值的节点
        时间复杂度&空间复杂度： O(1)
        """
        if data is None:
            return None
        node = Node(data, self.head)
        self.head = node
        return node

    def append(self, data):
        """
        实现描述：
        (1) 如果插入是空，则返回None
        (2) 根据输入数据创建一个节点
        (3) 若这是一个空列表：则将头指针指向这个节点
        (4) 否则为非空列表：则迭代到列表的最后；设置最终节点的尾指针为新节点
        :param data: 要插入的数据
        :return: 插入的当前值的节点
        时间复杂度： O(n)
        空间复杂度： O(1)
        """
        if data is None:
            return None
        node = Node(data)
        if self.head is None:
            self.head = node
            return node
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node
        return node

    def find(self, data):
        """
        (1) 若寻找的数据为None,则返回None
        (2) 若列表为空，则返回None
        (3) 对每个节点：如果值匹配，返回它；否则到下一个节点查询
        :param data:
        :return:
        时间复杂度： O(n)
        空间复杂度： O(1)
        """
        if data is None:
            return None
        curr_node = self.head
        while curr_node is not None:
            if curr_node.data == data:
                return curr_node
            curr_node = curr_node.next
        return None

    def delete(self, data):
        """
        (1) 若删除的数据是None 或者 列表是空列表，则返回空
        (2) 对每个节点，持续追踪之前和现在节点：
            如果删除值匹配当前节点的尾指针，则更新前一个节点的尾指针到现在节点的尾指针；否则查看下一个节点
        (3) 作为另一种方式：可以通过评估当前节点尾指针的值来避免使用双指针：
            如果尾指针指向节点的值匹配，则设置当前节点的尾指针到下个节点的尾指针
        :param data:
        :return:
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        if data is None or self.head is None
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        prev_node = self.head
        curr_node = self.head.next
        while curr_node is not None:
            if curr_node.data == data:
                prev_node.next = curr_node.next
                return
            prev_node = curr_node
            curr_node = curr_node.next

    def delete_alt(self, data):
        """
        第二种删除方式
        :param data:
        :return:
        """
        if data is None or self.head is None:
            return
        curr_node = self.head
        if curr_node.data == data:
            curr_node = curr_node.next
            return
        while curr_node.next is not None:
            if curr_node.next.data == data:
                curr_node.next = curr_node.next.next
                return
            curr_node = curr_node.next

    def print(self):
        """
        打印函数
        :return:
        """
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next

    def get_all_data(self):
        data = []
        curr_node = self,head
        while curr_node is not None:
            data.append(curr_node.data)
            curr_node = curr_node.next
        return data


"""
2. 从链表中移除重复元素
(1) 
"""




