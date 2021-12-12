# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/12/11 11:43
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function
from cpapi.all import MUuid, MObject, MDagPath, MObjectHandle, MFnDependencyNode, MSelectionList
from cpapi.utils import muuid_to_mobject, muuid_to_mdagpath
from .exc import *

class NodeRef(object):
    def __init__(self, uuid):
        """

        :type uuid: MUuid
        """
        self._muid = uuid

    def does_it_exist(self):
        """

        :rtype: bool
        """
        return self.muuid().uid.valid()

    def muuid(self):
        """

        :rtype: MUuid
        """
        return self._muid

    def mobject(self):
        """

        :rtype: MObject
        """
        return muuid_to_mobject(self.muuid())

    def mdagpath(self):
        """

        :rtype: MDagPath
        """
        return muuid_to_mdagpath(self.muuid())

    def full_path_name(self):
        """

        :rtype: unicode
        """
        return self.mdagpath().fullPathName()

    def partial_path_name(self):
        """

         :rtype: unicode
         """
        return self.mdagpath().partialPathName()

    def name(self):
        """

         :rtype: unicode
         """
        return MFnDependencyNode(self.mobject()).name()

    def absolute_name(self):
        """

         :rtype: unicode
         """
        return MFnDependencyNode(self.mobject()).absoluteName()

    def to_mel_object(self):
        """

         :rtype: Any
         """
        if self.does_it_exist():
            return self.full_path_name()
        else:
            raise EmptyObjectException("引用的节点已丢失")
