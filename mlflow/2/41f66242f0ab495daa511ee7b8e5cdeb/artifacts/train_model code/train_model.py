from sklearn.linear_model import LinearRegression
import pickle
import pandas as pd
import os
 
import mlflow
from mlflow.tracking import MlflowClient
 
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("train_model")
 
df = pd.read_csv('/home/admin123/xFlow/datasets/data_train.csv', header=None)
df.columns = ['id', 'counts']
model = LinearRegression()
 
with mlflow.start_run():
    mlflow.sklearn.log_model(model,
                             artifact_path="lr",
                             registered_model_name="lr")
    mlflow.log_artifact(local_path="/home/admin123/xFlow/scripts/train_model.py",
                        artifact_path="train_model code")
    mlflow.end_run()
 
model.fit(df['id'].values.reshape(-1,1), df['counts'])
 
with open('/home/admin123/xFlow/models/data.pickle', 'wb') as f:
    pickle.dump(model, f)
