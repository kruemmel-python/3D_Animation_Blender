## Übersicht

Dieses Repository enthält ein **Blender-Python-Skript**, das eine einfache Laufanimation für ein Hundemodell erstellt. Zusätzlich wird eine Kopfbewegung animiert, damit sich der Hund z. B. einmal umschauen kann.  
Das Skript nutzt **Python 3.12**-Features und folgt dabei den Prinzipien des [Zen of Python](https://peps.python.org/pep-0020/) für maximale Klarheit, Einfachheit und Lesbarkeit.

---

## Inhalte

- [Voraussetzungen](#voraussetzungen)  
- [Installation und Einrichtung](#installation-und-einrichtung)  
- [Projektstruktur](#projektstruktur)  
- [Verwendung](#verwendung)  
- [Funktionsweise & Codeerklärung](#funktionsweise--codeerklärung)  
- [Fehlersuche](#fehlersuche)  
- [Weiterführende Ideen](#weiterführende-ideen)
- [Vorschau](#vorschau)  

---

## Voraussetzungen

1. **Blender**: Du benötigst eine funktionsfähige Blender-Installation (Version 3.0 oder höher wird empfohlen).  
2. **Python 3.12**: Normalerweise wird Blender mit einer eigenen Python-Version ausgeliefert. Stelle sicher, dass deine Blender-Version eine kompatible Python-Variante enthält.  
3. **Hundemodell**: Das Skript setzt voraus, dass in deiner Blender-Datei ein Objekt namens `dog.001` existiert, das die Armature für das Hundemodell enthält. Die entsprechenden Knochen müssen vorhanden und richtig benannt sein. (Siehe unten im Abschnitt [Funktionsweise & Codeerklärung](#funktionsweise--codeerklärung).)

---

## Installation und Einrichtung

1. **Blender starten**  
   - Öffne Blender und erzeuge (oder öffne) eine Szene, in der bereits das Hundemodell mit der korrekten Armature (`dog.001`) existiert.  

2. **Skript hinzufügen**  
   - Lade die Datei `dog_walk_animation.py` (oder wie auch immer du das Skript nennen möchtest) herunter oder kopiere den Inhalt direkt.  
   - Öffne in Blender den **Text-Editor** (oben links auf *Text* klicken, dann *New* oder *Open* wählen) und füge den Skriptcode ein. Speichere ihn im Blender-Text-Editor oder als separate `.py`-Datei in deinem Projektverzeichnis.

3. **Python-Konsole oder Scripting-Tab**  
   - Blender bietet unten rechts standardmäßig einen kleinen Scripting-Tab an (abhängig vom Standard-Layout). Alternativ kannst du oben in der Menüleiste auf *Scripting* klicken, um eine größere Arbeitsoberfläche zu bekommen.  
   - Stelle sicher, dass das Skript im Blender-Python-Kontext ausgeführt wird, damit `bpy` verfügbar ist.

4. **Abhängigkeiten**  
   - Normalerweise brauchst du keine zusätzlichen Abhängigkeiten außer Blender und das integrierte `bpy`-Modul. Falls du externe Bibliotheken nutzen möchtest, kannst du sie entweder ins Blender-Python installieren oder global in dein System-Python (Achtung: Blender muss auf dieses System-Python verweisen).

---

## Projektstruktur

In diesem Repository könnten verschiedene Dateien und Ordner enthalten sein:

```
3D_Animation_Blender/
│
├─ dog_walk_animation.py      # Hauptskript für die Animation
├─ README.md                  # Diese Anleitung
├─ assets/                    # (Optional) Zusätzliche Dateien wie Texturen, Blend-Dateien
└─ examples/                  # (Optional) Beispielcode oder zusätzliche Scripts
```

> **Hinweis**: Du kannst deine Dateien natürlich anders organisieren. Wichtig ist, dass man das Skript und ggf. die zugehörige `.blend`-Datei leicht findet.

---

## Verwendung

1. **Blend-Datei öffnen**  
   - Starte Blender und öffne deine .blend-Datei mit dem Hundemodell.

2. **Skript ausführen**  
   - Wechsle in den Scripting-Tab.  
   - Lade das Skript `dog_walk_animation.py` (falls nicht schon geschehen).  
   - Klicke auf den *Run Script*-Button (oder drücke `Alt + P` im Text-Editor).  

3. **Ergebnis prüfen**  
   - Wechsel in den *Timeline*- oder *Dope Sheet*-Bereich und bewege den Zeitcursor (`Play`-Button drücken). Der Hund sollte nun eine einfache Laufbewegung ausführen, sowie in einem definierten Frame-Bereich den Kopf bewegen.  

4. **Anpassungen vornehmen**  
   - In `dog_walk_animation.py` findest du zahlreiche einstellbare Parameter (z. B. `ANIMATION_DURATION`, `cycle_duration`, `turn_frame_start` / `turn_frame_end` für die Kopfbewegung). Passe diese Werte an, um die Animation zu verfeinern.  

---

## Funktionsweise & Codeerklärung

Das Skript `dog_walk_animation.py` ist in übersichtliche Funktionen aufgeteilt:

1. **Globale Einstellungen (Animation & Szene)**  
   - `FPS`, `ANIMATION_DURATION`, `FRAME_START` und `FRAME_END` legen fest, wie lange und mit welcher Bildrate die Animation läuft.  
   - Blender wird angewiesen, die Szene entsprechend anzupassen.

2. **Armature & Knochen**  
   - Der Code versucht, das Objekt `dog.001` zu finden. Falls dieses nicht existiert, wird eine Fehlermeldung ausgegeben.  
   - Ein Dictionary `bones` legt die Knochennamen fest: `front_shoulder.L`, `thigh.L` usw. Der Eintrag `"head"` verweist auf den Kopfknochen, z. B. `"scull"`.

3. **Funktion `animate_leg_movement(...)`**  
   - Kümmert sich um die eigentliche Gehbewegung der vier Beine.  
   - Durchläuft alle Frames und wechselt in bestimmten Abständen (`cycle_duration`) zwischen zwei Phasen (Vorderbeine vorne / hinten, Hinterbeine umgekehrt).

4. **Funktion `animate_head_movement(...)`**  
   - Dreht den Kopf des Hundes in einem definierten Frame-Bereich (`turn_frame_start` bis `turn_frame_end`) und wieder zurück.  
   - Nutzt einfache Euler-Rotation (`XYZ`).

5. **Hauptfunktion `create_walking_animation(...)`**  
   - Ruft oben genannte Animationsfunktionen auf.  
   - Gibt eine Bestätigung aus, wenn alles fertig ist.

---

## Fehlersuche

- **KeyError: `'dog.001'`**  
  - Das bedeutet, dass in deiner Blend-Datei kein Objekt mit dem Namen `dog.001` gefunden wurde. Prüfe die Outliner-Liste in Blender und passe den Namen im Skript an.  

- **Bone XYZ existiert nicht**  
  - Möglicherweise hast du in deiner Armature andere Namen für die Schulter- und Beinknochen. Ändere die Einträge im Dictionary `bones`, sodass sie exakt mit den Blender-Knochen übereinstimmen.  

- **Kopf dreht sich nicht**  
  - Wenn der Keyframe-Bereich außerhalb deines `FRAME_END` liegt, oder der Knochennamen für `"head"` falsch ist, wird nichts passieren. Prüfe die Werte `turn_frame_start` und `turn_frame_end`, sowie den Knochennamen.  

- **Keine Animation**  
  - Stelle sicher, dass du das Skript wirklich in Blender (und nicht in einer separaten System-Python-Konsole) ausführst. In der Blender-Konsole oder im Scripting-Tab sollte kein Fehler angezeigt werden.  

---

## Weiterführende Ideen

- **Mehrere Gehphasen**  
  - Füge zusätzliche Schlüsselphasen hinzu, um einen realistischeren Gang (z. B. vier statt zwei Schritten) umzusetzen.  
- **Weitere Körperteile animieren**  
  - Ergänze eine Schwanzbewegung oder ein leichtes Federn des Rumpfes, um mehr Dynamik zu erzeugen.  
- **Kamera- und Lichtsteuerung**  
  - Automatisiere auch Kamerafahrten oder Lichtanimationen, um ganze Szenen in Blender zu skripten.  
- **Export als Video**  
  - Du kannst direkt aus Blender heraus ein Video rendern lassen. Achte dafür auf die Rendereinstellungen und Codec-Auswahl.  

---

### Lizenz und Danksagungen

- Dieses Projekt steht unter keiner speziellen Lizenz, sofern nicht anders vermerkt. Du bist frei, es nach Belieben zu verwenden, anzupassen oder zu verbessern.  

> Viel Spaß beim Ausprobieren und Anpassen!  
> Wenn du Fragen, Wünsche oder Feedback hast, erstelle gerne ein Issue oder einen Pull Request.

---
## Vorschau
![dog](https://github.com/user-attachments/assets/74f494ba-635b-4cb2-93ba-3ac4c9c5ce9f)



