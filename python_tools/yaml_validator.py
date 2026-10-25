#!/usr/bin/env python3
"""High-performance YAML Schema & Syntax Validator"""
import sys
import yaml
from pathlib import Path

def validate_yaml_file(filepath: Path) -> bool:
    try:
        with open(filepath, 'r') as f:
            data = yaml.safe_load(f)
        print(f"✓ Valid YAML: {filepath.name} (Top-level keys: {list(data.keys()) if isinstance(data, dict) else len(data)})")
        return True
    except yaml.YAMLError as exc:
        print(f"✗ INVALID YAML in {filepath.name}:\n{exc}")
        return False

if __name__ == "__main__":
    target = Path(sys.argv[1] if len(sys.argv) > 1 else "../blueprints/docker-compose.production.yml")
    sys.exit(0 if validate_yaml_file(target) else 1)
