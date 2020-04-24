### featuretools Worker memory is between 1 to 2 times the memory size of the EntitySet 问题解决
 
EntitySet 比较大， n_jobs 设置太大, 
报错 
`
Worker memory is between 1 to 2 times the memory size of the EntitySet
`

来源 
https://github.com/FeatureLabs/featuretools/blob/31ace1c2e37362f6aa3451cbf0c1b4f800542af4/featuretools/computational_backends/utils.py#L184

![2020-04-24-13-08-37](http://img.no1token.com/2020-04-24-13-08-37.png)

https://github.com/FeatureLabs/featuretools/blob/31ace1c2e37362f6aa3451cbf0c1b4f800542af4/featuretools/computational_backends/utils.py#L123
![2020-04-24-13-07-52](http://img.no1token.com/2020-04-24-13-07-52.png)

https://github.com/FeatureLabs/featuretools/blob/31ace1c2e37362f6aa3451cbf0c1b4f800542af4/featuretools/computational_backends/utils.py#L161
![2020-04-24-13-09-17](http://img.no1token.com/2020-04-24-13-09-17.png)


计算参考：
系数说明， 0.8 保留给系统内存,
但测试最好保险，结果再除以2
![2020-04-24-13-11-09](http://img.no1token.com/2020-04-24-13-11-09.png)
