# -*- coding: utf-8 -*-
"""Apply current chrome to every dist HTML page."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from refresh_site import main

if __name__ == "__main__":
    main()
