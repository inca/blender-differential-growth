import bpy

class DiffGrowthPanel(bpy.types.Panel):
    bl_label = "Differential Growth"
    bl_idname = "OBJECT_PT_diffgrow_panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'object'

    def draw(self, context):
        layout = self.layout
        obj = context.object
        settings = obj.diff_growth_settings

        box = layout.box()
        box.label(text='Basics')
        row = box.row()
        row.prop(settings, 'split_radius')
        row = box.row()
        row.prop(settings, 'repulsion_radius')
        row = box.row()
        row.prop(settings, 'dt')
        row = box.row()
        row.prop(settings, 'scale')

        box = layout.box()
        box.label(text='Noise')
        row = box.row()
        row.prop(settings, 'noise_scale')
        row = box.row()
        row.prop(settings, 'fac_noise')
        row = box.row()
        row.prop(settings, 'seed')

        box = layout.box()
        box.label(text='Growth Direction')
        row = box.row()
        row.prop(settings, 'growth_dir_obj')
        row = box.row()
        row.prop(settings, 'fac_growth_dir')

        box = layout.box()
        box.label(text='Growth Inhibitors')
        row = box.row()
        row.prop(settings, 'inhibit_base')
        row = box.row()
        row.prop(settings, 'inhibit_shell')

        row = layout.row()
        row.operator('object.diff_growth_step')
