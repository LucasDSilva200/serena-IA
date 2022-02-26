import sklearn
from sklearn.datasets import load_iris
import pandas as pd


iris = load_iris()
iris.target[[10,25,50]]
iris_df=pd.DataFrame(data=iris.data,columns=iris.feature_names)
iris_df['target']=iris.target
iris_df['target names'] = pd.Categorical.from_codes(iris.target, iris.target_names)
print(iris_df.head())