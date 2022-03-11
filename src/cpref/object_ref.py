# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/12/13 8:29
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function
from maya.api.OpenMaya import MSelectionList, MItSelectionList, MDagPath
from .exc import *

TPlug, TDagNode, TDependencyNode, TComponent = range(4)
TText = {
    TPlug: "Plug",
    TDagNode: "DagNode",
    TDependencyNode: "DependencyNode",
    TComponent: "Component",
}


class Ref(object):
    __slots__ = ("_sel", "ref_type")

    def __init__(self, obj_n):
        self._sel = MSelectionList()
        self._sel.add(obj_n)

        # 生成引用的对象类型
        _it_sel = MItSelectionList(self._sel)
        t = _it_sel.itemType()
        # if t == MItSelectionList.kUnknownItem:
        #     raise UnknownObjectTypeException("未知对象类型")
        if t == MItSelectionList.kPlugSelectionItem:
            self.ref_type = TPlug
        elif t == MItSelectionList.kDNselectionItem:
            self.ref_type = TDependencyNode
        elif t == MItSelectionList.kDagSelectionItem:
            if _it_sel.hasComponents():
                self.ref_type = TComponent
            else:
                self.ref_type = TDagNode
        else:
            raise UnknownObjectTypeException("未知对象类型")

    def __str__(self):
        return "{}<{}>".format(TText[self.ref_type], repr(self.as_string()))

    def unsafe_m_selection_list(self):
        """
        返回内部选择列表
        :rtype : MSelectionList
        """
        return self._sel

    # def unsafe_m_it_selection_list(self):
    #     """
    #     返回内部选择列表迭代器
    #     :rtype : MItSelectionList
    #     """
    #     return self._it_sel

    def unsafe_as_string_list(self):
        return self._sel.getSelectionStrings()

    def unsafe_m_dag_path(self):
        """
        :rtype: MDagPath
        """
        return self._sel.getDagPath(0)

    def unsafe_full_path_name(self):
        """
        :rtype: unicode
        """
        return self.unsafe_m_dag_path().fullPathName()

    def unsafe_partial_path_name(self):
        """
        :rtype: unicode
        """
        return self.unsafe_m_dag_path().partialPathName()

    def is_valid(self):
        return bool(len(self._sel.getSelectionStrings()))

    def is_null(self):
        return not self.is_valid()

    # def full_path_name(self):
    #     """
    #
    #     :rtype: unicode
    #     """
    #
    #     return self._sel.getDagPath(0).fullPathName()
    #
    # def partial_path_name(self):
    #     """
    #
    #     :rtype: unicode
    #     """
    #     return self._sel.getDagPath(0).partialPathName()
    #
    # def ref_type(self):
    #     """
    #     检查引用的对象类型
    #     :rtype: int
    #     """
    #     t = self._it_sel.itemType()
    #     # if t == MItSelectionList.kUnknownItem:
    #     #     raise UnknownObjectTypeException("未知对象类型")
    #     if t == MItSelectionList.kPlugSelectionItem:
    #         return TPlug
    #     if t == MItSelectionList.kDNselectionItem:
    #         return TDependencyNode
    #     if t == MItSelectionList.kDagSelectionItem:
    #         if self._it_sel.hasComponents():
    #             return TComponent
    #         return TDagNode
    #     raise UnknownObjectTypeException("未知对象类型")

    def as_string_list(self):
        o = self._sel.getSelectionStrings()
        if len(o):
            return o
        else:
            raise EmptyObjectException("引用的对象已丢失")

    def as_string(self):
        """

        :rtype: unicode|list
        """
        o = self._sel.getSelectionStrings()
        l = len(o)
        if l > 1:
            return o
        elif l:
            return o[0]
        else:
            raise EmptyObjectException("引用的对象已丢失")
