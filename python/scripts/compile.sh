#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 -m py_compile escape_vault.py main.py run_tests.py test_data.py
echo "Syntax OK"
