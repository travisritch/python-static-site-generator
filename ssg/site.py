from pathlib import Path

class Site:
    def __init__(self, source, dest):
        self._path = Path(source)
        self._dest = Path(dest)