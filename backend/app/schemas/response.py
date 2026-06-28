from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class ApiResponse(
    BaseModel,
    Generic[T],
):
    """
    Standard API response.
    """

    success: bool = True

    message: str = "Success"

    data: T


def success_response(
    data: Any,
    message: str = "Success",
) -> ApiResponse[Any]:

    return ApiResponse(
        success=True,
        message=message,
        data=data,
    )
