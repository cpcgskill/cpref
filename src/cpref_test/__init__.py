# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/12/12 11:39
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function
import os
import sys
from imp import reload

os.environ["CPREF_DEBUG"] = "on"
import cpref

if not sys.modules.get("cpref") is None:
    reload(cpref)


from cpref_test import (node, )

models = (node, )
for m in models:
    reload(m)


def test():
    for m in models:
        print("## test models {}:".format(m))
        m.test()
