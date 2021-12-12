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
```

### 功能介绍

#### Maya节点引用

Maya节点引用功能提供了对Maya节点长期引用

```python
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

test()
```

```
NodeRef __init__ >> <cpref.node.NodeRef object at 0x0000027A29459148>
NodeRef full_path_name >> |test_joint
NodeRef partial_path_name >> test_joint
NodeRef name >> test_joint
NodeRef absolute_name >> :test_joint
```

### 版权说明

该项目签署了Apache-2.0 授权许可，详情请参阅 LICENSE