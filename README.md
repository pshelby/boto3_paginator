# boto3 Pagination

This package provides the `slurp_items()` function as an interface to boto3's paginators.
It pages through service call results (via paginator objects) and returns an iterator over those pages, without having to deal with messy markers, tokens, or page identifiers.

## Usage

`slurp_items(client, method, next_page_key='NextToken', items_per_page=10, max_items=None, **method_args)`

**client** : A boto3 client to the target service (ec2, s3, etc.).

**method** : The paginator method to call against the target service.  A list of all paginators and their methods can be found in the [boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html).

**next\_page\_key** : Key name to use to iterate over pages. (Defaults to 'NextToken'.)

**items\_per\_page** : Number of results per page to return. (Defaults to 10 items.)

**max_items** : Total number of items to return.  (Defaults to all items.)

*\***method_args** : Keyword arguments that provide specific settings for the paginator method, or override other PaginationConfig settings.

## Development

### Testing

Unit tests are located in `tests/unit`, integration tests are in `tests/integration`, and the supplied static responses in `tests/fixtures`.  Integration tests require an enabled AWS profile.

```bash
PYTHONPATH=. pytest
```
