#!/bin/bash

python generateLinkSaverPost.py

git add -A
git commit -m "updated linksaver post"
git push