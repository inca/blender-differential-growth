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

        row = layout.row()
        row.prop(settings, 'seed')
        row = layout.row()
        row.prop(settings, 'collision_radius');
        row = layout.row()
        row.prop(settings, 'split_radius')
        row = layout.row()
        row.prop(settings, 'dt')

        row = layout.row()
        row.prop(settings, 'weight_decay')
        row.prop(settings, 'decay_boundary')

        row = layout.row()
        row.prop(settings, 'fac_attr')
        row = layout.row()
        row.prop(settings, 'fac_rep')
        row = layout.row()
        row.prop(settings, 'fac_noise')
        row.prop(settings, 'noise_scale')

        row = layout.row()
        row.operator('object.diff_growth_step')
