#!/bin/bash

echo "Generating Linksaver post..."

python scripts/generateLinksaverPost.py

echo "Done."

echo "Generating Ideas markdown file..."

python /home/tanner/Dropbox/sandbox/IdeaManager/markdown_generator.py

echo "Done."

echo "Generating Ideas post..."

python scripts/generateIdeasPost.py

echo "Done."

git add -A

echo "Added files"

git commit -m "updated linksaver, ideas, and posts"

echo "Pushing..."

git push