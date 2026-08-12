# Kriterien v2 — VORSCHLAG (nicht in Kraft)

> Status: **Entwurf aus der Methodikprüfung vom 12.08.2026**
> (`pruefung-methodik.md`, dort die Begründung je Änderung).
> Verbindlich bleibt bis zur Freigabe `kriterien.md`. Dieser Entwurf
> überschreibt nichts — er steht daneben, damit v1 und v2 an der nächsten
> Nischenprüfung parallel gefahren und verglichen werden können.

Die wichtigste Änderung ist keine inhaltliche, sondern eine strukturelle:
**Es gibt keine Note 1–10 mehr.** Vier Prüfungen ergaben 6/7/7/7 — eine
Skala, die nicht trennt, und eine Zahl, die entgegengesetzte Befunde auf
denselben Wert abbildet. Das Ergebnis einer Prüfung ist stattdessen:

```
ERGEBNIS = drei Tore (bestanden / gescheitert / nicht prüfbar)
         + fünf Kernzahlen (gemessen, mit Sichtbarkeitsgrenze)
         + Rangplatz nach Ertrag je Arbeitsstunde
         + die eine benannte Restschwäche
```

Empfehlung nur, wenn alle drei Tore bestanden sind UND der Rangplatz sie
trägt. „Nicht prüfbar" ist ein zulässiges Torergebnis und heißt: warten oder
Basislinie anlegen — es heißt **nicht** rot.

---

## Die drei Tore (K.-o.)

### Tor 1 — Rechtegrundlage *(neu)*

Woraus besteht das Material, und darf man es monetarisiert nutzen?

- Originaltext gemeinfrei? **Konkrete Übersetzung** gemeinfrei?
- Fremd-IP (Franchises, fremde Aufnahmen, Vorlesungen) = gescheitert, auch
  wenn Konkurrenzkanäle damit verdienen — geduldete Verletzung ist keine
  Grundlage.
- „Freies Material" ist nicht „freier Text" (irrtuemer #8): Nur ein konkret
  benanntes, abrufbares Werk zählt; Fundort mit Link und gemessenem Umfang.

### Tor 2 — Katalogwirkung *(aus K4, geschärft)*

Verdient ein Kanal weiter, wenn er nicht hochlädt?

- Mindestens ein Kanal der Nische mit ≥ 6 Wochen Uploadpause: Views/Monat
  **und** Modellumsatz während der Pause flach oder steigend.
- Neu: zusätzlich prüfen, ob die Katalog-Views den Umsatz tragen, wenn
  Neuvideo-Mediane fallen (quack-doc-Muster). Katalogwirkung ist die
  ökonomische Kernfrage dieses Geschäftsmodells — deshalb Tor, nicht Punkt.

### Tor 3 — Machbarkeit relativ zur eigenen Pipeline *(ersetzt K6-K.-o.)*

Nicht mehr „über 2 Uploads/Woche = rot". Stattdessen:

```
Median-Kadenz der Erfolgskanäle × Menschenstunden je Video
    ≤ verfügbare Wochenstunden?
```

Dazu wie bisher: Kann das Bild loopen, oder braucht jede Sekunde neues
Material? Und neu: Credits je Video × Kadenz gegen das Credit-Budget.
Eine Nische scheitert hier nur, wenn die eigene Kapazität die belegte
Erfolgskadenz nicht hergibt — nicht, weil eine universelle Zahl überschritten
ist. *(Herkunft der alten Schwelle „2/Woche": Setzung, nie aus Daten
abgeleitet — in den Gründungsdaten lagen alle Abstürzer darunter.)*

---

## Die fünf Kernzahlen (Pflichtmessungen, kein Punktesystem)

| # | Kernzahl | Regel | Herkunft der Schwellen |
|---|---|---|---|
| Z1 | **Ertrag je Arbeitsstunde** | `Monatsumsatz / (h je Video × Videos je Monat)`. Rangliste über alle geprüften Nischen; > 300 $/h grün, 100–300 gelb, < 100 rot | Bänder: Setzung (kriterien.md v1) |
| Z2 | **RPM, gerechnet** | IMMER `Umsatz / Views × 1000`, NIE das rpm-Feld. Diagnosegröße, kein Urteil: erklärt, *warum* Z1 ist, wie es ist | Regel: 3× reproduziert |
| Z3 | **Top-3-Anteil** | ab 20 Videos: Anteil der drei größten Videos an den Gesamtviews. < 35 % getragen, > 50 % Einzeltreffer | Schwellen: geeicht an G2 (n = 6), Richtung im Rückwärtstest bestätigt (n = 12, Spearman −0,46) |
| Z4 | **Monetarisierungsquote, live** | nur `check_channel_monetization` (bypassCache). Katalog-„nein" = **unbekannt**, zählt weder als ja noch als nein. Modellumsatz nicht monetarisierter Kanäle ist kontrafaktisch | Teil 0 der Prüfung: 7 von 11 Katalog-„nein" falsch |
| Z5 | **Videolänge & Watchtime-Produktion** | Ø Länge und `Länge × Kadenz` (Stunden je Woche) je Erfolgskanal. Lange Videos bei niedriger Kadenz können Drittel-RPM überkompensieren | Gates-Befund, Sleepy-Monk-Lauf |

*(v1-K3 „Ertrag je Video" entfällt — in Z1 enthalten, Spearman 0,71.
v1-K9 Geografie wird Fußnote von Z2: sie erklärt den RPM, sonst nichts.)*

## Nachfrage-Beleg (ersetzt K1)

Mindestens **3 unabhängige, live monetarisierte Kanäle mit ≥ 1.000 $/Monat
Modellumsatz**, davon mindestens einer mit ≥ 12 Monaten sichtbarer
Uploadhistorie. Der Outlier-Score ist Suchwerkzeug, kein Beleg — er adelt
Einzeltreffer (Lorevia 13,83 → 14 $/Monat) und hängt an NexLevs Kuration.
„Unabhängig" heißt: nicht erkennbar derselbe Betreiber.

## Haltbarkeit (ersetzt K5) — nur mit Zeitreihe

- Bewertbar erst ab **18 Monaten sichtbarer Historie** eines Kanals; darunter
  ausdrücklich **„nicht prüfbar"** — niemals automatisch rot.
- Maß: **Quartals-Mediane der Views neuer Videos** (wie g2-haltbarkeit),
  nicht das Datum des meistgesehenen Einzelvideos. Ein Kanal gilt als
  haltbar, wenn das aktuelle Halbjahres-Niveau ≥ 50 % seines besten
  Halbjahres liegt — Schwelle: Setzung, an Historically/quack doc/HMO geeicht.
- Immer gegen Tor 2 lesen: fallende Neuvideo-Mediane bei tragendem Katalog
  sind ein anderes Urteil als fallende Katalog-Views.

## Pflichtabschnitt „Sichtbarkeitsgrenze"

Jede Bewertung endet mit einer Tabelle: je Kernzahl **Zeitreihe /
Schnappschuss / Modellwert**, plus die Liste dessen, was von außen prinzipiell
unsichtbar ist (Retention, CTR, Impressionen, echte Umsätze). Dazu wird je
Prüfung eine **datierte Basislinien-Datei** committet (Kanal, Videoliste,
Views, Datum — Muster: `regeln/daten/g2-videos.tsv` im explainer-Repo), damit
die nächste Prüfung eine echte Zeitreihe hat und das Verfahren erstmals
kalibrierbar wird.

## Schwellenherkunft-Pflicht

Jede Schwelle in diesem Dokument trägt ihre Herkunft (gemessen an n = X, oder
Setzung). Eine Schwelle ohne Herkunftsangabe ist ungültig. Wer eine Schwelle
an Daten eicht, darf sie nicht an denselben Daten als bestätigt ausweisen.

---

## Übergang

Nächste Nischenprüfung **doppelt fahren**: v1-Note und v2-Ausgabe
nebeneinander, Abweichungen dokumentieren. Erst danach entscheiden, ob v2
`kriterien.md` ersetzt. Diese Datei ist bis dahin ein Vorschlag — genau wie
ihre Schwellen.
