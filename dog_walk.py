"""
Blender-Skript für eine einfache Hundelauf-Animation mit optionaler Kopfbewegung.
Kompatibel mit Python 3.12 und Blender's Python-API.

Voraussetzung:
- Das Objekt "dog.001" muss existieren und einen Armature-Typ haben.
- Die im Dictionary `bones` genannten Knochennamen müssen in der Armature vorhanden sein.
"""

import bpy

# ---------------------------------------------
# Globale Einstellungen (Animation & Szene)
# ---------------------------------------------

FPS: int = 24
ANIMATION_DURATION: int = 20  # in Sekunden
FRAME_START: int = 1
FRAME_END: int = ANIMATION_DURATION * FPS

# In Blender die Szenenparameter setzen
bpy.context.scene.frame_start = FRAME_START
bpy.context.scene.frame_end = FRAME_END
bpy.context.scene.render.fps = FPS

# ---------------------------------------------
# Armature & Knochenkonfiguration
# ---------------------------------------------
try:
    # Wir nehmen an, dass "dog.001" eine gültige Armature ist.
    armature = bpy.data.objects["dog.001"]
except KeyError as e:
    raise ValueError("Das Objekt 'dog.001' existiert nicht in der aktuellen Blend-Datei. "
                     "Bitte prüfe den Objektnamen.") from e

# Knochen, die animiert werden sollen
bones: dict[str, str] = {
    "front_left": "front_shoulder.L",
    "front_right": "front_shoulder.R",
    "back_left": "thigh.L",
    "back_right": "thigh.R",
    "head": "scull"
}

# ---------------------------------------------
# Funktion: Gehbewegung animieren
# ---------------------------------------------
def animate_leg_movement(arm_obj: bpy.types.Object,
                         bones_dict: dict[str, str],
                         cycle_duration: int = 40) -> None:
    """
    Erzeugt eine einfache Gehbewegung, indem Vorder- und Hinterläufe
    in zwei Positionen alternierend bewegt werden. Die Bewegung wird
    periodisch wiederholt, solange der Animationszeitraum läuft.
    
    :param arm_obj: Die Armature-Object-Referenz.
    :param bones_dict: Dictionary mit Zuordnung 'logischer Name' -> 'Knochenname'.
    :param cycle_duration: Anzahl der Frames pro Gehzyklus.
    """
    # Objekt im Pose-Modus bearbeiten
    bpy.context.view_layer.objects.active = arm_obj
    bpy.ops.object.mode_set(mode='POSE')

    # Zwei Phasen der Gehbewegung (Vorwärts-/Rückwärtsbewegung)
    # Winkel in Radiant oder Euler-Grad, je nach rotation_mode (hier: 'XYZ')
    gait_phases = [
        {"front_left":  0.2, "front_right": -0.2, "back_left": -0.3, "back_right":  0.3},
        {"front_left": -0.2, "front_right":  0.2, "back_left":  0.3, "back_right": -0.3}
    ]

    # Schleife über den gesamten Animationszeitraum
    for frame in range(FRAME_START, FRAME_END + 1, cycle_duration):
        # Wir durchlaufen die zwei Phasen
        for offset, angles in enumerate(gait_phases):
            for leg, bone_name in bones_dict.items():
                # Kopf überspringen, wird separat animiert
                if leg == "head":
                    continue
                
                # Pose-Bone aus Armature holen
                bone = arm_obj.pose.bones[bone_name]
                bone.rotation_mode = 'XYZ'
                
                # Aus dem Dictionary die Winkel holen und ansetzen
                angle = angles[leg]
                bone.rotation_euler = (angle, 0, 0)
                
                # Keyframe an passender Stelle eintragen
                bone.keyframe_insert(
                    data_path="rotation_euler",
                    frame=frame + offset * (cycle_duration // 2)
                )
    
    # Nach dem Animieren wieder in den Objektmodus wechseln
    bpy.ops.object.mode_set(mode='OBJECT')

# ---------------------------------------------
# Funktion: Kopfbewegung animieren
# ---------------------------------------------
def animate_head_movement(arm_obj: bpy.types.Object,
                          head_bone_name: str,
                          turn_frame_start: int = 60,
                          turn_frame_end: int = 90,
                          turn_angle_z: float = 0.3) -> None:
    """
    Dreht den Hundekopf in einem bestimmten Frame-Bereich nach links und wieder zurück.
    
    :param arm_obj: Die Armature-Object-Referenz.
    :param head_bone_name: Der Name des Kopf-Knochens.
    :param turn_frame_start: Frame, in dem der Kopf gedreht werden soll.
    :param turn_frame_end: Frame, in dem der Kopf zurückgedreht wird.
    :param turn_angle_z: Rotationswinkel im Z (links/rechts).
    """
    # Objekt im Pose-Modus bearbeiten
    bpy.context.view_layer.objects.active = arm_obj
    bpy.ops.object.mode_set(mode='POSE')
    
    head_bone = arm_obj.pose.bones[head_bone_name]
    head_bone.rotation_mode = 'XYZ'
    
    # Kopf nach links drehen
    head_bone.rotation_euler = (0, 0, turn_angle_z)
    head_bone.keyframe_insert(
        data_path="rotation_euler",
        frame=turn_frame_start
    )
    
    # Kopf zurück zur Mitte
    head_bone.rotation_euler = (0, 0, 0)
    head_bone.keyframe_insert(
        data_path="rotation_euler",
        frame=turn_frame_end
    )
    
    bpy.ops.object.mode_set(mode='OBJECT')

# ---------------------------------------------
# Haupt-Workflow
# ---------------------------------------------
def create_walking_animation() -> None:
    """
    Erstellt eine einfache Laufanimation für das Hundemodell 'dog.001'
    und fügt eine einmalige Kopfbewegung hinzu.
    """
    # Gehbewegung animieren
    animate_leg_movement(armature, bones, cycle_duration=40)
    
    # Optionale Kopfbewegung, wenn "head" im Dictionary vorhanden ist
    if "head" in bones:
        animate_head_movement(
            arm_obj=armature,
            head_bone_name=bones["head"],
            turn_frame_start=60,
            turn_frame_end=90,
            turn_angle_z=0.3
        )
    
    print("Laufanimation und Kopfbewegung wurden erfolgreich erstellt.")

# ---------------------------------------------
# Aufruf der Hauptfunktion
# ---------------------------------------------
if __name__ == "__main__":
    create_walking_animation()
