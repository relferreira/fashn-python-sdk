# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from scribo_fashn_ai import ScriboFashnAI, AsyncScriboFashnAI
from scribo_fashn_ai.types import RunPredictResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRun:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_predict(self, client: ScriboFashnAI) -> None:
        run = client.run.predict(
            inputs={
                "garment_image": "http://example.com/path/to/garment.jpg",
                "model_image": "http://example.com/path/to/model.jpg",
            },
            model_name="tryon-v1.6",
        )
        assert_matches_type(RunPredictResponse, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_predict_with_all_params(self, client: ScriboFashnAI) -> None:
        run = client.run.predict(
            inputs={
                "garment_image": "http://example.com/path/to/garment.jpg",
                "model_image": "http://example.com/path/to/model.jpg",
                "category": "auto",
                "garment_photo_type": "auto",
                "mode": "performance",
                "moderation_level": "conservative",
                "num_samples": 1,
                "output_format": "png",
                "return_base64": True,
                "seed": 0,
                "segmentation_free": True,
            },
            model_name="tryon-v1.6",
        )
        assert_matches_type(RunPredictResponse, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_predict(self, client: ScriboFashnAI) -> None:
        response = client.run.with_raw_response.predict(
            inputs={
                "garment_image": "http://example.com/path/to/garment.jpg",
                "model_image": "http://example.com/path/to/model.jpg",
            },
            model_name="tryon-v1.6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunPredictResponse, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_predict(self, client: ScriboFashnAI) -> None:
        with client.run.with_streaming_response.predict(
            inputs={
                "garment_image": "http://example.com/path/to/garment.jpg",
                "model_image": "http://example.com/path/to/model.jpg",
            },
            model_name="tryon-v1.6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunPredictResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRun:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_predict(self, async_client: AsyncScriboFashnAI) -> None:
        run = await async_client.run.predict(
            inputs={
                "garment_image": "http://example.com/path/to/garment.jpg",
                "model_image": "http://example.com/path/to/model.jpg",
            },
            model_name="tryon-v1.6",
        )
        assert_matches_type(RunPredictResponse, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_predict_with_all_params(self, async_client: AsyncScriboFashnAI) -> None:
        run = await async_client.run.predict(
            inputs={
                "garment_image": "http://example.com/path/to/garment.jpg",
                "model_image": "http://example.com/path/to/model.jpg",
                "category": "auto",
                "garment_photo_type": "auto",
                "mode": "performance",
                "moderation_level": "conservative",
                "num_samples": 1,
                "output_format": "png",
                "return_base64": True,
                "seed": 0,
                "segmentation_free": True,
            },
            model_name="tryon-v1.6",
        )
        assert_matches_type(RunPredictResponse, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_predict(self, async_client: AsyncScriboFashnAI) -> None:
        response = await async_client.run.with_raw_response.predict(
            inputs={
                "garment_image": "http://example.com/path/to/garment.jpg",
                "model_image": "http://example.com/path/to/model.jpg",
            },
            model_name="tryon-v1.6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunPredictResponse, run, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_predict(self, async_client: AsyncScriboFashnAI) -> None:
        async with async_client.run.with_streaming_response.predict(
            inputs={
                "garment_image": "http://example.com/path/to/garment.jpg",
                "model_image": "http://example.com/path/to/model.jpg",
            },
            model_name="tryon-v1.6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunPredictResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True
