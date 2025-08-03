# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["RunPredictParams", "Inputs", "InputsTryonV16Inputs", "InputsTryonV15Inputs"]


class RunPredictParams(TypedDict, total=False):
    inputs: Required[Inputs]
    """Contains all the input parameters for the selected model"""

    model_name: Required[Literal["tryon-v1.6", "tryon-v1.5"]]
    """Specifies the model version to use for the virtual try-on prediction.

    - `tryon-v1.6` - The latest and most advanced model, producing higher-quality
      outputs at 864×1296 resolution
    - `tryon-v1.5` - The previous stable release, generating outputs at 576×864
      resolution. Slightly faster than v1.6
    """


class InputsTryonV16Inputs(TypedDict, total=False):
    garment_image: Required[str]
    """
    Reference image of the clothing item to be tried on the model_image. Can be an
    image URL or base64 encoded image (must include prefix like
    data:image/jpg;base64,<YOUR_BASE64>).
    """

    model_image: Required[str]
    """
    Primary image of the person on whom the virtual try-on will be performed. Can be
    an image URL, base64 encoded image, or saved model reference (saved:<model_name>
    for Models Studio users).
    """

    category: Literal["auto", "tops", "bottoms", "one-pieces"]
    """Garment type classification.

    Use 'auto' to enable automatic classification. For flat-lay/ghost mannequin
    images, system detects type automatically. For on-model images, full-body shots
    default to full outfit swap.
    """

    garment_photo_type: Literal["auto", "flat-lay", "model"]
    """Specifies garment photo type to optimize internal parameters:

    - 'model': Photos of garments on a model
    - 'flat-lay': Flat-lay or ghost mannequin images
    - 'auto': Automatically detect photo type
    """

    mode: Literal["performance", "balanced", "quality"]
    """Operation mode:

    - 'performance': Faster but may compromise quality
    - 'balanced': Perfect middle ground between speed and quality
    - 'quality': Slower but delivers highest quality results
    """

    moderation_level: Literal["conservative", "permissive", "none"]
    """Sets content moderation level for garment images:

    - 'conservative': Stricter modesty standards, blocks
      underwear/swimwear/revealing outfits
    - 'permissive': Allows swimwear/underwear/revealing garments, blocks explicit
      nudity
    - 'none': Disables all content moderation (users remain responsible for ethical
      use)
    """

    num_samples: int
    """Number of images to generate in a single run.

    Multiple images increase chances of getting a good result due to the random
    element in image generation.
    """

    output_format: Literal["png", "jpeg"]
    """Desired output image format:

    - 'png': Highest quality, ideal for content creation
    - 'jpeg': Faster response with slight compression, suitable for real-time
      applications
    """

    return_base64: bool
    """
    When true, returns generated image as base64-encoded string instead of CDN URL.
    Enhances privacy as outputs are not stored on servers when enabled. Base64
    string includes format prefix (e.g., data:image/png;base64,...)
    """

    seed: int
    """Sets random operations to a fixed state.

    Use same seed to reproduce results with same inputs, or different seed to force
    different results.
    """

    segmentation_free: bool
    """
    Direct garment fitting without clothing segmentation, enabling bulkier garment
    try-ons with improved preservation of body shape and skin texture. Set to false
    if original garments are not removed properly.
    """


class InputsTryonV15Inputs(TypedDict, total=False):
    garment_image: Required[str]
    """
    Reference image of the clothing item to be tried on the model_image. Can be an
    image URL or base64 encoded image (must include prefix like
    data:image/jpg;base64,<YOUR_BASE64>).
    """

    model_image: Required[str]
    """
    Primary image of the person on whom the virtual try-on will be performed. Can be
    an image URL, base64 encoded image, or saved model reference (saved:<model_name>
    for Models Studio users).
    """

    category: Literal["auto", "tops", "bottoms", "one-pieces"]
    """Garment type classification.

    Use 'auto' to enable automatic classification. For flat-lay/ghost mannequin
    images, system detects type automatically. For on-model images, full-body shots
    default to full outfit swap.
    """

    garment_photo_type: Literal["auto", "flat-lay", "model"]
    """Specifies garment photo type to optimize internal parameters:

    - 'model': Photos of garments on a model
    - 'flat-lay': Flat-lay or ghost mannequin images
    - 'auto': Automatically detect photo type
    """

    mode: Literal["performance", "balanced", "quality"]
    """Operation mode:

    - 'performance': Faster but may compromise quality
    - 'balanced': Perfect middle ground between speed and quality
    - 'quality': Slower but delivers highest quality results
    """

    moderation_level: Literal["conservative", "permissive", "none"]
    """Sets content moderation level for garment images:

    - 'conservative': Stricter modesty standards, blocks
      underwear/swimwear/revealing outfits
    - 'permissive': Allows swimwear/underwear/revealing garments, blocks explicit
      nudity
    - 'none': Disables all content moderation (users remain responsible for ethical
      use)
    """

    num_samples: int
    """Number of images to generate in a single run.

    Multiple images increase chances of getting a good result due to the random
    element in image generation.
    """

    output_format: Literal["png", "jpeg"]
    """Desired output image format:

    - 'png': Highest quality, ideal for content creation
    - 'jpeg': Faster response with slight compression, suitable for real-time
      applications
    """

    return_base64: bool
    """
    When true, returns generated image as base64-encoded string instead of CDN URL.
    Enhances privacy as outputs are not stored on servers when enabled. Base64
    string includes format prefix (e.g., data:image/png;base64,...)
    """

    seed: int
    """Sets random operations to a fixed state.

    Use same seed to reproduce results with same inputs, or different seed to force
    different results.
    """

    segmentation_free: bool
    """
    Direct garment fitting without clothing segmentation, enabling bulkier garment
    try-ons with improved preservation of body shape and skin texture. Set to false
    if original garments are not removed properly.
    """


Inputs: TypeAlias = Union[InputsTryonV16Inputs, InputsTryonV15Inputs]
