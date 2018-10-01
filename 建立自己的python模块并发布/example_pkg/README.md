# Example Package

nestList.py是一个可以打印缩进列表的示例函数,示例代码如下：
```
from example_pkg_zx1 import nestList
alist = ["grace", "angle", "roy", 
            ["anna", "jhon", "richard", ["nio", "lily"]], 
            "bluce"]        
nestList.print_list(alist)
```