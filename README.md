
# Dog Walk Animation in Blender

Dieses Repository enthält ein Python-Skript zur Animation eines Hundemodells in Blender. Das Skript erstellt eine Gehbewegung sowie eine Kopfbewegung für ein rigged 3D-Modell.

## Inhalt

- `Animals.blend`: Blender-Projektdatei mit dem Hundemodell und seiner Knochenstruktur.
- `dog_walk.py`: Python-Skript zur Animation des Hundemodells.
- `dog.jpg`: Vorschau des animierten Modells.

## Voraussetzungen

- **Blender**: Version 3.0 oder höher
- Python-Integration in Blender (vorinstalliert)

## Funktionen des Skripts

1. **Gehbewegung**:
   - Die Vorder- und Hinterbeine des Hundes bewegen sich in einer natürlichen, gegenläufigen Weise.
   - Die Animation läuft in einem Endlosschleifenformat über 20 Sekunden.

2. **Kopfbewegung**:
   - Der Kopf des Hundes dreht sich während der Animation einmal nach links und kehrt zur Mitte zurück.

## Verwendung

1. **Blender öffnen**:
   - Öffnen Sie die Datei `Animals.blend` in Blender.

2. **Skript laden**:
   - Laden Sie das `dog_walk.py`-Skript in den Blender-Scripting-Editor.

3. **Skript ausführen**:
   - Drücken Sie `Alt + P`, um das Skript auszuführen. Die Animation wird automatisch auf die Zeitleiste angewendet.

4. **Animation abspielen**:
   - Wechseln Sie in den `Animation`-Tab und spielen Sie die Animation ab, um die Ergebnisse zu überprüfen.

## Anpassungen

### FPS ändern
Passen Sie die FPS (Frames per Second) in den Animationsparametern des Skripts an:
```python
fps = 24
```

### Animationsdauer ändern
Ändern Sie die Dauer der Animation, indem Sie die Variable `animation_duration` anpassen:
```python
animation_duration = 20  # in Sekunden
```

### Knochenanpassung
Wenn die Knochenbezeichnungen Ihres Modells von den Standardwerten abweichen, aktualisieren Sie die `bones`-Zuweisung:
```python
bones = {
    "front_left": "front_shoulder.L",
    "front_right": "front_shoulder.R",
    "back_left": "thigh.L",
    "back_right": "thigh.R",
    "head": "scull"
}
```

## Vorschau


![dog](https://github.com/user-attachments/assets/4769e056-4a04-4f39-ab6d-4ea75d85ea99)

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Siehe die `LICENSE`-Datei für weitere Informationen.

---

Viel Spaß beim Experimentieren mit 3D-Animationen in Blender!

