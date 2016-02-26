#!/bin/bash

python scripts/generateLinkSaverPost.py

echo "Generated post"

git add -A

echo "Added file"

git commit -m "updated linksaver post"

echo "Pushing..."

git push