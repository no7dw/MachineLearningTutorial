### 机器学习入门 快速版

本文地址： https://github.com/no7dw/MachineLearningTutorial

#### background
从数据量的角度，Machine Learning (ML) 是解决传统程序在数据量大，条件多的情况下，使用代码处理复杂场景已经力不从心的情况下的一种解决方案。
而Deep Learning 是进一步数据量爆炸的情况下，保证学习速度、效果的一种新的途径。

机器学习有多种算法类别
 - 有监督
 - 无监督

 有监督，常见：
 - KNN
 - Logistic Regression
 - Support Vector Machines
 - Decission Tree

 无监督，常见：
 - Hierachical Clustering
 - K-Means 
 - Hierachical Clustering
 - DBSCAN

 常见的算法都有包可以调用，但每种算法有pros and cons（对于精度、速度、边界值上），要根据常见去选择合适的算法。后续将逐渐总结这些算法的关键，优缺点、例子 在各个算法的子文件夹里面。

 ML的基本流程以有监督学习，举个例子：
 - 获取数据
 - 分train set , test set
 - 训练fit
 - predit
 - 检查准确率

简单总结就是：
 - 分、学、猜、再调整。
 
 - 分、猜、测、再调整

具体见KNN.ipynb

