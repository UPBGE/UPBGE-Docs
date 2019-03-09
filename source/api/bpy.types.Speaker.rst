Speaker(ID)
===========

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Speaker(ID)

   Speaker data-block for 3D audio speaker objects

   .. data:: animation_data

      Animation data for this data-block

      :type: :class:`AnimData`, (readonly)

   .. attribute:: attenuation

      How strong the distance affects volume, depending on distance model

      :type: float in [0, inf], default 0.0

   .. attribute:: cone_angle_inner

      Angle of the inner cone, in degrees, inside the cone the volume is 100 %

      :type: float in [0, 360], default 0.0

   .. attribute:: cone_angle_outer

      Angle of the outer cone, in degrees, outside this cone the volume is the outer cone volume, between inner and outer cone the volume is interpolated

      :type: float in [0, 360], default 0.0

   .. attribute:: cone_volume_outer

      Volume outside the outer cone

      :type: float in [0, 1], default 0.0

   .. attribute:: distance_max

      Maximum distance for volume calculation, no matter how far away the object is

      :type: float in [0, inf], default 0.0

   .. attribute:: distance_reference

      Reference distance at which volume is 100 %

      :type: float in [0, inf], default 0.0

   .. attribute:: muted

      Mute the speaker

      :type: boolean, default False

   .. attribute:: pitch

      Playback pitch of the sound

      :type: float in [0.1, 10], default 0.0

   .. data:: relative

      Whether the source is relative to the camera or not

      :type: boolean, default False, (readonly)

   .. attribute:: sound

      Sound data-block used by this speaker

      :type: :class:`Sound`

   .. attribute:: volume

      How loud the sound is

      :type: float in [0, 1], default 0.0

   .. attribute:: volume_max

      Maximum volume, no matter how near the object is

      :type: float in [0, 1], default 0.0

   .. attribute:: volume_min

      Minimum volume, no matter how far away the object is

      :type: float in [0, 1], default 0.0

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
   * :class:`ID.name`
   * :class:`ID.users`
   * :class:`ID.use_fake_user`
   * :class:`ID.tag`
   * :class:`ID.is_updated`
   * :class:`ID.is_updated_data`
   * :class:`ID.is_library_indirect`
   * :class:`ID.library`
   * :class:`ID.preview`

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
   * :class:`ID.copy`
   * :class:`ID.user_clear`
   * :class:`ID.user_remap`
   * :class:`ID.make_local`
   * :class:`ID.user_of_id`
   * :class:`ID.animation_data_create`
   * :class:`ID.animation_data_clear`
   * :class:`ID.update_tag`

.. rubric:: References

.. hlist::
   :columns: 2

   * :mod:`bpy.context.speaker`
   * :class:`BlendData.speakers`
   * :class:`BlendDataSpeakers.new`
   * :class:`BlendDataSpeakers.remove`

