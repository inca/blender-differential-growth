import bpy

class DiffGrowthSettings(bpy.types.PropertyGroup):

    split_radius: bpy.props.FloatProperty(
        name="Split Radius",
        description="Edges above this radius will be subdivided",
        default=.5,
        min=.01,
        max=10,
    )

    repulsion_radius: bpy.props.FloatProperty(
        name="Repulsion Radius",
        description="",
        default=1,
        min=0,
        max=10,
    )

    dt: bpy.props.FloatProperty(
        name="Step size",
        description="How much growth to apply on each step",
        default=.1,
        min=.001,
        max=10,
    )

    scale: bpy.props.FloatVectorProperty(
        name="Step Scale",
        description="Applies per-component scale to each movement; can be used to limit motion to specific axis",
        default=(1.0,1.0,1.0),
        size=3,
        subtype='XYZ'
    )

    seed: bpy.props.IntProperty(
        name="Seed",
        description="Noise seed",
        default=1,
        min=1,
        max=1000,
    )

    noise_scale: bpy.props.FloatProperty(
        name="Noise Scale",
        description="Higher value produce high frequency noise",
        default=2,
        min=0.01,
        max=100,
    )

    growth_dir_obj: bpy.props.PointerProperty(
        name="Growth Direction Object",
        description="The object towards which to grow; if not specified, +Z is used",
        type=bpy.types.Object
    )

    fac_attr: bpy.props.FloatProperty(
        name="Attraction Factor",
        description="Attraction Factor",
        default=0,
        min=0,
        max=1000,
    )

    fac_rep: bpy.props.FloatProperty(
        name="Repulsion Factor",
        description="Repulsion Factor",
        default=1,
        min=0,
        max=1000,
    )

    fac_noise: bpy.props.FloatProperty(
        name="Noise Factor",
        description="Noise Factor",
        default=1,
        min=0,
        max=1000,
    )

    fac_growth_dir: bpy.props.FloatProperty(
        name="Growth Direction Factor",
        description="Growth Direction Factor",
        default=0,
        min=-1000,
        max=1000,
    )

    inhibit_base: bpy.props.FloatProperty(
        name="Base Factor",
        description="Inhibit non-boundary growth",
        default=1,
        min=0,
        max=10,
    )

    inhibit_shell: bpy.props.FloatProperty(
        name="Shell Factor",
        description="Inhibit growth based on vertex sharpness",
        default=0,
        min=0,
        max=10,
    )
