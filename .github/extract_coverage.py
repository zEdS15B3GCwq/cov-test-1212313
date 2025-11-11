import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from sphinx.search import en


def get_coverage_color(pct):
    if pct >= 90:
        return "brightgreen"
    if pct >= 80:
        return "green"
    if pct >= 70:
        return "yellow"
    if pct >= 60:
        return "orange"
    return "red"


# Check if coverage.xml exists
coverage_file = Path("coverage.xml")
if not coverage_file.exists():
    print("Error: coverage.xml not found", file=sys.stderr)
    sys.exit(1)

# Parse coverage.xml
tree = ET.parse("coverage.xml")
root = tree.getroot()
coverage = float(root.attrib["line-rate"]) * 100

# Create badges directory
Path("badges").mkdir(exist_ok=True)

# Generate badge JSON
badge_data = {
    "schemaVersion": 1,
    "label": "coverage",
    "message": f"{coverage:.1f}%",
    "color": get_coverage_color(coverage),
}

with open("badges/coverage.json", "w", encoding="utf-8") as f:
    json.dump(badge_data, f, indent=2)

print(f"Coverage: {coverage:.1f}%")
