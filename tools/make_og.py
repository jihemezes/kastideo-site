#!/usr/bin/env python3
"""Génère les images de partage 1200x630 (public/og-fr.jpg, public/og-en.jpg).

Usage : python3 tools/make_og.py   (nécessite Playwright et Chromium)
"""
import functools
import http.server
import os
import threading

from playwright.sync_api import sync_playwright

PUB = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "public")

TEXT = {
    "fr": ("Lecteur IPTV pour Mac, Windows, Linux, Android, iPhone et iPad",
           "Un seul lecteur pour <em>tout</em> ce que vous regardez",
           "Guide TV · Replay · Enregistrement · Films et séries", "Gratuit · kastideo.com"),
    "en": ("IPTV player for Mac, Windows, Linux, Android, iPhone and iPad",
           "One player for <em>everything</em> you watch",
           "TV guide · Replay · Recording · Movies and series", "Free · kastideo.com"),
}

PAGE = """<!doctype html><html><head><meta charset="utf-8"><base href="http://127.0.0.1:{port}/">
<link rel="stylesheet" href="site.css">
<style>
html,body{{margin:0;width:1200px;height:630px;overflow:hidden}}
body{{position:relative;font-family:"Inter",sans-serif;color:#fff}}
.backdrop img{{width:900px;height:900px}}
.card{{position:absolute;left:70px;top:70px;right:70px;bottom:70px;display:flex;flex-direction:column;justify-content:center}}
.brand{{display:flex;align-items:center;gap:18px;margin-bottom:34px}}
.brand img{{width:84px;height:84px;border-radius:20px}}
.brand strong{{font:900 40px Nunito,sans-serif}}
.eyebrow{{font-size:22px;letter-spacing:.12em;text-transform:uppercase;color:#FF9933;font-weight:600;margin:0 0 16px}}
h1{{font-size:76px;line-height:1.02;margin:0 0 24px;max-width:900px}}
.sub{{font-size:28px;color:#d9d0f0;margin:0 0 10px}}
.free{{font:800 26px Nunito,sans-serif;color:#FF9933}}
</style></head><body>
<div class="backdrop"><img src="icon-512.png" alt=""></div>
<div class="card">
<div class="brand"><img src="icon-192.png" alt=""><strong>Kastideo</strong></div>
<p class="eyebrow">{eyebrow}</p><h1>{h1}</h1><p class="sub">{sub}</p><p class="free">{free}</p>
</div></body></html>"""


class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


def main():
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Q, directory=PUB))
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={"width": 1200, "height": 630})
        for lang, (eyebrow, h1, sub, free) in TEXT.items():
            html = PAGE.format(port=port, eyebrow=eyebrow, h1=h1, sub=sub, free=free)
            tmp = os.path.join(PUB, "_og.html")
            open(tmp, "w", encoding="utf-8").write(html)
            pg.goto(f"http://127.0.0.1:{port}/_og.html")
            pg.wait_for_timeout(600)
            pg.screenshot(path=os.path.join(PUB, f"og-{lang}.png"))
            from PIL import Image
            Image.open(os.path.join(PUB, f"og-{lang}.png")).convert("RGB").save(
                os.path.join(PUB, f"og-{lang}.jpg"), "JPEG", quality=88, optimize=True, progressive=True)
            os.remove(os.path.join(PUB, f"og-{lang}.png"))
        b.close()
    os.remove(os.path.join(PUB, "_og.html"))
    srv.shutdown()


if __name__ == "__main__":
    main()
