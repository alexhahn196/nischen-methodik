# Kriterien v1 — die 9 Prüfpunkte jeder Nischenprüfung

> **Stand bis 11.08.2026. Abgelöst durch v2, siehe `pruefung-methodik.md`.
> Wird bei der nächsten Nischenprüfung parallel mitgefahren, um v2 zu
> kalibrieren.** Der Inhalt unten ist unverändert die Fassung vom 11.08.2026.

Diese Liste ist verbindlich. Jede Nischenprüfung in diesem Repo arbeitet sie
vollständig ab, in dieser Reihenfolge, mit gemessenen Zahlen.
Was nicht gemessen wurde, wird als **geschätzt** oder **unbekannt** markiert —
nie als Befund verkauft.

---

## 1. Nachfrage

Mindestens **3 Kanäle mit outlierScore >= 2**.

Ein einzelner starker Kanal ist kein Nachweis, dass die Nische trägt — er ist
ein Nachweis, dass dieser eine Kanal trägt. Drei unabhängige Kanäle oberhalb
der Schwelle zeigen, dass die Nachfrage nicht an einer Person hängt.

---

## 2. RPM

**IMMER Umsatz geteilt durch Views rechnen. NIE das `rpm`-Feld nehmen.**

Im `rpm`-Feld steht der Werbe-RPM auf *monetarisierten Wiedergaben*. Das ist
nicht der Betrag, den der Kanal je 1.000 Gesamtviews verdient — der Faktor
liegt bei **5 bis 7 zu hoch**.

```
RPM_real = Monatsumsatz / (Views pro Monat / 1000)
```

Belegfall siehe `irrtuemer.md`: The Sleep Bible meldet 26,53 $, real sind es
3,90 $.

---

## 3. Ertrag je Video und Monat

```
Ertrag je Video = Monatsumsatz / Videoanzahl im Katalog
```

Diese Zahl entscheidet, ob ein Katalog überhaupt lohnt. Ein Kanal mit
2.000 $/Monat auf 25 Videos (80 $/Video) und einer mit 2.000 $/Monat auf
2 Videos (1.000 $/Video) sind wirtschaftlich verschiedene Geschäfte.

---

## 4. KATALOGWIRKUNG *(K.-o.-Kriterium)*

**Verdient ein Kanal weiter, wenn er nicht hochlädt?**

Nachweis an **mindestens einem Kanal mit >= 6 Wochen Uploadpause**:
steigen Abos und Views trotz Pause weiter, halten sie, oder fallen sie?

Ohne diesen Nachweis ist die Nische ein Job, kein Katalog. Rot hier ist ein
K.-o.

---

## 5. HALTBARKEIT

**Liegt der Views-Gipfel etablierter Kanäle im laufenden Jahr oder früher?**

- Gipfel im laufenden Jahr → grün
- Gipfel im **1.–2. Lebensjahr** des Kanals → **rot**

Ein Gipfel im ersten oder zweiten Lebensjahr bedeutet: Der Kanal wurde von
einer Welle getragen, nicht von der Nische. Prüfung braucht mindestens einen
Kanal mit **12+ Monaten Verlauf**.

---

## 6. Kadenz-Machbarkeit *(K.-o.-Kriterium)*

**Median Uploads/Woche der Erfolgskanäle. Über 2 = rot.**

Zusätzlich die Produktionsfrage: **Kann das Bild loopen, oder braucht jede
Sekunde neues Material?** Ein 3-Stunden-Video aus 4 geloopten Clips und ein
10-Minuten-Video mit 40 Schnitten sind nicht derselbe Aufwand, egal was die
Kadenz sagt.

---

## 7. ERTRAG JE ARBEITSSTUNDE

**Nicht "wenig Aufwand" — Ertrag je Stunde Menschenarbeit.**

```
Arbeitsstunden/Monat = Stunden Menschenarbeit je Video × Videos je Monat
Ertrag je Arbeitsstunde = Monatsumsatz / Arbeitsstunden pro Monat
```

| Bereich | Bewertung |
|---|---|
| über 300 $/h | grün |
| 100–300 $/h | gelb |
| unter 100 $/h | rot |

Eine Nische mit 3 h/Woche und 8.000 $/Monat schlägt eine mit 0 h und 5.000 $.
**Aufwand allein ist KEIN Ausschlussgrund.** Nur der Quotient zählt.

---

## 8. Monetarisierungsquote

Anteil der gefundenen Kanäle, die tatsächlich monetarisiert sind.

Eine Nische, deren Gewinnerkanäle keine Werbung schalten, beweist Nachfrage,
aber nicht Umsatz. Immer je Kanal einzeln prüfen, nie hochrechnen.

---

## 9. Geografie

Tier-1-Anteil (US/CA/UK/AU/DE …) an den Views.

Er erklärt den RPM. Ein niedriger RPM bei hohem Tier-1-Anteil hat eine andere
Ursache als einer bei 80 % Tier-3 — und nur die erste Ursache lässt sich
beheben.

---

## K.-o.-Regel

**K.-o. nur bei rot in 1, 4 oder 6.**

Alles andere ist ein Abschlag in der Note, kein Ausschluss. Insbesondere ist
ein hoher Aufwand (Kriterium 7) kein K.-o., solange der Stundenertrag stimmt.

---

## Notenskala

| Note | Bedeutung |
|---|---|
| 9–10 | starten, ohne weitere Prüfung |
| 8 | starten, mit benannter Restschwäche |
| 7 | trägt, aber ein Kernkriterium ist rot oder unbelegt |
| 5–6 | Einzelfälle funktionieren, die Nische nicht |
| 1–4 | widerlegt |

**Schwelle für eine Empfehlung: 8 von 10.**
Erreicht keine Unterrichtung diese Schwelle, wird das deutlich gesagt und die
beste mit ihrer Schwäche benannt. Nicht schönrechnen.
