# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Callable, Optional
from typing_extensions import Literal, Required, TypedDict

from .status_retrieve_response import StatusRetrieveResponse
from .run_predict_params import Inputs

__all__ = ["RunSubscribeParams"]


class RunSubscribeParams(TypedDict, total=False):
    inputs: Required[Inputs]
    """Contains all the input parameters for the selected model"""

    model_name: Required[Literal["tryon-v1.6", "tryon-v1.5"]]
    """Specifies the model version to use for the virtual try-on prediction.

    - `tryon-v1.6` - The latest and most advanced model, producing higher-quality
      outputs at 864×1296 resolution
    - `tryon-v1.5` - The previous stable release, generating outputs at 576×864
      resolution. Slightly faster than v1.6
    """

    pool_interval: Optional[float]
    """The interval in seconds to poll the status of the prediction."""

    timeout: Optional[float]
    """The timeout in seconds to cancel the prediction."""

    on_enqueued: Optional[Callable[[str], None]]
    """A callback function that is called when the prediction is enqueued."""

    on_queue_update: Optional[Callable[[StatusRetrieveResponse], None]]
    """A callback function that is called when the prediction status is updated.""" 