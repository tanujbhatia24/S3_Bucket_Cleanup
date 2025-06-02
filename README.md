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
- Created a bucket named `tanuj-s3-cleanup-bucket`
- Uploaded multiple test files

### 2. IAM Role Setup
- Created role: `tanuj_lambda_s3_cleanup_role`
- Attached policy: `AmazonS3FullAccess`

### 3. Lambda Function Setup
- Function Name: `S3CleanupFunction_tanuj`
- Runtime: Python 3.x
- Attached IAM Role: `tanuj_lambda_s3_cleanup_role`
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
  ![image](https://github.com/user-attachments/assets/67cf74fe-e83e-43a0-a2a1-1abf5b198525)<br>
  ![image](https://github.com/user-attachments/assets/dbf5b0c4-60c6-4bd1-8b8a-cefc692a739a)<br>
  
- IAM role with permissions<br>
  ![image](https://github.com/user-attachments/assets/15fad19b-5bba-4017-845a-49c1b99dc17d)<br>

- Lambda function<br>
  ![image](https://github.com/user-attachments/assets/959be881-fa48-4a97-aa18-10678ba3b34c)<br>

- Lambda test execution<br>
  ![image](https://github.com/user-attachments/assets/f47a44bb-13ed-4d3a-99d9-9f049d592278)<br>
  ![image](https://github.com/user-attachments/assets/766492a6-3ff9-4ce3-9028-4cd05cfc2302)<br>
  
- S3 bucket after cleanup<br>
  ![image](https://github.com/user-attachments/assets/f0ac290c-e89c-4d8d-840b-e354a72b3c99)<br>
---

## License
This project is intended for educational and demonstration purposes. You are welcome to use and adapt it as a reference; however, please ensure that your work represents your own understanding and is not reproduced verbatim.
