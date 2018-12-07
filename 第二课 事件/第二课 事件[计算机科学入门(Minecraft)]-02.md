### 实践：黄金路
如下图，当[玩家步行时]()是一种针对玩家具体行为的事件处理程序。它的下拉菜单列出了玩家可能执行的各种动作，如步行、跳跃、在熔岩中游泳等等。
![image.png](https://upload-images.jianshu.io/upload_images/13863515-f75b5230bc3ba5ad.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
你可以配置此事件处理程序，以便在玩家行走时发生某些事情。例如，在行走的任意位置放置花朵。
##### 开始实践
###### 开始监听行走事件
1. 从玩家工具箱中将[当玩家步行时]()块拖至代码编辑区。
![当玩家步行时事件处理程序块](https://upload-images.jianshu.io/upload_images/13863515-7ee5df39abd22f1c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
##### 放一些草块
2. 从方块工具箱中将[放置 位置]()块拖放到[当玩家步行时]()块上，直到你听到并看到它卡入到位（如果卡到位会有咔的声响）。
![image.png](https://upload-images.jianshu.io/upload_images/13863515-e66761942c9a9c6e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
##### 放一朵花
3. 使用[放置 位置]()块的下拉菜单，选择蒲公英（黄色花）。
![image.png](https://upload-images.jianshu.io/upload_images/13863515-81e67e368904d0fe.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
##### 四处走走，种花
现在，在游戏中无论走到哪里都会留下蒲公英的痕迹！在我的世界中尝试按键盘上的**w**健向前行走，然后看看身后，你应该会看到一串花！
> 摄像头视角    
按F5可以切换视角，这样你就看到行走时出现的花朵。    

![image.png](https://upload-images.jianshu.io/upload_images/13863515-cba5d42c09cf9c76.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> **教师提醒**
鲜花被放置在(~0 ~0 ~0)。我们将在下一课中更详细地探索坐标系。当前只要知道三个坐标（X，Y，Z）在Minecraft游戏中代表不同方向就够了：
> * X坐标 - 东/西
> * Y坐标 - 向上/向下
> * Z坐标 - 北/南     
> 上一个例子中的花放在(~0 ~0 ~0)。波浪号（〜）表示相对于玩家的相对坐标，因此距离玩家有0个块。   
##### 尝试用黄金块
因为在[放置位置]()块中你使用的坐标是(~0 ~0 \~0)，花朵被放置在地面上。中间的~0为Y坐标，表示块向上或向下放置的距离。
现在假如你想在身后留下一条黄金道路，这样不管你走到哪里就会创建一条“黄金块路”。你可以在[放置位置]()块中用同样的方法做到，只需把花朵替换为金块。
![image.png](https://upload-images.jianshu.io/upload_images/13863515-858cd30581c0a98b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
看看会发生什么：
![image.png](https://upload-images.jianshu.io/upload_images/13863515-e94751b172a78157.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
这是正确的想法，但是不完全是你想要的结果。实际上你是在身后留下一了堵金墙，这是很不方便的。该如何把这些块下沉到地面以形成一条黄金路哪？
让我们将Y坐标减1，使块的底面离地面往下1个等级。
![image.png](https://upload-images.jianshu.io/upload_images/13863515-2fa1f00803bd93fc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

现在让我们看看会发生什么：
![image.png](https://upload-images.jianshu.io/upload_images/13863515-0730b960b184ad59.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
好多了！尝试做出一条合适的黄金路，至少三个块宽，这样你和你的朋友可以并排走路。**提示:**在方块工具箱中使用一个不同的块！

**解答:**
![image.png](https://upload-images.jianshu.io/upload_images/13863515-0cd9c4c9184bcc76.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/13863515-ee98777e6ce30c78.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
##### 坐标系和事件
现在你已经使用坐标系和事件进行了一些实验。下节课会更多关注坐标系(X,Y,Z)，但是这里仅做简要提及。如果你对坐标系有点困惑，请不用担心！
##### 挑战
希望你对事件的理解更加清晰了。尝试如下挑战以获得关于事件的更多练习。
###### 挑战1 - 创建钻石天花板
使用黄金路的例子作为开始。如何在行走的时候创建钻石天花板？如果下雨时，天花板可能更好！
![image.png](https://upload-images.jianshu.io/upload_images/13863515-128a4f7aa5775235.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
>中间坐标（X，Y，Z）Y需要修改，使你可以将砖块放在头顶上方。你的角色是两个块高，但是是从0开始的。因此，你的角色的头位于1。将Y改为2或3会将块放在角色的头部正上方。

![image.png](https://upload-images.jianshu.io/upload_images/13863515-9601f89e4307af9f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
###### 挑战2 - 飞行时建造
作为挑战，当你的角色飞行（**minecraft游戏创造模式下快速按下两次空格健会进入飞行模式**）时放置一些东西！这个概念类似于你之前放置花朵和金块的方式，但是你需要改变一些东西。使用如下图所示的坐标。你能搞清楚会发生什么吗？
>使用这些坐标
![walk through air](http://upload-images.jianshu.io/upload_images/13863515-6b8dee882590ff15.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### Experiments
这里没有规则......复制代码并修改看看你可以创造出什么样的结果。给出了建议，但随心所欲！
###### 实验1 - 魔毯骑行
如果你建造了一个神奇的地毯来支持你在世界各地的移动，该怎么做？主要关注两个事件：[当玩家步行时]()和[当玩家飞行时]()。
你怎么能改变这段代码？你能用其他事件吗？还有什么可以改变的？
###### 实验2 - 魔毯艺术魅力
如果您根据事件构建了一个在魔毯（改变块的设置），该如何做？你飞行时可能会发生什么其他事情与你走路时有所不同？