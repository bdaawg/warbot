#!/usr/bin/env python3
"""
    WorldVisualizer
    =============

"""

import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import cartopy.feature as cfeature

class WorldVisualizer:
    """WorldVisualizer Class

    Handles all things related to visualizing the battles fought between neighbors on a map.

    """

    def __init__(self, countries: dict):
        self._countries = countries
        self._map_projection = ccrs.Miller()

    def update_visualization(self):
        """creates a new and updated representation of the map."""
