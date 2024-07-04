@echo off

pipenv sync
pipenv run python culling.py j1407b.jpg

@echo on
