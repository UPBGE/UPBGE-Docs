BlendDataLibraries(bpy_struct)
==============================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: BlendDataLibraries(bpy_struct)

   Collection of libraries

   .. data:: is_updated

      :type: boolean, default False, (readonly)

   .. method:: tag(value)

      tag

      :arg value:

         Value

      :type value: boolean

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


   .. method:: load(filepath, link=False, relative=False)
   
      Returns a context manager which exposes 2 library objects on entering.
      Each object has attributes matching bpy.data which are lists of strings to be linked.
   
      :arg filepath: The path to a blend file.
      :type filepath: string
      :arg link: When False reference to the original file is lost.
      :type link: bool
      :arg relative: When True the path is stored relative to the open blend file.
      :type relative: bool



      .. literalinclude:: ..\examples\bpy.types.BlendDataLibraries.load.py


   .. method:: write(filepath, datablocks, relative_remap=False, fake_user=False, compress=False)
   
      Write data-blocks into a blend file.
   
      .. note::
   
         Indirectly referenced data-blocks will be expanded and written too.
   
      :arg filepath: The path to write the blend-file.
      :type filepath: string
      :arg datablocks: set of data-blocks (:class:`bpy.types.ID` instances).
      :type datablocks: set
      :arg relative_remap: When True, remap the paths relative to the current blend-file.
      :type relative_remap: bool
      :arg fake_user: When True, data-blocks will be written with fake-user flag enabled.
      :type fake_user: bool
      :arg compress: When True, write a compressed blend file.
      :type compress: bool



      .. literalinclude:: ..\examples\bpy.types.BlendDataLibraries.write.py


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

   * :class:`BlendData.libraries`

