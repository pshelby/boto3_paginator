#!/usr/bin/env python

"""Paginate boto3 service call results."""

from botocore.exceptions import OperationNotPageableError


class PaginationError():
    """Error object returned upon pagination problems."""

    def __init__(self, msg):
        """Init object."""
        self.error = msg

    def __iter__(self):
        """Iterate method."""
        return self

    def __next__(self):     # pylint: disable=no-self-use
        """Incrementor for iterator.

        Needed to create an interator.
        """
        raise StopIteration

    def __repr__(self):
        """Represent class in readable format."""
        return self.error


def slurp_items(client, method, next_page_key='NextToken', items_per_page=10,
                max_items=None, **method_args):
    """Return pages from a service method's call."""
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

        # Create a PageIterator from the Paginator
        page_iterator = paginator.paginate(**paginate_args)

        return page_iterator
    except OperationNotPageableError:
        # If method doesn't have a paginator, try regular method
        results = []
        returned_page = {next_page_key: 'START'}

        while next_page_key in returned_page and returned_page[next_page_key]:
            returned_page = getattr(client, method)(**method_args)
            results.append(returned_page)

        return results
    except AttributeError:
        return PaginationError('Bad client object')
    except KeyError:
        return PaginationError('Bad method : %s' % method)
