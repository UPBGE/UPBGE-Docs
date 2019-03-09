SequenceProxy(bpy_struct)
=========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: SequenceProxy(bpy_struct)

   Proxy parameters for a sequence strip

   .. attribute:: build_100

      Build 100% proxy resolution

      :type: boolean, default False

   .. attribute:: build_25

      Build 25% proxy resolution

      :type: boolean, default False

   .. attribute:: build_50

      Build 50% proxy resolution

      :type: boolean, default False

   .. attribute:: build_75

      Build 75% proxy resolution

      :type: boolean, default False

   .. attribute:: build_free_run

      Build free run time code index

      :type: boolean, default False

   .. attribute:: build_free_run_rec_date

      Build free run time code index using Record Date/Time

      :type: boolean, default False

   .. attribute:: build_record_run

      Build record run time code index

      :type: boolean, default False

   .. attribute:: directory

      Location to store the proxy files

      :type: string, default "", (never None)

   .. attribute:: filepath

      Location of custom proxy file

      :type: string, default "", (never None)

   .. attribute:: quality

      JPEG Quality of proxies to build

      :type: int in [0, 32767], default 0

   .. attribute:: timecode

      Method for reading the inputs timecode

      * ``NONE`` No TC in use.
      * ``RECORD_RUN`` Record Run, Use images in the order as they are recorded.
      * ``FREE_RUN`` Free Run, Use global timestamp written by recording device.
      * ``FREE_RUN_REC_DATE`` Free Run (rec date), Interpolate a global timestamp using the record date and time written by recording device.
      * ``RECORD_RUN_NO_GAPS`` Record Run No Gaps, Like record run, but ignore timecode, changes in framerate or dropouts.

      :type: enum in ['NONE', 'RECORD_RUN', 'FREE_RUN', 'FREE_RUN_REC_DATE', 'RECORD_RUN_NO_GAPS'], default 'NONE'

   .. attribute:: use_overwrite

      Overwrite existing proxy files when building

      :type: boolean, default False

   .. attribute:: use_proxy_custom_directory

      Use a custom directory to store data

      :type: boolean, default False

   .. attribute:: use_proxy_custom_file

      Use a custom file to read proxy data from

      :type: boolean, default False

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

   * :class:`EffectSequence.proxy`
   * :class:`ImageSequence.proxy`
   * :class:`MetaSequence.proxy`
   * :class:`MovieSequence.proxy`
   * :class:`SceneSequence.proxy`

