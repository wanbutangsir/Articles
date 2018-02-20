#coding=utf-8
### 导入相关的库
import numpy as np
import pandas as pd
from IPython.display import display 

data = pd.read_csv("customers.csv") #读入数据
data.drop(['Region', 'Channel'], axis = 1, inplace = True) #删除'Region', 'Channel'特征值
print("2. 读取数据集")
print("数据集有 {} 样本和 {} 特征值.".format(*data.shape))

print("3.1 统计数据")
display(data.describe())


indices = [3, 141, 340] # 样本的索引
samples = pd.DataFrame(data.loc[indices], columns = data.keys()).reset_index(drop = True) # 创建samples保存样本数据
print("从数据集中采样的数据包括:")
display(samples)

new_data = data.copy()
new_data.drop(['Delicatessen'], axis = 1, inplace = True) # 删除特征值作为新的数据集

from sklearn.cross_validation import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(new_data, data['Delicatessen'], test_size=0.25, random_state=42) # 将数据集划分为训练和测试集

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0) # 创建学习器
regressor.fit(X_train, y_train) # 训练学习器

score = regressor.score(X_test, y_test) # 得到效果得分
print("决策树学习器得分：{}".format(score))

pd.scatter_matrix(data, alpha = 0.3, figsize = (14,8), diagonal = 'kde');
