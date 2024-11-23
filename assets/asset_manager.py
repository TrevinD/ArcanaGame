# asset_manager.py
import pygame
import os

from collections import OrderedDict
import pygame
import json


class AssetManager:
    def __init__(self, max_cache_size: int = 100):
        self.cache = OrderedDict()
        self.max_cache_size = max_cache_size

    def _load_image(self, path: str) -> pygame.Surface:
        try:
            return pygame.image.load(path)
        except pygame.error as e:
            print(f"Error loading image: {e}")
            return None

    def _load_font(self, path: str) -> pygame.font.Font:
        try:
            return pygame.font.Font(path, 0)  # Load font without size (0)
        except pygame.error as e:
            print(f"Error loading font: {e}")
            return None

    def render_text(self, font: pygame.font.Font, text: str, size: int, color: tuple) -> pygame.Surface:
        font_size = font.size(size)  # Set font size for rendering
        return font.render(text, font_size, color)

    def _load_json(self, path: str) -> dict:
        try:
            with open(path, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            print(f"Error loading JSON: {e}")
            return None

    def load_asset(self, path: str, asset_type: str = 'image') -> any:
        """
        Load an asset from the given path, caching it for future use.

        :param path: Asset file path
        :param asset_type: Type of asset (image, font, json, etc.)
        :return: Loaded asset, or None on failure
        """
        if path in self.cache:
            # Move to end to mark as recently used
            self.cache.move_to_end(path)
            return self.cache[path]

        if asset_type == 'image':
            asset = self._load_image(path)
        elif asset_type == 'font':
            # TODO: Pass size as an argument or configure a default size
            asset = self._load_font(path, 24)
        elif asset_type == 'json':
            asset = self._load_json(path)
        else:
            print(f"Unsupported asset type: {asset_type}")
            return None

        if asset:
            if len(self.cache) >= self.max_cache_size:
                # Evict the least recently used asset (first in the ordered dict)
                self.cache.popitem(last=False)
            self.cache[path] = asset
        return asset




