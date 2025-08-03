# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["StatusRetrieveResponse"]


class StatusRetrieveResponse(BaseModel):
    id: Optional[str] = None
    """The prediction ID"""

    error: Optional[str] = None
    """Error message if status is 'failed'"""

    output: Optional[List[str]] = None
    """
    Array of output images (only present when status is 'completed'). Contains URLs
    when return_base64=false, or base64-encoded strings when return_base64=true.
    """

    status: Optional[Literal["starting", "in_queue", "processing", "completed", "failed"]] = None
    """Current status of the prediction"""
