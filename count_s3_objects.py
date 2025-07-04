
import boto3

bucket_name = 'anu-web-bucket-2025'  
s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)

object_count = sum(1 for _ in bucket.objects.all())
print(f"Total objects in '{{bucket_name}}': {{object_count}}")
