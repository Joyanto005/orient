#!/bin/bash
echo "Starting token refresh script..."
python3 generate.py
python3 -m http.server 10000