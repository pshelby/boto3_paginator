"""Static data for S3 stubbing."""

from datetime import datetime

S3_LIST_OBJECTS_RESPONSE = {
    'Contents': [
        {
            'ETag': '"1"',
            'Key': 'AWSLogs/000000000000/',
            'LastModified': datetime.utcnow(),
            'Owner': {
                'DisplayName': 'owner-1',
                'ID': '1'
            },
            'Size': 0,
            'StorageClass': 'STANDARD'
        },
        {
            'ETag': '"a4a901f98ae5ca161fa523ffd3233f0c"',
            'Key': 'AWSLogs/000000000000/CloudTrail/us-east-1/\
                    2018/06/26/0.json.gz',
            'LastModified': datetime.utcnow(),
            'Owner': {
                'DisplayName': 'owner-1',
                'ID': '1'
            },
            'Size': 807,
            'StorageClass': 'STANDARD'
        },
        {
            'ETag': '"2248ae82bd76540443bd2d5218265819"',
            'Key': 'AWSLogs/000000000000/CloudTrail/us-east-1/\
                    2018/06/26/1.json.gz',
            'LastModified': datetime.utcnow(),
            'Owner': {
                'DisplayName': 'owner-1',
                'ID': '1'
            },
            'Size': 671,
            'StorageClass': 'STANDARD'
        },
        {
            'ETag': '"b3e5482d0bc0a612399f60920b538a69"',
            'Key': 'AWSLogs/000000000000/CloudTrail/us-east-1/\
                    2018/06/26/2.json.gz',
            'LastModified': datetime.utcnow(),
            'Owner': {
                'DisplayName': 'owner-1',
                'ID': '1'
            },
            'Size': 679,
            'StorageClass': 'STANDARD'
        },
        {
            'ETag': '"144c2f558839e4bb8c60ac693462006c"',
            'Key': 'AWSLogs/000000000000/CloudTrail/us-east-1/\
                    2018/06/26/3.json.gz',
            'LastModified': datetime.utcnow(),
            'Owner': {
                'DisplayName': 'owner-1',
                'ID': '1'
            },
            'Size': 810,
            'StorageClass': 'STANDARD'
        }
    ],
    'EncodingType': 'url',
    'IsTruncated': True,
    'Marker': '',
    'MaxKeys': 1000,
    'Name': '000000000000-awsmacietrail-dataevent',
    'Prefix': '',
    'ResponseMetadata': {
        'HTTPHeaders': {
            'content-type': 'application/xml',
            'date': 'Thu, 30 May 2019 18:13:16 GMT',
            'server': 'AmazonS3',
            'transfer-encoding': 'chunked',
            'x-amz-bucket-region': 'us-east-1',
            'x-amz-id-2': '...',
            'x-amz-request-id': '================'
        },
        'HTTPStatusCode': 200,
        'HostId': '==========================================\
                ==================================',
        'RequestId': '================',
        'RetryAttempts': 0
    }
}

S3_LIST_BUCKETS_RESPONSE = {
    'Buckets': [
        {
            'Name': 'bucket1',
            'CreationDate': datetime.utcnow()
        },
    ],
    'Owner': {
        'DisplayName': 'owner1',
        'ID': 'owner1'
    }
}
