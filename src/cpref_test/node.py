# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/12/12 11:40
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function


def test():
    import maya.cmds as mc
    from cpapi.iter import selected
    from cpapi.utils import mobject_to_muuid
    from cpref.node import NodeRef
    mc.joint(n="test_joint")
    mc.select(["test_joint"], r=True)
    uid = mobject_to_muuid(list(selected())[0])
    r = NodeRef(uid)
    print("NodeRef __init__ >>", r)
    print("NodeRef full_path_name >>", r.full_path_name())
    print("NodeRef partial_path_name >>", r.partial_path_name())
    print("NodeRef name >>", r.name())
    print("NodeRef absolute_name >>", r.absolute_name())
