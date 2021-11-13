# Support script reload for imports
if 'bpy' in locals():
    import importlib
    importlib.reload(panel)
    importlib.reload(op_grow)
else:
    from . import panel
    from . import op_grow
    from . import settings

import bpy

bl_info = {
    'name': 'Differential Growth',
    'description': 'Grow mesh into nature-inspired wavy forms',
    'version': (1, 0),
    'author': 'Boris Okunskiy',
    'tracker_url': 'https://github.com/inca/blender-differential-growth/issues',
    'location': 'Properties > Object > Differential Growth',
    'blender': (2, 90, 0),
    'category': 'Object'
}

def register():
    bpy.utils.register_class(settings.DiffGrowthSettings)
    bpy.utils.register_class(op_grow.DiffGrowthStepOperator)
    bpy.utils.register_class(panel.DiffGrowthPanel)

    bpy.types.Object.diff_growth_settings = \
        bpy.props.PointerProperty(type=settings.DiffGrowthSettings)

    print('Differential Growth Registered')

def unregister():
    bpy.utils.unregister_class(panel.DiffGrowthPanel)
    bpy.utils.unregister_class(op_grow.DiffGrowthStepOperator)
    bpy.utils.unregister_class(settings.DiffGrowthSettings)

    print('Differential Growth Unregistered')

if __name__ == '__main__':
    register()
