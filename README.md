# cpref

Maya 对象引用库

## 目录

- [快速开始](#快速开始)
- [功能介绍](#功能介绍)
    - [Maya节点引用](#Maya节点引用)
- [版权说明](#版权说明)

### 快速开始

#### 如果你的Maya有pip那么

```commandline
cd "C:\Program Files\Autodesk\Maya2022\bin"
mayapy -m pip install cpref
```

#### 如果没有

1. 打开C:\Users\PC\Documents\maya文件夹
2. 进入scripts文件夹，如果没有就创建它
3. 下载完整的cpref代码
4. 解压并进入解压完成的文件夹
5. 将src目录中的cpref文件夹复制到scripts
6. 打开maya，如果已经打开了就重启它
7. 打开脚本编辑器并执行以下示例代码

```python
import maya.mel as mel
from cpref.object_ref import Ref

mel.eval("""polySphere -r 1 -sx 20 -sy 20 -ax 0 1 0 -cuv 2 -ch 1 -n test_poly;
doGroup 0 1 1;
doGroup 0 1 1;
doGroup 0 1 1;
doGroup 0 1 1;
doGroup 0 1 1;
setKeyframe {"group5"};""")
r = Ref("test_poly")
print("Ref __init__ >>", r)
print("Ref is_null >>", r.is_null())
print("Ref as_string >>", r.as_string())
print("Ref as_string_list >>", r.as_string_list())
```

### 功能介绍

#### Maya节点引用

Maya节点引用功能提供了对Maya节点长期引用

```python
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
setKeyframe {"group5"};""")
    r = Ref("test_poly")
    print("Ref __init__ >>", r)
    print("Ref is_null >>", r.is_null())
    print("Ref as_string >>", r.as_string())
    print("Ref as_string_list >>", r.as_string_list())

    print("")
    print("")

    print("### test unsafe methods")
    print("Ref unsafe_m_selection_list >>", r.unsafe_m_selection_list())
    print("Ref unsafe_as_string_list >>", r.unsafe_as_string_list())
    print("Ref unsafe_m_dag_path >>", r.unsafe_m_dag_path())
    print("Ref unsafe_full_path_name >>", r.unsafe_full_path_name())
    print("Ref unsafe_partial_path_name >>", r.unsafe_partial_path_name())

    print("")
    print("")

    print("### test test_poly")
    r = Ref("test_poly")
    print("Ref format >>", r)
    print("Ref ref_type >>", r.ref_type)

    print("### test test_poly.vtx[*]")
    r = Ref("test_poly.vtx[*]")
    print("Ref format >>", r)

    print("### test test_poly.vtx[0]")
    r = Ref("test_poly.vtx[0]")
    print("Ref format >>", r)

    print("### test test_poly.tx")
    r = Ref("test_poly.tx")
    print("Ref format >>", r)
    print("Ref ref_type >>", r.ref_type)

    print("")
    print("")

    print("### test object null check")
    r = Ref("test_poly")
    mel.eval("file -f -new;")
    print("Ref is_null >>", r.is_null())


test()
```

```
Ref __init__ >> DagNode<u'test_poly'>
Ref is_null >> False
Ref as_string >> test_poly
Ref as_string_list >> (u'test_poly',)


### test unsafe methods
Ref unsafe_m_selection_list >> ('test_poly')
Ref unsafe_as_string_list >> (u'test_poly',)
Ref unsafe_m_dag_path >> test_poly
Ref unsafe_full_path_name >> |group5|group4|group3|group2|group1|test_poly
Ref unsafe_partial_path_name >> test_poly


### test test_poly
Ref format >> DagNode<u'test_poly'>
Ref ref_type >> 1
### test test_poly.vtx[*]
Ref format >> Component<u'test_poly.vtx[0:381]'>
### test test_poly.vtx[0]
Ref format >> Component<u'test_poly.vtx[0]'>
### test test_poly.tx
Ref format >> Plug<u'test_poly.translateX'>
Ref ref_type >> 0


### test object null check
Ref is_null >> True
```

### 版权说明

该项目签署了Apache-2.0 授权许可，详情请参阅 LICENSE