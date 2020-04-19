## 神经网络 Neural Networks 教程 快速入门

#### 神经网络的loss function

#### 神经网络的激活函数 activation functions 之间的对比 
先看图了解定义：
![2020-04-19-23-05-41](http://img.no1token.com/2020-04-19-23-05-41.png)

 - Sigmoid 特点
     -  z 趋向无穷大，g(z) ~ 1
     -  z 趋向负无穷大，g(z) ~ 0
     -  z = 0 -> g(z) 0.5

    适合于 0 , 1 的可能性。其他大部分情况都不用。

 - TanH 特点
     -  z 趋向无穷大，g(z) ~ 1
     -  z 趋向负无穷大，g(z) ~ -1
     -  z = 0 -> g(z) 0


 - ReLU 特点
     - rectified linear unit
     -  z >= 0，z
     -  z < 0，g(z) = 0
    
    适用于z < 0 , 想忽略结果的常见

 - Leaky ReLU 特点
     -  z >= 0，z
     -  z < 0，g(z) = 0.01*z
    
    ReLU 改进版，希望z < 0 , 想有少量效果

哪些场景用用哪个？Andrew 指出除了特点概率输出[0,1] 可以用Sigmoid, 其他大部分都用ReLU or Leaky ReLU。但具体以最优结果为准，实际的编码尝试中，都可以去试试。



#### Gradient Descent 

正如之前说的，机器学习就是： 学、猜、再调整。 GD 在“猜” 比较神奇，算是一个伟大的算法。主要是用于反向推断。

##### 算法原理
看图：
![2020-04-19-23-22-39](http://img.no1token.com/2020-04-19-23-22-39.png)

convex function vs non-convex function :

- convex  has only one optimism point
- non-convex  has multiple optimism points

通过初始化，因为训练一直Y，本质求weight matrix，所以往各个方向去猜，能判断是否偏离目的地。

##### Gradient Descent 实现的注意点
以两层的NN 为例：
关键backprogagation 公式如下：
![2020-04-19-23-21-13](http://img.no1token.com/2020-04-19-23-21-13.png)

注意：
 - 上面提及初始化W matrix，我们通常要用的是np.random.randn (有负数)，而非np.random.rand（正数）。
 - learning rate：
    - 其中的公式 W1 = W1 - learning_rate*dW1
    - 设置过大，会导致计算偏快，但可能错失最优点
    - 设置过小，会导致计算偏慢
 - 设置多少层NN：
    - 与learning rate 设置类似，只是反向
    - 设置大些，会导致计算偏慢，但准确率更优
    - 设置过小，会导致计算偏快，但准确率达不到要求

 - 图片的处理:
    - 自己实现的话，要先预处理，size & 颜色(RGB channel)要统一
    - tensorflow 处理的话，有函数tf.image.resize可以统一处理