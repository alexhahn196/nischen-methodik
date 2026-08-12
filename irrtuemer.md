# Irrtümer — Messfehler, die sich nicht wiederholen dürfen

Jeder Eintrag hier ist ein Fehler, der schon einmal gemacht wurde, mit dem
Beleg, an dem er aufgefallen ist. Vor jeder Nischenprüfung lesen.

---

## 1. Das `rpm`-Feld ist nicht der RPM

Zwischen dem gemeldeten `rpm`-Feld und dem gerechneten RPM liegt **Faktor 5
bis 7**. Das Feld gibt den Werbe-RPM auf monetarisierten Wiedergaben an, nicht
den Ertrag je 1.000 Gesamtviews.

> **Beleg:** *The Sleep Bible* meldet **26,53 $**.
> Real: **3,90 $** — 2.711 $ Umsatz bei 695.760 Views.

**Regel:** Umsatz durch Views. Immer. Das Feld nur als Nebennotiz führen.

---

## 2. Der 4-Monats-Filter zeigt Trend, nicht Haltbarkeit

Ein kurzes Fenster misst, was gerade läuft. Es sagt nichts darüber, ob es in
einem Jahr noch läuft.

> **Beleg:** *Lorevia* — 32 Mio. Views, Outlier 13,83.
> Heute: **14 $/Monat.**

**Regel:** Haltbarkeit braucht mindestens einen Kanal mit 12+ Monaten Verlauf
und die Frage, wo sein Views-Gipfel liegt.

---

## 3. Ein Treffer ist kein Kanal

Ein virales Video macht Gesamtviews, aber kein Geschäft.

> **Beleg:** *ExplainMatics* — 652.000 Views auf **einem** Video,
> **68 $/Monat.**

**Frühwarnzahl: Top-3-Anteil an den Gesamtviews, ab 20 Videos gerechnet.**

| Top-3-Anteil | Deutung |
|---|---|
| unter 35 % | getragener Katalog |
| 35–50 % | Graubereich |
| über 50 % | Einzeltreffer |

---

## 4. Crossref-Gesamttrefferzahlen messen nichts

Wenn ein Instrument fast alles bestätigt, bestätigt es nichts.

> **Beleg:** 41 von 42 Fragen "gut belegt" ist ein **kaputtes Instrument**,
> kein Befund.

**Regel:** Eine Prüfung, die praktisch nie *nein* sagt, wird verworfen und
nicht als Bestätigung zitiert.

---

## 5. Vor jeder Klassifikation nie die Views sehen

Wer die Views kennt, bevor er klassifiziert, findet **garantiert** ein Muster —
und zwar das, welches die Views erklärt.

**Regel:** Erst Merkmale festlegen und zuordnen, dann die Leistungsdaten
aufdecken. Nie umgekehrt.

---

## 6. Aufstiege haben sichtbare Ursachen, Abstürze nicht

Bei Aufstiegen lassen sich die Ursachen in den Metadaten wiederfinden
(Formatwechsel, Titelmuster, Thumbnail-Umstellung, Längenwechsel). Bei
Abstürzen nicht — die Metadaten sehen davor und danach gleich aus.

> **Belegt an:** Axen, quack doc, History Mapped Out, Folks of Yore,
> Professor Historian.

**Folge:** Man kann aus Metadaten lernen, wie ein Kanal steigt — aber man kann
aus ihnen **nicht** vorhersagen, ob er fällt. Ein Kanal, der heute läuft, ist
kein Beleg dafür, dass er morgen läuft. Deshalb Kriterium 5 (Haltbarkeit).

---

## 7. Das Katalogfeld `isMonetizationEnabled` ist veraltet — live prüfen

Das Monetarisierungsfeld im NexLev-Katalog steht systematisch zu oft auf
`false`. Kriterium 8 wird dadurch zu pessimistisch beantwortet.

> **Beleg (11.08.2026):** Der Katalog meldete *Story Classics*, *The Sleepy
> Historian*, *Moon Mind Temple*, *Sublime AudioBooks* und *AudioBooksCollection*
> als **nicht monetarisiert**. Die Live-API meldete alle fünf als
> **monetarisiert**.

**Regel:** Die Monetarisierungsquote nie aus dem Katalogfeld ableiten. Immer
`check_channel_monetization` (mit `bypassCache`) oder
`get_batch_channel_metrics_v2` gegen die gefundenen Kanäle laufen lassen.

Umgekehrt bleibt der Befund bei echten Nicht-Monetarisierten belastbar: *Hush
Little Lamb*, *Sleepy People*, *Mind Palace* und *Whispered Sleep Sagas* (Harry
Potter) sind auch live nicht monetarisiert.

> **Nachtrag 12.08.2026 (Methodikprüfung, Teil 0):** Das Feld ist nicht
> systematisch invertiert, sondern in beide Richtungen unzuverlässig. Über
> beide Prüftage wurden 11 Katalog-„nein"-Kanäle live geprüft: **7 falsch**
> (u. a. Rest In Faith, Saints for Sleep, Moon Mind Temple, The Sleepy
> Historian), **4 richtig** (Hush Little Lamb, Selah, Rest in Jesus, Just
> Free Audiobooks). Regel geschärft: Ein Katalog-„nein" heißt **„Umsatz
> unbekannt"** — es zählt weder als ja noch als nein, und die 0-$-Zeilen des
> Katalogs sind keine Umsatzmessung.

---

## 8. „Freies Material" ist nicht „freier Text"

Ein Kanal, der über ein gemeinfreies Thema spricht, rezitiert deshalb noch
lange keinen gemeinfreien Text. Der Unterschied entscheidet über die
Rechtefrage und über die Frage, ob ein Skript geschrieben werden muss.

> **Beleg:** *Sleepy Monk* galt als Beleg für „kein geschriebenes Skript, weil
> der Text aus einer freien Quelle kommt". Seine Titel benennen kein Werk —
> *„The Best Buddhist Teachings for Sleep"*, *„No-Mind: Zen Stories"*. Das
> Skript ist geschrieben, nur eben von einem Modell. Von sechs geprüften
> Unterrichtungen rezitierte **eine einzige** tatsächlich gemeinfreie Werke.

**Regel:** Klassifikationsregel vor dem Ansehen der Titel festlegen (siehe #5),
dann anwenden: Nur wer ein **konkret benanntes Werk** vorliest, arbeitet mit
vorhandenem Text. Generische Themen-Titel bedeuten geschriebenes Skript.

**Zweite Falle derselben Art:** Fremdes IP ist auch kein freier Text.
Warhammer 40K, Game of Thrones, Harry Potter und Twilight tragen in dieser
Nische die höchsten Umsätze — als geduldete Verletzung, jederzeit per Claim
abschaltbar.

---

## 9. Kurze Werke tragen keinen Katalog

Vor der Textauswahl den **Umfang messen**, nicht annehmen. Bei 150 Wörtern je
Minute Sprechtempo ergibt sich die Audiolänge direkt aus der Wortzahl.

> **Beleg (gemessen auf Project Gutenberg):** Dhammapada 15.243 Wörter ≈ 1,7 h.
> Tao Te King 13.729 Wörter ≈ 1,5 h. Beide sind nach **zwei** 3-Stunden-Videos
> aufgebraucht.
> Dagegen: *The Adventures of Sherlock Holmes* 107.518 Wörter ≈ 12 h,
> *Grimms' Fairy Tales* 104.152 Wörter, *Arabian Nights* 114.644 Wörter.

**Regel:** `curl` auf `gutenberg.org/cache/epub/<id>/pg<id>.txt`, dann `wc -w`.
Dabei die Datei-ID am `Title:`-Feld gegenprüfen — Gutenberg-IDs aus dem
Gedächtnis sind unzuverlässig (#56812 ist nicht Seneca, sondern Omans
*Peninsular War*).

**Erreichbarkeit aus dem Container (11.08.2026):** gutenberg.org **200**,
en.wikisource.org **200**, sacred-texts.com **403**.

---

## 10. Übersetzungsrechte prüfen, nicht nur den Originaltext

Ein gemeinfreier Originaltext bedeutet **nicht**, dass die gängige Übersetzung
frei ist. Die Übersetzung ist ein eigenes, urheberrechtlich geschütztes Werk.

> **Beleg:** Die Bibel ist gemeinfrei — die **NIV-Übersetzung ist geschützt.**
> Deshalb WEBBE (World English Bible, British Edition).

**Regel:** Bei jeder Textquelle **zwei** Fragen stellen:
1. Ist der Originaltext gemeinfrei?
2. Ist die **konkret verwendete Übersetzung** gemeinfrei?

Und den Fundort belegen (Project Gutenberg, sacred-texts, Wikisource) — mit
Link und Umfang.

---

## 11. Eine Nischenregel ist kein allgemeines Bewertungskriterium

Die Kadenzregel („über 2 Uploads/Woche = rot") stammt aus **10 Kanälen
derselben Nische** (BibelTube-Umfeld: Gewinner 1,3–1,5/Wo, alle 8 Verlierer
2,0–13,5/Wo). Dort trennt sie sauber. Als **allgemeines** K.-o.-Kriterium
über fremde Nischen übernommen, trennte sie nicht mehr — sie sortierte
Gewinner aus.

> **Beleg (Rückwärtstest, 12.08.2026):** Das K.-o. hätte Sleepy Monk
> (4,8/Wo) und SleepNomad (2,3/Wo) verworfen — heute 2.618 und
> 2.480 $/Monat. Median der verworfenen Kanäle **2.549 $** gegen **1.355 $**
> bei den durchgelassenen; Korrelation Kadenz/Umsatz **+0,45**. In den
> Gründungsdaten der Regel selbst lag zudem kein einziger Absturzkanal über
> 2/Woche — die Schwelle hatte dort nie etwas getrennt.

**Regel:** Vor der Übernahme einer Schwelle prüfen, **woran sie geeicht
wurde**. Eine Regel aus n Kanälen *einer* Nische ist eine Betreiberregel
für diese Nische (für BibelTube gilt die Kadenzregel deshalb weiter). Zum
Bewertungskriterium über Nischen hinweg wird sie erst, wenn sie an fremden
Nischen bestanden hat — die Kadenzregel hat diesen Test nicht bestanden.

---

## 12. Eine Ungleichung mit unbekannter rechter Seite ist kein Tor

Tor 3 lautet `Kadenz × Menschenstunden je Video ≤ verfügbare Wochenstunden`.
In sechs Torurteilen wurde **„bestanden"** vergeben, ohne dass die rechte
Seite je einen Wert hatte: „verfügbare Wochenstunden" kommt im gesamten Repo
**genau einmal** vor — in der Formel selbst.

Was tatsächlich geprüft wurde, war nicht die Ungleichung, sondern der
Eindruck, die linke Seite sei klein. Damit war stillschweigend wieder eine
**universelle Schwelle** im Einsatz — genau die, die Tor 3 laut eigener
Begründung abgeschafft hat (#11). Ein K.-o.-Kriterium durch ein Tor zu
ersetzen, dessen Vergleichsgröße nie erhoben wird, ändert nur den Namen.

Dieselbe Prüfung fehlte auf der zweiten Hälfte: `Credits je Video × Kadenz
gegen das Credit-Budget` wurde in keiner einzigen Bewertung gerechnet.

> **Beleg (12.08.2026):** Die linke Seite war ebenfalls unbelegt. Der Faktor
> „Menschenstunden je Video" stand in keiner Bewertung als Zahl; rückgerechnet
> waren **vier verschiedene Werte** im Umlauf (0,33 / 0,75 / 1,00 / ~4,06 h),
> die dokumentierte Zuweisungsregel („0,75 h KI-Skript, 1,0 h Hörbuch")
> beschrieb **4 von 13** Rechnungen richtig, und innerhalb *einer*
> Unterrichtung bekamen strukturgleiche Kanäle verschiedene Werte. Folgen:
> eine Ampel kippt (Sleepy Time Historian 131 gelb → 98 rot), Rangplätze
> tauschen, und die Plätze 1 und 2 der Gesamtrangliste liegen **1,9 %**
> auseinander — ein Rangtausch ab 2 % Formatunterschied.
> Vollständig in [`zeitmodell.md`](zeitmodell.md).

**Regel, dreiteilig:**
1. Ein Tor, das zwei Größen vergleicht, ist erst geprüft, wenn **beide** einen
   ausgewiesenen Wert haben. Sonst lautet das Ergebnis „nicht prüfbar" oder —
   wenn nur die eigene Seite fehlt — **„bestanden ab X"**, nie „bestanden".
2. Jede Eingangsgröße einer Rechnung wird **ausgeschrieben**, nicht nur als
   „geschätzt" gekennzeichnet. Eine Zahl, die niemand nennt, kann niemand
   prüfen — und sie wird dann pro Zeile verschieden gewählt, ohne dass es
   auffällt.
3. Fragt ein Kriterium nach der **eigenen** Pipeline, ist eine Schätzung
   fremder Pipelines keine Antwort darauf. Stunden je Video kommen aus der
   eigenen Produktion (`zeitmodell.md`), nicht aus einer Vermutung über den
   Konkurrenten.
