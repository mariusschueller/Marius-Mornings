import cadquery as cq

# --- Define the parameters for the model ---
height = 60.0
width = 80.0
thickness = 10.0
diameter = 22.0
padding = 12.0


base = cq.Workplane("XY").box(height, width, thickness)

base_with_hole = base.faces(">Z").workplane().hole(diameter)

base_with_fillet = base_with_hole.edges("|Z").fillet(10)

loop = base_with_fillet

for i in range(5):
    action = (
        loop.faces(">Z")
        .workplane()
        .rect(height - padding, width - padding, forConstruction=True)
        .vertices()
        .cboreHole(2.4, 4.4, 2.1)
    )
    loop = action
    padding += 10

result = (
    loop
)


show_object(result)
cq.exporters.export(result, "result.stl")