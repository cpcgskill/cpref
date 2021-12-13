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
    import maya.mel as mel
    from cpref.object_ref import Ref
    mel.eval("""polySphere -r 1 -sx 20 -sy 20 -ax 0 1 0 -cuv 2 -ch 1 -n test_poly;
doGroup 0 1 1;
doGroup 0 1 1;
doGroup 0 1 1;
doGroup 0 1 1;
doGroup 0 1 1;
setKeyframe -breakdown 0 -preserveCurveShape 0 -hierarchy none -controlPoints 0 -shape 0 {"group5"};""")
    r = Ref("test_poly")
    print("Ref __init__ >>", r)
    print("Ref mel_object >>", r.mel_object())
    print("Ref full_path_name >>", r.full_path_name())
    print("Ref partial_path_name >>", r.partial_path_name())

    print("### test test_poly")
    r = Ref("test_poly")
    print("Ref format >>", r)
    print("Ref ref_type >>", r.ref_type())

    print("### test test_poly.vtx[*]")
    r = Ref("test_poly.vtx[*]")
    print("Ref format >>", r)

    print("### test test_poly.vtx[0]")
    r = Ref("test_poly.vtx[0]")
    print("Ref format >>", r)

    print("### test test_poly.tx")
    r = Ref("test_poly.tx")
    print("Ref format >>", r)
    print("Ref ref_type >>", r.ref_type())

    #
    # print("### test all nodes")
    # for i in mc.ls("*"):
    #     r = Ref(i)
    #     print("test all Ref format >>", r)
    #     for attr in mc.listAttr(i):
    #         try:
    #             r = Ref("{}.{}".format(i, attr))
    #         except:
    #             print("ERROR!!!", "{}.{}".format(i, attr))
    #             continue
    #         print("test all Ref format >>", r)
    # print("NodeRef full_path_name >>", r.full_path_name())
    # print("NodeRef partial_path_name >>", r.partial_path_name())
    # print("NodeRef name >>", r.name())
    # print("NodeRef absolute_name >>", r.absolute_name())
