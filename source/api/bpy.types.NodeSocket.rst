NodeSocket(bpy_struct)
======================

.. module:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`NodeSocketStandard`

.. class:: NodeSocket(bpy_struct)

   Input or output socket of a node

   .. attribute:: bl_idname

      :type: string, default "", (never None)

   .. attribute:: draw_shape

      Socket shape

      :type: enum in ['CIRCLE', 'SQUARE', 'DIAMOND'], default 'CIRCLE'

   .. attribute:: enabled

      Enable the socket

      :type: boolean, default False

   .. attribute:: hide

      Hide the socket

      :type: boolean, default False

   .. attribute:: hide_value

      Hide the socket input value

      :type: boolean, default False

   .. data:: identifier

      Unique identifier for mapping sockets

      :type: string, default "", (readonly, never None)

   .. data:: is_linked

      True if the socket is connected

      :type: boolean, default False, (readonly)

   .. data:: is_output

      True if the socket is an output, otherwise input

      :type: boolean, default False, (readonly)

   .. attribute:: link_limit

      Max number of links allowed for this socket

      :type: int in [1, 4095], default 0

   .. attribute:: name

      Socket name

      :type: string, default "", (never None)

   .. data:: node

      Node owning this socket

      :type: :class:`Node`, (readonly)

   .. attribute:: show_expanded

      Socket links are expanded in the user interface

      :type: boolean, default False

   .. attribute:: type

      Data type

      :type: enum in ['CUSTOM', 'VALUE', 'INT', 'BOOLEAN', 'VECTOR', 'STRING', 'RGBA', 'SHADER'], default 'VALUE'

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

   * :class:`CompositorNodeOutputFileFileSlots.new`
   * :class:`CompositorNodeOutputFileFileSlots.remove`
   * :class:`CompositorNodeOutputFileLayerSlots.new`
   * :class:`CompositorNodeOutputFileLayerSlots.remove`
   * :class:`Node.inputs`
   * :class:`Node.outputs`
   * :class:`NodeInputs.new`
   * :class:`NodeInputs.remove`
   * :class:`NodeLink.from_socket`
   * :class:`NodeLink.to_socket`
   * :class:`NodeLinks.new`
   * :class:`NodeLinks.new`
   * :class:`NodeOutputs.new`
   * :class:`NodeOutputs.remove`
   * :class:`NodeSocketInterface.from_socket`
   * :class:`NodeSocketInterface.init_socket`
   * :class:`UILayout.template_node_link`
   * :class:`UILayout.template_node_view`

