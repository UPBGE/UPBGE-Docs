bpy_prop_collection
===================

.. module:: bpy.types

.. class:: bpy_prop_collection

   built-in class used for all collections.

   .. note::

      Note that bpy.types.bpy_prop_collection is not actually available from within Blender,
      it only exists for the purpose of documentation.

   .. method:: find(key)
   
      Returns the index of a key in a collection or -1 when not found
      (matches pythons string find function of the same name).
   
      :arg key: The identifier for the collection member.
      :type key: string
      :return: index of the key.
      :rtype: int


   .. method:: foreach_get(attr, seq)
   
      This is a function to give fast access to attributes within a collection.

      Only works for 'basic type' properties (bool, int and float)!
      Multi-dimensional arrays (like array of vectors) will be flattened into seq.

      .. literalinclude:: ..\examples\bpy.types.bpy_prop_collection.foreach_get.py
         :lines: 5-


   .. method:: foreach_set(attr, seq)
   
      This is a function to give fast access to attributes within a collection.

      Only works for 'basic type' properties (bool, int and float)!
      seq must be uni-dimensional, multi-dimensional arrays (like array of vectors) will be re-created from it.

      .. literalinclude:: ..\examples\bpy.types.bpy_prop_collection.foreach_set.py
         :lines: 5-


   .. method:: get(key, default=None)
   
      Returns the value of the item assigned to key or default when not found
      (matches pythons dictionary function of the same name).
   
      :arg key: The identifier for the collection member.
      :type key: string
      :arg default: Optional argument for the value to return if
         *key* is not found.
      :type default: Undefined


   .. method:: items()
   
      Return the identifiers of collection members
      (matching pythons dict.items() functionality).
   
      :return: (key, value) pairs for each member of this collection.
      :rtype: list of tuples


   .. method:: keys()
   
      Return the identifiers of collection members
      (matching pythons dict.keys() functionality).
   
      :return: the identifiers for each member of this collection.
      :rtype: list of strings


   .. method:: values()
   
      Return the values of collection
      (matching pythons dict.values() functionality).
   
      :return: the members of this collection.
      :rtype: list


