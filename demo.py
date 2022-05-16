"""
The script iterates through an S3 bucket and tries to find a certain substring
in all of the text files.
Return all file names, where the file content contains said substring.
"""
import time
import argparse
import boto3
from botocore.exceptions import ClientError


def search_substring(filename):
    """
    - Load an object from S3, based on the reference to S3 bucket and
    the reference to this object (filename) in this bucket.
    - Extract object content only if content-type is "text/plain"
    - To find out if substring exists in the content, and to reduce
    reading time read the content line by line
    - Print object name if substring exists
    """
    s3_resource = session.resource('s3')
    s3_object = s3_resource.Bucket(f"{s3_bucket_name}").Object(f"{filename}").get()
    if s3_object['ResponseMetadata']['HTTPHeaders']["content-type"] == "text/plain":
        for line in s3_object['Body'].iter_lines():
            if substring in line.decode('utf-8'):
                print(filename)
                break


def list_files_in_bucket():
    """
        List objects in S3 Bucket. If an object has size bigger than 0,
        invoke the func "find_substr_in_file" with
        object name as an argument
    """
    s3_client = session.client('s3')
    s3_content = s3_client.list_objects(Bucket=s3_bucket_name)['Contents']
    for s3_key in s3_content:
        s3_object = s3_key['Key']
        if s3_key['Size'] > 0:
            search_substring(s3_object)


if __name__ == '__main__':
    start = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-b',
        dest="s3_bucket_name",
        required=True,
        help="S3 bucket name")
    parser.add_argument(
        '-s',
        dest="substring",
        required=True,
        help="substring to find")
    parser.add_argument(
        '-p',
        dest="profile",
        default='default',
        help="AWS profile to use")
    args = parser.parse_args()

    s3_bucket_name, substring, profile = \
        args.s3_bucket_name, args.substring, args.profile

    try:
        session = boto3.session.Session(profile_name=profile)
        list_files_in_bucket()
        end = time.time()
        print(f"Total: parsing time {end - start:.3f}")
    except ClientError as e:
        print(f"[ERROR]:{e}")
