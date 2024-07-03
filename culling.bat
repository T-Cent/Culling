@echo off

python3 -m venv .venv
pipenv sync
pipenv run python culling.py here

@echo on
