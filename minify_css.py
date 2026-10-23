import subprocess
import sys

# Official minification via lightningcss as defined in tools/build-website-min-css.sh
try:
    subprocess.run(['bash', 'tools/build-website-min-css.sh'], check=True)
    print("Successfully built website.min.css from website.src.css using lightningcss.")
except Exception as e:
    print(f"Error running lightningcss: {e}", file=sys.stderr)
    sys.exit(1)
