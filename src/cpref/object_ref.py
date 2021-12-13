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
from maya.api.OpenMaya import MSelectionList, MItSelectionList
from .exc import *


class Ref(object):
    TPlug, TDagNode, TDependencyNode, TComponent = range(4)
    TText = {
        TPlug: "Plug",
        TDagNode: "DagNode",
        TDependencyNode: "DependencyNode",
        TComponent: "Component",
    }

    def __init__(self, obj_n):
        self._sel = MSelectionList()
        self._sel.add(obj_n)
        self._it_sel = MItSelectionList(self._sel)

    def __str__(self):
        return "{}<{}>".format(self.TText[self.ref_type()], repr(self.mel_object()))

    def full_path_name(self):
        """

        :rtype: unicode
        """

        return self._sel.getDagPath(0).fullPathName()

    def partial_path_name(self):
        """

        :rtype: unicode
        """
        return self._sel.getDagPath(0).partialPathName()

    def ref_type(self):
        t = self._it_sel.itemType()
        if t == MItSelectionList.kUnknownItem:
            raise UnknownObjectTypeException("未知对象类型")
        if t == MItSelectionList.kPlugSelectionItem:
            return self.TPlug
        if t == MItSelectionList.kDNselectionItem:
            return self.TDependencyNode
        if t == MItSelectionList.kDagSelectionItem:
            if self._it_sel.hasComponents():
                return self.TComponent
            return self.TDagNode
        raise UnknownObjectTypeException("未知对象类型")

    def mel_object_list(self):
        o = self._sel.getSelectionStrings()
        if len(o):
            return o
        else:
            raise EmptyObjectException("引用的对象已丢失")

    def mel_object(self):
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