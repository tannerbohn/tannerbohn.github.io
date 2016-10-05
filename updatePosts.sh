#!/bin/bash

python scripts/generateLinksaverPost.py

echo "Generated Linksaver post"

python scripts/generateIdeasPost.py

echo "Generated Ideas post"

git add -A

echo "Added files"

git commit -m "updated linksaver and ideas posts"

echo "Pushing..."

git push