import io
import base64
from PIL import Image


def compress_image(image_bytes: bytes, max_size: int = 800, quality: int = 85) -> bytes:
    """Compress image for thumbnail generation."""
    img = Image.open(io.BytesIO(image_bytes))

    # Convert RGBA to RGB if necessary
    if img.mode == "RGBA":
        bg = Image.new("RGB", img.size, (255, 255, 255))
        bg.paste(img, mask=img.split()[3])
        img = bg

    # Resize maintaining aspect ratio
    img.thumbnail((max_size, max_size), Image.LANCZOS)

    buffer = io.BytesIO()
    img.save(buffer, format="JPEG", quality=quality, optimize=True)
    return buffer.getvalue()


def image_to_base64(image_bytes: bytes) -> str:
    """Convert image bytes to base64 string for AI APIs."""
    return base64.b64encode(image_bytes).decode("utf-8")
