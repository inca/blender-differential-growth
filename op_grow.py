import bpy
import bmesh
import math
from mathutils import Vector, kdtree, noise

class DiffGrowthStepOperator(bpy.types.Operator):
    bl_label = "Diff Growth Step"
    bl_idname="object.diff_growth_step"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        obj = context.object

        if obj.vertex_groups.active_index == -1:
            self.report({ "WARNING" }, "A vertex group is required; switch to Weight Paint and define the growth area")
            return { "CANCELLED" }

        settings = obj.diff_growth_settings
        bm = bmesh.new()
        bm.from_mesh(obj.data)

        grow_step(
            obj,
            bm,
            settings
        )

        bm.to_mesh(obj.data)
        bm.free()
        obj.data.update()
        return { "FINISHED" }


def grow_step(
    obj,
    bm,
    settings,
):
    group_index = obj.vertex_groups.active_index
    seed_vector = Vector((0, 0, 1)) * settings.seed

    # Collect vertices with weights
    verts = []
    edges = set()

    for vert in bm.verts:
        weight = get_vertex_weight(bm, vert, group_index)
        if weight > 0:
            verts.append(vert)
            for edge in vert.link_edges:
                edges.add(edge)

    kd = kdtree.KDTree(len(bm.verts))
    for i, vert in enumerate(bm.verts):
        kd.insert(vert.co, i)
    kd.balance()

    # Calc forces
    for vert in verts:
        weight = get_vertex_weight(bm, vert, group_index)
        if weight == 0:
            continue
        f_attr = calc_vert_attraction(vert)
        f_rep = calc_vert_repulsion(vert, kd, settings.collision_radius)
        f_noise = noise.noise_vector(vert.co * settings.noise_scale + seed_vector)
        growth_vec = Vector((0, 0, 1))
        if settings.growth_dir_obj:
            growth_vec = (settings.growth_dir_obj.location - vert.co).normalized()
        # print('%s %s %s' % (f_attr, f_rep, f_noise))
        force = \
            settings.fac_attr * f_attr + \
            settings.fac_rep * f_rep + \
            settings.fac_noise * f_noise + \
            settings.fac_growth_dir * growth_vec;
        offset = force * settings.dt * settings.dt * weight;
        vert.co += offset

    # Readjust weights
    for i, vert in enumerate(bm.verts):
        w = get_vertex_weight(bm, vert, group_index)
        if not vert.is_boundary:
            if (w == 1):
                # Hack to prevent non-reducing "red areas" after certain subdivision patters
                w -= 0.01;
        if (not vert.is_boundary) or settings.decay_boundary:
            w = w ** settings.weight_decay;
        set_vertex_weight(bm, vert, group_index, w)

    # Subdivide
    edges_to_subdivide = []
    for edge in edges:
        avg_weight = calc_avg_edge_weight(bm, [edge], group_index)
        if avg_weight == 0:
            continue
        l = edge.calc_length()
        if (l / settings.split_radius) > (1 / avg_weight):
            edges_to_subdivide.append(edge)

    if len(edges_to_subdivide) > 0:
        print("Subdividing %i" % len(edges_to_subdivide))
        bmesh.ops.subdivide_edges(
            bm,
            edges=edges_to_subdivide,
            smooth=1.0,
            cuts=1,
            use_grid_fill=True,
            use_single_edge=True)
        # Triangulate adjacent faces
        adjacent_faces = set()
        for edge in edges_to_subdivide:
            adjacent_faces.update(edge.link_faces)
        bmesh.ops.triangulate(
            bm,
            faces=list(adjacent_faces))

def get_vertex_weight(bm, vert, group_index):
    weight_layer = bm.verts.layers.deform.active
    weights = vert[weight_layer]
    return weights[group_index] if group_index in weights else 0

def set_vertex_weight(bm, vert, group_index, weight):
    weight_layer = bm.verts.layers.deform.active
    weights = vert[weight_layer]
    weights[group_index] = weight

def calc_avg_edge_length(edges):
    sum = 0.0
    for edge in edges:
        sum += edge.calc_length()
    return sum / len(edges)

def calc_min_edge_length(edges):
    val = 100000
    for edge in edges:
        val = min(edge.calc_length(), val)
    return val

def calc_avg_edge_weight(bm, edges, group_index):
    sum = 0.0
    n = 0
    for edge in edges:
        for vert in edge.verts:
            sum += get_vertex_weight(bm, vert, group_index)
            n += 1
    return sum / n

def calc_vert_attraction(vert):
    result = Vector()
    for edge in vert.link_edges:
        other = edge.other_vert(vert)
        if other == None:
            continue
        result += other.co - vert.co
    return result

def calc_vert_repulsion(vert, kd, radius):
    result = Vector()
    for (co, index, distance) in kd.find_range(vert.co, radius * 2):
        if (index == vert.index):
            continue;
        direction = (vert.co - co).normalized()
        magnitude = math.exp(distance - radius)
        # magnitude = 1 / (distance * distance)
        result += direction * magnitude
    return result;
