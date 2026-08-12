# Prüfung der Methodik — kritisch, nicht bestätigend

**Geprüft am 12.08.2026.** 0 Credits, keine Videosichtung.
Grundlage: `kriterien.md`, `irrtuemer.md`, alle `bewertungen/`, dazu die vier
Erhebungen aus dem öffentlichen Repo `explainer-channel`
(`regeln/messungen.md`, `regeln/ink-vs-axen.md`, `regeln/g2-haltbarkeit.md`,
`regeln/themenwahl-test.md` — von den Branches
`claude/kanal-2-datengrundlage-bldjee` und
`claude/established-channels-analysis-rsbu8a`; auf `main` existiert `regeln/`
nicht).

**Ergebnis in einem Satz:** Die Messregeln der Methodik (RPM rechnen,
live prüfen, Katalogwirkung, gemessen/geschätzt trennen) halten der Prüfung
stand — die **Bewertungsarchitektur** (9 gleichgewichtete Kriterien, zwei der
drei K.-o.-Schwellen, die 1-10-Note) hält ihr nicht stand und ist in Teilen
durch die eigenen Daten widerlegt.

---

## TEIL 0 — Die Monetarisierungs-Aussage aus bibel-schlaf.md

**Die Aussage hält.** Live-Prüfung am 12.08.2026, `check_channel_monetization`
mit `bypassCache=true`, dieselbe Methode wie beim Sleepy-Monk-Lauf:

| Kanal | Katalogfeld | Live 12.08.2026 | Katalog korrekt? |
|---|---|---|---|
| **Hush Little Lamb** (`UCBnoLXdJ9tIR-8vjSdgiYAw`) | nein | **NICHT monetarisiert** | ja |
| **Selah** (`UCiolk5zOhJjJta3iS6HJDCw`) | nein | **NICHT monetarisiert** | ja |
| Rest in Jesus (`UCo6ArZxfwPQ4uSCFiqfDK9A`) | nein | nicht monetarisiert | ja |
| Rest In Faith (`UCMbWbGbTG23WSa5M6VJgctw`) | nein | **monetarisiert** | **NEIN** |
| Saints for Sleep (`UCC1IC-KjIUocGrBtHe5tUoA`) | nein | **monetarisiert** | **NEIN** |
| Night Psalms (`UCP7dYl63OzMZXZiWlOCcv1g`, Positivkontrolle) | ja | monetarisiert | ja |

(Night Psalms lieferte zweimal „Service unavailable" und erst im dritten
Versuch ein Ergebnis — einzelne Fehlschläge dieses Endpunkts sind kein Befund.)

**Der neue Befund liegt in der Kanalbeschreibung.** Hush Little Lamb schreibt
wörtlich: Spenden helfen, *„to keep our videos **ad-free**"* — die fehlende
Monetarisierung ist eine **Entscheidung des Betreibers** (Ministry-Modell mit
Spendenfinanzierung), keine Eigenschaft der Nische. Damit ist die offene Frage
aus `bewertungen/bibel-schlaf.md` beantwortet. Die rote Ampel bleibt trotzdem
rot: Für einen werbefinanzierten Einstieg ist der Umsatz der Nische weiterhin
**unbelegt** — die Gewinner beweisen Nachfrage, nicht Erlös. Note bleibt 7/10;
die Datei ist entsprechend aktualisiert.

Neue Messwerte [gemessen, 12.08.2026]: Hush Little Lamb 11.200 Abos
(21.06.-Pause hält an, 7,4 Wochen; Abos seit dem letzten Stand 10.900 weiter
gestiegen), 8 Videos, 1.117.234 Gesamtviews. Selah 5.930 Abos, 13 Videos,
445.455 Gesamtviews; NexLev-Modellumsatz 1.990 $/Monat bei real 0 $ —
**die Modellumsätze nicht monetarisierter Kanäle sind kontrafaktisch** und
dürfen nie als Ertragsbeleg zitiert werden.

**Verfeinerung von Irrtum #7:** Das Katalogfeld ist nicht systematisch
invertiert, sondern schlicht unzuverlässig. Über beide Prüftage zusammen wurden
11 Kanäle mit Katalog-„nein" live geprüft: **7 falsch, 4 richtig** (heute
zusätzlich gefunden: Moon Mind Temple und The Sleepy Historian sind live
monetarisiert, beide standen im Katalog auf „nein" mit 0 $ Umsatz). Ein
Katalog-„nein" bedeutet nicht „verdient nichts", sondern **„Umsatz unbekannt"**
— das betrifft auch jede Monetarisierungsquote (Kriterium 8), die je aus
Katalogdaten gerechnet wurde. `irrtuemer.md` #7 hat einen Nachtrag bekommen.

---

## TEIL 1 — Der Rückwärtstest

### Anlage

15 Kanäle aus 9 Nischen, alle mit erstem Video vor dem **Cutoff 11.08.2025**;
je Kanal wurde rekonstruiert, was ein Prüfer am Cutoff sehen konnte, und gegen
den heutigen Stand gehalten. Datumsrekonstruktion: Bei YouTube-Listen springt
die Relativangabe genau an der 12-Monats-Grenze von „X months ago" auf
„1 year ago" — die Grenze **ist** der Cutoff (±Wochen, [abgeleitet]). Für die
vier History-Explainer-Kanäle liegen exakte Zeitstempel in
`regeln/daten/g2-videos.tsv` [gemessen]. Umsätze heute: NexLev-Modell
[geschätzt], für die G2-Kanäle live am 12.08.2026 gezogen.

### Der wichtigste Befund steht vor jeder Zahl

**Die Gesamtnote ist rückwärts nicht berechenbar.** Von den 9 Kriterien sind
**7 reine Gegenwarts-Schnappschüsse**: Outlier-Score (1), RPM (2), Umsatz je
Video (3), Katalogwirkung (4), Ertrag je Arbeitsstunde (7), Monetarisierung
(8) und Geografie (9) lassen sich für einen Zeitpunkt vor zwölf Monaten mit
den verfügbaren Werkzeugen **nicht rekonstruieren** — es gibt keine
Zeitreihen. Rückwärts prüfbar sind nur Kadenz (6, aus Uploaddaten) und ein
Teil von Haltbarkeit (5, aus Upload-Datum des heutigen Top-Videos, mit
Vorbehalt kumulativer Views).

Ein Bewertungsverfahren, dessen Note sich nicht rückdatieren lässt, **kann
grundsätzlich nie an Ergebnissen kalibriert werden**. Es kann treffend sein
oder nicht — man wird es aus dem Verfahren selbst heraus nie erfahren. Das ist
die schwerste strukturelle Schwäche der Methodik, und sie war vor diesem Test
nirgends dokumentiert.

### Die Tabelle

Stand am Cutoff [abgeleitet aus gemessenen Uploaddaten; G2 exakt gemessen] →
Ergebnis heute [Umsatz: NexLev-Modell]:

| Kanal | Nische | Alter@Cut | Videos@Cut | Kadenz@Cut | Top-Video@Cut im Lebensjahr | Top-3-Anteil@Cut¹ | $/Mo heute | aktiv heute |
|---|---|---|---|---|---|---|---|---|
| Sleepy Monk | Östl. Weisheit | 2,4 Mon | ~49 | **4,8 → K.-o.** | 1 (zwangsläufig) | (82 %)¹ | **2.618** | nein (14 Wo Pause) |
| SleepNomad² | Philosophie | 3,1 Mon | ≥31 | **2,3 → K.-o.** | 1 (zwangsläufig) | n. e. | **2.480** | ja |
| Moon Mind Temple | Östl. Weisheit | 5,3 Mon | ~168² | **7,3 → K.-o.** | 1 (zwangsläufig) | (66 %)¹ | unbekannt³ | ja |
| Folks of Yore | Hist-Explainer | 4,5 Mon | 7 | 0,36 | 1 (zwangsläufig) | 61,8 % | 236 | ja |
| The Sleep Bible | Bibel-Schlaf | 8,7 Mon | 20 | 0,53 | 1 (zwangsläufig) | 50,2 % | 2.038 | ja |
| The Sleepy Historian | Geschichte-Schlaf | 15,5 Mon | ~78 | 1,16 | 2 | (38 %)¹ | unbekannt³ | nein |
| quack doc | Hist-Explainer | 17,1 Mon | 54 | 0,73 | 1 | 34,5 % | **11.714** | ja |
| Caddy Sleeps | Gaming-Schlaf | 19,4 Mon | ~39 | 0,46 | 1 | (29 %)¹ | 1.355 | ja |
| Down To Sleep Extra | Fandom-Lore | 20,5 Mon | 18 | 0,20 | 1 | 31,9 % | 201 | nein |
| Historically | Hist-Explainer | 27,9 Mon | 13 | 0,11 | **2** | 41,8 % | **22.173** | ja |
| History Mapped Out | Hist-Explainer | 28,3 Mon | 86 | 0,70 | 2 | 22,4 % | 3.190 | ja |
| Gates of Imagination | Literatur | 29,0 Mon | ~115 | 0,91 | 3 | (36 %)¹ | 2.899 | ja |
| Lectures f. Sleep & Study | Vorlesungen | 37,4 Mon | 11 | 0,07 | 1 | 90,1 % | **0** (nicht mon.) | nein (seit 03/2025) |
| Classic Audiobooks Elliot | Literatur | 41,4 Mon | ~183 | 1,02 | 2 | (48 %)¹ | 206 | nein |
| Story Classics | Literatur | 59,0 Mon | 12 | 0,05 | 1 | 80,1 % | 172 | nein (65 Wo) |

¹ Werte in Klammern: aus der Popular-Seite gerechnet, die nur die obersten
Videos enthält — **obere Schranken** [abgeleitet]. Ohne Klammern: vollständige
Kataloge [gemessen].
² SleepNomad: NexLev-Katalog führt 167 Videos, sichtbar sind **61** — rund
100 Videos wurden gelöscht. Alle SleepNomad-Zahlen sind dadurch unsicher; der
Fall ist zugleich ein eigener Befund (siehe Überlebensverzerrung).
³ Live monetarisiert, Katalogumsatz 0 — realer Umsatz unbekannt (Teil 0).

### Sagt die Gesamtnote etwas vorher?

**Sie ist nicht berechenbar (siehe oben) — und die berechenbaren Bestandteile
sagen teils das Gegenteil dessen vorher, was die Kriterien behaupten:**

**Kriterium 6 (Kadenz > 2 = rot, K.-o.) ist als Nischen-K.-o. widerlegt.**
Am Cutoff hätte es Sleepy Monk (4,8/Wo) und SleepNomad (2,3/Wo) verworfen —
heute 2.618 und 2.480 $/Monat, zwei der drei umsatzstärksten Schlafkanäle des
Samples. Median-Umsatz der verworfenen Kanäle: **2.549 $**; Median der
durchgelassenen: **1.355 $**. Über alle 13 Kanäle mit bekanntem Umsatz
korreliert Kadenz@Cutoff **positiv** mit dem heutigen Umsatz (Spearman +0,45)
[abgeleitet]. Dazu passt der Sleepy-Monk-Lauf selbst: Das K.-o. traf dort die
Unterrichtung Geschichte/Wissenschaft — mit 11.494 $/Monat und 853 $/h beim
Spitzenkanal. Und in den Gründungsdaten der Methodik (g2-haltbarkeit) liegt
**kein einziger** der abgestürzten Kanäle über 2/Woche: quack doc 0,73–1,0,
History Mapped Out 0,70, Professor Historian 1,65 — die Schwelle „über 2 =
rot" trennt in den Daten, aus denen die Methodik stammt, **nichts**. Sie ist
eine Machbarkeits-Überlegung, die als Qualitätsurteil verkleidet wurde.

**Kriterium 5 (Gipfel im 1.–2. Lebensjahr = rot) ist in der praktizierten Form
doppelt defekt.** Erstens: Bei **7 von 13** Kanälen war der Kanal am Cutoff
jünger als 24 Monate — der Gipfel liegt dann **zwangsläufig** im 1.–2.
Lebensjahr. Ein Kriterium, das bei jeder jungen Nische automatisch feuert,
misst nichts. Zweitens: Bei den sechs alten Kanälen markiert die
Top-Video-Datierung **Historically rot** (größtes Video im Publikationsmonat
23) — ausgerechnet den einzigen Kanal, dessen Niveau nachweislich über drei
Jahre hält, mit heute 22.173 $/Monat, und ausgerechnet den Kanal, aus dessen
Messung das Kriterium stammt. Die Quelle (`g2-haltbarkeit.md`) misst
**Quartals-Mediane**; `kriterien.md` hat daraus „Views-Gipfel" gemacht, und
die Sleepy-Monk-Prüfung hat das aufs meistgesehene Einzelvideo angewandt. Die
Operationalisierung hat das Kriterium bei der Übernahme korrumpiert — von mir,
in beiden Dokumenten.

**Das prädiktivste Einzelmaß ist keines der 9 Kriterien.** Der
**Top-3-Anteil am Cutoff** — die Frühwarnzahl aus `irrtuemer.md` #3, die es
nie in die Kriterienliste geschafft hat — korreliert mit −0,46 (Spearman,
n = 12) mit dem heutigen Umsatz, betragsgleich mit den besten anderen Größen
und in der theoretisch erwarteten Richtung: Lectures 90 % → 0 $;
Story Classics 80 % → 172 $; Folks of Yore 62 % → 236 $; dagegen
History Mapped Out 22 % → 3.190 $, quack doc 35 % → 11.714 $, Historically
42 % → 22.173 $. Gegenbeispiel im Sample: Down To Sleep Extra (32 %, getragen)
liegt trotzdem bei 201 $ — die Zahl ist ein Frühwarnsignal, kein Orakel.

**Was gar nichts vorhersagt:** das Kanalalter am Cutoff (−0,35, getrieben von
zwei alten Leichen) und Kriterium 5 in der Einzelvideo-Form — die Gruppe
„Gipfel im Lebensjahr 2" enthält gleichzeitig den besten Kanal des Samples
(Historically, 22.173 $) und einen der schwächsten (Elliot, 206 $).

**Was die Kriterien richtig erkannt hätten:** die Verlierer. Lectures for
Sleep & Study sah am Cutoff tot aus (5 Monate Pause, 90 % Top-3, fremdes
Vorlesungsmaterial) und ist heute tot. Story Classics und Elliot zeigten
Einzeltreffer-Signaturen und dümpeln. Aber: erkannt über Pause und
Top-3-Anteil — zwei Größen, die **nicht** unter den 9 Kriterien stehen.

**Und ein Befund, der zwei Kriterien gleichzeitig betrifft:** quack doc gilt
nach der Haltbarkeitsmessung als „um Faktor 12 gefallen" — und verdient heute
11.714 $/Monat bei 2,47 Mio. Views/Monat [gemessen live]. Der **Median neuer
Videos** ist gefallen; die **Katalog-Views** tragen den Umsatz weiter. Das
heißt: In einer Nische mit Katalogwirkung (K4 grün) ist ein K5-Absturz der
Neuvideo-Mediane nicht dasselbe wie ein Umsatzabsturz. K4 und K5 sind keine
unabhängigen Prüfungen, sondern zwei Seiten derselben Frage „woher kommen die
Views" — die Methodik behandelt sie als getrennte, gleichgewichtige Punkte.

### Vorbehalte dieses Tests, vollständig

n = 15 (13 mit bekanntem Umsatz) ist klein. Alle Kanäle sind **Überlebende** —
gelöschte Kanäle kann der Test nicht sehen (SleepNomads ~100 gelöschte Videos
zeigen, dass selbst Überlebende ihre Geschichte kürzen). Views sind kumulativ:
der Top-3-Anteil und die Gipfel-Datierung am Cutoff sind mit **heutigen**
Views gerechnet — ein nach dem Cutoff explodiertes Altvideo verfälscht beide
[abgeleitet, nicht korrigierbar]. Die Label-Grenze „1 year ago" hat
Wochen-Unschärfe. Umsätze sind NexLev-Modellwerte, keine Auszahlungen. Und die
Nischenzusammensetzung ist nicht zufällig, sondern aus den eigenen früheren
Prüfungen gewachsen.

---

## TEIL 2 — Kritik der Konstruktion

### 1. Redundanz: die drei Geldkriterien sind höchstens 1,5 Informationen

Spearman-Matrix über die 17 Kanäle des Sleepy-Monk-Laufs [abgeleitet aus
gemessenen/geschätzten Werten vom 11.08.2026]:

| | RPM | $/Mo | $/Video | Kadenz | $/h | Outlier |
|---|---|---|---|---|---|---|
| **RPM (K2)** | 1 | 0,20 | 0,19 | 0,62 | **−0,21** | −0,21 |
| **$/Monat** | | 1 | 0,60 | 0,41 | 0,49 | 0,19 |
| **$/Video (K3)** | | | 1 | −0,03 | **0,71** | 0,50 |
| **Kadenz (K6)** | | | | 1 | −0,41 | −0,45 |
| **$/Arbeitsstunde (K7)** | | | | | 1 | 0,61 |

K3 und K7 teilen sich denselben Zähler und korrelieren mit 0,71 — wer beide
als getrennte Punkte zählt, zählt den Umsatz doppelt. Und das als
Qualitätsmerkmal geführte **RPM-Kriterium korreliert leicht negativ (−0,21)
mit der Zielgröße $/Arbeitsstunde**: Im Sample verlangen die Hoch-RPM-Nischen
hohe Kadenz (RPM↔Kadenz +0,62) und fressen den Vorteil wieder auf — genau der
Gates-of-Imagination-Befund (3,38 $ RPM, 837 $/h) gegen die Zen-Kanäle
(8–9,6 $ RPM, 32–277 $/h). **K2 ist eine unverzichtbare Messgröße und ein
untaugliches Bewertungskriterium.**

### 2. Gewichtung: Gleichgewichtung ist durch nichts begründet

Alle 9 zählen gleich — Katalogwirkung so viel wie Geografie. Aus den Daten
lässt sich eine Rangfolge begründen: **K4 (Katalogwirkung)** ist der einzige
Befund, der über alle Erhebungen robust ist (sechs Kanäle mit 15–78 Wochen
Pause, Views flach bis +16 %) und der wirtschaftlich dominiert (quack doc:
Neuvideo-Median −92 %, Umsatz trotzdem fünfstellig — der Katalog ist der
Umsatz). **K7** ist die Zielgröße. **K9 (Geografie)** hat in keiner einzigen
Prüfung je ein Urteil geändert — es erklärt den RPM, mehr nicht. **K1
(Outlier ≥ 2 bei 3 Kanälen)** hat als Schwelle zweimal Unsinn produziert: Im
Sleepy-Monk-Lauf disqualifizierte es die tragfähigste Unterrichtung
(Gemeinfreie Literatur, ein einziger Kanal ≥ 2), während Lorevia mit Outlier
13,83 heute 14 $/Monat verdient (`irrtuemer.md` #2) und The World Before Dawn
mit 31,59 eine 5-Video-Leiche ist. Der Outlier-Score misst Ausreißer —
`irrtuemer.md` #3 sagt selbst, dass Ausreißer nichts beweisen. Ein Kriterium,
das auf einer Kennzahl steht, deren Untauglichkeit im eigenen
Irrtümer-Dokument steht, ist ein Konstruktionsfehler.

### 3. Überlebensverzerrung: überall, und ein neuer Beleg

NexLev indexiert einen kuratierten Bestand (~50.000 Kanäle); tote und
gelöschte Kanäle verschwinden. Schon die „Verlierergruppe" G3 der
Gründungsmessung bestand aus Überlebenden, die weiter hochladen. Neu aus
diesem Test: **SleepNomad hat ~100 von 167 Videos gelöscht** — der sichtbare
Katalog ist auch bei überlebenden Kanälen eine geschönte Geschichte. Jede
Kadenz-, Ertrag-je-Video- und Top-3-Rechnung auf Katalogbasis erbt das. Nicht
heilbar mit diesen Werkzeugen; es gehört als Standard-Vorbehalt in jede
Bewertung, nicht nur in die Irrtümerliste.

### 4. Zirkularität: dreimal fündig

- **K5-Schwelle** („Gipfel im 1.–2. Lebensjahr = rot") stammt aus n = 2
  echten Abstürzen (quack doc, History Mapped Out) derselben G2-Messung, an
  der sie demonstriert wird — und der Plateau-Gegenfall (Historically) fällt
  bei wörtlicher Anwendung selbst durch (Teil 1).
- **Top-3-Schwellen** (35 %/50 %) sind an der G2-Gruppe geeicht und wurden
  bisher nur an ihr gezeigt. Der Rückwärtstest hier ist ihre erste Prüfung an
  fremden Kanälen — bestanden (Richtung stimmt), aber die konkreten
  Schwellenwerte bleiben Setzungen.
- **K6-Schwelle** („über 2 = rot"): in den Gründungsdaten trennt sie nichts
  (alle Abstürzler < 2, siehe Teil 1) — sie wurde nie aus Daten abgeleitet.
- Die 9 Kriterien insgesamt wurden **nach** den drei ersten Nischenprüfungen
  kodifiziert und erklären deren Ergebnisse — die Noten 7/7/7 sind keine
  unabhängige Bestätigung des Verfahrens, sondern seine Definition.

Positiv festzuhalten: Der Themenwahl-Test im explainer-Repo hat seine eigene
Zirkularität (zwei Merkmale aus den Vorhersage-Videos abgeleitet) selbst
erkannt und ausgewiesen — das Muster „Herkunft der Schwelle nennen" muss in
die Kriterien selbst.

### 5. Fehlende Kriterien

- **Videolänge / Watchtime-Produktion.** Der stärkste Ökonomie-Befund des
  Sleepy-Monk-Laufs (368 min × 0,8/Wo schlägt 183 min × 2,9/Wo trotz
  Drittel-RPM) kommt in den 9 Kriterien nur als Nebensatz über Loops vor.
  Länge gehört als Pflicht-Messgröße in jede Prüfung; ob als eigenes Kriterium
  oder in K7 integriert, ist zweitrangig — nicht erfasst werden darf sie nie.
- **Top-3-Anteil.** Bester Prädiktor im Rückwärtstest, ab 20 Videos messbar,
  steht bisher nur in den Irrtümern. Gehört in den Kriterienkatalog.
- **Rechtegrundlage.** Die Sleepy-Monk-Prüfung drehte sich am Ende um genau
  diese Frage (Fremd-IP-Lore, Übersetzungsrechte, „freies Material ≠ freier
  Text") — und die 9 Kriterien enthalten **kein** Rechte-Kriterium. Ein
  Prüfschritt, der faktisch immer durchgeführt wird, aber nirgends gefordert
  ist, wird irgendwann vergessen.
- **Zeitreihen-Basislinie.** Die G2-Messung funktionierte nur, weil
  `g2-videos.tsv` als datierte Basislinie committet wurde. Keine Regel der
  Methodik fordert das für Nischenprüfungen — deshalb ist der
  Katalog-Snapshot-Vergleich im Sleepy-Monk-Lauf undatiert geblieben
  (Vorbehalt dort selbst benannt).

### 6. Die Skala: 6, 7, 7, 7

Vier Prüfungen, vier Noten in einem Zwei-Punkte-Band — **eine Skala, die
nicht trennt, ist keine Skala.** Schlimmer: Es gibt keine definierte Abbildung
von 9 Ampeln auf eine Zahl. Bibel-Schlaf (K8 rot, K4 grün) und
History-Explainer (K4 rot, K8 grün) bekamen dieselbe 7 für entgegengesetzte
Befunde; die Note transportiert die Information nicht, sie vernichtet sie.
Die K.-o.-Regel und die Rangliste nach $/Arbeitsstunde haben in den
bisherigen Prüfungen die gesamte Entscheidungsarbeit geleistet — die Note hing
dekorativ daneben. **Empfehlung: Note abschaffen; Tore + Rangliste + benannte
Restschwäche sind das ehrlichere Format** (Details in der v2-Fassung von
`kriterien.md`, seit 12.08.2026 aktiv).

---

## TEIL 3 — Wird an der falschen Stelle gemessen?

Die Vorgeschichte ist eindeutig: In vier Erhebungen trennte kein messbares
Oberflächenmerkmal Gewinner von Verlierern (messungen.md: kein Titel-,
Thumbnail-, Tempo-, CTA-, Quellen-Merkmal trennt G1 von G3; ink-vs-axen:
Like-Rate und Kommentarrate zeigen sogar **für** den Verlierer; Themenwahl:
0 von 7 Merkmalen bei 429 Videos, 69,2 % der Streuung innerhalb der Kanäle).

### Was von außen prinzipiell unsichtbar ist

Retention/Wiedergabedauer, CTR, Impressionen, Traffic-Quellen
(Browse/Suggested/Search), echte Umsätze, A/B-Thumbnail-Daten.
`get_daily_analytics` und alle `get_my_*`-Werkzeuge funktionieren nur für
eigene Kanäle (in `g2-haltbarkeit.md` ausdrücklich belegt). **Genau die
Größen, die die Auslieferung steuern, sind für Fremdkanäle nicht beobachtbar.**
Die 69,2 % Innerhalb-Kanal-Streuung liegen fast vollständig in diesem blinden
Feld.

### Die messbaren Stellvertreter sind geprüft — und haben versagt

Das ist der unbequeme Teil: Es ist nicht so, dass Stellvertreter fehlen —
die vorhandenen wurden gemessen und **zeigen in die falsche Richtung**:

| Stellvertreter | Messung | Ergebnis |
|---|---|---|
| Like-Rate | ink-vs-axen, 26 Videos | Axen (Absturz) 2,92 % **>** Ink (Aufstieg) 2,00 % |
| Kommentare je 1.000 Views | ink-vs-axen, 3 Videos | Axen-Treffer 2,08 **>** Ink-Treffer 0,91; beim späten Axen-Video 16 von 20 Top-Kommentaren von Bot-Konten — Signal vergiftet |
| Titel-/Themenmerkmale | 429 Videos, blind | 0 von 7 halten |
| Thumbnail-Metriken | messungen.md | Verlierer haben die **größte** Schrift |

Ungeprüfte, kostenlose Kandidaten bleiben: Abo-Zuwachs je Video (braucht
selbst angelegte Snapshot-Reihen), view-gewichtete Videolänge
(`weighted_avg_duration` aus `get_geography_revenue` — zeigt, welche Länge die
Views tatsächlich einsammelt; das ist ein Format-Signal, **keine** Retention),
`youtube_channel_outliers` je Kanal. Erwartung dämpfen: Die bisherige
Trefferquote externer Stellvertreter liegt bei null.

### Die richtige Konsequenz ist nicht „mehr messen", sondern Ebenen trennen

Die Befunde ordnen sich, sobald man drei Ebenen unterscheidet:

1. **Nischenökonomie** (RPM real, Katalogwirkung, Monetarisierung, Rechte,
   Länge×Kadenz): von außen **messbar**, und die Methodik hat hier
   nachweislich Diskriminierungskraft — der Sleepy-Monk-Lauf hat eine
   Nischendefinition widerlegt, Faktor-3-RPM-Unterschiede gemessen und eine
   falsche Grundannahme gekippt. Hier funktioniert das Verfahren.
2. **Kanalüberleben**: teilweise messbar (Top-3-Anteil, Zeitreihen), aber
   Abstürze haben keine sichtbaren Ursachen (g2-haltbarkeit) — vorhersagbar
   ist hier nichts, nur früh erkennbar.
3. **Video-Erfolg**: von außen nicht messbar (Themenwahl-Test, 69,2 %).

Die 9 Kriterien vermischen die Ebenen und tun so, als wäre alles Ebene 1.
**Ein Kriterium „Beurteilbarkeit von außen" ist sinnvoll** — nicht als Ampel,
sondern als Pflichtabschnitt jeder Bewertung: Welche der Kernzahlen stehen auf
Zeitreihen, welche auf Schnappschüssen, welche auf Modellwerten. Der
Sleepy-Monk-Lauf hat das implizit getan (Abschnitt „gemessen / geschätzt /
unbekannt"); v2 macht es zur Pflicht mit festem Raster.

---

## Vorschlag kriterien.md v2

> **Nachtrag 12.08.2026:** Der Vorschlag wurde übernommen. Die v2-Fassung ist
> jetzt [`kriterien.md`](kriterien.md); die abgelöste 9-Kriterien-Fassung
> liegt unverändert in [`kriterien-v1.md`](kriterien-v1.md) und wird bei der
> nächsten Prüfung parallel mitgefahren (Kalibrierregel im README).

Begründung je Änderung:

| # | Änderung | Begründung (Beleg) |
|---|---|---|
| 1 | **Note 1–10 abschaffen**; Ausgabe = Tore + Rangliste ($/h) + benannte Restschwäche | 6/7/7/7 trennt nichts; keine definierte Abbildung Ampeln→Zahl; Note hat in 4 Prüfungen keine Entscheidung getragen (Teil 2.6) |
| 2 | **K6 vom Nischen-K.-o. zum Machbarkeits-Tor relativ zur eigenen Pipeline** („Kadenz × Menschenstunden je Video ≤ verfügbare Stunden") | K.-o. hätte Sleepy Monk und SleepNomad verworfen (2.618/2.480 $); Schwelle „>2" trennt in den Gründungsdaten nichts; Kadenz korreliert +0,45 mit Umsatz (Teil 1) |
| 3 | **K5 neu operationalisieren**: Quartals-Mediane der Neuvideo-Views, bewertbar erst ab 18 Monaten Historie, sonst ausdrücklich „nicht prüfbar" — nie automatisch rot | Einzelvideo-Form ist bei 7/13 Kanälen zwangsläufig rot und markiert Historically (22.173 $/Mo, hält seit 3 Jahren) als rot (Teil 1) |
| 4 | **Top-3-Anteil wird Kernzahl** (ab 20 Videos; < 35 % getragen, > 50 % Einzeltreffer, Schwellen als Setzung gekennzeichnet) | Bester Prädiktor des Rückwärtstests (−0,46); bisher nur in irrtuemer.md (Teil 1) |
| 5 | **Rechtegrundlage wird Tor 1** (Originaltext, Übersetzung, Fremd-IP) | Sleepy-Monk-Prüfung entschied sich an der Rechtefrage; in den 9 Kriterien fehlt sie komplett (Teil 2.5) |
| 6 | **K2 RPM: Messgröße statt Bewertungskriterium** (Pflichtmessung, fließt nicht in ein Urteil) | RPM korreliert −0,21 mit $/h; hoher RPM ist kein Vorteil, wenn Kadenz/Länge dagegenstehen (Teil 2.1) |
| 7 | **K3 streichen** (in $/h enthalten), dafür **Videolänge & Watchtime-Produktion (Länge × Kadenz) als Pflicht-Messgrößen** | K3↔K7 Spearman 0,71 — Doppelzählung; Längenbefund war der Kernbefund des Sleepy-Monk-Laufs (Teil 2.1, 2.5) |
| 8 | **K1 Nachfrage neu**: ≥ 3 unabhängige, **live monetarisierte** Kanäle mit ≥ 1.000 $/Monat Modellumsatz, davon ≥ 1 mit ≥ 12 Monaten Historie — Outlier-Score nur noch als Suchwerkzeug | Outlier ≥ 2 disqualifizierte die tragfähigste Unterrichtung und adelt Einzeltreffer (Lorevia 13,83 → 14 $/Mo) (Teil 2.2) |
| 9 | **K8 nur noch live** (`check_channel_monetization`), Katalog-„nein" = „unbekannt" | 7 von 11 Katalog-„nein" waren falsch (Teil 0) |
| 10 | **Pflichtabschnitt „Sichtbarkeitsgrenze"** je Bewertung: Zeitreihe / Schnappschuss / Modellwert je Kernzahl, plus Basislinien-Datei (datierte Rohdaten wie `g2-videos.tsv`) | Gesamtnote war rückwärts nicht berechenbar; ohne Basislinien bleibt jede künftige Kalibrierung unmöglich (Teil 1, Teil 3) |
| 11 | **Schwellenherkunft-Pflicht**: jede Schwelle trägt ihre Quelle (gemessen an n = X / Setzung) | Drei Zirkularitätsfunde (Teil 2.4) |

## Was NICHT geändert werden sollte — mit Beleg

1. **„RPM immer rechnen, nie das Feld"** — dreifach unabhängig reproduziert
   (The Sleep Bible 26,53→3,90; Gates 13,11→3,38; sechs weitere Kanäle Faktor
   3–5). Die am besten belegte Regel des Repos.
2. **Katalogwirkung als K.-o.-Tor** — robustester Befund über alle
   Erhebungen (sechs Pausen-Kanäle, 15–78 Wochen, kein Einbruch) und
   ökonomisch dominant (quack doc). Nur die Operationalisierung wird
   präzisiert (Views **und** Umsatzniveau während der Pause).
3. **Klassifikationsregel vor Datensicht** (irrtuemer #5) — hat im
   Sleepy-Monk-Lauf die eigene Lieblingsannahme gekippt. Ein Verfahren, das
   nein sagen kann, ist das Wertvollste hier; nicht anfassen.
4. **Live-Monetarisierungsprüfung** — Teil 0 bestätigt sie erneut.
5. **Trennung gemessen/geschätzt/abgeleitet/unbekannt** — sie ist der Grund,
   warum diese Prüfung überhaupt möglich war: Nur weil die alten Dokumente
   ihre Herkunft je Zahl ausweisen, ließen sich die Fehler heute lokalisieren.
6. **Der 0-Credit-Metadaten-Ansatz** insgesamt: Er hat vier Erhebungen
   getragen und seine eigene Grenze (Ebene 2/3) selbst sichtbar gemacht. Die
   Grenze gehört dokumentiert, nicht der Ansatz verworfen.

## Trennung gemessen / abgeleitet / unbekannt

**Gemessen:** alle Live-Monetarisierungsstatus (12.08.2026); Abos, Videozahlen,
Gesamtviews der Teil-0-Kanäle; G2-Uploaddaten und -Views
(`g2-videos.tsv`); Uploaddaten/Views der Schlafkanäle von den
Videolisten-Seiten (Views gerundet); Redundanz-Matrix-Eingangswerte, soweit im
Sleepy-Monk-Lauf gemessen.

**Abgeleitet:** alles am Cutoff Rekonstruierte (Label-Grenze ±Wochen);
Top-3-Anteile aus Popular-Seiten (obere Schranken); alle
Spearman-Korrelationen; die Kadenz@Cutoff bei Kanälen mit unvollständiger
Pagination (Sleepy Monk ~49, Moon Mind ~168, Elliot ~183).

**Unbekannt:** reale Umsätze aller Kanäle (NexLev-Modelle, bei nicht
monetarisierten kontrafaktisch); Umsatz von Moon Mind Temple und The Sleepy
Historian (live monetarisiert, Katalog 0); Gründe der SleepNomad-Löschungen;
Retention/CTR/Impressionen sämtlicher Fremdkanäle; das Schicksal der Kanäle,
die vor dieser Messung gelöscht wurden.
