# __init__.py
from .flux_kontext_inpaint_conditioning import FluxKontextInpaintingConditioning

NODE_CLASS_MAPPINGS = {
    "FluxKontextInpaintingConditioning": FluxKontextInpaintingConditioning,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "FluxKontextInpaintingConditioning": "No Fun Flux Kontext Inpaint Conditioning",
}

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
]
