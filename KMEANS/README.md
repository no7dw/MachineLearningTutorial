### K-Means 算法

K-Means 属于无监督，k-NN k-means 类算法都是需要指定k。

但是如何K设置什么值合适，通过使用轮廓系数(Silhouette Value)来去评价，进行K 小，分类足够区分度

Silhouette Value

The silhouette value for each point is a measure of how similar that point is to points in its own cluster compared to points in other clusters, and ranges from -1 to +1.

The silhouette value for the ith point, Si, is defined as

Si = (bi-ai)/ max(ai,bi) where ai is the average distance from the ith point to the other points in the same cluster as i, and bi is the minimum average distance from the ith point to points in a different cluster, minimized over clusters.


解析：
其实就是再一次算看看，想要达到：第i点离它对应cluster中心点的距离要近，离其他点对于的cluster中心点要远。
这个跟本质K-means的euclidean 算法是一致的。
Si 公式越大，效果越好。

![2020-04-19-22-25-13](http://img.no1token.com/2020-04-19-22-25-13.png)

**我们倾向去最大的Si，对应最小的K**

见Clus-K-Means-images.ipynb 的find_best_k()

![2021-01-22-15-40-17](http://img.no1token.com/2021-01-22-15-40-17.png)




