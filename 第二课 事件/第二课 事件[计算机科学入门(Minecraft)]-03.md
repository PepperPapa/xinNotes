#### 实践：鹦鹉
##### 检查是否有[被破坏时]()块
1. 从[方块]()工具箱，将[被破坏时]()块拖放至代码工作区。这将是你的事件处理程序。
![image.png](https://upload-images.jianshu.io/upload_images/13863515-f1e5c42d158d6fe3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
##### 查找蛋糕
使用下拉菜单，选择蛋糕。可以直接输入“蛋糕”进行搜索。
![image.png](https://upload-images.jianshu.io/upload_images/13863515-7a6243b332320bb7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
##### 产生一个动物
从[生物]()工具箱，放置[生成animal]()块到[被破坏时]()块中，直到卡到位。
![image.png](https://upload-images.jianshu.io/upload_images/13863515-d7ffbfe202b71910.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
##### 把它变成一支鹦鹉
通过[生成animal]()块中的下拉菜单，选择鹦鹉。你希望在头部上方产生鹦鹉，因此将[生成animal]()块中的坐标y修改为1。
![image.png](https://upload-images.jianshu.io/upload_images/13863515-edd2af783947706f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
##### 更多鹦鹉！
这只会在你头顶产生一直鹦鹉，所以让我们用一个[重复]()循环来产生24只鹦鹉。
1. 从[循环]()工具箱，在[生成animal]()块周围放置一个[重复]()循环。
2. 在这个[重复]()循环中，输入数字24。
![image.png](https://upload-images.jianshu.io/upload_images/13863515-29b7382112c1acb7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
##### 运行代码
要在游戏中运行此功能，添加一个蛋糕到你的玩家库中（按E打开库存），在工具栏中选择蛋糕（使用鼠标滚轮或数字键进行选择物品），然后右键单击放置蛋糕到地面上。
然后换回你的手，用鼠标左键单击蛋糕可以摧毁它 - 你会看到一群鹦鹉出现！
![image.png](https://upload-images.jianshu.io/upload_images/13863515-b07f887488c72a6d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
##### 挑战
尝试完成如下挑战以获得更多事件练习。
###### 挑战1 - 让豹猫出现
修改当前代码，以便当你摧毁草块时出现5个豹猫。
###### 挑战2 - 使用tnt输出单词“broken”
让我们改变当草块被破坏时发生了什么。现在让我们使用tnt输出单词“broken”。
> make code中使用搜索查找“输出”，然后使用这个坐标以便输出的开始位置离你远一点！
![image.png](https://upload-images.jianshu.io/upload_images/13863515-61ae24d5c9e9a4d9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
##### 实验
这里没有规则......复制代码并修改看看你可以创造出什么样的结果。给出了建议，但随心所欲！
### 实验1 - 自动放置蛋糕
自动移动蛋糕到你的库存。你不需要手动添加蛋糕到你的玩家库存就可以运行这个游戏。你可以在开始时给自己什么其他的东西？？？
### 实验2 - 链式事件
这里你可以看到一个链式事件。你摧毁蛋糕产生鹦鹉，然后如果你杀死鹦鹉，你会产生骷髅马。你可以构造出其他因果链吗？