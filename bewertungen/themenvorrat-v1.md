# Themenvorrat v1 — belegte Nachfrage für einen englischsprachigen History-Explainer

**Erhoben am 12.08.2026.** Basislinie: `bewertungen/daten/themen-messung-2026-08.tsv`.

**Sprachregelung, verbindlich für dieses Dokument:** Es heißt **belegte
Nachfrage**, nicht „Hype-Potenzial". Der Unterschied ist inhaltlich, nicht
stilistisch. Belegte Nachfrage ist eine Messung an der Vergangenheit: *Hat
dieses Thema bei mehreren unabhängigen Kanälen Publikum getragen?* Das ist
prüfbar. Eine Vorhersage ist es nicht. Nirgendwo in diesem Dokument steht,
dass ein Thema funktionieren **wird** — der 429-Video-Blindtest
(`kriterien.md`, Sichtbarkeitsgrenze Punkt 3) hat 0 von 7
Oberflächenmerkmalen bestätigt, Themenwahl eingeschlossen.

---

## 1. Vorregistrierung (Phase B) — Wortlaut unverändert

> **Festgeschrieben am 12.08.2026, bevor ein einziger Kandidat gemessen
> wurde.** Nach Phase C darf an diesem Abschnitt nichts mehr geändert werden.
> Jede Abweichung wäre nachträgliche Anpassung an das Ergebnis
> (`irrtuemer.md` #5).

### 1.1 Die drei Klassifikationsachsen aus Phase A

Jeder Kandidat wurde vor jeder Messung auf genau drei Achsen zugeordnet:

| Achse | Ausprägungen |
|---|---|
| **Epoche** | Antike · Mittelalter · Frühe Neuzeit · 19. Jh. · 20. Jh. |
| **Region** | Europa · Naher Osten · Asien · Afrika · Amerika |
| **Typ** | benanntes Einzelereignis · Person · Institution/Reich · Epochenüberblick |

**Regel für Region bei See- und Polarereignissen:** Zuordnung nach der
Herkunftsregion der handelnden Expedition/Flotte, nicht nach dem Ort. Titanic,
Endurance, Franklin → Europa; Whaleship Essex, USS Indianapolis → Amerika.
Festgelegt vor der Messung, damit die Zuordnung nicht später zum Ergebnis
passend gedreht werden kann.

**Regel für Typ bei Aufständen:** „Aufstand" ist kein eigener Typ, sondern ein
benanntes Einzelereignis. Vorher festgelegt, weil sonst nachträglich eine
vierte Kategorie hätte entstehen können.

### 1.2 Erwartung: welche Achse hängt am stärksten mit Nachfrage zusammen

**Primäre Erwartung — die Achse TYP trennt am stärksten.**

Erwartete Rangfolge:
`benanntes Einzelereignis > Person > Institution/Reich > Epochenüberblick`

Begründung, vorab: Das Format braucht einen geschlossenen Bogen — Ausgangslage,
Zuspitzung, Ausgang. Ein benanntes Einzelereignis liefert diesen Bogen
mitgeliefert. Ein Epochenüberblick hat keinen Ausgang, sondern nur Verlauf, und
muss den Bogen künstlich herstellen.

**Sekundäre Erwartung — Epoche:**
`20. Jh. > 19. Jh. > Frühe Neuzeit > Mittelalter > Antike`
Begründung: Nähe zur Gegenwart, mehr Anknüpfungspunkte beim Publikum.

**Tertiäre Erwartung — Region:**
`Europa > Amerika > Naher Osten > Asien > Afrika`
Begründung: englischsprachiges Publikum, europazentrierter Schulkanon.

**Falls keine der drei Achsen trennt**, ist genau das der Befund — dann ist die
Ergebnisliste eine Liste belegter *Einzelthemen* ohne verallgemeinerbare Regel,
und sie wird in Phase F ausdrücklich so bezeichnet.

### 1.3 Schwellen für Phase C — vorab festgelegt

**Nachfragebänder über N2 (Median-Views der Treffer):**

| N2 | Urteil |
|---|---|
| ≥ 300.000 | stark belegt |
| 150.000 – 299.999 | belegt |
| 100.000 – 149.999 | schwach belegt (Bodeneffekt, siehe unten) |

*Bodeneffekt, vorab benannt:* Der Filter `minView 100000` ist eine
Messuntergrenze. Der Median kann konstruktionsbedingt nicht unter 100.000
fallen. Ein N2 nahe 100.000 heißt deshalb **nicht** „schwache Nachfrage",
sondern „an der Messgrenze, nicht auflösbar". Das ist eine Grenze des
Instruments, kein Befund über das Thema.

**Mindestbelege, damit ein Thema überhaupt in die Rangliste darf:**

| Größe | Schwelle | Begründung |
|---|---|---|
| N1 (bereinigte Treffer) | ≥ 3 | unter 3 ist „mehrfach unabhängig" nicht behauptbar |
| N3 (unterschiedliche Kanäle) | ≥ 3 | `irrtuemer.md` #3 auf Themenebene: ein Kanal mit fünf Videos ist ein Kanal, keine Nachfrage |

**Sortierung:** nach N2 absteigend. Bei Gleichstand entscheidet N3. Nicht nach
Maximum, nicht nach Trefferzahl — beides prämiert Lotterien.

**D3-Sättigungsverdacht:** N1 > 60 **und** jüngster Treffer älter als 18 Monate
(also vor dem 12.02.2025). Markierung, keine Streichung — es ist eine
Hypothese, keine Messung.

**Katalogtest auf Themenebene (zu Tor 2):** Für die 20 stärksten Themen wird am
ältesten Treffer geprüft, ob alte Videos zum Thema weiterlaufen.

### 1.4 Auswertungsverfahren für Phase F — vorab festgelegt

Spearman-Rangkorrelation zwischen N2 und jeder Achse, über **alle** bereinigt
gemessenen Kandidaten, nicht nur die Top 10.

- **Epoche** ist ordinal und wird 1–5 kodiert (Antike = 1 … 20. Jh. = 5).
- **Region** und **Typ** sind nominal. Sie werden nach der in 1.2
  vorregistrierten Erwartungsrangfolge kodiert (Typ: Epochenüberblick = 1,
  Institution/Reich = 2, Person = 3, Einzelereignis = 4; Region: Afrika = 1,
  Asien = 2, Naher Osten = 3, Amerika = 4, Europa = 5). **Die Kodierung ist
  die Hypothese.** Ein negatives Rho widerlegt damit die vorregistrierte
  Richtung und bestätigt nicht etwa eine umgekehrte.
- **Trennschwelle: |Rho| ≥ 0,30.** Darunter gilt die Achse als nicht trennend.
  Herkunft der Schwelle: **Setzung** (`kriterien.md`, Schwellenherkunft-Pflicht).

### 1.5 Vorab offengelegte Abweichungen vom Messauftrag

Drei Abweichungen, festgehalten **vor** der Messung, damit sie nicht später als
Anpassung erscheinen:

1. **`limit 100` → `limit 40`.** Die API liefert je Video ~40 Zeilen Metadaten
   (Thumbnails, Keywords, Beschreibung). 87 Kandidaten × 100 Videos passen
   nicht in einen Arbeitsdurchgang. Bei den wenigen Themen mit über 40
   bereinigten Treffern wird die Kappung in der Messtabelle ausgewiesen; N2
   ist dann der Median der 40 stärksten und **überschätzt** den wahren Median.
2. **`isExactMatch` wird für ALLE Kandidaten gesetzt, nicht nur „wo sinnvoll".**
   Grund, gemessen im Vortest: Die Fuzzy-Suche filtert nicht, sie sortiert nur.
   `Battle of Cannae Hannibal` fuzzy ergab `total` = 348.325 mit einer
   Kannibalen-Horrorserie auf Platz 5. Eine Trefferzahl aus der Fuzzy-Suche
   wäre keine Messung. Exakt gematcht wird ein **distinktiver Kernbegriff**
   (meist der Eigenname), nicht der volle Titelvorschlag.
3. **Bereinigung von Fehltreffern ist Pflicht.** Exact-Match auf den Titel
   trifft auch Fremdkontexte: `Trafalgar` liefert „Domination At Trafalgar"
   (Spielvideo) und „What if a Modern Destroyer fought the Trafalgar fleet?"
   (Hypothetik). Solche Treffer werden gestrichen; die Messtabelle führt
   **N1 roh** und **N1 bereinigt** getrennt.

### 1.6 Bekannter Verstoß gegen die Blindheit — offengelegt

Beim Vortest des Messprotokolls, **vor** Niederschrift dieser Vorregistrierung,
wurden Trefferzahl und Spitzenwert von **A02 Cannae** und **N-Nichtkandidat
Trafalgar** sichtbar. Cannae ist ein Kandidat der Liste. Für dieses eine Thema
ist die Blindheit nach `irrtuemer.md` #5 also nicht gewahrt. Es bleibt in der
Messung, wird aber in Phase F von der Spearman-Rechnung **ausgeschlossen** und
darf nicht als Beleg für eine Achse zitiert werden. Trafalgar war kein Kandidat
und wurde nicht nachträglich aufgenommen.

---

## 2. Phase A — der Themenvorrat, blind aufgebaut

**87 Kandidaten.** Aufgebaut aus Sachquellen (Wikipedia-Übersichtslisten zu
Schlachten, Belagerungen, Expeditionen, Seuchen, Aufständen, Dynastien,
Schiffsuntergängen; Britannica-Überblicksartikel), **nicht** aus YouTube.
Während Phase A wurde keine Viewzahl und keine YouTube-Abfrage angesehen.

Notiert wurde je Kandidat nur: Titelvorschlag, Epoche, Region, Typ — und der
Kernbegriff, mit dem in Phase C exakt gesucht wird. Keine Zahlen.

*(Die Messwerte in Abschnitt 3 wurden erst nach Festschreibung dieses
Abschnitts und der Vorregistrierung erhoben.)*

### Verteilung des Vorrats

| Epoche | n | | Region | n | | Typ | n |
|---|---|---|---|---|---|---|---|
| Antike | 18 | | Europa | 40 | | Einzelereignis | 56 |
| Mittelalter | 18 | | Asien | 13 | | Person | 13 |
| Frühe Neuzeit | 18 | | Amerika | 14 | | Institution/Reich | 9 |
| 19. Jh. | 16 | | Afrika | 11 | | Epochenüberblick | 9 |
| 20. Jh. | 17 | | Naher Osten | 9 | | | |

**Die Streuung ist ungleich, und das ist eine Schwäche des Vorrats, keine
Eigenschaft der Geschichte.** Europa ist mit 40 von 87 überrepräsentiert,
Einzelereignisse mit 56 von 87 ebenfalls. Für die Spearman-Rechnung in Phase F
heißt das: Die Achsen Region und Typ haben in den schwach besetzten
Ausprägungen (Naher Osten n = 9, Epochenüberblick n = 9) wenig Auflösung. Vorab
festgehalten, nicht nachträglich als Entschuldigung eingeführt.

---

## 3. Was das Messinstrument tatsächlich misst — der wichtigste Befund

**Vor jeder Rangliste steht dieser Befund, weil er alle Zahlen darunter
relativiert.** Der Auftrag unterstellt, `search_videos` könne zählen, wie viele
Videos es *zu einem Thema* gibt. Das kann es nicht. Es zählt, wie viele Videos
eine bestimmte **Zeichenfolge im Titel** tragen. Das sind verschiedene Dinge,
und der Abstand ist groß und unvorhersagbar. Fünf Belege, alle am 12.08.2026
gemessen:

**(1) Die Fuzzy-Suche filtert nicht, sie sortiert nur.** `Battle of Cannae
Hannibal` ohne `isExactMatch` meldet `total` = **348.325** Treffer — das ist
praktisch der gesamte gefilterte Korpus. Auf Platz 5 stand eine
Kannibalen-Horrorserie namens *Gannibal*. Eine Trefferzahl aus der Fuzzy-Suche
wäre keine Messung gewesen, sondern eine Zufallszahl.

**(2) Exakte Langform-Bezeichnungen finden nichts.** Getestet wurden vier
Standardbezeichnungen gegen ihre Kurzform:

| Langform | N1 | Kurzform | N1 |
|---|---|---|---|
| `Destruction of Carthage` | **0** | `Carthage` | 19 |
| `Third Servile War` | **0** | `Spartacus` | 58 |
| `Siege of Masada` | **0** | `Masada` | 3 |
| `Hannibal Barca` | **0** | — | — |
| `Siege of Baghdad` | **0** | — | — |

Besonders deutlich bei Masada: Die Kurzform findet ein Video mit dem Titel
*„Episode 6: The **Seige** of Masada"* — die Langformsuche verfehlt es an einem
**Tippfehler**. Der Substring-Test ist gegen Schreibweisen so empfindlich, dass
er als Themenzähler unbrauchbar ist.

**(3) Kurze Eigennamen messen den Namensraum, nicht das Thema.** Die zehn
stärksten `Terracotta`-Treffer enthalten Skibidi-Toilet-Analysen,
Ziegelmauer-Bauanleitungen, indische Jali-Fassaden und ein italienisches
Tontopf-Rezept. Der stärkste `Carthage`-Treffer (311.223) ist ein
Bodycam-Video aus **Carthage, Texas**. Der stärkste `Trafalgar`-Treffer ist ein
Spielvideo.

**(4) `englishOnly` prüft nicht die Sprache.** Das Flag prüft laut
Werkzeugbeschreibung, ob der **Titel reines ASCII** ist. Durchgelassen wurden
deshalb u. a. *„Battle of Thermopylae in Hindi"*, *„Batalha de Gaugamela"*
(portugiesisch) und *„RECONQUISTA: 700 Tahun Sejarah…"* (indonesisch). Bei
`Gaugamela` war der **einzige** Treffer portugiesisch — die bereinigte
Trefferzahl fiel damit von 1 auf 0.

**(5) Der Filmnamensraum verschluckt ganze Themen.** `Spartacus` hat 58
Treffer; die 15 stärksten sind fast vollständig die Starz-Serie *Blood and
Sand*, Kirk-Douglas-Filmclips, Hindi-Recaps und ein YouTuber namens
*SPARTACUS 18*. `Spanish Armada` hat 2 Treffer — **beide** sind
*„What If a Modern Destroyer/Submarine Fought the Spanish Armada?"*. Nach
Bereinigung bleibt für die Spanische Armada **null** belegte Nachfrage, was
mit Sicherheit falsch ist und nur heißt: Das Instrument sieht sie nicht.

**Folge für alles Weitere:** N1 ist keine Themenzählung, sondern eine
**Titelphrasen-Zählung mit anschließender Handbereinigung**. Ein niedriges N1
belegt **nicht**, dass ein Thema kein Publikum hat — es belegt, dass unter
dieser einen Phrase wenig läuft. Umgekehrt gilt der positive Befund weiterhin:
Wo mehrere unabhängige Kanäle unter derselben Phrase sechsstellige Views
erreicht haben, ist das eine belegte Nachfrage. **Die Liste unten kann
Nachfrage nachweisen, aber ihr Fehlen nicht.**

### Abweichungen vom Messauftrag, vollständig

| Auftrag | Tatsächlich | Grund |
|---|---|---|
| `limit 100` | 5–15, je Block | Antwortgröße: ~400–600 Token je Video. Auch die in 1.5 vorregistrierten 40 wurden nicht durchgehalten. **Abweichung von der eigenen Vorregistrierung** — hier offengelegt statt dort nachträglich korrigiert. |
| N2 = Median aller Treffer | Median der stärksten `<fenster>` Treffer, wo N1_roh > Fenster | dito. Betrifft 7 der 14 bestandenen Themen; in der TSV als `n2_ueberschaetzt=ja` markiert. **Die betroffenen N2 sind Obergrenzen, keine Mediane.** |
| 70–90 Kandidaten gemessen | **37 von 87 gemessen**, davon 31 vollständig bereinigt | Messkapazität. Die 50 nicht gemessenen sind unten namentlich aufgeführt und tragen „nicht erhoben", nicht 0. |
| Katalogtest am ältesten Treffer der Top 20 | **nicht durchgeführt** | Messkapazität. Tor 2 auf Themenebene bleibt offen. |
| `isExactMatch` „wo sinnvoll" | für alle | Befund (1) |

---

## 4. Messtabelle — alle 87 Kandidaten

Vollständige Werte in `bewertungen/daten/themen-messung-2026-08.tsv`.
`—` heißt **nicht erhoben**, nicht 0.

### 4.1 Gemessen und bestanden (14)

| # | Thema | Ep. | Reg. | Typ | N1 roh | N1 ber | **N2** | N3 | N4 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Battle of Waterloo | 19. | Eur | Ereig | 29 | 3 | **600.711** ⚠ | 3 | 2025-05-17 |
| 2 | Genghis Khan | MA | Asi | Person | 60 | 6 | **575.725** ⚠ | 6 | 2025-11-26 |
| 3 | Fall of Constantinople | MA | NO | Ereig | 4 | 4 | **559.308** | 4 | 2026-05-08 |
| 4 | Donner Party | 19. | Ame | Ereig | 6 | 4 | **495.875** | 4 | 2025-08-21 |
| 5 | Reconquista | MA | Eur | Epoche | 11 | 5 | **329.288** ⚠ | 4 | 2025-12-26 |
| 6 | Siege of Vienna 1683 | FNZ | Eur | Ereig | 3 | 3 | **301.438** | 3 | 2026-07-10 |
| 7 | Terracotta Army | Ant | Asi | Person | 8 | 8 | **285.811** | 7 | 2025-09-26 |
| 8 | Al Capone | 20. | Ame | Person | 15 | 3 | **281.872** ⚠ | 3 | 2026-01-27 |
| 9 | Battle of Agincourt | MA | Eur | Ereig | 7 | 6 | **277.369** | 6 | 2025-11-27 |
| 10 | Black Death | MA | Eur | Ereig | 23 | 7 | **262.432** ⚠ | 7 | 2026-01-27 |
| 11 | Fall of Tenochtitlan | FNZ | Ame | Ereig | 3 | 3 | **198.000** | 3 | 2026-04-29 |
| 12 | Siege of Syracuse | Ant | Eur | Ereig | 4 | 3 | **193.907** | 3 | 2026-07-28 |
| 13 | Joan of Arc | MA | Eur | Person | 9 | 3 | **188.751** ⚠ | 3 | 2025-06-26 |
| 14 | Franklin Expedition | 19. | Eur | Ereig | 3 | 3 | **116.292** | 3 | 2025-09-16 |

⚠ = N2 ist Median des Messfensters, nicht aller Treffer → **Obergrenze**.

### 4.2 Gemessen, an einem Tor gescheitert (10)

| Thema | N1 roh | N1 ber | N3 | Ergebnis |
|---|---|---|---|---|
| Fourth Crusade | 3 | 2 | 2 | N3-Tor verfehlt (3. Treffer: Crusader-Kings-III-Gameplay) |
| Boudica | 3 | 2 | 2 | N3-Tor verfehlt (3. Treffer: Hindi-Filmerklärung) |
| Mansa Musa | 4 | 2 | 2 | N3-Tor verfehlt (stärkster Treffer: MacG-Podcast) |
| Christmas Truce 1914 | 5 | 2 | 2 | N3-Tor verfehlt (Sainsbury's-Werbereaktion, Sabaton-Songreaktion, Merz-Tagesnachricht) |
| Wilhelm Gustloff | 3 | 2 | 2 | N3-Tor verfehlt |
| Spartacus | 58 | 1 | 1 | N1-Tor verfehlt — Namensraum von der Starz-Serie belegt |
| Masada | 3 | 1 | 1 | N1-Tor verfehlt (Sonnenaufgangskonzert, Tourismusvideo) |
| Peasants Revolt 1381 | 1 | 1 | 1 | N1-Tor verfehlt |
| Crips and Bloods | 82 | 2/5 | 2 | **Fenster zu klein** — bei 82 Rohtreffern sagt ein Top-5-Fenster nichts |
| Battle of Stalingrad | 80 | 1/5 | 1 | **Fenster zu klein** — Top 5 sind Spielfilm, CoD-Gameplay, Museumsführung |

### 4.3 Gemessen, keine belegte Nachfrage unter dieser Phrase (7)

| Thema | N1 roh | Befund |
|---|---|---|
| Spanish Armada | 2 | beide Treffer „What If a Modern Destroyer/Submarine…" → 0 bereinigt |
| Battle of Gaugamela | 1 | einziger Treffer portugiesisch → 0 bereinigt |
| Antonine Plague | 0 | null Treffer über 100k |
| Kingdom of Kush | 0 | null Treffer |
| House of Wisdom | 0 | null Treffer |
| Siege of Baghdad 1258 | 0 | null Treffer |
| Tulsa Race Massacre | 0 | null Treffer |

### 4.4 Nur die Spitze gesichtet, nicht bereinigt erhoben (6)

Diese sechs haben belegbare Rohtreffer, aber **kein gültiges N2/N3**, weil die
volle Trefferliste nicht gezogen wurde. Sie sind **nicht** ausgeschlossen — sie
sind ungemessen und gehören in die nächste Runde.

| Thema | N1 roh | gesichtete Spitze |
|---|---|---|
| Pompeii | **47** | NOVA/PBS 986.540 (Gegenwarts-Vulkanrisiko, vermutlich raus); Isa por ahí 924.849 |
| Destruction of Carthage | **19** | Bodycam Carthage/Texas 311.223 (raus); Without History 230.212 |
| Battle of Thermopylae | **17** | HistoryMarche 1.580.460; Hindi-Video 1.090.825 (raus) |
| Bronze Age Collapse | 5 | Invicta 1.316.219; Predictive History 256.980 |
| Library of Alexandria | 4 | Mile-Higher-Podcast 261.237 (raus); ESOTERICA 235.168 |
| Battle of Cannae | 3 | **von der Auswertung ausgeschlossen** — Blindheit verletzt (§1.6) |

**Pompeii und Thermopylae sind die wahrscheinlichsten Nachrücker in die Top 10**
und der billigste nächste Messschritt.

### 4.5 Nicht erhoben (50)

Vollständig, damit die Lücke nachprüfbar ist. Über diese Themen sagt dieses
Dokument **nichts**:

*Antike:* Julius Caesar · Fall of Rome · Persian Empire.
*Mittelalter:* Hastings · Viking Age · Knights Templar · Hundred Years' War ·
Mongol Invasions of Japan · Byzantine Empire · Vlad the Impaler.
*Frühe Neuzeit:* Inca Empire · Thirty Years' War · Salem Witch Trials ·
Blackbeard · Great Fire of London · Suleiman the Magnificent · Oda Nobunaga ·
Zheng He · Middle Passage · Dutch East India Company · Siege of Malta ·
Lepanto · Gunpowder Plot · Dahomey · Ivan the Terrible.
*19. Jh.:* Napoleon (Russlandfeldzug) · Krakatoa · Taiping Rebellion ·
Indian Rebellion 1857 · Isandlwana · Scramble for Africa · Potato Famine ·
Whaleship Essex · Alamo · Charge of the Light Brigade · Opium Wars ·
Haitian Revolution · Congo Free State.
*20. Jh.:* Titanic · Shackleton/Endurance · Verdun · Gallipoli · Spanish Flu ·
Romanov-Erschießung · Siege of Leningrad · USS Indianapolis ·
Partition of India · Mau Mau Uprising · Armenian Genocide.

---

## 5. Phase D — was gestrichen wurde und warum

### D1 Stil (Anker `stil-anker-v1`, `d9ec37ca-e7aa-49c6-bebb-3c90339bd6b1`)

Gemalte Nachtszene, **eine** warme Lichtquelle, Figur ohne Blickkontakt.

**Gestrichen:**

- **Crips and Bloods** — der Grenzfall, den du ausdrücklich prüfen wolltest.
  **Urteil: trägt nicht.** Nicht wegen des Jahrhunderts, sondern wegen des
  Bildinventars: Die Nische ist ohne erkennbare Fahrzeuge, Straßenzüge und
  Kleidung der 1970er–90er nicht erzählbar, und ihre Bildsprache stützt sich
  auf Pressefotos. Beides schließt D1 ausdrücklich aus. Eine gemalte Nachtszene
  mit einer Laterne könnte *ein* Thumbnail tragen, aber keine Serie.
  *Gegenprobe im selben Jahrhundert:* **Al Capone trägt** — Speakeasy bei
  Nacht, eine Lampe, Hut, Rückenansicht; Fahrzeuge der 1920er lesen als
  historisch, nicht als Gegenwartstechnik. **Das 20. Jahrhundert ist also
  nicht pauschal ausgeschlossen; entscheidend ist, ob die Gegenwart im Bild
  auftaucht.**
- **Reconquista** — **bedingt gestrichen.** Als 800-Jahre-Epochenüberblick
  braucht das Thema eine Karte als Hauptmotiv, und Karten schließt D1 aus.
  Es bleibt in der Liste, weil es sich auf ein benanntes Einzelereignis
  verengen lässt: **Las Navas de Tolosa 1212** oder der Fall Granadas 1492.
  In dieser Verengung trägt der Nachtstil.
- **Battle of Stalingrad** — nicht wegen des Stils, sondern D1 *und* Messfenster:
  Ruinen bei Nacht mit Feuerschein trügen den Stil gut; der Namensraum ist
  aber von Spielfilmen und CoD-Gameplay belegt, sodass keine belastbare
  Nachfragemessung möglich war.

**Ausdrücklich nicht gestrichen, mit Begründung:**

- **Terracotta Army** — Statuen *haben keinen Blickkontakt*; unterirdische
  Grube, Fackel als einzige Lichtquelle. Der Anker passt hier besser als bei
  jedem anderen Thema der Liste.
- **Franklin Expedition** — arktische Polarnacht, Schiff im Eis, eine Laterne.
  Kein Diagramm nötig, keine Gegenwartstechnik.
- **Black Death** — Pestarzt mit Laterne in nächtlicher Gasse.
- **Donner Party** — Schneelager, ein Feuer, abgewandte Figuren.
- **Siege of Syracuse** — *bedingt.* Das ikonische Motiv (Archimedes'
  Brennspiegel) ist eine Tagszene. Die Belagerung selbst ist nachts erzählbar;
  wer den Brennspiegel als Aufhänger will, verlässt den Anker.

### D2 Rechte (Tor 1)

**Gestrichen:** keines der 14 bestandenen Themen braucht fremdes IP.

**Als Risiko markiert, nicht gestrichen:**

- **Al Capone** — Person der Zeitgeschichte, Nachfahren leben. Kein
  Rechteproblem für die Darstellung historischer Tatsachen, aber
  Sorgfaltspflicht bei Behauptungen über benannte Personen.
- **Crips and Bloods** — dieselbe Lage, verschärft: benannte lebende Personen.
  Bereits über D1 gestrichen.

**Ein Fund, der D2 auf Themenebene belegt:** *Spartacus* ist kein
Rechteproblem für uns (die Antike ist gemeinfrei), aber der **Namensraum**
gehört faktisch der Starz-Serie. Wer dieses Thema bespielt, konkurriert im
Suchergebnis mit einem laufenden Franchise. Das ist kein Rechte-, sondern ein
Auffindbarkeitsproblem — gehört aber in dieselbe Entscheidung.

### D3 Sättigungsverdacht (N1 > 60 **und** jüngster Treffer älter als 18 Monate)

**Kein einziges Thema löst die Marke aus.** Die beiden Kandidaten mit den
meisten Rohtreffern — Crips (82) und Stalingrad (80) — haben jüngste Treffer
von 2025, also weit innerhalb der 18 Monate. Genghis Khan liegt mit 60 exakt
auf, aber nicht über der Schwelle.

**Das ist ein Nullbefund und wird als solcher berichtet.** Eine Prüfung, die
bei 37 gemessenen Themen kein einziges Mal anschlägt, hat an diesen Daten
keine Trennkraft gezeigt (`irrtuemer.md` #4, in die andere Richtung gelesen).
Der vorregistrierte Sättigungstest ist damit **ungeprüft**, nicht *bestanden*.

---

## 6. Top 10 — belegte Nachfrage

Sortiert nach N2, bei Gleichstand nach N3. Die zwei stärksten Fremdvideos sind
**Vergleichsanker**, keine Vorbilder — sie belegen nur, dass das Thema bei
anderen getragen hat.

### 1 · Waterloo — „The Night Before Waterloo"
`N1 29 roh / 3 bereinigt · N2 600.711 ⚠ · N3 3 · N4 2025-05-17 (756.161)`
19. Jh. · Europa · Einzelereignis
**Stil D1: trägt.** Biwak in der Regennacht vor der Schlacht, brennendes
Hougoumont — eine Feuerquelle, abgewandte Figuren.
**Rechte D2: frei.**
⚠ Warnung: 26 der 29 Rohtreffer wurden nicht bereinigt; N2 ist eine Obergrenze.
Der stärkste Rohtreffer (1.348.897) ist ein Filmclip aus *Napoleon* (2023) —
der Namensraum ist teilweise vom Film besetzt.
Anker: Serious History *„Napoleon's Epic Final Battle | Battle of Waterloo
1815"* 756.161 (2025-05-17) · Battle Guide *„How A Farmhouse Ended An Empire"*
600.711 (2025-02-04)

### 2 · Genghis Khan — „The Night the Steppe Chose a Khan"
`N1 60 roh / 6 bereinigt · N2 575.725 ⚠ · N3 6 · N4 2025-11-26 (552.307)`
Mittelalter · Asien · Person
**Stil D1: trägt.** Steppenlager, ein Feuer, Reiterfigur von hinten.
**Rechte D2: frei.**
⚠ 60 Rohtreffer, Fenster 8 — N2 ist eine deutliche Obergrenze. Höchstes N3 der
Personen-Themen; die Nachfrage ist breit getragen.
Anker: Serious History *„The Worst Things Genghis Khan did to his Enemies"*
1.473.108 (2024-10-17) · Horses *„GENGHIS KHAN: The Peasant Who Conquered the
World"* 766.460 (2024-12-12)

### 3 · Fall Konstantinopels 1453 — „The Last Night of Rome"
`N1 4 roh / 4 bereinigt · N2 559.308 · N3 4 · N4 2026-05-08 (293.000)`
Mittelalter · Naher Osten · Einzelereignis
**Stil D1: trägt.** Nächtliche Belagerung, Fackeln auf den Theodosianischen
Mauern.
**Rechte D2: frei.**
**Sauberster Messwert der Top 3:** alle 4 Treffer bereinigt gesichtet, kein
Fenstereffekt. Jüngster Treffer erst 3 Monate alt.
Anker: Timeline HT *„The Fall of Constantinople 1453: The City Falls, An Era
Ends"* 1.166.655 (2025-02-17) · CTV BANGLA *„History of Muhammad Al Fatih…"*
825.617 (2024-10-16)

### 4 · Donner Party — „Eighty-Seven Went Into the Snow"
`N1 6 roh / 4 bereinigt · N2 495.875 · N3 4 · N4 2025-08-21 (143.172)`
19. Jh. · Amerika · Einzelereignis
**Stil D1: trägt am besten von allen.** Schneelager, ein Feuer, abgewandte
Figuren — der Anker beschreibt diese Szene fast wörtlich.
**Rechte D2: frei** (1846).
Vollständig bereinigt, kein Fenstereffekt. Zwei Spielfilme gestrichen.
Anker: The Lore Lodge *„Cannibals on The California Trail | The TRUE Story of
the Donner Party"* 1.175.915 (2024-09-03) · Footprints of The Frontier
*„The Donner Party: Cannibals on The California Trail"* 818.833 (2024-08-20)

### 5 · Reconquista → **Las Navas de Tolosa 1212**
`N1 11 roh / 5 bereinigt · N2 329.288 ⚠ · N3 4 · N4 2025-12-26 (140.379)`
Mittelalter · Europa · Epochenüberblick
**Stil D1: bedingt — nur in der Verengung.** Als 800-Jahre-Überblick braucht es
eine Karte (D1-Ausschluss). Als benannte Nachtschlacht trägt es.
**Rechte D2: frei.**
Drei Treffer wegen spanischer, französischer und indonesischer Titel gestrichen,
einer wegen Gegenwartspolitik.
Anker: History Mapped Out *„The Reconquista: The Victory of Christianity and
the Unification Of Spain"* 1.631.219 (2025-02-09) · Bellum et Historia
*„Battle of Las Navas de Tolosa 1212"* 494.154 (2025-08-30)

### 6 · Wiener Türkenbelagerung 1683 — „The Night Vienna Held"
`N1 3 roh / 3 bereinigt · N2 301.438 · N3 3 · N4 2026-07-10 (192.000)`
Frühe Neuzeit · Europa · Einzelereignis
**Stil D1: trägt.** Belagerungsfeuer vor der Stadtmauer bei Nacht.
**Rechte D2: frei.**
Vollständig bereinigt. **Jüngster Treffer der gesamten Liste** (vor einem
Monat, 192.000 Views) — das Thema ist aktiv und trägt weiterhin.
Anker: Мудреныч *„The Siege of Vienna"* 734.111 (2025-02-25) · Timeline HT
*„The Moment the Ottoman Empire Was Stopped in Europe"* 301.438 (2025-06-17)

### 7 · Terrakotta-Armee — „The Army That Was Never Meant to Be Seen"
`N1 8 roh / 8 bereinigt · N2 285.811 · N3 7 · N4 2025-09-26 (100.779)`
Antike · Asien · Person
**Stil D1: trägt hervorragend.** Grabgrube, Fackel, tausend Figuren **ohne
Blickkontakt** — der Anker ist hier wörtlich erfüllt.
**Rechte D2: frei.**
**Höchstes N3 (7) bei vollständiger Bereinigung — formal der bestbelegte
Wert der Liste.** Aber mit einem Vorbehalt, der ihn halbiert: **6 der 8 Treffer
sind Varianten desselben Titels** („Terracotta Army Mystery Solved in 2025,
And It's Not Good") von verschiedenen KI-Slop-Kanälen. Gemessen wurde damit
womöglich **eine Titelwelle, nicht ein Thema**. N3 = 7 unterschiedliche Kanäle
ist formal erfüllt, inhaltlich aber schwächer als die Zahl aussieht.
Anker: ЧТИВО *„The Terracotta Army: Why Archaeologists Fear Uncovering the
Tomb of Emperor Qin Shi Huang"* 726.282 (2024-12-27) · La mente curiosa
*„They've just decoded the inscriptions on the Terracotta Army"* 373.930
(2025-08-26)

### 8 · Al Capone — „The Night Chicago Belonged to Him"
`N1 15 roh / 3 bereinigt · N2 281.872 ⚠ · N3 3 · N4 2026-01-27 (281.381)`
20. Jh. · Amerika · Person
**Stil D1: trägt** — und beantwortet deine Grenzfallfrage positiv. Speakeasy
bei Nacht, eine Lampe, Hut von hinten. Fahrzeuge der 1920er lesen historisch.
**Rechte D2: Risiko markiert** — Person der Zeitgeschichte, lebende Nachfahren.
Gestrichen: ein Club-DJ-Set („Caribbean Thursdays at Al Capone") und ein
KI-Sammelvideo.
Anker: World View – History *„Eliot Ness vs. Al Capone – The Gangster
Chronicles"* 1.501.437 (2024-10-16) · Bloody Reports *„1928: The Deal With Al
Capone That Made Bumpy Johnson Untouchable"* 281.872 (2025-12-26)

### 9 · Azincourt 1415 — „The Mud at Agincourt"
`N1 7 roh / 6 bereinigt · N2 277.369 · N3 6 · N4 2025-11-27 (872.761)`
Mittelalter · Europa · Einzelereignis
**Stil D1: trägt.** Regennacht vor der Schlacht, Lagerfeuer, Schlamm.
**Rechte D2: frei.**
**Das robusteste Profil der Liste:** vollständig bereinigt, N3 = 6 bei nur
einem gestrichenen Treffer (dem Schlachtschiff *HMS Agincourt*), und der
**jüngste Treffer ist zugleich der stärkste** (872.761, vor neun Monaten).
Anker: Bellum et Historia *„Agincourt 1415 – The battle that changed Warfare
forever!"* 872.761 (2025-11-27) · Serious History *„Most Epic Upset in
Medieval History | Battle of Agincourt 1415"* 727.941 (2025-07-17)

### 10 · Schwarzer Tod — „The Lantern in the Empty Street"
`N1 23 roh / 7 bereinigt · N2 262.432 ⚠ · N3 7 · N4 2026-01-27 (246.767)`
Mittelalter · Europa · Einzelereignis
**Stil D1: trägt hervorragend.** Pestarzt mit Laterne, leere Gasse bei Nacht.
**Rechte D2: frei.**
⚠ 23 Rohtreffer, Fenster 8. N3 = 7 unter den acht stärksten — die Nachfrage ist
breit und von etablierten Kanälen getragen (History Hit, Dan Snow).
Anker: Discovery Future *„Ancient DNA Finally Reveals the REAL Origin of the
Black Death"* 1.635.482 (2025-08-04) · ElDiaQue *„The day the Black Death
began"* 350.233 (2024-12-16)

---

## 7. Plätze 11–14 (Reserve)

**Es sind nur vier, nicht zehn.** Von 37 gemessenen Kandidaten haben 14 beide
Tore bestanden; nach den Top 10 bleiben vier. Die Reserve auf zehn aufzufüllen
hieße, Themen aufzunehmen, die an N1 oder N3 gescheitert sind — das wäre
genau die nachträgliche Schwellenlockerung, die §1.3 ausschließt.

| # | Thema | N2 | N3 | Kurzbefund |
|---|---|---|---|---|
| 11 | **Fall von Tenochtitlán** | 198.000 | 3 | FNZ/Amerika. *Noche Triste* — der Stil trägt wörtlich („die traurige Nacht"). Vollständig bereinigt, jüngster Treffer April 2026. Stärkster Reservekandidat. |
| 12 | **Belagerung von Syrakus** | 193.907 | 3 | Antike/Europa. Vollständig bereinigt, jüngster Treffer **28.07.2026** — der aktuellste der Liste. Stil bedingt (Brennspiegel ist Tagmotiv). |
| 13 | **Jeanne d'Arc** | 188.751 | 3 | MA/Europa. Knapp bestanden: 6 von 9 Treffern gestrichen (Kostümbau-Videos, LEGO-Kinderkanal, koreanische Tagespolitik). |
| 14 | **Franklin-Expedition** | 116.292 | 3 | 19./Europa. N2 an der Messgrenze (Bodeneffekt, §1.3) — belastbar ist hier nur „drei unabhängige Kanäle über 100k", nicht die Höhe. Stil trägt hervorragend. |

**Realistische Nachrücker vor der nächsten Runde:** Pompeii (47 Rohtreffer) und
Thermopylae (17) aus Abschnitt 4.4 — beide ungemessen, beide mit einer Spitze
über 900.000 Views.

---

## 8. Phase F — Auswertung der Vorregistrierung

### 8.1 Spearman über alle bereinigt gemessenen Kandidaten (n = 14)

Kodierung wie in §1.4 vorregistriert. Cannae ausgeschlossen (§1.6).

**Rechenweg:** Spearman als Pearson-Korrelation auf Durchschnittsrängen. Die
gängige Kurzformel `1 − 6·Σd²/n(n²−1)` ist bei Bindungen **ungültig**, und hier
gibt es viele (Typ hat nur drei besetzte Stufen, Region vier). Eine erste
Handrechnung mit der Kurzformel ergab +0,04 / +0,16 / −0,28 und war damit bei
zwei von drei Achsen irreführend — insbesondere beim Vorzeichen des Typs.
Gültig sind die Werte unten.

| Achse | vorregistrierte Erwartung | **Rho** | \|Rho\| ≥ 0,30 | Ergebnis |
|---|---|---|---|---|
| **Typ** (primär) | Ereignis > Person > Institution > Überblick | **−0,12** | nein | **widerlegt** |
| **Epoche** (sekundär) | 20. > 19. > FNZ > MA > Antike | **+0,12** | nein | **nicht bestätigt** |
| **Region** (tertiär) | Europa > Amerika > NO > Asien > Afrika | **−0,42** | **ja** | **widerlegt, Effekt oberhalb der Schwelle in der Gegenrichtung** |

### 8.2 Was das heißt

**Die primäre Erwartung ist widerlegt.** Ich hatte vorab geschrieben, der Typ
trenne am stärksten, weil ein benanntes Einzelereignis einen geschlossenen
Bogen mitliefert. Rho = **−0,12** ist rechnerisch nichts — und was da ist, zeigt
schwach in die *entgegengesetzte* Richtung. Der einzige Epochenüberblick der
bestandenen Liste (Reconquista) landet auf **Platz 5 von 14**; er hätte nach
meiner Hypothese am Ende stehen müssen.

**Die Epoche trennt nicht.** Rho = +0,12, weit unter der Schwelle.

**Die Region ist der einzige Befund oberhalb der Schwelle — und er widerlegt
die Vorregistrierung, statt sie zu bestätigen.** Rho = **−0,42** bei einer
Kodierung, die Europa als höchsten Wert setzt, heißt: In der bestandenen Liste
liegen die europäischen Themen systematisch am *unteren* Ende des Medians. Vorn
stehen die beiden asiatischen (Genghis Khan Platz 2, Terrakotta-Armee Platz 7)
und das nahöstliche Thema (Konstantinopel Platz 3); von den acht europäischen
Themen liegen fünf in der unteren Hälfte.

Nach der in §1.4 vorregistrierten Leseregel — *„Ein negatives Rho widerlegt die
vorregistrierte Richtung und bestätigt nicht etwa eine umgekehrte"* — ist das
**kein** Beleg für „mach asiatische Themen". Es ist ein Beleg dafür, dass meine
Begründung („englischsprachiges Publikum, europazentrierter Schulkanon")
falsch war.

**Ein wahrscheinlicher Mechanismus, ausdrücklich als Hypothese markiert:**
Europa ist im Vorrat mit 40 von 87 überrepräsentiert und im gemessenen Korpus
mit 8 von 14. Wo viele Kanäle dasselbe bespielen, verteilt sich das Publikum;
wo wenige es tun, sammelt es sich. Das wäre ein **Wettbewerbs-, kein
Nachfrageeffekt** — und er würde erklären, warum ausgerechnet die Region
trennt. **Nicht gemessen, nicht behauptet.** Prüfauftrag Nr. 1 für die nächste
Runde: Kanalzahl je Thema erheben und gegen N2 rechnen.

### 8.3 Der eigentliche Befund

> **Keine Achse trennt in der vorhergesagten Richtung. Die Top 10 ist deshalb
> eine Liste belegter Einzelthemen ohne verallgemeinerbare Regel.**

Es gibt nach diesen Daten keine Aussage der Form „mach Einzelereignisse" oder
„mach 20. Jahrhundert" oder „bleib in Europa" — die letzte ist sogar aktiv
widerlegt. Jedes der 14 Themen steht für sich.

Der Regionseffekt (−0,42) ist der einzige, der die Schwelle reißt. Er beruht
auf **n = 14 mit vier besetzten Regionsstufen, davon zwei mit je zwei Themen**.
Daraus eine Regel zu machen, wäre Mustersuche im Rauschen — genau das, wovor
`irrtuemer.md` #5 warnt. Er ist als **Hypothese für die nächste Messung**
festgehalten, nicht als Befund.

Das fügt sich in den Bestand: Der 429-Video-Blindtest fand kein trennendes
Oberflächenmerkmal *innerhalb* einer Themenbandbreite. Diese Messung findet
kein trennendes Klassifikationsmerkmal *zwischen* Themen, das in die
vorhergesagte Richtung zeigt. Zwei unabhängige Erhebungen, beide vorregistriert,
beide negativ.

---

## 9. Was diese Liste NICHT sagt

**Sie sagt nicht, dass diese Themen für deinen Kanal funktionieren werden.**
Sie sagt: Diese Themen haben bei **anderen** Kanälen **mehrfach unabhängig**
Publikum über 100.000 Views getragen, gemessen am 12.08.2026 im NexLev-Katalog.
Das ist eine Aussage über die Vergangenheit fremder Kanäle.

**Der 429-Video-Blindtest steht dem nicht entgegen** — er misst etwas anderes.
Er hat gezeigt, dass sich *innerhalb* einer Themenbandbreite aus
Oberflächenmerkmalen (Titel, Thumbnail, Tempo, Quellenarbeit, Themenwahl) nicht
vorhersagen lässt, welches Video läuft: 0 von 7 Merkmalen trennten. Diese
Messung vergleicht **Nachfrageniveaus zwischen Themen**, nicht Varianz
innerhalb eines Themas. Beide Befunde können gleichzeitig wahr sein: Ein Thema
kann belegt Publikum haben **und** das einzelne Video darüber trotzdem
unvorhersagbar sein. Genau das ist die Sichtbarkeitsgrenze aus `kriterien.md`
Punkt 3.

**Weitere Grenzen, die aus dieser Messung folgen:**

1. **Ein niedriges N1 ist kein Gegenbeweis.** Siehe Abschnitt 3: Die Spanische
   Armada hat nach dieser Messung null belegte Nachfrage. Das ist mit Sicherheit
   falsch und heißt nur, dass die Phrase nicht misst.
2. **Sieben der vierzehn N2-Werte sind Obergrenzen**, keine Mediane. Die
   Rangfolge zwischen ⚠-Themen und sauber gemessenen ist deshalb nicht
   belastbar. Konkret: Waterloo (Platz 1) ist ein Median aus 3 von 29 Treffern;
   Agincourt (Platz 9) ist ein Median aus 6 von 7. **Agincourt ist der
   verlässlichere Wert, obwohl er acht Plätze tiefer steht.**
3. **Views sind nicht Umsatz.** Diese Messung sagt nichts über RPM,
   Monetarisierung oder Ertrag je Arbeitsstunde — die fünf Kernzahlen aus
   `kriterien.md` sind hier **nicht** erhoben.
4. **Tor 2 (Katalogwirkung) ist auf Themenebene ungeprüft.** Der
   vorgesehene Test am ältesten Treffer wurde nicht durchgeführt.
5. **50 von 87 Kandidaten sind ungemessen.** Jedes von ihnen könnte in die
   Top 10 gehören. Die Liste ist eine Rangfolge der *gemessenen* Themen, nicht
   der besten.

---

## 10. Sichtbarkeitsgrenze

| Größe | Basis |
|---|---|
| N1, N2, N3, N4 | **Schnappschuss** (eine Messung, 12.08.2026) — keine Zeitreihe |
| N2 bei 7 von 14 Themen | **Obergrenze**, nicht Median (Messfenster < N1_roh) |
| N3 | gemessen, aber nur innerhalb des Messfensters |
| Katalogtest Tor 2 | **nicht erhoben** |
| Monetarisierung, RPM, $/h | **nicht erhoben** — nicht Gegenstand dieser Messung |
| Stilurteil D1 | **Setzung**, kein Messwert — Einschätzung gegen den Anker |

Von außen prinzipiell unsichtbar bleiben Retention, CTR, Impressionen,
Traffic-Quellen und echte Umsätze. Diese Messung beurteilt **Themennachfrage
in der Vergangenheit fremder Kanäle** — über den Erfolg eines eigenen Videos
sagt sie nichts (`kriterien.md`, Sichtbarkeitsgrenze).

**Basislinie:** `bewertungen/daten/themen-messung-2026-08.tsv`, datiert
12.08.2026. Die nächste Messung mit identischen Filtern ergibt eine echte
Zeitreihe — dann wird erstmals prüfbar, ob N2 je Thema stabil ist oder ob diese
ganze Rangfolge ein Schnappschussartefakt war.
