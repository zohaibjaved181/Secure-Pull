#!/usr/bin/env python3
"""Generate full Secure Pull Architecture HTML presentation with 7+ pages."""
import os

def main():
    html = get_html()
    with open('/projects/sandbox/Secure-Pull/index.html', 'w') as f:
        f.write(html)
    print("HTML presentation generated successfully!")

def get_html():
    return HEAD + SECTION1 + SECTION2 + SECTION3 + SECTION4 + SECTION5 + SECTION6 + SECTION7 + FOOTER

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Secure Pull Architecture - Enterprise Patching Solution</title>
'''

if __name__ == '__main__':
    main()
