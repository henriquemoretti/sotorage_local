from google.cloud import storage
import pandas as pd

client = storage.Client()

bucket_name = "minhasoperacoes-staging"
bucket = client.get_bucket(bucket_name)

blobs = bucket.list_blobs()
for blob in blobs:
    print(blob.name)
    
csv_files = [blob.name for blob in bucket.list_blobs() if blob.name.endswith(".csv")]
print(csv_files)