import bpy

# Animationsparameter
fps = 24
animation_duration = 20  # in Sekunden
frame_start = 1
frame_end = animation_duration * fps
bpy.context.scene.frame_start = frame_start
bpy.context.scene.frame_end = frame_end
bpy.context.scene.render.fps = fps

# Hundemodell und Pose-Modus
armature = bpy.data.objects["dog.001"]
bpy.context.view_layer.objects.active = armature
bpy.ops.object.mode_set(mode='POSE')

# Knochenzuordnung
bones = {
    "front_left": "front_shoulder.L",
    "front_right": "front_shoulder.R",
    "back_left": "thigh.L",
    "back_right": "thigh.R",
    "head": "scull"  # Kopfknochen korrekt zugeordnet
}

# Animationslogik: Gehbewegung (Loop über gesamten Animationszeitraum)
cycle_duration = 40  # Frames pro Bewegungszyklus
for frame in range(frame_start, frame_end + 1, cycle_duration):
    for offset, angles in enumerate([
        {"front_left": 0.2, "front_right": -0.2, "back_left": -0.3, "back_right": 0.3},
        {"front_left": -0.2, "front_right": 0.2, "back_left": 0.3, "back_right": -0.3}
    ]):
        for leg, bone_name in bones.items():
            if leg == "head":
                continue  # Kopf wird separat animiert
            bone = armature.pose.bones[bone_name]
            bone.rotation_mode = 'XYZ'
            bone.rotation_euler = (angles[leg], 0, 0)
            bone.keyframe_insert(data_path="rotation_euler", frame=frame + offset * (cycle_duration // 2))

# Kopfbewegung hinzufügen (nur einmal während der Animation, außerhalb der Schleife)
if "head" in bones:
    head_bone = armature.pose.bones[bones["head"]]
    head_bone.rotation_mode = 'XYZ'
    # Kopf nach links drehen
    head_bone.rotation_euler = (0, 0, 0.3)
    head_bone.keyframe_insert(data_path="rotation_euler", frame=60)
    # Kopf zurück zur Mitte drehen
    head_bone.rotation_euler = (0, 0, 0)
    head_bone.keyframe_insert(data_path="rotation_euler", frame=90)

bpy.ops.object.mode_set(mode='OBJECT')
print("Laufanimation für das Hundemodell erstellt und einmalige Kopfbewegung hinzugefügt.")
