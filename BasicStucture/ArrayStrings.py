#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   Description :  基础数据结构3.2： 数组与字符串
   Author :       
   Date :         2020-08-26 19:47
   Email:         @my.bristol.ac.uk
   Mobile:         
-------------------------------------------------

"""

"""
1. 判断一个字符串是否包含唯一的字符
2. 判断一个字符串是否有其他排列
3. 判断一个字符串是否是其他字符串的回转
4. 压缩一个字符串
5. 反序一个字符串
6. 给定两个字符串，找出单个不同的字符
7. 找到两个切片索引，使得值等于特定的值
8. 实现一个哈希表
9. 实现fizz和buzz
"""


"""
# 8. 实现哈希表的数据结构
(1) hash功能：返回 键 与 表大小 求膜
(2) set: 为寻找的主键设定索引，如果存在则替代否则增加
(3) get: 为寻找的主键获得主键，如果存在则获得值，否则报错
(4) remove: 为寻找的主键获得主键, 如果存在则删除item元素，否则报错
"""


# 定义基本的item类
class Item(object):
    def __init__(self, key, value):
        """
        初始化
        :param key: 键
        :param value: 值
        """
        self.key = key
        self.value = value

    def __str__(self):
        """
        :return: print信息
        """
        return "key:{self.key} value:{self.value}".format(self=self)


# 定义哈希表的类
class HashTable(object):
    def __init__(self, size):
        """
        初始化
        :param size: 哈希表大小,并初始化表大小为size长度
        """
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        """
        实现 hash_function, 返回求暮值, 是此键的索引
        :param key:
        :return:
        """
        return key % self.size

    def set(self, key, value):
        """
        设定值
        :param key: 主键
        :param value: 值
        :return:
        """
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                item.value = value
                return
        self.table[hash_index].append(Item(key, value))

    def get(self, key):
        """
        得到值
        :param key:
        :return:
        """
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                return item.value
        raise KeyError("Key not found")

    def remove(self, key):
        hash_index = self._hash_function(key)
        for index, item in enumerate(self.table[hash_index]):
            if item.key == key:
                del self.table[hash_index][index]
                return
        raise KeyError("Key not Found")




