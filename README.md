# Nomie Backup File Utilities

This repo contains various tools for the maintenance and modification of your
Nomie backup files.

## Current tools and functions:
* `clear.py` - This standalone script removes duplicate versions of the same
  entry keeping only the highest `_rev` value. Running `python3 clear.py` will
  guide you through the process of clearing the backup. It creates a backup of
  the backup, so you personal data won't be lost.
* `nomie2to3.py` - This converts a Nomie 2 Dropbox backup file to an ical file
  for importing events into Nomie 3. This file can be imported into Google
  Calendar and many other calendar systems. The web server can be run by
  executing `python3 server.py` and then loaded at the root URL.

## Requirements
* Python3

## Contributions and Requests

Have a tool that could help others? Want a new utility or feature? Simply open
an issue or start a pull request.
