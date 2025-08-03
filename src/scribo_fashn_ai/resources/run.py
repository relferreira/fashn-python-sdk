# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import run_predict_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.run_predict_response import RunPredictResponse

__all__ = ["RunResource", "AsyncRunResource"]


class RunResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RunResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relferreira/fashn-python-sdk#accessing-raw-response-data-eg-headers
        """
        return RunResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relferreira/fashn-python-sdk#with_streaming_response
        """
        return RunResourceWithStreamingResponse(self)

    def predict(
        self,
        *,
        inputs: run_predict_params.Inputs,
        model_name: Literal["tryon-v1.6", "tryon-v1.5"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunPredictResponse:
        """
        Initiate a new try-on prediction

        Args:
          inputs: Contains all the input parameters for the selected model

          model_name: Specifies the model version to use for the virtual try-on prediction.

              - `tryon-v1.6` - The latest and most advanced model, producing higher-quality
                outputs at 864×1296 resolution
              - `tryon-v1.5` - The previous stable release, generating outputs at 576×864
                resolution. Slightly faster than v1.6

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/run",
            body=maybe_transform(
                {
                    "inputs": inputs,
                    "model_name": model_name,
                },
                run_predict_params.RunPredictParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunPredictResponse,
        )


class AsyncRunResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRunResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/relferreira/fashn-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncRunResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/relferreira/fashn-python-sdk#with_streaming_response
        """
        return AsyncRunResourceWithStreamingResponse(self)

    async def predict(
        self,
        *,
        inputs: run_predict_params.Inputs,
        model_name: Literal["tryon-v1.6", "tryon-v1.5"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunPredictResponse:
        """
        Initiate a new try-on prediction

        Args:
          inputs: Contains all the input parameters for the selected model

          model_name: Specifies the model version to use for the virtual try-on prediction.

              - `tryon-v1.6` - The latest and most advanced model, producing higher-quality
                outputs at 864×1296 resolution
              - `tryon-v1.5` - The previous stable release, generating outputs at 576×864
                resolution. Slightly faster than v1.6

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/run",
            body=await async_maybe_transform(
                {
                    "inputs": inputs,
                    "model_name": model_name,
                },
                run_predict_params.RunPredictParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunPredictResponse,
        )


class RunResourceWithRawResponse:
    def __init__(self, run: RunResource) -> None:
        self._run = run

        self.predict = to_raw_response_wrapper(
            run.predict,
        )


class AsyncRunResourceWithRawResponse:
    def __init__(self, run: AsyncRunResource) -> None:
        self._run = run

        self.predict = async_to_raw_response_wrapper(
            run.predict,
        )


class RunResourceWithStreamingResponse:
    def __init__(self, run: RunResource) -> None:
        self._run = run

        self.predict = to_streamed_response_wrapper(
            run.predict,
        )


class AsyncRunResourceWithStreamingResponse:
    def __init__(self, run: AsyncRunResource) -> None:
        self._run = run

        self.predict = async_to_streamed_response_wrapper(
            run.predict,
        )
