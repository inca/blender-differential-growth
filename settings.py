import bpy

class DiffGrowthSettings(bpy.types.PropertyGroup):

    seed: bpy.props.IntProperty(
        name="Seed",
        description="Noise seed",
        default=1,
        min=1,
        max=1000,
    )

    split_radius: bpy.props.FloatProperty(
        name="Split Radius",
        description="Radius for edge subdivision",
        default=.1,
        min=.01,
        max=2,
    )

    collision_radius: bpy.props.FloatProperty(
        name="Repulsion Radius",
        description="Radius for calculating the repulsion force",
        default=.1,
        min=.01,
        max=2,
    )


    dt: bpy.props.FloatProperty(
        name="dt",
        description="Time step for simulation; smaller values produce more accurate result, but take longer",
        default=.025,
        min=.001,
        max=1,
    )

    weight_decay: bpy.props.FloatProperty(
        name="Weight Decay",
        description="Value of 1.0 causes no decay, higher values cause weight to drop more quickly",
        default=1.5,
        min=0.01,
        max=10,
    )

    noise_scale: bpy.props.FloatProperty(
        name="Noise Scale",
        description="Higher value produce high frequency noise",
        default=5,
        min=0.01,
        max=100,
    )

    fac_attr: bpy.props.FloatProperty(
        name="Attraction Factor",
        description="Attraction Factor",
        default=1,
        min=0,
        max=100,
    )

    fac_rep: bpy.props.FloatProperty(
        name="Repulsion Factor",
        description="Repulsion Factor",
        default=1,
        min=0,
        max=100,
    )

    fac_noise: bpy.props.FloatProperty(
        name="Noise Factor",
        description="Noise Factor",
        default=1,
        min=0,
        max=100,
    )
