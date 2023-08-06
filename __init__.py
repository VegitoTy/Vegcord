__title__ = "Vegcord"
__author__ = "VegitoTy"
__version__ = "1.0.0"

from typing import Literal, NamedTuple

class VersionInfo(NamedTuple):
    major : int
    minor : int
    micro : int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]

version_info : VersionInfo = VersionInfo(major=0, minor=0, micro=0, releaselevel='alpha')