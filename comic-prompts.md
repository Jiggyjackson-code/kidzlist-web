# Bild-Prompts -- Landingpage-Comic (K78), 8 Panels

Zweck: die 8 Platzhalter-Felder des Landingpage-Comics durch echte Bilder ersetzen.
Story: Seite 1 = das Problem (Morgen- und Abend-Trotz), Seite 2 = die Loesung mit
Kidslist (das Maedchen macht Morgen-/Abendroutine selbststaendig und freut sich).

## Ablauf (Arbeitsteilung)
1. **Gerit** generiert in **ChatGPT / GPT-Image**: zuerst das **Figuren-Blatt**, dann die 8 Panels.
2. **Gerit** legt die 8 PNGs unter ihrem exakten Namen ab in:
   `C:\Users\Gerit\OneDrive\work\Cortex-Medien\kidslist\comic\<name>.png`
   Namen (genau so): `morgen-problem-1`, `morgen-problem-2`, `abend-problem-1`,
   `abend-problem-2`, `morgen-app-1`, `morgen-app-2`, `abend-app-1`, `abend-app-2`.
3. **Claude** wandelt sie zu `assets/img/comic/<name>.webp` (verkleinern, KEINE Freistellung --
   Panels sind Vollbilder). Die Landingpage zeigt sie dann automatisch statt der Emoji-Platzhalter.

## WICHTIG -- Format
- **Kein Text, keine Sprechblasen, keine Buchstaben, kein Logo im Bild.** Die Sprechblasen
  (DE/EN/GR) legt der Code als eigene Ebene drueber.
- **Platz fuer die Sprechblase freilassen** (ruhige Flaeche): siehe pro Panel "oben-links"
  bzw. "unten-rechts".
- **Quadratisch (1:1)**, Figuren mittig mit etwas Rand -- die Felder werden je nach Raster
  beschnitten und langsam gezoomt (Ken-Burns), Wichtiges darf nicht am Rand kleben.
- **Tageszeit-Stimmung** beachten: Morgen hell, Abend warm/gedaempft (steht in jedem Prompt).
- Bei den App-Panels (5+7) ein **Tablet mit buntem, freundlichem Kinder-Bildschirm** zeigen,
  aber **ohne lesbaren Text/echtes Logo** (Bild-KIs verhunzen UI-Text -- Lehre #146).

## Konsistenz -- der wichtigste Schritt (Figuren-Blatt zuerst!)
GPT-Image haelt Figuren NICHT von allein ueber 8 Bilder gleich. Darum:
1. **Zuerst dieses Figuren-Blatt generieren** (ein Bild, Maedchen + Mutter, neutraler
   Hintergrund). Das ist der Anker.
2. Dann **jedes der 8 Panels in derselben ChatGPT-Unterhaltung** erzeugen und das
   Figuren-Blatt als **Referenzbild mitgeben**, mit dem Zusatz:
   *"same girl and same mother as in the reference sheet -- same faces, hair and clothes."*

### Figuren-Blatt (Prompt)
Soft children's book illustration with a visible crayon / coloured-pencil texture, warm
friendly colours. **Character reference sheet** on a plain light background, showing two
characters full-body, standing side by side, friendly neutral pose:
- **a cheerful little girl, about 3-4 years old**, wavy brown hair in two small pigtails,
  big friendly eyes, wearing a **sunny yellow t-shirt and blue dungarees**;
- **a warm young mother, about 30**, shoulder-length brown hair, wearing a **soft light-blue
  top and jeans**.
No text, no labels. Clear, consistent character design to be reused in later scenes.

*(Details wie Haarfarbe/Kleidung darfst du frei aendern -- Hauptsache, sie bleiben
danach in allen 8 Panels gleich.)*

## Gemeinsamer Stil-Satz (steckt in jedem Panel-Prompt)
> Soft children's book illustration with a **visible crayon / coloured-pencil texture**:
> gentle hand-drawn look, warm cosy colours, friendly and heartwarming. Same girl and
> mother as in the reference sheet (same faces, hair, clothes). **No text, no speech
> bubbles, no letters.** Square 1:1, characters centred with a little margin.

---

## Die 8 Panel-Prompts (englisch -- copy-paste, Figuren-Blatt als Referenz mitgeben)

### Seite 1 -- das Problem

**1 -- `morgen-problem-1`**  (Morgen / Sprechblase oben-links)
Soft children's book illustration, crayon texture, warm cosy colours. Same girl and mother
as in the reference sheet. Scene: **a child's bedroom in soft morning light through the
window; the mother stands by the bed, gently trying to wake the little girl who is still
snuggled under the blanket.** Calm morning mood. No text. Leave a calm empty area in the
**top-left** for a speech bubble. Square 1:1.

**2 -- `morgen-problem-2`**  (Morgen / Sprechblase unten-rechts)
Soft children's book illustration, crayon texture, warm colours. Same girl and mother as in
the reference sheet. Scene: **the little girl standing by the bed, arms crossed, pouting and
refusing to get dressed, a half-worn shirt lying nearby; the mother beside her looking
patient.** Cute, mild morning tantrum, bright light. No text. Leave a calm empty area in the
**bottom-right** for a speech bubble. Square 1:1.

**3 -- `abend-problem-1`**  (Abend / Sprechblase oben-links)
Soft children's book illustration, crayon texture, warm colours. Same girl and mother as in
the reference sheet. Scene: **the same child's room in the evening, warm lamp light, curtains
drawn, a teddy on the bed; the mother gently invites the girl to come to bed.** Sleepy, cosy
evening mood. No text. Leave a calm empty area in the **top-left** for a speech bubble. Square 1:1.

**4 -- `abend-problem-2`**  (Abend / Sprechblase unten-rechts)
Soft children's book illustration, crayon texture, warm colours. Same girl and mother as in
the reference sheet. Scene: **the girl sitting on the floor still playing with toys, looking
up and protesting, not wanting to stop; evening lamp light.** Cute reluctance. No text. Leave
a calm empty area in the **bottom-right** for a speech bubble. Square 1:1.

### Seite 2 -- die Loesung mit Kidslist

**5 -- `morgen-app-1`**  (heller Morgen / Sprechblase oben-links)
Soft children's book illustration, crayon texture, bright cheerful colours. Same girl as in
the reference sheet. Scene: **a bright sunny morning; the girl proudly holds a tablet showing
a colourful, friendly kids app screen (no readable text or logo) and happily does her morning
routine all by herself, smiling.** Joyful, sunny mood. No text. Leave a calm empty area in the
**top-left** for a speech bubble. Square 1:1.

**6 -- `morgen-app-2`**  (heller Morgen / Sprechblase unten-rechts)
Soft children's book illustration, crayon texture, bright cheerful colours. Same girl as in
the reference sheet. Scene: **the girl beaming with joy as a glowing golden collectible star
with soft sparkles appears in front of her -- she just earned a reward.** Bright, celebratory
morning mood. No text. Leave a calm empty area in the **bottom-right** for a speech bubble.
Square 1:1.

**7 -- `abend-app-1`**  (warmer Abend / Sprechblase oben-links)
Soft children's book illustration, crayon texture, warm cosy colours. Same girl as in the
reference sheet. Scene: **a cosy warm evening in the child's room; the girl calmly does her
evening routine with the tablet (colourful friendly kids screen, no readable text), content
and focused.** Soft warm lamp light. No text. Leave a calm empty area in the **top-left** for
a speech bubble. Square 1:1.

**8 -- `abend-app-2`**  (warmer Abend / Sprechblase unten-rechts)
Soft children's book illustration, crayon texture, warm cosy colours. Same girl as in the
reference sheet. Scene: **the girl happily finished, arms up in a little cheer, cosy and proud,
ready for bed with a big smile; maybe one or two small stars in the air.** Warm, heartwarming
evening mood. No text. Leave a calm empty area in the **bottom-right** for a speech bubble.
Square 1:1.
