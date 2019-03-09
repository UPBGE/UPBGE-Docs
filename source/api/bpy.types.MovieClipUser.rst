MovieClipUser(bpy_struct)
=========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: MovieClipUser(bpy_struct)

   Parameters defining how a MovieClip data-block is used by another data-block

   .. attribute:: frame_current

      Current frame number in movie or image sequence

      :type: int in [-1048574, 1048574], default 0

   .. attribute:: proxy_render_size

      Draw preview using full resolution or different proxy resolutions

      :type: enum in ['PROXY_25', 'PROXY_50', 'PROXY_75', 'PROXY_100', 'FULL'], default 'FULL'

   .. attribute:: use_render_undistorted

      Render preview using undistorted proxy

      :type: boolean, default False

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

.. rubric:: References

.. hlist::
   :columns: 2

   * :class:`BackgroundImage.clip_user`
   * :class:`SpaceClipEditor.clip_user`
   * :class:`UILayout.template_marker`
   * :class:`UILayout.template_movieclip_information`

