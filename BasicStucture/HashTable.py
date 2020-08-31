#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('/Users/msb/Downloads/_work/JupyterScript_ipy/program_works/model_try/ds')
# sys.path.append('C:\\Users\\\\Downloads\\coding\\ProjectAll\\test\\DataStructure')
from BasicStucture.ArrayStrings import HashTable, Item

"""
-------------------------------------------------
   Description :  基础数据结构三：散列表
   Author :       
   Date :         2020/8/11  1:14
   Software:      PyCharm
   Email:         @my.brisol.ac.uk  
-------------------------------------------------

"""


class HashTablev2(HashTable):
    """
    （1）其假设key必定为自然数，但是其实并不是如此. key可能为非自然数
    （2）如果运气差，求膜全部到一个
    """
    # def trans_key(self, key):





