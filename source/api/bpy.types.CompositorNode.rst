CompositorNode(NodeInternal)
============================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`Node`, :class:`NodeInternal`

subclasses --- 
:class:`CompositorNodeAlphaOver`, :class:`CompositorNodeBilateralblur`, :class:`CompositorNodeBlur`, :class:`CompositorNodeBokehBlur`, :class:`CompositorNodeBokehImage`, :class:`CompositorNodeBoxMask`, :class:`CompositorNodeBrightContrast`, :class:`CompositorNodeChannelMatte`, :class:`CompositorNodeChromaMatte`, :class:`CompositorNodeColorBalance`, :class:`CompositorNodeColorCorrection`, :class:`CompositorNodeColorMatte`, :class:`CompositorNodeColorSpill`, :class:`CompositorNodeCombHSVA`, :class:`CompositorNodeCombRGBA`, :class:`CompositorNodeCombYCCA`, :class:`CompositorNodeCombYUVA`, :class:`CompositorNodeComposite`, :class:`CompositorNodeCornerPin`, :class:`CompositorNodeCrop`, :class:`CompositorNodeCurveRGB`, :class:`CompositorNodeCurveVec`, :class:`CompositorNodeDBlur`, :class:`CompositorNodeDefocus`, :class:`CompositorNodeDespeckle`, :class:`CompositorNodeDiffMatte`, :class:`CompositorNodeDilateErode`, :class:`CompositorNodeDisplace`, :class:`CompositorNodeDistanceMatte`, :class:`CompositorNodeDoubleEdgeMask`, :class:`CompositorNodeEllipseMask`, :class:`CompositorNodeFilter`, :class:`CompositorNodeFlip`, :class:`CompositorNodeGamma`, :class:`CompositorNodeGlare`, :class:`CompositorNodeGroup`, :class:`CompositorNodeHueCorrect`, :class:`CompositorNodeHueSat`, :class:`CompositorNodeIDMask`, :class:`CompositorNodeImage`, :class:`CompositorNodeInpaint`, :class:`CompositorNodeInvert`, :class:`CompositorNodeKeying`, :class:`CompositorNodeKeyingScreen`, :class:`CompositorNodeLensdist`, :class:`CompositorNodeLevels`, :class:`CompositorNodeLumaMatte`, :class:`CompositorNodeMapRange`, :class:`CompositorNodeMapUV`, :class:`CompositorNodeMapValue`, :class:`CompositorNodeMask`, :class:`CompositorNodeMath`, :class:`CompositorNodeMixRGB`, :class:`CompositorNodeMovieClip`, :class:`CompositorNodeMovieDistortion`, :class:`CompositorNodeNormal`, :class:`CompositorNodeNormalize`, :class:`CompositorNodeOutputFile`, :class:`CompositorNodePixelate`, :class:`CompositorNodePlaneTrackDeform`, :class:`CompositorNodePremulKey`, :class:`CompositorNodeRGB`, :class:`CompositorNodeRGBToBW`, :class:`CompositorNodeRLayers`, :class:`CompositorNodeRotate`, :class:`CompositorNodeScale`, :class:`CompositorNodeSepHSVA`, :class:`CompositorNodeSepRGBA`, :class:`CompositorNodeSepYCCA`, :class:`CompositorNodeSepYUVA`, :class:`CompositorNodeSetAlpha`, :class:`CompositorNodeSplitViewer`, :class:`CompositorNodeStabilize`, :class:`CompositorNodeSunBeams`, :class:`CompositorNodeSwitch`, :class:`CompositorNodeSwitchView`, :class:`CompositorNodeTexture`, :class:`CompositorNodeTime`, :class:`CompositorNodeTonemap`, :class:`CompositorNodeTrackPos`, :class:`CompositorNodeTransform`, :class:`CompositorNodeTranslate`, :class:`CompositorNodeValToRGB`, :class:`CompositorNodeValue`, :class:`CompositorNodeVecBlur`, :class:`CompositorNodeViewer`, :class:`CompositorNodeZcombine`

.. class:: CompositorNode(NodeInternal)

   

   .. method:: tag_need_exec()

      Tag the node for compositor update


   .. method:: update()

   .. classmethod:: bl_rna_get_subclass(id, default=None)
   
      :arg id: The RNA type identifier.
      :type id: string
      :return: The RNA type or default when not found.
      :rtype: :class:`bpy.types.Struct` subclass


   .. classmethod:: bl_rna_get_subclass_py(id, default=None)
   
      :arg id: The RNA type identifier.
      :type id: string
      :return: The class or default when not found.
      :rtype: type


.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`Node.type`
   * :class:`Node.location`
   * :class:`Node.width`
   * :class:`Node.width_hidden`
   * :class:`Node.height`
   * :class:`Node.dimensions`
   * :class:`Node.name`
   * :class:`Node.label`
   * :class:`Node.inputs`
   * :class:`Node.outputs`
   * :class:`Node.internal_links`
   * :class:`Node.parent`
   * :class:`Node.use_custom_color`
   * :class:`Node.color`
   * :class:`Node.select`
   * :class:`Node.show_options`
   * :class:`Node.show_preview`
   * :class:`Node.hide`
   * :class:`Node.mute`
   * :class:`Node.show_texture`
   * :class:`Node.shading_compatibility`
   * :class:`Node.bl_idname`
   * :class:`Node.bl_label`
   * :class:`Node.bl_description`
   * :class:`Node.bl_icon`
   * :class:`Node.bl_static_type`
   * :class:`Node.bl_width_default`
   * :class:`Node.bl_width_min`
   * :class:`Node.bl_width_max`
   * :class:`Node.bl_height_default`
   * :class:`Node.bl_height_min`
   * :class:`Node.bl_height_max`

.. rubric:: Inherited Functions

.. hlist::
   :columns: 2

   * :class:`bpy_struct.as_pointer`
   * :class:`bpy_struct.driver_add`
   * :class:`bpy_struct.driver_remove`
   * :class:`bpy_struct.get`
   * :class:`bpy_struct.is_property_hidden`
   * :class:`bpy_struct.is_property_readonly`
   * :class:`bpy_struct.is_property_set`
   * :class:`bpy_struct.items`
   * :class:`bpy_struct.keyframe_delete`
   * :class:`bpy_struct.keyframe_insert`
   * :class:`bpy_struct.keys`
   * :class:`bpy_struct.path_from_id`
   * :class:`bpy_struct.path_resolve`
   * :class:`bpy_struct.property_unset`
   * :class:`bpy_struct.type_recast`
   * :class:`bpy_struct.values`
   * :class:`Node.socket_value_update`
   * :class:`Node.is_registered_node_type`
   * :class:`Node.poll`
   * :class:`Node.poll_instance`
   * :class:`Node.update`
   * :class:`Node.insert_link`
   * :class:`Node.init`
   * :class:`Node.copy`
   * :class:`Node.free`
   * :class:`Node.draw_buttons`
   * :class:`Node.draw_buttons_ext`
   * :class:`Node.draw_label`
   * :class:`Node.poll`
   * :class:`NodeInternal.poll`
   * :class:`NodeInternal.poll_instance`
   * :class:`NodeInternal.update`
   * :class:`NodeInternal.draw_buttons`
   * :class:`NodeInternal.draw_buttons_ext`

