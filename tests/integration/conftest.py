"""Fixtures for integration tests."""

from pytest import fixture


@fixture(scope="module")
def test_bucket():
    """Create an S3 bucket for integration tests."""
    import boto3

    bucket_name = 'boto3-paginator-integration-test'

    s3_client = boto3.client('s3')
    _ = s3_client.create_bucket(Bucket=bucket_name)
    s3_client.put_bucket_versioning(
        Bucket=bucket_name,
        VersioningConfiguration={'MFADelete': 'Disabled',
                                 'Status': 'Enabled'})
    print('S3 bucket "%s" created' % bucket_name)

    yield bucket_name

    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket(bucket_name)
    bucket.objects.all().delete()
    bucket.delete()
    print('S3 bucket "%s" deleted' % bucket_name)
