Sequences(bpy_struct)
=====================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: Sequences(bpy_struct)

   Collection of Sequences

   .. method:: new_clip(name, clip, channel, frame_start)

      Add a new movie clip sequence

      :arg name:

         Name for the new sequence

      :type name: string, (never None)
      :arg clip:

         Movie clip to add

      :type clip: :class:`MovieClip`, (never None)
      :arg channel:

         Channel, The channel for the new sequence

      :type channel: int in [1, 32]
      :arg frame_start:

         The start frame for the new sequence

      :type frame_start: int in [-1048574, 1048574]
      :return:

         New Sequence

      :rtype: :class:`Sequence`

   .. method:: new_mask(name, mask, channel, frame_start)

      Add a new mask sequence

      :arg name:

         Name for the new sequence

      :type name: string, (never None)
      :arg mask:

         Mask to add

      :type mask: :class:`Mask`, (never None)
      :arg channel:

         Channel, The channel for the new sequence

      :type channel: int in [1, 32]
      :arg frame_start:

         The start frame for the new sequence

      :type frame_start: int in [-1048574, 1048574]
      :return:

         New Sequence

      :rtype: :class:`Sequence`

   .. method:: new_scene(name, scene, channel, frame_start)

      Add a new scene sequence

      :arg name:

         Name for the new sequence

      :type name: string, (never None)
      :arg scene:

         Scene to add

      :type scene: :class:`Scene`, (never None)
      :arg channel:

         Channel, The channel for the new sequence

      :type channel: int in [1, 32]
      :arg frame_start:

         The start frame for the new sequence

      :type frame_start: int in [-1048574, 1048574]
      :return:

         New Sequence

      :rtype: :class:`Sequence`

   .. method:: new_image(name, filepath, channel, frame_start)

      Add a new image sequence

      :arg name:

         Name for the new sequence

      :type name: string, (never None)
      :arg filepath:

         Filepath to image

      :type filepath: string, (never None)
      :arg channel:

         Channel, The channel for the new sequence

      :type channel: int in [1, 32]
      :arg frame_start:

         The start frame for the new sequence

      :type frame_start: int in [-1048574, 1048574]
      :return:

         New Sequence

      :rtype: :class:`Sequence`

   .. method:: new_movie(name, filepath, channel, frame_start)

      Add a new movie sequence

      :arg name:

         Name for the new sequence

      :type name: string, (never None)
      :arg filepath:

         Filepath to movie

      :type filepath: string, (never None)
      :arg channel:

         Channel, The channel for the new sequence

      :type channel: int in [1, 32]
      :arg frame_start:

         The start frame for the new sequence

      :type frame_start: int in [-1048574, 1048574]
      :return:

         New Sequence

      :rtype: :class:`Sequence`

   .. method:: new_sound(name, filepath, channel, frame_start)

      Add a new sound sequence

      :arg name:

         Name for the new sequence

      :type name: string, (never None)
      :arg filepath:

         Filepath to movie

      :type filepath: string, (never None)
      :arg channel:

         Channel, The channel for the new sequence

      :type channel: int in [1, 32]
      :arg frame_start:

         The start frame for the new sequence

      :type frame_start: int in [-1048574, 1048574]
      :return:

         New Sequence

      :rtype: :class:`Sequence`

   .. method:: new_effect(name, type, channel, frame_start, frame_end=0, seq1=None, seq2=None, seq3=None)

      Add a new effect sequence

      :arg name:

         Name for the new sequence

      :type name: string, (never None)
      :arg type:

         Type, type for the new sequence

      :type type: enum in ['CROSS', 'ADD', 'SUBTRACT', 'ALPHA_OVER', 'ALPHA_UNDER', 'GAMMA_CROSS', 'MULTIPLY', 'OVER_DROP', 'WIPE', 'GLOW', 'TRANSFORM', 'COLOR', 'SPEED', 'MULTICAM', 'ADJUSTMENT', 'GAUSSIAN_BLUR', 'TEXT', 'COLORMIX']
      :arg channel:

         Channel, The channel for the new sequence

      :type channel: int in [1, 32]
      :arg frame_start:

         The start frame for the new sequence

      :type frame_start: int in [-inf, inf]
      :arg frame_end:

         The end frame for the new sequence

      :type frame_end: int in [-inf, inf], (optional)
      :arg seq1:

         Sequence 1 for effect

      :type seq1: :class:`Sequence`, (optional)
      :arg seq2:

         Sequence 2 for effect

      :type seq2: :class:`Sequence`, (optional)
      :arg seq3:

         Sequence 3 for effect

      :type seq3: :class:`Sequence`, (optional)
      :return:

         New Sequence

      :rtype: :class:`Sequence`

   .. method:: remove(sequence)

      Remove a Sequence

      :arg sequence:

         Sequence to remove

      :type sequence: :class:`Sequence`, (never None)

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

   * :class:`SequenceEditor.sequences`

