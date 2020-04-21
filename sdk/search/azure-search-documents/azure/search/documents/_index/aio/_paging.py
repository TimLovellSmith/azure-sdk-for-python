# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Union

from azure.core.async_paging import AsyncItemPaged, AsyncPageIterator, ReturnType
from .._generated.models import SearchRequest, SearchDocumentsResult
from .._paging import (
    convert_search_result,
    pack_continuation_token,
    unpack_continuation_token,
)


class AsyncSearchItemPaged(AsyncItemPaged[ReturnType]):
    def __init__(self, *args, **kwargs):
        super(AsyncSearchItemPaged, self).__init__(*args, **kwargs)
        self._first_page_iterator_instance = None

    async def __anext__(self) -> ReturnType:
        if self._page_iterator is None:
            self._page_iterator = self.by_page()
            self._first_page_iterator_instance = self._page_iterator
            return await self.__anext__()
        if self._page is None:
            # Let it raise StopAsyncIteration
            self._page = await self._page_iterator.__anext__()
            return await self.__anext__()
        try:
            return await self._page.__anext__()
        except StopAsyncIteration:
            self._page = None
            return await self.__anext__()

    def _first_iterator_instance(self):
        if self._first_page_iterator_instance is None:
            self._page_iterator = self.by_page()
            self._first_page_iterator_instance = self._page_iterator
        return self._first_page_iterator_instance

    async def get_facets(self) -> Union[dict, None]:
        """Return any facet results if faceting was requested.

        """

        page_iterator = self._first_iterator_instance()
        if page_iterator._current_page is None:
            response = await page_iterator._get_next(page_iterator.continuation_token)
            _response = SearchDocumentsResult.deserialize(response)
            facets = _response.facets
            if facets is not None:
                _facets = {k: [x.as_dict() for x in v] for k, v in facets.items()}
                return _facets
            return None
        return page_iterator.response.facets

    async def get_coverage(self):
        # type: () -> float
        """Return the covereage percentage, if `minimum_coverage` was
        specificied for the query.

        """
        page_iterator = self._first_iterator_instance()
        if page_iterator._current_page is None:
            response = await page_iterator._get_next(page_iterator.continuation_token)
            _response = SearchDocumentsResult.deserialize(response)
            return _response.coverage
        return page_iterator.response.coverage

    async def get_count(self):
        # type: () -> float
        """Return the count of results if `include_total_result_count` was
        set for the query.

        """
        page_iterator = self._first_iterator_instance()
        if page_iterator._current_page is None:
            response = await page_iterator._get_next(page_iterator.continuation_token)
            _response = SearchDocumentsResult.deserialize(response)
            return _response.count
        return page_iterator.response.count
