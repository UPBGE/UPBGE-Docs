CyclesLampSettings(bpy_struct)
==============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: CyclesLampSettings(bpy_struct)

   

   .. attribute:: cast_shadow

      Lamp casts shadows

      :type: boolean, default True

   .. attribute:: is_portal

      Use this area lamp to guide sampling of the background, note that this will make the lamp invisible

      :type: boolean, default False

   .. attribute:: max_bounces

      Maximum number of bounces the light will contribute to the render

      :type: int in [0, 1024], default 1024

   .. attribute:: samples

      Number of light samples to render for each AA sample

      :type: int in [1, 10000], default 1

   .. attribute:: use_multiple_importance_sampling

      Use multiple importance sampling for the lamp, reduces noise for area lamps and sharp glossy materials

      :type: boolean, default True

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

