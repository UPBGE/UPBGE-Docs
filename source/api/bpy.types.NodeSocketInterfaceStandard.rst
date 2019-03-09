NodeSocketInterfaceStandard(NodeSocketInterface)
================================================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`NodeSocketInterface`

subclasses --- 
:class:`NodeSocketInterfaceBool`, :class:`NodeSocketInterfaceColor`, :class:`NodeSocketInterfaceFloat`, :class:`NodeSocketInterfaceFloatAngle`, :class:`NodeSocketInterfaceFloatFactor`, :class:`NodeSocketInterfaceFloatPercentage`, :class:`NodeSocketInterfaceFloatTime`, :class:`NodeSocketInterfaceFloatUnsigned`, :class:`NodeSocketInterfaceInt`, :class:`NodeSocketInterfaceIntFactor`, :class:`NodeSocketInterfaceIntPercentage`, :class:`NodeSocketInterfaceIntUnsigned`, :class:`NodeSocketInterfaceShader`, :class:`NodeSocketInterfaceString`, :class:`NodeSocketInterfaceVector`, :class:`NodeSocketInterfaceVectorAcceleration`, :class:`NodeSocketInterfaceVectorDirection`, :class:`NodeSocketInterfaceVectorEuler`, :class:`NodeSocketInterfaceVectorTranslation`, :class:`NodeSocketInterfaceVectorVelocity`, :class:`NodeSocketInterfaceVectorXYZ`

.. class:: NodeSocketInterfaceStandard(NodeSocketInterface)

   

   .. data:: type

      Data type

      :type: enum in ['CUSTOM', 'VALUE', 'INT', 'BOOLEAN', 'VECTOR', 'STRING', 'RGBA', 'SHADER'], default 'VALUE', (readonly)

   .. method:: draw(context, layout)

      Draw template settings

      :type context: :class:`Context`, (never None)
      :arg layout:

         Layout, Layout in the UI

      :type layout: :class:`UILayout`, (never None)

   .. method:: draw_color(context)

      Color of the socket icon

      :type context: :class:`Context`, (never None)
      :return:

         Color

      :rtype: float array of 4 items in [0, 1]

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
   * :class:`NodeSocketInterface.name`
   * :class:`NodeSocketInterface.identifier`
   * :class:`NodeSocketInterface.is_output`
   * :class:`NodeSocketInterface.bl_socket_idname`

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
   * :class:`NodeSocketInterface.draw`
   * :class:`NodeSocketInterface.draw_color`
   * :class:`NodeSocketInterface.register_properties`
   * :class:`NodeSocketInterface.init_socket`
   * :class:`NodeSocketInterface.from_socket`

