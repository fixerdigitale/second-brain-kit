#!/usr/bin/env bash
# Lancia prova_ripristino.py con Python 3 (Mac, Linux, Git Bash su Windows).
# Sola lettura se lo dice lo script Python. Uso: bash prova-ripristino.sh [argomenti]
dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
for py in python3 python py; do
  # su Mac senza strumenti per sviluppatori /usr/bin/python3 apre una finestra di installazione: lo saltiamo
  if [ "$(uname -s 2>/dev/null)" = Darwin ] && [ "$(command -v "$py" 2>/dev/null)" = /usr/bin/python3 ] \
     && ! xcode-select -p >/dev/null 2>&1; then continue; fi
  if command -v "$py" >/dev/null 2>&1 && "$py" -c 'import sys; sys.exit(0 if sys.version_info[0]==3 else 1)' >/dev/null 2>&1; then
    exec "$py" "$dir/prova_ripristino.py" "$@"
  fi
done
echo "Python 3 non trovato / Python 3 not found." >&2
exit 3
