Group Operators
===============

.. module:: bpy.ops.group

.. function:: create(name="Group")

   Create an object group from selected objects

   :arg name:

      Name, Name of the new group

   :type name: string, (optional, never None)

.. function:: objects_add_active(group='')

   Add the object to an object group that contains the active object

   :arg group:

      Group, The group to add other selected objects to

   :type group: enum in [], (optional)

.. function:: objects_remove(group='')

   Remove selected objects from a group

   :arg group:

      Group, The group to remove this object from

   :type group: enum in [], (optional)

.. function:: objects_remove_active(group='')

   Remove the object from an object group that contains the active object

   :arg group:

      Group, The group to remove other selected objects from

   :type group: enum in [], (optional)

.. function:: objects_remove_all()

   Remove selected objects from all groups

