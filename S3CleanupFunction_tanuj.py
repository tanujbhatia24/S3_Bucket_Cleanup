import boto3
from datetime import datetime, timezone, timedelta

def lambda_handler(event, context):
    bucket_name = 'prashant-batch10'
    s3 = boto3.client('s3')
    deleted_files = []
    retained_files = []
    all_files = []
    threshold = timedelta(days=30)
    now = datetime.now(timezone.utc)

    print(f"Scanning bucket: {bucket_name} for cleanup...")

    paginator = s3.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(Bucket=bucket_name)

    for page in page_iterator:
        if 'Contents' not in page:
            continue

        for obj in page['Contents']:
            key = obj['Key']
            last_modified = obj['LastModified']
            age = now - last_modified
            all_files.append(f"{key} (LastModified: {last_modified}, Age: {age.days} days)")

            if age > threshold:
                try:
                    s3.delete_object(Bucket=bucket_name, Key=key)
                    deleted_files.append(key)
                    print(f"Deleted: {key} (Age: {age.days} days)")
                except Exception as e:
                    print(f"Failed to delete {key}: {e}")
            else:
                retained_files.append(key)
                print(f"Retained: {key} (Age: {age.days} days)")

    return {
        'statusCode': 200,
        'body': {
            'total_files': len(all_files),
            'deleted_files': deleted_files,
            'retained_files': retained_files
        }
    }
