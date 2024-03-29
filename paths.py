from pathlib import Path
from typing import Optional

from appdirs import user_cache_dir, user_config_dir

from elmada.mode import is_safe_mode
from elmada.mappings import COUNTRIES_FOR_ANALYSIS


def _get_cache_directory() -> Path:
    """Returns the path to cache directory and creates it, if not yet existing."""
    fp = Path(user_cache_dir(appname="elmada", appauthor="DrafProject"))
    fp.mkdir(parents=True, exist_ok=True)
    return fp


def _get_config_directory() -> Path:
    """Returns the path to config directory and creates it, if not yet existing."""
    fp = Path(user_config_dir(appname="elmada", appauthor="DrafProject")) / "api_keys"
    fp.mkdir(parents=True, exist_ok=True)
    return fp


BASE_DIR = Path(__file__).resolve().parent
CACHE_DIR = _get_cache_directory()
KEYS_DIR = _get_config_directory()
DATA_DIR = BASE_DIR / "data/raw"
SAFE_CACHE_DIR = BASE_DIR / "data/safe_cache"


def mode_dependent_cache_dir(year: Optional[int] = None, country: Optional[str] = None):
    is_safe_year = year in range(2017, 2101) or year is None
    is_safe_country = country in COUNTRIES_FOR_ANALYSIS or country is None
    return SAFE_CACHE_DIR if (is_safe_mode() and is_safe_year and is_safe_country) else CACHE_DIR
