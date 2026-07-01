# -*- coding: utf-8 -*-
# build_comic.py -- Landingpage-Comic-Bilder aufbereiten:
# OneDrive .../kidslist/comic/<name>.png -> auf max 1200px -> WEBP -> assets/img/comic/<name>.webp
# Namen werden normalisiert (_ -> -), damit sie exakt zu den data-img der Landingpage passen.
# Figuren-Blaetter (comic_reference*) werden uebersprungen (nur Konsistenz-Anker, kein Einbau).
# Wiederholbar (ueberschreibt). Bricht ab, wenn die Namen nicht exakt die 8 erwarteten ergeben.
import os, sys
from PIL import Image

SRC = r"C:\Users\Gerit\OneDrive\work\Cortex-Medien\kidslist\comic"
DST = r"D:\Projekte\kidslist-web\assets\img\comic"
MAX = 1200
ERWARTET = {"morgen-problem-1", "morgen-problem-2", "abend-problem-1", "abend-problem-2",
            "morgen-app-1", "morgen-app-2", "abend-app-1", "abend-app-2"}

def main():
    sys.stdout.reconfigure(encoding="utf-8")
    os.makedirs(DST, exist_ok=True)
    erzeugt = set()
    for f in sorted(os.listdir(SRC)):
        if not f.lower().endswith(".png"):
            continue
        stem = os.path.splitext(f)[0]
        if stem.lower().startswith("comic_reference"):
            print("uebersprungen (Figuren-Blatt):", f)
            continue
        key = stem.replace("_", "-")
        im = Image.open(os.path.join(SRC, f)).convert("RGB")
        im.thumbnail((MAX, MAX), Image.LANCZOS)
        ziel = os.path.join(DST, key + ".webp")
        im.save(ziel, "WEBP", quality=85, method=6)
        erzeugt.add(key)
        print("OK %s -> %s.webp (%dx%d, %d Bytes)" % (f, key, im.size[0], im.size[1], os.path.getsize(ziel)))
    fehlend = ERWARTET - erzeugt
    unerwartet = erzeugt - ERWARTET
    print("\nErzeugt:", len(erzeugt),
          "| fehlend:", sorted(fehlend) or "keine",
          "| unerwartet:", sorted(unerwartet) or "keine")
    if fehlend or unerwartet:
        sys.exit("ABBRUCH: Namen passen nicht exakt zu den 8 erwarteten data-img.")

if __name__ == "__main__":
    main()
