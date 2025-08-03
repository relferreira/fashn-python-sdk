# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import time
from typing import Callable
from typing_extensions import Literal

import httpx

from ..types import run_predict_params, run_subscribe_params
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
from ..types.status_retrieve_response import StatusRetrieveResponse

__all__ = ["RunResource", "AsyncRunResource"]

DEFAULT_POOL_INTERVAL = 0.5
DEFAULT_TIMEOUT = 120.0


class RunResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RunResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/scribo-fashn-ai-python#accessing-raw-response-data-eg-headers
        """
        return RunResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/scribo-fashn-ai-python#with_streaming_response
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

    def subscribe(
        self,
        *,
        inputs: run_subscribe_params.Inputs,
        model_name: Literal["tryon-v1.6", "tryon-v1.5"],
        pool_interval: float | None = None,
        timeout: float | None = None,
        on_enqueued: Callable[[str], None] | None = None,
        on_queue_update: Callable[[StatusRetrieveResponse], None] | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        request_timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatusRetrieveResponse:
        """
        Subscribe to a prediction status

        Args:
          inputs: Contains all the input parameters for the selected model

          model_name: Specifies the model version to use for the virtual try-on prediction.

              - `tryon-v1.6` - The latest and most advanced model, producing higher-quality
                outputs at 864×1296 resolution
              - `tryon-v1.5` - The previous stable release, generating outputs at 576×864
                resolution. Slightly faster than v1.6

          pool_interval: The interval in seconds to poll the status of the prediction.

          timeout: The timeout in seconds to cancel the prediction.

          on_enqueued: A callback function that is called when the prediction is enqueued.

          on_queue_update: A callback function that is called when the prediction status is updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          request_timeout: Override the client-level default timeout for this request, in seconds
        """
        # Start the prediction
        response = self.predict(
            inputs=inputs,
            model_name=model_name,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=request_timeout,
        )

        if not response.id:
            raise ValueError("Prediction ID is required")

        if on_enqueued:
            on_enqueued(response.id)

        return self._subscribe_to_status(
            response.id,
            pool_interval=pool_interval,
            timeout=timeout,
            on_queue_update=on_queue_update,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            request_timeout=request_timeout,
        )

    def _subscribe_to_status(
        self,
        id: str,
        *,
        pool_interval: float | None = None,
        timeout: float | None = None,
        on_queue_update: Callable[[StatusRetrieveResponse], None] | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        request_timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatusRetrieveResponse:
        poll_interval = pool_interval if pool_interval is not None else DEFAULT_POOL_INTERVAL
        timeout_duration = timeout if timeout is not None else DEFAULT_TIMEOUT

        start_time = time.time()

        while True:
            current_time = time.time()
            if timeout_duration and (current_time - start_time) > timeout_duration:
                raise TimeoutError("Timeout exceeded while waiting for prediction completion")

            try:
                status = self._client.status.retrieve(
                    id,
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=request_timeout,
                )

                if on_queue_update:
                    on_queue_update(status)

                if status.status == "completed":
                    return status
                elif status.status == "failed":
                    error_msg = status.error or "Unknown error"
                    raise RuntimeError(f"Prediction failed: {error_msg}")

                self._sleep(poll_interval)
            except Exception as e:
                if isinstance(e, (TimeoutError, RuntimeError)):
                    raise
                raise RuntimeError(f"Error while polling status: {e}") from e


class AsyncRunResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRunResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/scribo-fashn-ai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRunResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/scribo-fashn-ai-python#with_streaming_response
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

    async def subscribe(
        self,
        *,
        inputs: run_subscribe_params.Inputs,
        model_name: Literal["tryon-v1.6", "tryon-v1.5"],
        pool_interval: float | None = None,
        timeout: float | None = None,
        on_enqueued: Callable[[str], None] | None = None,
        on_queue_update: Callable[[StatusRetrieveResponse], None] | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        request_timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatusRetrieveResponse:
        """
        Subscribe to a prediction status

        Args:
          inputs: Contains all the input parameters for the selected model

          model_name: Specifies the model version to use for the virtual try-on prediction.

              - `tryon-v1.6` - The latest and most advanced model, producing higher-quality
                outputs at 864×1296 resolution
              - `tryon-v1.5` - The previous stable release, generating outputs at 576×864
                resolution. Slightly faster than v1.6

          pool_interval: The interval in seconds to poll the status of the prediction.

          timeout: The timeout in seconds to cancel the prediction.

          on_enqueued: A callback function that is called when the prediction is enqueued.

          on_queue_update: A callback function that is called when the prediction status is updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          request_timeout: Override the client-level default timeout for this request, in seconds
        """
        # Start the prediction
        response = await self.predict(
            inputs=inputs,
            model_name=model_name,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=request_timeout,
        )

        if not response.id:
            raise ValueError("Prediction ID is required")

        if on_enqueued:
            on_enqueued(response.id)

        return await self._subscribe_to_status(
            response.id,
            pool_interval=pool_interval,
            timeout=timeout,
            on_queue_update=on_queue_update,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            request_timeout=request_timeout,
        )

    async def _subscribe_to_status(
        self,
        id: str,
        *,
        pool_interval: float | None = None,
        timeout: float | None = None,
        on_queue_update: Callable[[StatusRetrieveResponse], None] | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        request_timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatusRetrieveResponse:
        poll_interval = pool_interval if pool_interval is not None else DEFAULT_POOL_INTERVAL
        timeout_duration = timeout if timeout is not None else DEFAULT_TIMEOUT

        start_time = time.time()

        while True:
            current_time = time.time()
            if timeout_duration and (current_time - start_time) > timeout_duration:
                raise TimeoutError("Timeout exceeded while waiting for prediction completion")

            try:
                status = await self._client.status.retrieve(
                    id,
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=request_timeout,
                )

                if on_queue_update:
                    on_queue_update(status)

                if status.status == "completed":
                    return status
                elif status.status == "failed":
                    error_msg = status.error or "Unknown error"
                    raise RuntimeError(f"Prediction failed: {error_msg}")

                await self._sleep(poll_interval)
            except Exception as e:
                if isinstance(e, (TimeoutError, RuntimeError)):
                    raise
                raise RuntimeError(f"Error while polling status: {e}") from e


class RunResourceWithRawResponse:
    def __init__(self, run: RunResource) -> None:
        self._run = run

        self.predict = to_raw_response_wrapper(
            run.predict,
        )
        self.subscribe = to_raw_response_wrapper(
            run.subscribe,
        )


class AsyncRunResourceWithRawResponse:
    def __init__(self, run: AsyncRunResource) -> None:
        self._run = run

        self.predict = async_to_raw_response_wrapper(
            run.predict,
        )
        self.subscribe = async_to_raw_response_wrapper(
            run.subscribe,
        )


class RunResourceWithStreamingResponse:
    def __init__(self, run: RunResource) -> None:
        self._run = run

        self.predict = to_streamed_response_wrapper(
            run.predict,
        )
        self.subscribe = to_streamed_response_wrapper(
            run.subscribe,
        )


class AsyncRunResourceWithStreamingResponse:
    def __init__(self, run: AsyncRunResource) -> None:
        self._run = run

        self.predict = async_to_streamed_response_wrapper(
            run.predict,
        )
        self.subscribe = async_to_streamed_response_wrapper(
            run.subscribe,
        )
