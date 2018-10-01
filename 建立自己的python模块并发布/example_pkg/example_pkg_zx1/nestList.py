#python 3.7
"""
模块示例
可以打印嵌套列表
"""

# indent表示缩进，默认0表示无缩进
def print_list(lst, indent = 0):
    for item in lst:
        # 判断列表lst中的每一项是否是list对象，
        # 如果是则递归调用print_list，同时缩进级别加1
        if isinstance(item, list):   
            print_list(item, indent + 1)
        else:
            print("--" * indent, end="")
            print(item)

if __name__ == "__main__":
    # 测试示例
    alist = ["grace", "angle", "roy", 
             ["anna", "jhon", "richard", ["nio", "lily"]], 
             "bluce"]        
    print_list(alist)