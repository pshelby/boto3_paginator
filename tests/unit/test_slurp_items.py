#!/usr/bin/env python

'''Test slurp_items() using boto3 client paginators.'''

from unittest import mock

import boto3
from botocore.paginate import PageIterator

from src.boto3_paginator import PaginationError, slurp_items
from tests.fixtures.boto3_responses import EC2_DESCRIBE_INSTANCES_RESPONSE, S3_LIST_OBJECTS_RESPONSE

EC2_CLIENT = boto3.client('ec2')
S3_CLIENT = boto3.client('s3')

@mock.patch('botocore.paginate.PageIterator._make_request')
def test_simple_call(mock_api):
    '''Happy path: required args.'''
    mock_api.return_value = EC2_DESCRIBE_INSTANCES_RESPONSE
    iterator = slurp_items(EC2_CLIENT, 'describe_instances')
    assert isinstance(iterator, PageIterator)
    for item in iterator:
        assert item['Reservations'][0]['Instances'][0]['InstanceId'] == 'i-00000000000000000'
        break

@mock.patch('botocore.paginate.PageIterator._make_request')
def test_different_client(mock_api):
    '''Happy path: s3 client + required args.'''
    mock_api.return_value = S3_LIST_OBJECTS_RESPONSE
    iterator = slurp_items(S3_CLIENT, 'list_objects', **{'Bucket': 'paginator-test-bucket'})
    assert isinstance(iterator, PageIterator)
    for item in iterator:
        assert item['Contents'][0]['Key'] == 'AWSLogs/000000000000/'
        break

@mock.patch('botocore.paginate.PageIterator._make_request')
def test_method_args(mock_api):
    '''Happy path: required args + method_args.'''
    mock_api.return_value = EC2_DESCRIBE_INSTANCES_RESPONSE
    method_args = {'Filters': [{'Name': 'instance-state-name', 'Values': ['running']}]}
    iterator = slurp_items(EC2_CLIENT, 'describe_instances', **method_args)
    assert isinstance(iterator, PageIterator)
    for item in iterator:
        assert item['Reservations'][0]['Instances'][0]['InstanceId'] == 'i-00000000000000000'
        break

@mock.patch('botocore.paginate.PageIterator._make_request')
def test_max_items(mock_api):
    '''Happy path: required args + max_items.'''
    mock_api.return_value = EC2_DESCRIBE_INSTANCES_RESPONSE
    iterator = slurp_items(EC2_CLIENT, 'describe_instances', max_items=1)
    assert isinstance(iterator, PageIterator)
    assert len([page for page in iterator]) == 1
    for item in iterator:
        assert item['Reservations'][0]['Instances'][0]['InstanceId'] == 'i-00000000000000000'
        break

@mock.patch('botocore.paginate.PageIterator._make_request')
def test_items_per_page(mock_api):
    '''Happy path: required args + items_per_page.'''
    mock_api.return_value = EC2_DESCRIBE_INSTANCES_RESPONSE
    iterator = slurp_items(EC2_CLIENT, 'describe_instances', items_per_page=20)
    assert isinstance(iterator, PageIterator)
    for item in iterator:
        assert item['Reservations'][0]['Instances'][0]['InstanceId'] == 'i-00000000000000000'
        break

@mock.patch('botocore.paginate.PageIterator._make_request')
def test_bad_client(mock_api):
    '''Sad path: bad client obj.'''
    mock_api.return_value = EC2_DESCRIBE_INSTANCES_RESPONSE
    iterator = slurp_items(None, 'describe_instances')
    assert isinstance(iterator, PaginationError)
    print(iterator)
    for item in iterator:
        print(item)
        assert item == 'Bad client object'

@mock.patch('botocore.paginate.PageIterator._make_request')
def test_bad_method(mock_api):
    '''Sad path: bad method for client.'''
    mock_api.return_value = EC2_DESCRIBE_INSTANCES_RESPONSE
    iterator = slurp_items(EC2_CLIENT, 'list_objects')
    assert isinstance(iterator, PaginationError)
    for item in iterator:
        assert item == 'Bad method'
