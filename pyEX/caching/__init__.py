# -*- coding: utf-8 -*-
from ._version import __version__  # noqa: F401
import pystore


class Storage(object):
    def __init__(self, path):
        self.path = path
        self.store = pystore.store(self.path)
        self.collections = {}

    def init(self, collections):
        for c in collections:
            c = c.upper()
            self.collections[c] = self.store.collection(c)

# import pystore
# pystore.set_path("~/pystore")
# pystore.list_stores()
# store = pystore.store('mydatastore')
# store.list_collections()
# collection = store.collection('NASDAQ')
# collection.list_items()
# # Store the first 100 rows of the data in the collection under "AAPL"
# collection.write('AAPL', aapl[:100], metadata={'source': 'Quandl'})

# # Reading the item's data
# item = collection.item('AAPL')
# data = item.data  # <-- Dask dataframe (see dask.pydata.org)
# metadata = item.metadata
# df = item.to_pandas()

# # Append the rest of the rows to the "AAPL" item
# collection.append('AAPL', aapl[100:])

# # Reading the item's data
# item = collection.item('AAPL')
# data = item.data
# metadata = item.metadata
# df = item.to_pandas()


# # --- Query functionality ---

# # Query avaialable symbols based on metadata
# collection.list_items(some_key='some_value', other_key='other_value')


# # --- Snapshot functionality ---

# # Snapshot a collection
# # (Point-in-time named reference for all current symbols in a collection)
# collection.create_snapshot('snapshot_name')

# # List available snapshots
# collection.list_snapshots()

# # Get a version of a symbol given a snapshot name
# collection.item('AAPL', snapshot='snapshot_name')

# # Delete a collection snapshot
# collection.delete_snapshot('snapshot_name')


# # Delete the item from the current version
# collection.delete_item('AAPL')

# # Delete the collection
# store.delete_collection('NASDAQ')
