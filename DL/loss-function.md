### difference between loss function and cost function

loss function vs cost function
loss functin is for single data point, and cost function is general for sum of loss functions of a whole data set.
#### sample 
loss function -- 误差 
    square loss
    ![2020-06-28-13-46-31](http://img.no1token.com/2020-06-28-13-46-31.png)
cost function -- 均误差
    mean squared error MSE
    ![2020-06-28-13-47-04](http://img.no1token.com/2020-06-28-13-47-04.png)


有了train data, predict 后，根据loss function —> 算出data point数值。调整参数/系数 目的是为了 cost function 的结果偏向小， 均误差局部/全局最优

![2020-06-28-13-29-29](http://img.no1token.com/2020-06-28-13-29-29.png)

common cost function:
- MSE
    ![2020-06-28-13-47-04](http://img.no1token.com/2020-06-28-13-47-04.png)
- MAE
    ![2020-06-28-13-49-38](http://img.no1token.com/2020-06-28-13-49-38.png)
- MBE
    ![2020-06-28-13-49-51](http://img.no1token.com/2020-06-28-13-49-51.png)

common lost function:

- Cross Entropy Loss/Negative Log Likehood
    ![2020-06-28-13-50-23](http://img.no1token.com/2020-06-28-13-50-23.png)
- SVMLoss for Classification
    ![2020-06-28-13-50-07](http://img.no1token.com/2020-06-28-13-50-07.png)

[ref](https://stats.stackexchange.com/questions/179026/objective-function-cost-function-loss-function-are-they-the-same-thing#:~:text=The%20loss%20function%20computes%20the,of%20the%20entire%20training%20set.)