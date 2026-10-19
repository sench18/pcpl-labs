#!/bin/sh
# Запуск из папки Cargo-проекта независимо от текущего каталога.
set -eu
cd "$(dirname "$0")"
if command -v cargo >/dev/null 2>&1; then
    exec cargo "$@"
fi
if [ -x "$HOME/.cargo/bin/cargo" ]; then
    exec "$HOME/.cargo/bin/cargo" "$@"
fi
printf '%s\n' 'Cargo не найден. Установка: https://rust-lang.org/tools/install/' >&2
exit 127
