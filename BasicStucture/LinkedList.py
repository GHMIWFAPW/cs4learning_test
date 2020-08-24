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
<<<<<<< Updated upstream
2. 从链表中删除重复值
(1) 单链表、无循环
(2) 不能插入空值
(3) 已有实现的链表 
(4) 可以使用额外的数据结构
(5) 内存够

实现（1）： 哈希表循环
1. 对于每个节点，如果节点值再哈希表内，则删除这个节点；否则将此节点的值添加汝哈希表

时间复杂度：O(n)
空间复杂度：O(n)

实现（2）： In-Place
1. 对于每个节点，其于其他每个节点相比较，删除哪些于当前节点相同值的节点

时间复杂度：O(n^2)
空间复杂度：O(1)
"""

class MoveRed4LinkedList(LinkedList):
    def remove_dupes(self):
        """
        删除重复值函数
        :return:
        """
        if self.head is None:
            return
        node = self.head
        seen_data = set()
        # 开始遍历
        while node is not None:
            # 判断值是否再其中
            if node.data not in seen_data:
                seen_data.add(node.data)
                prev = node
                node = node.next
            else:
                prev.next = node.next
                node = node.next

    def remove_dupes_single_pointer(self):
        if self.head is None:
            return
        node = self.head
        seen_data = set(node.data)
        while node.next is not None:
            if node.next.data in seen_data:
                node.next = node.next.next
            else:
                seen_data.add(node.next.data)
                node = node.next

    def remove_dupes_in_place(self):
        curr = self.head
        while curr is not None:
            runner = curr
            while runner.next is not None:
                if runner.next.data == curr.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            curr = curr.next

# TODO:单元测试


"""
3. 找到第K个到最后一个的数据 【即：先给出K个位置，而后一起遍历，剩下的，则就是第k个到最后一个】
（1）单链表、无环
（2）K为有效整数
（3）K为0时，返回最后以给元素
（4）若比链表大，则返回NONE
（5）不能使用其他的数据结构
（6）已有基本节点结构和链表结构

实现方案：
设置两个指针，快和慢
对快指针开始，按照其值增加
同时增加两个指针直到快指针到最后
返回慢指针的值

时间复杂度：O(n)
空间复杂度：O(1)
"""

class Kth2Last(LinkedList):
    """
    设置两个链表，(1) 先将指针指完前K个点；(2)
    """
    def kth_to_last_elem(self, k):
        if self.head is None:
            return None
        fast = self.head
        slow = self.head
        # 对快指针一个开始头，增加之
        for _ in range(k):
            fast = fast.next
            # 如果k>= 链表尺寸，则返回none
            if fast is None:
                return None

        # 同时增加两个指针的值，直到快指针到达最终.则快的遍历完的次数，即为 MAX- K，
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        return slow.data


#TODO:测试代码


"""
4. 删除链表中的一个节点  [删除中一个节点，只给出这个节点]
实现：需要两个指针，一个用于当前节点另一个用户下一个。复制下一个节点的data到当前节点的data并更新当前节点的next指针
时间复杂度：O(1)
空间复杂度：O(1)
=======
2. 从链表中移除重复元素
(1) 
>>>>>>> Stashed changes
"""

class DelNode(LinkedList):
    def delete_node(self, node):
        """
        :param node: 要删除的节点
        :return:
        """
        if node is None:
            return
        if node.next is None:
            node.data = None
        else:
            node.data = node.next.data
            node.next = node.next.next

"""
5. 基于一个给定值分区链表 【所有节点中比给定值小的先于等于或大于的】

实现：创建左右链表。对于在列表中的每个元素，如果比给定值小，则加入左链表，否则加入右链表。最后左右链表合并
"""

class PartitionLinkedList(LinkedList):
    def partition(self, data):
        if self.head is None:
            return
        left = PartitionLinkedList(None)
        right = PartitionLinkedList(None)
        curr = self.head

        # 创建左右列表
        while curr is not None:
            if curr.data < data:
                left.append(curr.data)
            elif curr.data == data:
                right.insert(curr.data)
            else:
                right.append(curr.data)
        curr_left = left.head
        if curr_left is None:
            return right
        else:
            while curr_left.next is not None:
                curr_left = curr_left.next
            curr_left.next = right.head
            return left

# TODO:测试代码


"""
6. 加和两个反序存在于链表中的值

"""

class AddReverse(LinkedList):
    def _add_reverse(self, first_node, second_node, carry):
        """
        :param first_node: 第一个链表内的节点
        :param second_node: 第二个链表内的节点
        :param carry:  存储器，用于存储进位
        :return: 每一个位置的节点
        """
        if first_node is None and second_node is None and not carry:
            return None
        value = carry
        value += first_node.data if first_node is not None else 0
        value += second_node.data if second_node is not None else 0
        carry = 1 if value >=10 else 0
        value %= 10
        node = Node(value)
        node.next = self._add_reverse(
            first_node.next if first_node is not None else None,
            second_node.next if second_node is not None else None,
            carry
        )
        return node

    def add_reverse(self, first_list, second_list):
        """若传入的两个列表为有一个为空则无需计算，否则调用。最终返回一个链表，值为加和后的值
        :param first_list:
        :param second_list:
        :return:
        """
        if first_list is None or second_list is None:
            return None
        head = self._add_reverse(first_list, second_list, 0)
        return AddReverse(head)
