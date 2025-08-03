# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["RunPredictResponse"]


class RunPredictResponse(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the prediction"""

    error: Optional[str] = None
    """Error message if any"""
