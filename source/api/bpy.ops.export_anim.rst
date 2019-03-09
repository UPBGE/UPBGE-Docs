Export Anim Operators
=====================

.. module:: bpy.ops.export_anim

.. function:: bvh(filepath="", check_existing=True, filter_glob="*.bvh", global_scale=1.0, frame_start=0, frame_end=0, rotate_mode='NATIVE', root_transform_only=False)

   Save a BVH motion capture file from an armature

   :arg filepath:

      File Path, Filepath used for exporting the file

   :type filepath: string, (optional, never None)
   :arg check_existing:

      Check Existing, Check and warn on overwriting existing files

   :type check_existing: boolean, (optional)
   :arg filter_glob:

      filter_glob

   :type filter_glob: string, (optional, never None)
   :arg global_scale:

      Scale, Scale the BVH by this value

   :type global_scale: float in [0.0001, 1e+06], (optional)
   :arg frame_start:

      Start Frame, Starting frame to export

   :type frame_start: int in [-inf, inf], (optional)
   :arg frame_end:

      End Frame, End frame to export

   :type frame_end: int in [-inf, inf], (optional)
   :arg rotate_mode:

      Rotation, Rotation conversion

      * ``NATIVE`` Euler (Native), Use the rotation order defined in the BVH file.
      * ``XYZ`` Euler (XYZ), Convert rotations to euler XYZ.
      * ``XZY`` Euler (XZY), Convert rotations to euler XZY.
      * ``YXZ`` Euler (YXZ), Convert rotations to euler YXZ.
      * ``YZX`` Euler (YZX), Convert rotations to euler YZX.
      * ``ZXY`` Euler (ZXY), Convert rotations to euler ZXY.
      * ``ZYX`` Euler (ZYX), Convert rotations to euler ZYX.

   :type rotate_mode: enum in ['NATIVE', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'], (optional)
   :arg root_transform_only:

      Root Translation Only, Only write out translation channels for the root bone

   :type root_transform_only: boolean, (optional)

   :file: `addons\io_anim_bvh\__init__.py\:202 <https://developer.blender.org/diffusion/BA/addons\io_anim_bvh\__init__.py$202>`_

