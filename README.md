# Automated S3 Bucket Cleanup Using AWS Lambda and Boto3
This project automates the deletion of objects older than 30 days in an S3 bucket using a Lambda function written in Python and Boto3.
---

## Objective
Automatically clean up S3 storage by removing files older than 30 days using a scheduled or manually-invoked Lambda function.
---

## Tools & Technologies
- AWS S3
- AWS Lambda
- AWS IAM
- Python 3.x
- Boto3
---

## Setup Instructions
### 1. S3 Bucket Creation
- Created a bucket named `my-s3-cleanup-bucket`
- Uploaded multiple test files

### 2. IAM Role Setup
- Created role: `lambda_s3_cleanup_role`
- Attached policy: `AmazonS3FullAccess`

### 3. Lambda Function Setup
- Function Name: `S3CleanupFunction`
- Runtime: Python 3.x
- Attached IAM Role: `lambda_s3_cleanup_role`
- Code Logic:
  - List objects in bucket
  - Compare `LastModified` date
  - Delete if older than 30 days
  - Log deleted filenames
---

## Testing
- Manually triggered the function from the Lambda console
- Verified S3 bucket before and after:
  - Old files were removed
  - Recent files were retained
---

## Screenshots
- S3 bucket before cleanup<br>
- IAM role with permissions<br>
- Lambda function<br>
- Lambda test execution<br>
- S3 bucket after cleanup<br>
---

## License
This project is intended for educational and demonstration purposes. You are welcome to use and adapt it as a reference; however, please ensure that your work represents your own understanding and is not reproduced verbatim.
