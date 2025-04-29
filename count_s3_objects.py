
import boto3

bucket_name = 'your-bucket-name'  # Replace with your bucket name
s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)

object_count = sum(1 for _ in bucket.objects.all())
print(f"Total objects in '{{bucket_name}}': {{object_count}}")
