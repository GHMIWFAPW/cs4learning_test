#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   Description :  基础数据结构四：二叉搜索树
   Author :       
   Date :         2020/8/11  1:15
   Software:      PyCharm
   Email:         @my.brisol.ac.uk  
-------------------------------------------------

"""

"""
1. 实现构建一个二叉搜索树
具备插入功能:
(1) 若根为空，则返回 Node(data)
(2) 若data小于等于当前节点值：
        若当前节点的左节点是空，设置其为节点值
        否则，遍历插入左子树
(3) 否则：
        若当前节点的右子树为空，则设置为节点值
        否则，遍历插入右子树

时间复杂度：O(h), h是树的高度
    平衡树中，高度为 log(n)
    在极端最差案例中，则如同链表结构 O(n)
    
空间复杂度：
   (1) 递归： O(m), m是递归的次数
   (2) 尾递归: O(1)

"""


# 定义树节点
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        """
        用于print自身值的魔法方法
        :return:
        """
        return str(self.data)


# 定义二叉树
class Bst(object):
    def __init__(self, root=None):
        """
        初始化
        :param root: 根
        """
        self.root = root

    # 对节点插入数据
    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if data <= node.data:
            if node.left is None:
                node.left = self._insert(node.left, data)
                node.left.parent = node
                return node.left
            else:
                return self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = self._insert(node.right, data)
                node.right.parent = node
                return node.right
            else:
                return self._insert(node.right, data)

    # 调用
    def insert(self, data):
        if data is None:
            raise ValueError("data cannot be None")
        if self.root is None:
            self.root = Node(data)
            return self.root
        else:
            return self._insert(self.root, data)


"""
2. 在一棵二叉树上，实现三种不同的深度优先遍历
前序(pre-order) ; 中序(in-order) ; 后续(post-order) 的遍历，代表的是根节点相对于左右节点的位置遍历方式

中序遍历：
  递归调用中序遍历于左子树
  访问当前节点
  递归调用中序遍历于右子树
  
前序遍历：
  访问当前节点
  递归调用前序遍历于左子树
  递归调用前序遍历于右子树
  
后续遍历：
  递归调用后续遍历于左子树
  递归调用后续遍历于右子树
  访问当前节点
"""


class BstDfs(Bst):
    # 中序遍历
    def in_order_traversal(self, node, visit_func):
        if node is not None:
            self.in_order_traversal(node.left, visit_func)
            visit_func(node)
            self.in_order_traversal(node.right, visit_func)

    # 前序遍历
    def pre_order_traversal(self, node, visit_func):
        if node is not None:
            visit_func(node)
            self.pre_order_traversal(node.left, visit_func)
            self.pre_order_traversal(node.right, visit_func)

    # 后序遍历
    def post_order_traversal(self, node, visit_func):
        if node is not None:
            self.post_order_traversal(node.left, visit_func)
            self.post_order_traversal(node.right, visit_func)
            visit_func(node)


"""
3. 实现广度优先的树遍历

实现方案：
(1) 使用根初始化队列
(2) 当队列不为空时：
    出队并打印
    进队左子树
    进队右子树

时间复杂度：O(N)
空间复杂度：O(N)

"""
from collections import deque


class BstBfs(Bst):
    def bfs(self, visit_func=None):
        if self.root is None:
            raise TypeError("root is none")
        queue = deque()
        queue.append(self.root)
        while queue:
            node = queue.popleft()
            if visit_func:
                visit_func(node)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return str(queue)


def run_BstBfs():
    x = BstBfs(Node(5))
    x.insert(2)
    x.insert(8)
    x.insert(1)
    x.insert(3)
    print(x.bfs(True))


"""
4.  判断一棵二叉树的高度

方案：
若当前节点为空，则高度为0
否则返回1+ 左右子树最大的高度

时间复杂度：O(N)
空间复杂度：O(h)， h是树的高度
"""


class BstHeight(Bst):
    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left),
                       self.height(node.right))

# 树高度判定
def run_BstHeight():
    x = BstHeight(Node(5))
    x.insert(2)
    x.insert(8)
    x.insert(1)
    x.insert(3)
    print("根所在的高度: {}".format(x.height(x.root)))


"""
5. 对已排序数组，创建一个具有最小高度的二叉搜索树

方案：将中值作为根，递归半分数组，并抽取左右半截的中值插入树的节点
时间复杂度：O(N)
空间复杂度：O(h)
"""


class BstMin(object):
    def create_min_bst(self, array):
        if array is None:
            return
        return self._create_min_bst(array, 0, len(array)-1)

    def _create_min_bst(self, array, start, end):
        if end < start:
            return None
        mid = (start + end) >> 1
        node = Node(array[mid])
        node.left = self._create_min_bst(array, start, mid-1)
        node.right = self._create_min_bst(array, mid+1, end)
        return Node


def run_bstmin():
    min_bst = BstMin()
    x = [5, 2, 8, 1, 3, 10]
    min_bst.create_min_bst(x)
    print(min_bst)


"""
6. 检测一个二叉树是否是平衡树

检查高度的同时检测是否平衡

方案：
(1) 若根为空，则返回0
(2) 递归检测是否左侧的子树是平衡树并得到其高度 
(3) 递归检测是否右侧的子树是平衡树并得到其高度
(4) 对比左右子树的高度
(5) 若都满足，则返回1+ max(左树高，右树高)


时间复杂度：O(N)
空间复杂度: O(H) H是树高度
"""


class Bst_Balance(Bst):
    def _check_balance(self, node):
        if node is None:
            return 0
        left_height = self._check_balance(node.left)
        if left_height == -1:
            return -1
        right_height = self._check_balance(node.right)
        if right_height == -1:
            return -1
        diff = abs(left_height - right_height)
        if diff > 1:
            return -1
        return 1 + max(left_height, right_height)
    def check_balance(self):
        if self.root is None:
            raise TypeError("Root cannot be None")
        height = self._check_balance(self.root)
        return height != -1


"""
7. 找到二叉树给定节点的中序后继节点

定义：
后继：
(1) 所有关键字胡不限通，则节点x的后继是大于x.key的最小关键字的节点
(2) 如果x节点的右节点为空且有一个后继节点，则后继节点是x的最底层祖先，且y的左子树节点也是x的一个祖先
方案：
(1) 如果节点有右子树， 返回其内部的最左侧的左子树节点
(2) 若无右子树，则向上找一个节点，这个节点是它父节点的左节点:
    1) 
"""


class Bst_Successor(object):
    def get_next(self, node):
        if node is None:
            return None
        if node.right is not None:
            return self._left_most(node.right)
        else:
            return self._next_ancesor(node)

    def _left_most(self, node):
        if node.left is not None:
            return self._left_most(node.left)
        else:
            return node.data

    def _next_ancesor(self, node):
        if node.parent is not None:
            if node.parent.data > node.data:
                return node.parent.data
            else:
                return self._next_ancesor(node.parent)
        return None


if __name__ == '__main__':
    # run_BstBfs()
    # run_BstHeight()
    run_bstmin()

