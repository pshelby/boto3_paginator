#!/usr/bin/env python

'''Paginate boto3 service call results.'''

class PaginationError():
    '''Error object returned upon pagination problems.'''
    def __init__(self, msg):
        self.error = msg

    def __iter__(self):
        return self

    def __next__(self):     # pylint: disable=no-self-use
        raise StopIteration # Method is needed to create iterator

    def __repr__(self):
        return self.error


def slurp_items(client, method, items_per_page=10, max_items=None, **method_args):
    '''Return pages from a service method's call.'''
    paginate_args = {}

    # Add number of items per page
    paginate_args['PaginationConfig'] = {'PageSize': items_per_page}

    # Add max_items if provided
    if max_items:
        paginate_args['PaginationConfig']['MaxItems'] = max_items

    # Synthesize arguments to paginate()
    if method_args:
        paginate_args.update(method_args)

    # Create a reusable Paginator
    try:
        paginator = client.get_paginator(method)
    except AttributeError:
        return PaginationError('Bad client object')
    except KeyError:
        return PaginationError('Bad method')

    # Create a PageIterator from the Paginator
    page_iterator = paginator.paginate(**paginate_args)

    return page_iterator
