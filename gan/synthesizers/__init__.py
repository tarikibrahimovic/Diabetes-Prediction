"""Synthesizers module."""

from gan.synthesizers.ctgan import CTGAN
from gan.synthesizers.tvae import TVAE

__all__ = (
    'CTGAN',
    'TVAE'
)


def get_all_synthesizers():
    return {
        name: globals()[name]
        for name in __all__
    }
