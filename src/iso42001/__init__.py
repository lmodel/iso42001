"""iso42001.

ISO/IEC 42001:2023 AI management system records (LinkML)
"""

try:
    from iso42001._version import __version__, __version_tuple__
except ImportError:  # pragma: no cover
    __version__ = "0.0.0"
    __version_tuple__ = (0, 0, 0)
