bpy_extras submodule (bpy_extras.io_utils)
==========================================

.. module:: bpy_extras.io_utils

.. function:: orientation_helper_factory(name, axis_forward='Y', axis_up='Z')

.. function:: axis_conversion(from_forward='Y', from_up='Z', to_forward='Y', to_up='Z')

   Each argument us an axis in ['X', 'Y', 'Z', '-X', '-Y', '-Z']
   where the first 2 are a source and the second 2 are the target.

.. function:: axis_conversion_ensure(operator, forward_attr, up_attr)

   Function to ensure an operator has valid axis conversion settings, intended
   to be used from :class:`bpy.types.Operator.check`.
   
   :arg operator: the operator to access axis attributes from.
   :type operator: :class:`bpy.types.Operator`
   :arg forward_attr: attribute storing the forward axis
   :type forward_attr: string
   :arg up_attr: attribute storing the up axis
   :type up_attr: string
   :return: True if the value was modified.
   :rtype: boolean

.. function:: create_derived_objects(scene, ob)

.. function:: free_derived_objects(ob)

.. function:: unpack_list(list_of_tuples)

.. function:: unpack_face_list(list_of_tuples)

.. function:: path_reference(filepath, base_src, base_dst, mode='AUTO', copy_subdir='', copy_set=None, library=None)

   Return a filepath relative to a destination directory, for use with
   exporters.
   
   :arg filepath: the file path to return,
      supporting blenders relative '//' prefix.
   :type filepath: string
   :arg base_src: the directory the *filepath* is relative too
      (normally the blend file).
   :type base_src: string
   :arg base_dst: the directory the *filepath* will be referenced from
      (normally the export path).
   :type base_dst: string
   :arg mode: the method used get the path in
      ['AUTO', 'ABSOLUTE', 'RELATIVE', 'MATCH', 'STRIP', 'COPY']
   :type mode: string
   :arg copy_subdir: the subdirectory of *base_dst* to use when mode='COPY'.
   :type copy_subdir: string
   :arg copy_set: collect from/to pairs when mode='COPY',
      pass to *path_reference_copy* when exporting is done.
   :type copy_set: set
   :arg library: The library this path is relative to.
   :type library: :class:`bpy.types.Library` or None
   :return: the new filepath.
   :rtype: string

.. function:: path_reference_copy(copy_set, report=<built-in function print>)

   Execute copying files of path_reference
   
   :arg copy_set: set of (from, to) pairs to copy.
   :type copy_set: set
   :arg report: function used for reporting warnings, takes a string argument.
   :type report: function

.. function:: unique_name(key, name, name_dict, name_max=-1, clean_func=None, sep='.')

   Helper function for storing unique names which may have special characters
   stripped and restricted to a maximum length.
   
   :arg key: unique item this name belongs to, name_dict[key] will be reused
      when available.
      This can be the object, mesh, material, etc instance its self.
   :type key: any hashable object associated with the *name*.
   :arg name: The name used to create a unique value in *name_dict*.
   :type name: string
   :arg name_dict: This is used to cache namespace to ensure no collisions
      occur, this should be an empty dict initially and only modified by this
      function.
   :type name_dict: dict
   :arg clean_func: Function to call on *name* before creating a unique value.
   :type clean_func: function
   :arg sep: Separator to use when between the name and a number when a
      duplicate name is found.
   :type sep: string

.. data:: path_reference_mode

   constant value (<built-in function EnumProperty>, {'name': 'Path Mode', 'description': 'Method used to reference paths', 'items': (('AUTO', 'Auto', 'Use Relative paths with subdirectories only'), ('ABSOLUTE', 'Absolute', 'Always write absolute paths'), ('RELATIVE', 'Relative', 'Always write relative paths (where possible)'), ('MATCH', 'Match', 'Match Absolute/Relative setting with input path'), ('STRIP', 'Strip Path', 'Filename only'), ('COPY', 'Copy', 'Copy the file to the destination path (or subdirectory)')), 'default': 'AUTO', 'attr': 'path_mode'})

.. class:: ExportHelper


   .. method:: check(context)

   .. method:: invoke(context, event)



.. class:: ImportHelper


   .. method:: check(context)

   .. method:: invoke(context, event)



