#!/usr/bin/env python

"""Test slurp_items() using boto3 client paginators."""

from pprint import PrettyPrinter

import boto3
from botocore.paginate import PageIterator

from src.boto3_paginator import slurp_items

PP = PrettyPrinter(indent=4)
EC2_CLIENT = boto3.client('ec2')
S3_CLIENT = boto3.client('s3')


def test_ec2_describe_instances():
    """Happy path: required args."""
    iterator = slurp_items(EC2_CLIENT, 'describe_instances')
    assert isinstance(iterator, PageIterator)
    print(iterator)
    for item in iterator:
        PP.pprint(item)


def test_s3_list_buckets():
    """Happy path: required args."""
    iterator = slurp_items(S3_CLIENT, 'list_buckets')
    assert getattr(iterator, '__iter__', False)
    print(iterator)
    for item in iterator:
        PP.pprint(item)


def test_s3_list_object_versions(test_bucket):
    """Happy path: required args."""
    iterator = slurp_items(
        S3_CLIENT, 'list_object_versions',
        **{'Bucket': test_bucket})
    assert getattr(iterator, '__iter__', False)


def test_s3_list_object_versions_max(test_bucket):
    """Happy path: max arg."""
    iterator = slurp_items(
        S3_CLIENT, 'list_object_versions', max_items=2,
        **{'Bucket': test_bucket})
    assert getattr(iterator, '__iter__', False)


def test_bad_client():
    """Sad path: bad client."""
    iterator = slurp_items(
        None, 'list_object_versions',
        **{'Bucket': 'not-used'})
    assert getattr(iterator, '__iter__', False)
    PP.pprint(iterator)
    for item in iterator:
        PP.pprint(item)


def test_s3_bad_method():
    """Sad path: bad method."""
    iterator = slurp_items(
        S3_CLIENT, 'list_object_versions_bad',
        **{'Bucket': 'not-used'})
    assert getattr(iterator, '__iter__', False)
    PP.pprint(iterator)
    for item in iterator:
        PP.pprint(item)
