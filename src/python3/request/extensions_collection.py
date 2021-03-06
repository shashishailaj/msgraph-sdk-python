# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import extension_request_builder 
from ..model.extension import Extension
import json
import asyncio

class ExtensionsCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the ExtensionsCollectionRequest
        
        Args:
            request_url (str): The url to perform the ExtensionsCollectionRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(ExtensionsCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the ExtensionsCollectionPage

        Returns: 
            :class:`ExtensionsCollectionPage<msgraph.request.extensions_collection.ExtensionsCollectionPage>`:
                The ExtensionsCollectionPage
        """
        self.method = "GET"
        collection_response = ExtensionsCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)

    @asyncio.coroutine
    def get_async(self):
        """Gets the ExtensionsCollectionPage in async

        Yields: 
            :class:`ExtensionsCollectionPage<msgraph.request.extensions_collection.ExtensionsCollectionPage>`:
                The ExtensionsCollectionPage
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        collection_page = yield from future
        return collection_page

class ExtensionsCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the ExtensionRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a ExtensionRequestBuilder for
        
        Returns: 
            :class:`ExtensionRequestBuilder<msgraph.request.extension_request_builder.ExtensionRequestBuilder>`:
                A ExtensionRequestBuilder for that key
        """
        return extension_request_builder.ExtensionRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self,select=None, filter=None, top=None, skip=None, order_by=None, options=None):
        """Builds the ExtensionsCollectionRequest
        
        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            top (int): Default None, the number of items to return in a result.
            order_by (str): Default None, comma-separated list of properties
                that are used to sort the order of items in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`ExtensionsCollectionRequest<msgraph.request.extensions_collection.ExtensionsCollectionRequest>`:
                The ExtensionsCollectionRequest
        """
        req = ExtensionsCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(select=select, filter=filter, top=top, skip=skip, order_by=order_by, )
        return req

    def get(self):
        """Gets the ExtensionsCollectionPage

        Returns: 
            :class:`ExtensionsCollectionPage<msgraph.request.extensions_collection.ExtensionsCollectionPage>`:
                The ExtensionsCollectionPage
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the ExtensionsCollectionPage in async

        Yields: 
            :class:`ExtensionsCollectionPage<msgraph.request.extensions_collection.ExtensionsCollectionPage>`:
                The ExtensionsCollectionPage
        """
        collection_page = yield from self.request().get_async()
        return collection_page


class ExtensionsCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`ExtensionsCollectionPage<msgraph.request.extensions_collection.ExtensionsCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = ExtensionsCollectionPage(self._prop_dict["value"])

        return self._collection_page


class ExtensionsCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the Extension at the index specified
        
        Args:
            index (int): The index of the item to get from the ExtensionsCollectionPage

        Returns:
            :class:`Extension<msgraph.model.extension.Extension>`:
                The Extension at the index
        """
        return Extension(self._prop_list[index])

    def extensions(self):
        """Get a generator of Extension within the ExtensionsCollectionPage
        
        Yields:
            :class:`Extension<msgraph.model.extension.Extension>`:
                The next Extension in the collection
        """
        for item in self._prop_list:
            yield Extension(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the ExtensionsCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = ExtensionsCollectionRequest(next_page_link, client, options)
