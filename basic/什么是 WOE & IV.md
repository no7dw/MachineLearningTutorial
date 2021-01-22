### 什么是 WOE & IV & Entropy & Information Gain & GINI

#### WOE 公式
WOE = In(% of non-events ➗ % of events)

#### IV
IV = ∑ (% of non-events - % of events) * WOE

![2021-01-22-00-17-36](http://img.no1token.com/2021-01-22-00-17-36.png)


[参考资料](https://www.listendata.com/2015/03/weight-of-evidence-woe-and-information.html)

至于 上面的指的数值范围以及意义，见这个笔记
[如何评估一个机器学习模型](https://www.evernote.com/l/ASrzNBLx2c5Bd6imLOzNppf-RH_5J7YzUNg)

#### Entropy
作用：measure of disorder

![2021-01-22-12-06-37](http://img.no1token.com/2021-01-22-12-06-37.png)

看Pi取值分布对E(S)的影响。Pi 是 class i的概率
![2021-01-22-12-09-12](http://img.no1token.com/2021-01-22-12-09-12.png)

看出：概率分布越不均，E(S)值越小。均分，则值为0。
#### Information Gain

![2021-01-22-12-10-39](http://img.no1token.com/2021-01-22-12-10-39.png)

特点：当Informatin Gain 越大时，E(Y) 要趋向大， E(Y|X) 趋向小。

X 拆解成具体的子分类 -- 也就是分箱

![2021-01-22-12-13-35](http://img.no1token.com/2021-01-22-12-13-35.png)
##### X分箱后的Weighted Average 计算E(Y|X)

由于期望趋势E(Y|X) 小， 要通过 Weighted Average 计算 E(Y|X) 。
 所以，相当于X的分箱的分布期望是E(Xi) 越小： 
 - 分布越不均,即E(Xi)小，weighted %占比大。
 - 分布均 ,即E(Xi)大，weighted %占比小。

 总结来说就是期望这样的X：分布越不均，并且占比越大 
因此Information Gain 用于多个特征挑选DecisionTree 分叉时的决策先后顺序

[参考资料](https://towardsdatascience.com/entropy-how-decision-trees-make-decisions-2946b9c18c8)

