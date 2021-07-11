import bpy

PI = 3.14159

location = (-1.2, -2.4, 0)
rotation = (
    63.6 * PI / 180,
    0,
    46.7 * PI / 180,
)

bpy.ops.object.text_add(enter_editmode=True, location=location, rotation=rotation)

bpy.ops.font.select_all()
bpy.ops.font.delete(type='SELECTION')

bpy.ops.font.text_insert(text="Hello, world!")

bpy.ops.object.editmode_toggle()
