"""
blocklist.py

This file just contains the blocklist of the JWT tokens. It will be imported by the app and
the logout resource so that tokens can be added to the blacklist when a user logs out.
"""

BLOCKLIST = set()