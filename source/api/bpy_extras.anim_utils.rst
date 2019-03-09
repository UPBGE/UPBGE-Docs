bpy_extras submodule (bpy_extras.anim_utils)
============================================

.. module:: bpy_extras.anim_utils

.. function:: bake_action(obj, *, action, frames, **kwargs)

   :arg obj: Object to bake.
   :type obj: :class:`bpy.types.Object`
   :arg action: An action to bake the data into, or None for a new action
      to be created.
   :type action: :class:`bpy.types.Action` or None
   :arg frames: Frames to bake.
   :type frames: iterable of int
   
   :return: an action or None
   :rtype: :class:`bpy.types.Action`

.. function:: bake_action_objects(object_action_pairs, *, frames, **kwargs)

   A version of :func:`bake_action_objects_iter` that takes frames and returns the output.
   
   :arg frames: Frames to bake.
   :type frames: iterable of int
   
   :return: A sequence of Action or None types (aligned with `object_action_pairs`)
   :rtype: sequence of :class:`bpy.types.Action`

.. function:: bake_action_iter(obj, *, action, only_selected=False, do_pose=True, do_object=True, do_visual_keying=True, do_constraint_clear=False, do_parents_clear=False, do_clean=False)

   An coroutine that bakes action for a single object.
   
   :arg obj: Object to bake.
   :type obj: :class:`bpy.types.Object`
   :arg action: An action to bake the data into, or None for a new action
      to be created.
   :type action: :class:`bpy.types.Action` or None
   :arg only_selected: Only bake selected bones.
   :type only_selected: bool
   :arg do_pose: Bake pose channels.
   :type do_pose: bool
   :arg do_object: Bake objects.
   :type do_object: bool
   :arg do_visual_keying: Use the final transformations for baking ('visual keying')
   :type do_visual_keying: bool
   :arg do_constraint_clear: Remove constraints after baking.
   :type do_constraint_clear: bool
   :arg do_parents_clear: Unparent after baking objects.
   :type do_parents_clear: bool
   :arg do_clean: Remove redundant keyframes after baking.
   :type do_clean: bool
   
   :return: an action or None
   :rtype: :class:`bpy.types.Action`

.. function:: bake_action_objects_iter(object_action_pairs, **kwargs)

   An coroutine that bakes actions for multiple objects.
   
   :arg object_action_pairs: Sequence of object action tuples,
      action is the destination for the baked data. When None a new action will be created.
   :type object_action_pairs: Sequence of (:class:`bpy.types.Object`, :class:`bpy.types.Action`)

