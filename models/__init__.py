#!/usr/bin/python3
"""Initializes the package"""
from models.engines.file_storage import FileStorage
storage = FileStorage()
storage.reload()
