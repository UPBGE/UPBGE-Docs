Brush Operators
===============

.. module:: bpy.ops.brush

.. function:: active_index_set(mode="", index=0)

   Set active sculpt/paint brush from it's number

   :arg mode:

      Mode, Paint mode to set brush for

   :type mode: string, (optional, never None)
   :arg index:

      Number, Brush number

   :type index: int in [-inf, inf], (optional)

   :file: `startup\bl_operators\wm.py\:168 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\wm.py$168>`_

.. function:: add()

   Add brush by mode type

.. function:: curve_preset(shape='SMOOTH')

   Set brush shape

   :arg shape:

      Mode

   :type shape: enum in ['SHARP', 'SMOOTH', 'MAX', 'LINE', 'ROUND', 'ROOT'], (optional)

.. function:: reset()

   Return brush to defaults based on current tool

.. function:: scale_size(scalar=1.0)

   Change brush size by a scalar

   :arg scalar:

      Scalar, Factor to scale brush size by

   :type scalar: float in [0, 2], (optional)

.. function:: stencil_control(mode='TRANSLATION', texmode='PRIMARY')

   Control the stencil brush

   :arg mode:

      Tool

   :type mode: enum in ['TRANSLATION', 'SCALE', 'ROTATION'], (optional)
   :arg texmode:

      Tool

   :type texmode: enum in ['PRIMARY', 'SECONDARY'], (optional)

.. function:: stencil_fit_image_aspect(use_repeat=True, use_scale=True, mask=False)

   When using an image texture, adjust the stencil size to fit the image aspect ratio

   :arg use_repeat:

      Use Repeat, Use repeat mapping values

   :type use_repeat: boolean, (optional)
   :arg use_scale:

      Use Scale, Use texture scale values

   :type use_scale: boolean, (optional)
   :arg mask:

      Modify Mask Stencil, Modify either the primary or mask stencil

   :type mask: boolean, (optional)

.. function:: stencil_reset_transform(mask=False)

   Reset the stencil transformation to the default

   :arg mask:

      Modify Mask Stencil, Modify either the primary or mask stencil

   :type mask: boolean, (optional)

.. function:: uv_sculpt_tool_set(tool='PINCH')

   Set the UV sculpt tool

   :arg tool:

      Tool

      * ``PINCH`` Pinch, Pinch UVs.
      * ``RELAX`` Relax, Relax UVs.
      * ``GRAB`` Grab, Grab UVs.

   :type tool: enum in ['PINCH', 'RELAX', 'GRAB'], (optional)

