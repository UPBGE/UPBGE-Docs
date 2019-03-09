Poselib Operators
=================

.. module:: bpy.ops.poselib

.. function:: action_sanitize()

   Make action suitable for use as a Pose Library

.. function:: apply_pose(pose_index=-1)

   Apply specified Pose Library pose to the rig

   :arg pose_index:

      Pose, Index of the pose to apply (-2 for no change to pose, -1 for poselib active pose)

   :type pose_index: int in [-2, inf], (optional)

.. function:: browse_interactive(pose_index=-1)

   Interactively browse poses in 3D-View

   :arg pose_index:

      Pose, Index of the pose to apply (-2 for no change to pose, -1 for poselib active pose)

   :type pose_index: int in [-2, inf], (optional)

.. function:: new()

   Add New Pose Library to active Object

.. function:: pose_add(frame=1, name="Pose")

   Add the current Pose to the active Pose Library

   :arg frame:

      Frame, Frame to store pose on

   :type frame: int in [0, inf], (optional)
   :arg name:

      Pose Name, Name of newly added Pose

   :type name: string, (optional, never None)

.. function:: pose_move(pose='', direction='UP')

   Move the pose up or down in the active Pose Library

   :arg pose:

      Pose, The pose to move

   :type pose: enum in [], (optional)
   :arg direction:

      Direction, Direction to move the chosen pose towards

   :type direction: enum in ['UP', 'DOWN'], (optional)

.. function:: pose_remove(pose='')

   Remove nth pose from the active Pose Library

   :arg pose:

      Pose, The pose to remove

   :type pose: enum in [], (optional)

.. function:: pose_rename(name="RenamedPose", pose='')

   Rename specified pose from the active Pose Library

   :arg name:

      New Pose Name, New name for pose

   :type name: string, (optional, never None)
   :arg pose:

      Pose, The pose to rename

   :type pose: enum in [], (optional)

.. function:: unlink()

   Remove Pose Library from active Object

