#!/usr/bin/env bash
# Chumbo + Maré (IntelliJ) — remove o plugin de tema. Mesmos argumentos do install.sh:
#   ./uninstall.sh                   IDE aberto
#   ./uninstall.sh ~/.local/opt/...  esse IDE
exec "$(cd "$(dirname "$0")" && pwd)/install.sh" --uninstall "$@"
