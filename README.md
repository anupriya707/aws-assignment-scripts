# aws-assignment-scripts
AWS Assignment Scripts
This repository contains a set of Python scripts developed for AWS-related tasks and a CSV file analysis project.

Files Included:

analyze_csv.py

Reads the students.csv file.

Calculates the average of grades.

Prints names of students with an average grade above a threshold.

count_s3_objects.py

Uses boto3 to count and display the number of objects in a specified S3 bucket.

list_s3_buckets.py

Lists all S3 buckets in the configured AWS account.

upload_to_s3.py

Uploads a local file to a specified S3 bucket.

Requirements:

Python 3.x

boto3 library (install using pip install boto3)

AWS credentials must be configured (via AWS CLI or environment variables)

How to Use:

Clone the repository:
git clone https://github.com/anupriya707/aws-assignment-scripts.git
cd aws-assignment-scripts

Install dependencies:
pip install boto3

Run the script.

Note:

Ensure your AWS credentials are set up correctly using aws configure before running any S3-related scripts.
