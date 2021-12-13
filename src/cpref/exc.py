# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/12/12 8:59
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function

class CPRefException(Exception):
    """基础异常"""
    pass


class EmptyObjectException(CPRefException):
    """空对象异常"""
    pass


class UnknownObjectTypeException(CPRefException):
    """未知对象类型异常"""
    pass


__all__ = ['CPRefException', 'EmptyObjectException', 'UnknownObjectTypeException']
