NodeSocketStandard(NodeSocket)
==============================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`NodeSocket`

subclasses --- 
:class:`NodeSocketBool`, :class:`NodeSocketColor`, :class:`NodeSocketFloat`, :class:`NodeSocketFloatAngle`, :class:`NodeSocketFloatFactor`, :class:`NodeSocketFloatPercentage`, :class:`NodeSocketFloatTime`, :class:`NodeSocketFloatUnsigned`, :class:`NodeSocketInt`, :class:`NodeSocketIntFactor`, :class:`NodeSocketIntPercentage`, :class:`NodeSocketIntUnsigned`, :class:`NodeSocketShader`, :class:`NodeSocketString`, :class:`NodeSocketVector`, :class:`NodeSocketVectorAcceleration`, :class:`NodeSocketVectorDirection`, :class:`NodeSocketVectorEuler`, :class:`NodeSocketVectorTranslation`, :class:`NodeSocketVectorVelocity`, :class:`NodeSocketVectorXYZ`, :class:`NodeSocketVirtual`

.. class:: NodeSocketStandard(NodeSocket)

   

   .. data:: links

      List of node links from or to this socket
      (readonly)

   .. method:: draw(context, layout, node, text)

      Draw socket

      :type context: :class:`Context`, (never None)
      :arg layout:

         Layout, Layout in the UI

      :type layout: :class:`UILayout`, (never None)
      :arg node:

         Node, Node the socket belongs to

      :type node: :class:`Node`, (never None)
      :arg text:

         Text, Text label to draw alongside properties

      :type text: string, (never None)

   .. method:: draw_color(context, node)

      Color of the socket icon

      :type context: :class:`Context`, (never None)
      :arg node:

         Node, Node the socket belongs to

      :type node: :class:`Node`, (never None)
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
   * :class:`NodeSocket.name`
   * :class:`NodeSocket.identifier`
   * :class:`NodeSocket.is_output`
   * :class:`NodeSocket.hide`
   * :class:`NodeSocket.enabled`
   * :class:`NodeSocket.link_limit`
   * :class:`NodeSocket.is_linked`
   * :class:`NodeSocket.show_expanded`
   * :class:`NodeSocket.hide_value`
   * :class:`NodeSocket.node`
   * :class:`NodeSocket.type`
   * :class:`NodeSocket.draw_shape`
   * :class:`NodeSocket.bl_idname`
   * :class:`NodeSocket.links`
   * :class:`NodeSocket.links`

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
   * :class:`NodeSocket.draw`
   * :class:`NodeSocket.draw_color`

