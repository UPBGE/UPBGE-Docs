ID Property Access (idprop.types)
=================================

.. module:: idprop.types

.. class:: IDPropertyArray


   .. method:: to_list()
   
      Return the array as a list.


   .. attribute:: typecode

      The type of the data in the array {'f': float, 'd': double, 'i': int}.




.. class:: IDPropertyGroup


   .. method:: clear()
   
      Clear all members from this group.


   .. method:: get(key, default=None)
   
      Return the value for key, if it exists, else default.


   .. method:: items()
   
      Return the items associated with this group.


   .. method:: iteritems()
   
      Iterate through the items in the dict; behaves like dictionary method iteritems.


   .. method:: keys()
   
      Return the keys associated with this group as a list of strings.


   .. method:: pop(key)
   
      Remove an item from the group, returning a Python representation.
   
      :raises KeyError: When the item doesn't exist.
   
      :arg key: Name of item to remove.
      :type key: string


   .. method:: to_dict()
   
      Return a purely python version of the group.


   .. method:: update(other)
   
      Update key, values.
   
      :arg other: Updates the values in the group with this.
      :type other: :class:`IDPropertyGroup` or dict


   .. method:: values()
   
      Return the values associated with this group.


   .. attribute:: name

      The name of this Group.




.. class:: IDPropertyGroupIter




