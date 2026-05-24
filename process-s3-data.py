import pandas as pd
import boto3

s3 = boto3.client('s3')

bucket_name = 'amzn-s3-learning-2026q2'
file_name = 'flights.csv'

s3.download_file(bucket_name, file_name, "flights_local.csv")

print("File downloaded successfully")

df = pd.read_csv("flights_local.csv")

# print(df.head())

df["Status"] = "Processed"

print(df.head())

processed_file = "processed_file.csv"
df.to_csv(processed_file, index=False)
print("Downloaded processed file")

s3.upload_file(processed_file, bucket_name, "processed_file.csv")
print("Processed file uploaded to s3")