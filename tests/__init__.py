#!/usr/bin/python3
"""Utility functions for testing the AirBnb clone modules.
"""
import os
from typing import TextIO
from models.engine.file_storage import FileStorage

def delete_file(file_path: str):
    """Removes a file if it exists.

    Args:
        file_path (str): The path to the file to remove.
    """
    try:
        os.remove(file_path)
    except FileNotFoundError:
        pass

def clear_stream(stream: TextIO):
    """Clears the contents of a given stream.

    Args:
        stream (TextIO): The stream to clear.
    """
    if stream.seekable():
        stream.seek(0)
        stream.truncate()

def reset_store(store: FileStorage, file_path='file.json'):
    """Resets the items in the given FileStorage.

    Args:
        store (FileStorage): The FileStorage to reset.
        file_path (str): The path to the store's file (default is 'file.json').
    """
    with open(file_path, 'w') as file:
        file.write('{}')
    store.reload()

def read_text_file(file_name: str) -> str:
    """Reads the contents of a given file.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        str: The contents of the file, or an empty string if the file does not exist.
    """
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return ''

def write_text_file(file_name: str, text: str):
    """Writes text to a given file.

    Args:
        file_name (str): The name of the file to write to.
        text (str): The content to write into the file.
    """
    with open(file_name, 'w') as file:
        file.write(text)

