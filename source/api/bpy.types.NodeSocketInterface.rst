NodeSocketInterface(bpy_struct)
===============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

subclasses --- 
:class:`NodeSocketInterfaceStandard`

.. class:: NodeSocketInterface(bpy_struct)

   Parameters to define node sockets

   .. attribute:: bl_socket_idname

      :type: string, default "", (never None)

   .. data:: identifier

      Unique identifier for mapping sockets

      :type: string, default "", (readonly, never None)

   .. data:: is_output

      True if the socket is an output, otherwise input

      :type: boolean, default False, (readonly)

   .. attribute:: name

      Socket name

      :type: string, default "", (never None)

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

   .. method:: register_properties(data_rna_type)

      Define RNA properties of a socket

      :arg data_rna_type:

         Data RNA Type, RNA type for special socket properties

      :type data_rna_type: :class:`Struct`

   .. method:: init_socket(node, socket, data_path)

      Initialize a node socket instance

      :arg node:

         Node, Node of the socket to initialize

      :type node: :class:`Node`, (never None)
      :arg socket:

         Socket, Socket to initialize

      :type socket: :class:`NodeSocket`, (never None)
      :arg data_path:

         Data Path, Path to specialized socket data

      :type data_path: string, (never None)

   .. method:: from_socket(node, socket)

      Setup template parameters from an existing socket

      :arg node:

         Node, Node of the original socket

      :type node: :class:`Node`, (never None)
      :arg socket:

         Socket, Original socket

      :type socket: :class:`NodeSocket`, (never None)

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

   * :class:`NodeTree.inputs`
   * :class:`NodeTree.outputs`
   * :class:`NodeTreeInputs.new`
   * :class:`NodeTreeInputs.remove`
   * :class:`NodeTreeOutputs.new`
   * :class:`NodeTreeOutputs.remove`

