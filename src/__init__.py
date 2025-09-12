"""Init file for the src package."""

from .scraper import EuroScraper
from .data_manager import DataManager
from .config import *
from .utils import *

__all__ = ['EuroScraper', 'DataManager']
