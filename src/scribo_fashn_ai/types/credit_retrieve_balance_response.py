# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CreditRetrieveBalanceResponse", "Credits"]


class Credits(BaseModel):
    on_demand: int
    """On-demand credits purchased separately"""

    subscription: int
    """Credits from active subscription"""

    total: int
    """Total available credits"""


class CreditRetrieveBalanceResponse(BaseModel):
    credits: Optional[Credits] = None
