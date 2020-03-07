import bpy

bl_info = {
    "name" : "Poselib2Morph",
    "author" : "12funkeys",
    "version" : (0,1),
    "blender" : (2, 81, ),
    "location" : "COMMUNITY",
    "description" : "Poselib converts to Morph",
    "warning" : "",
    "wiki_url" : "",
    "tracker_url" : "",
    "category" : "Object"
}

# operatator
class P2M_OT_converter(bpy.types.Operator):
    bl_idname = "pose.2morph"
    bl_label = "Poselib2Morph"
    bl_description = "Poselib converts to Morph"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.mode == 'OBJECT'

    def draw(self, context):
        layout = self.layout
        layout.label(text="OK!")

    def execute(self, context):

        ab = bpy.context.active_object
        mods = ab.modifiers

        for m in mods:
            if m.type == 'ARMATURE':

                pose_lib = m.object.pose_library
                posemaker = pose_lib.pose_markers
                mName = m.name
                mObj = m.object

                for i,x in enumerate(posemaker):
                    #print (i,x.name,m.name,mObj)
                    bpy.context.view_layer.objects.active = mObj
                    bpy.ops.pose.select_all(action='SELECT')
                    bpy.ops.poselib.apply_pose(pose_index=i)
                    bpy.context.view_layer.objects.active = ab
                    bpy.context.object.modifiers[mName].name = x.name
                    bpy.ops.object.modifier_apply(apply_as='SHAPE', modifier=x.name)
                    newmod = ab.modifiers.new(mName,"ARMATURE")
                    newmod.object = mObj

        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator("pose.2morph")


classes = [
    P2M_OT_converter
]

# クラスの登録
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_MT_object.append(menu_func)

# クラスの登録解除
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

# main
if __name__ == "__main__":
    register()
