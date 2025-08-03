# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from scribo_fashn_ai import ScriboFashnAI, AsyncScriboFashnAI
from scribo_fashn_ai.types import CreditRetrieveBalanceResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCredits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_balance(self, client: ScriboFashnAI) -> None:
        credit = client.credits.retrieve_balance()
        assert_matches_type(CreditRetrieveBalanceResponse, credit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_balance(self, client: ScriboFashnAI) -> None:
        response = client.credits.with_raw_response.retrieve_balance()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = response.parse()
        assert_matches_type(CreditRetrieveBalanceResponse, credit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_balance(self, client: ScriboFashnAI) -> None:
        with client.credits.with_streaming_response.retrieve_balance() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = response.parse()
            assert_matches_type(CreditRetrieveBalanceResponse, credit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCredits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_balance(self, async_client: AsyncScriboFashnAI) -> None:
        credit = await async_client.credits.retrieve_balance()
        assert_matches_type(CreditRetrieveBalanceResponse, credit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_balance(self, async_client: AsyncScriboFashnAI) -> None:
        response = await async_client.credits.with_raw_response.retrieve_balance()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = await response.parse()
        assert_matches_type(CreditRetrieveBalanceResponse, credit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_balance(self, async_client: AsyncScriboFashnAI) -> None:
        async with async_client.credits.with_streaming_response.retrieve_balance() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = await response.parse()
            assert_matches_type(CreditRetrieveBalanceResponse, credit, path=["response"])

        assert cast(Any, response.is_closed) is True
