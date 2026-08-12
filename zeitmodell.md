# Zeitmodell — Menschenstunden je Video

> Angelegt am 12.08.2026, weil Tor 3 der aktiven Methodik
> (`kriterien.md`) und die Kernzahl Z1 beide auf einer Zahl stehen, die
> **nirgends im Repo ausgeschrieben war**: den Menschenstunden je Video.
> Diese Datei nennt sie, zerlegt sie, und weist je Bestandteil die Herkunft
> aus (Schwellenherkunft-Pflicht, `kriterien.md`).

---

## Teil 1 — Was tatsächlich gerechnet wurde (Rückrechnung)

Keine Bewertung hat den verwendeten Stundenwert je Kanal genannt. Er lässt
sich aber aus den veröffentlichten Tabellen zurückrechnen:
`h je Video = (h/Monat) ÷ (Kadenz × 4,33)`, gegengeprüft über
`Umsatz ÷ ($/h) ÷ (Kadenz × 4,33)`. Beide Wege stimmen auf ±0,01 h überein.

Quelle: `bewertungen/einschlaf-freie-texte.md`, „Kriterium 7 im Querschnitt".

| Kanal | Unterrichtung | Videos/Mo | **h je Video (rückgerechnet)** |
|---|---|---|---|
| Bedtime & Historian | Geschichte | 13,47 | **1,00** |
| Sleepy History Channel | Geschichte | 8,62 | **1,00** |
| Silence of the Earth | Geschichte | 7,40 | **1,00** |
| Sleepy Time Historian | Geschichte | 33,08 | **0,75** |
| Gates of Imagination | Literatur | 3,46 | **1,00** |
| Story Classics | Literatur | 0,22 | **0,99** |
| Classic Audiobooks w/ Elliot | Literatur | 3,98 | **1,00** |
| Midnight Lorekeeper | Mythos/Lore | 7,75 | **0,75** |
| Dreams of Olympus | Mythos/Lore | 1,13 | **0,98** |
| Sleepy Monk | Östl. Weisheit | 12,60 | **0,75** |
| Midnight Monk | Östl. Weisheit | 13,03 | **0,75** |
| SleepNomad | Philosophie | 11,21 | **1,00** |
| Sleepy Philosophy | Philosophie | 19,70 | **1,00** |

### Die dokumentierte Regel beschreibt diese Rechnung nicht

`einschlaf-freie-texte.md` gibt als Regel an: *„0,75 h bei KI-Skript-Kanälen,
1,0 h bei Hörbuchkanälen"*. Angewandt wurde sie auf **4 von 13** Kanälen.
Neun KI-Skript-Kanäle wurden mit 1,0 h gerechnet — darunter drei der vier
Geschichte-Kanäle, deren Textquelle dieselbe Datei als *„frei erfundene
Fragestellungen. Kein Werk, keine Quelle, reines Skript"* einordnet.

Am schärfsten innerhalb **einer** Unterrichtung: Bedtime & Historian,
Sleepy History Channel und Silence of the Earth bekamen 1,0 h,
Sleepy Time Historian 0,75 h — vier strukturgleiche KI-Skript-Schlafkanäle,
zwei verschiedene Stundenwerte, kein genannter Grund.

### Was die Wahl bewegt

| Wirkung | Beleg |
|---|---|
| **Eine Ampel kippt** | Sleepy Time Historian: 131 $/h (gelb) bei 0,75 h → **98 $/h (rot)** bei 1,0 h. Die Grenze liegt bei 100 $/h. |
| **Rangplätze tauschen** | Bei einheitlich 1,0 h fällt Midnight Lorekeeper (426 → 318) unter Dreams of Olympus (329 → 323); bei einheitlich 0,75 h steigt SleepNomad (221 → 295) über Sleepy Monk (277) und Midnight Monk (259). |
| **Platz 1 und 2 der Gesamtrangliste sind nicht getrennt** | Bedtime & Historian 853 $/h gegen Gates of Imagination 837 $/h = **1,9 % Abstand**. Beide wurden mit 1,0 h gerechnet. Der Rang tauscht, sobald ein Geschichte-Video **2 % mehr** Menschenarbeit kostet als ein Hörbuch-Video. |

Die README-Aussage „die Rangfolge ist robuster als die Beträge" gilt also nur
gegen eine *gleichmäßige* Verschiebung des Niveaus — nicht gegen das
*Verhältnis* zwischen den Formaten, und genau darauf standen die Ränge.

### Der nie genannte vierte Wert

`bewertungen/history-explainer.md` führt Z1 mit *„Ink Explainer ~735 $/h"* und
der Fußnote „Stunden je Video geschätzt", ohne Zahl. Rückgerechnet aus den in
derselben Datei stehenden Werten (9.560 $/Monat, 0,74 Uploads/Woche):

```
h/Monat = 9.560 ÷ 735 = 13,01     Videos/Monat = 0,74 × 4,33 = 3,20
h je Video = 13,01 ÷ 3,20 = 4,06
```

**Rund 4 Stunden je Video** — das Fünffache des Schlaf-Formats, nie
ausgeschrieben. *(Vorbehalt: Der 735-$-Wert stammt aus der v1-Erhebung; falls
er auf einem älteren Umsatzstand beruht, erbt diese Rückrechnung den Fehler.)*

**Bilanz über das ganze Repo:** vier verschiedene Stundenwerte im Umlauf —
0,33 h, 0,75 h, 1,0 h und ~4,06 h. Der einzige, der je ausgeschrieben wurde,
ist 0,33 h (Bibel-Schlaf, „~20 min") — ausgerechnet in der Nische, für die Z1
gar nicht gerechnet wurde. Genannt wo unbenutzt, unbenannt wo entscheidend.

---

## Teil 2 — Das Zeitmodell

**Grundregel: Tor 3 fragt nach der *eigenen* Pipeline.** Geschätzte Stunden
fremder Kanäle beantworten die Frage nicht — sie sind eine Vermutung über
deren Produktion, nicht eine Messung der eigenen Kapazität. Für Tor 3 **und**
für Z1 gilt deshalb: Stunden immer aus der eigenen Pipeline.

Das Repo enthält genau **einen** Eigen-Pipeline-Wert: die dokumentierte
BibelTube-Pipeline mit **~20 min je Video** (Auswahl + Aussprache-QA, Bild
loopt). Er ist der Anker; alle anderen Formate werden als Delta dagegen
gesetzt.

| Format | Zerlegung | **h je Video** | Herkunft |
|---|---|---|---|
| **Bibel-Rezitation** (Loop, fester Kanon) | Abschnittsauswahl 5 · Aussprache-QA 5 · Zusammenbau/Export 5 · Titel+Upload 5 | **0,33** (20 min) | **dokumentiert** (BibelTube-Pipeline) |
| **Gemeinfreie Literatur** (Loop, fremder Langtext) | Anker 20 · Werkauswahl + Rechteprüfung Original/Übersetzung 10 (irrtuemer #10) · Textbeschaffung + Bereinigung, Kapitelmarken 10 · erweiterte Aussprache-QA fremder Eigennamen 5 | **0,75** (45 min) | Anker dokumentiert, **Delta Setzung** |
| **KI-Skript-Langform** (Loop, generiertes Skript) | Anker 20 · Themen-/Winkelwahl 5 · Skriptlauf + Stichprobendurchsicht 15 · Faktenstichprobe 5 | **0,75** (45 min) | Anker dokumentiert, **Delta Setzung** |
| **Kurzform-Eigentext** (Morgengebet, 2.500 Wörter selbst) | Anker 20 · Text schreiben und redigieren 40 | **1,0** (60 min) | Anker dokumentiert, **Delta Setzung** |
| **Explainer** (Bild loopt **nicht**, jede Sekunde neues Material) | kein Anker anwendbar — Materialbeschaffung und Schnitt dominieren | **~4,06** | **rückgerechnet** aus dem v1-Wert (oben) |

Dass gemeinfreie Literatur und KI-Skript auf denselben Wert fallen, ist kein
Zufall der Zuweisung, sondern der bereits protokollierte Befund aus
`einschlaf-freie-texte.md`: *„ein KI-Skript kostet ähnlich wenig Menschenarbeit
wie eine Textauswahl"*. Renderzeit von TTS und Export ist Maschinenzeit und
zählt nicht mit; gezählt ist nur betreute Arbeit.

**Wie dieses Modell zu widerlegen ist.** Alle Deltas sind Setzungen. Sie
werden geprüft, indem drei eigene Videos je Format mit der Stoppuhr entlang
der obigen Zerlegung gemessen und als datierte Basislinie committet werden
(`kriterien.md`, Pflichtabschnitt Sichtbarkeitsgrenze). Bis dahin trägt jede
$/h-Zahl und jedes Tor-3-Ergebnis diesen Vorbehalt sichtbar mit.

---

## Teil 3 — Die Zeitseite von Tor 3

### Median-Kadenz: zwei dokumentierte Werte sind keine Mediane

Tor 3 verlangt die **Median-Kadenz der Erfolgskanäle**. Nachgerechnet:

| Unterrichtung | Kadenzen sortiert | Median | dokumentiert | |
|---|---|---|---|---|
| Geschichte/Wissenschaft | 1,71 · 1,99 · 3,11 · 7,64 | **2,55** | 3,11 | **falsch** |
| Mythos/Lore | 0,26 · 0,91 · 1,79 · 2,58 | **1,35** | 1,79 | **falsch** |
| Gemeinfreie Literatur | 0,05 · 0,80 · 0,92 | 0,80 | 0,80 | ok |
| Östliche Weisheit | 2,13 · 2,91 · 3,01 | 2,91 | 2,91 | ok |
| Philosophie/Stoa | 2,59 · 3,44 · 4,55 | 3,44 | 3,44 | ok |

Beide Fehler liegen in den Gruppen mit **geradem n**: statt des Mittels der
beiden mittleren Werte wurde der obere der beiden genommen. Die davon
abhängigen v1-Ampeln kippen nicht (2,55 liegt weiter über 2, 1,35 weiter
darunter) — aber beide Zahlen gehen jetzt in Tor 3 ein und waren falsch.

### Kapazitätsbedarf je Nische

`Median-Kadenz × h je Video`. Die verfügbaren Wochenstunden sind
**ausdrücklich offen gelassen** (Betreiberentscheidung, 12.08.2026); das
Torergebnis ist deshalb eine **Schwelle**, kein „bestanden":

| Nische | Median-Kadenz | h/Video | **h/Woche** | h/Monat | Tor 3, Zeitseite |
|---|---|---|---|---|---|
| Bibel-Schlaf | 0,50 | 0,33 | **0,17** | 0,7 | bestanden ab 0,2 h/Woche |
| Gemeinfreie Literatur | 0,80 | 0,75 | **0,60** | 2,6 | bestanden ab 0,6 h/Woche |
| Mythos/Lore | 1,35 | 0,75 | **1,01** | 4,4 | bestanden ab 1,0 h/Woche |
| Geschichte/Wissenschaft | 2,55 | 0,75 | **1,91** | 8,3 | bestanden ab 1,9 h/Woche |
| Östliche Weisheit | 2,91 | 0,75 | **2,18** | 9,5 | bestanden ab 2,2 h/Woche |
| Philosophie/Stoa | 3,44 | 0,75 | **2,58** | 11,2 | bestanden ab 2,6 h/Woche |
| History-Explainer | 0,74 | 4,06 | **3,00** | 13,0 | bestanden ab 3,0 h/Woche |
| Morgengebet | **nicht erhoben** | 1,0 | — | — | **nicht prüfbar** — nur die Kadenz fehlt noch; bei täglichem Upload wären es 7,0 h/Woche |

**Der wirtschaftlich wichtigste Punkt dieser Tabelle:** Die teuerste Nische
der Liste ist nicht die mit der höchsten Kadenz, sondern die mit der
niedrigsten — History-Explainer verlangt bei 0,74 Uploads/Woche mehr
Wochenstunden als Philosophie/Stoa bei 3,44. Der Kadenz-K.-o. aus v1 hätte
genau falsch herum sortiert (irrtuemer #11), und die Zeitseite von Tor 3
zeigt, warum: Nicht die Uploadzahl kostet Zeit, sondern die Frage, ob das
Bild loopt.

---

## Teil 4 — Die Creditseite von Tor 3

**Credit-Budget: 50–200 $/Monat** (Betreiberangabe, 12.08.2026). Daraus folgt
je Nische, was ein einzelnes Video an Credits kosten darf —
`Budget ÷ Videos je Monat`:

| Nische | Videos/Monat | **erlaubte Credits je Video** |
|---|---|---|
| Bibel-Schlaf | 2,17 | 23,09 – 92,38 $ |
| History-Explainer | 3,20 | 15,60 – 62,42 $ |
| Gemeinfreie Literatur | 3,46 | 14,43 – 57,74 $ |
| Mythos/Lore | 5,85 | 8,55 – 34,21 $ |
| Geschichte/Wissenschaft | 11,04 | 4,53 – 18,11 $ |
| Östliche Weisheit | 12,60 | 3,97 – 15,87 $ |
| Philosophie/Stoa | 14,90 | 3,36 – 13,43 $ |
| Morgengebet | nicht erhoben | **nicht prüfbar** |

Gegenzulesen mit der Produktionsfrage aus `kriterien.md`: Bei den
Loop-Formaten fällt der Credit-Aufwand einmalig je Video (oder wird zwischen
Videos wiederverwendet) und passt in jede Spalte dieser Tabelle. Beim
History-Explainer braucht **jede Sekunde neues Material** — 15,60 $ je Video
am unteren Rand des Budgets ist die Zahl, an der diese Nische auf der
Creditseite scheitern kann. **Gemessen ist dieser Aufwand nicht**; die
tatsächlichen Credits je Video sind für keine Nische erhoben und bleiben
Prüfauftrag.

**Torergebnis Creditseite: für keine Nische abgeschlossen** — das Budget steht
jetzt, die Credits je Video nicht.

---

## Trennung gemessen / abgeleitet / gesetzt / unbekannt

**Gemessen:** Kadenzen, Umsätze, Videozahlen (NexLev, 11.–12.08.2026, in den
Bewertungen belegt); die 20-min-Angabe der BibelTube-Pipeline (eigene,
dokumentierte Pipeline); Credit-Budget (Betreiberangabe).

**Abgeleitet:** alle rückgerechneten h-je-Video-Werte aus Teil 1; die
korrigierten Mediane; Kapazitätsbedarf und erlaubte Credits je Video.

**Gesetzt:** sämtliche Deltas des Zeitmodells in Teil 2 (Minutenwerte je
Arbeitsschritt) — prüfbar per Stoppuhr an drei eigenen Videos je Format,
bisher nicht geprüft.

**Unbekannt:** die tatsächlichen Menschenstunden der Fremdkanäle (waren es nie
anders); die Credits je Video in allen Nischen; die verfügbaren Wochenstunden
(bewusst offen gelassen — deshalb Schwellenform statt Urteil).
