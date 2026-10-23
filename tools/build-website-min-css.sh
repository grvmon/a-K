#!/bin/bash
# Rebuild website.min.css from the readable source (the old unminified website.min.css, keep it as website.src.css if you edit CSS by hand).
# npx lightningcss-cli is the only dependency. Run from repo root.
set -e
npx --yes lightningcss-cli@1 --minify website.src.css -o website.min.css
