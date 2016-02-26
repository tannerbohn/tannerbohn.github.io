#!/bin/bash

python scripts/generateLinksaverPost.py

echo "Generated post"

git add -A

echo "Added file"

git commit -m "updated linksaver post"

echo "Pushing..."

git push