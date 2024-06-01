# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sandbox import Sandbox, AsyncSandbox

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV2:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Sandbox) -> None:
        v2 = client.v2.retrieve()
        assert v2 is None

    @parametrize
    def test_raw_response_retrieve(self, client: Sandbox) -> None:
        response = client.v2.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert v2 is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Sandbox) -> None:
        with client.v2.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True


class TestAsyncV2:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSandbox) -> None:
        v2 = await async_client.v2.retrieve()
        assert v2 is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSandbox) -> None:
        response = await async_client.v2.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = await response.parse()
        assert v2 is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSandbox) -> None:
        async with async_client.v2.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True
