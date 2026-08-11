#!/usr/bin/env python3
"""Smoke tests for Agent Guild website."""
import httpx, sys

BASE = "https://marianstancik.dev"
PAGES = {
    "/": "Domov",
    "/kurz": "Kurz", 
    "/o-nas": "O nás",
    "/faq": "FAQ",
    "/blog": "Blog",
    "/affiliate": "Affiliate",
    "/en": "English Home",
    "/en/kurz": "English Course",
    "/en/o-nas": "English About",
    "/en/faq": "English FAQ",
    "/en/blog": "English Blog",
    "/en/affiliate": "English Affiliate",
}

ASSETS = ["/styles.css", "/app.js", "/favicon.svg", "/sitemap.xml", "/robots.txt", "/llms.txt"]

failed = 0
passed = 0

# Test pages
for url, name in PAGES.items():
    try:
        resp = httpx.get(f"{BASE}{url}", follow_redirects=True, timeout=15)
        if resp.status_code == 200:
            # Check content
            title = "Prime Agent Masterclass" in resp.text or "Agent Guild" in resp.text
            nav = '<nav' in resp.text
            footer = '<footer' in resp.text
            if title and nav and footer:
                print(f"  ✅ {url} ({name})")
                passed += 1
            else:
                print(f"  ❌ {url} ({name}) - missing content")
                failed += 1
        else:
            print(f"  ❌ {url} ({name}) - {resp.status_code}")
            failed += 1
    except Exception as e:
        print(f"  ❌ {url} - {e}")
        failed += 1

# Test assets
for url in ASSETS:
    try:
        resp = httpx.get(f"{BASE}{url}", follow_redirects=True, timeout=15)
        if resp.status_code == 200:
            print(f"  ✅ {url} ({len(resp.text)} bytes)")
            passed += 1
        else:
            print(f"  ❌ {url} - {resp.status_code}")
            failed += 1
    except Exception as e:
        print(f"  ❌ {url} - {e}")
        failed += 1

# Summary
print(f"
{'='*40}")
print(f"Results: {passed} passed, {failed} failed")
if failed > 0:
    print("❌ SOME TESTS FAILED")
    sys.exit(1)
else:
    print("✅ ALL TESTS PASSED")
