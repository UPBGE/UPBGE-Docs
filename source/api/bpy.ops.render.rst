Render Operators
================

.. module:: bpy.ops.render

.. function:: cycles_integrator_preset_add(name="", remove_active=False)

   Add an Integrator Preset

   :arg name:

      Name, Name of the preset, used to make the path name

   :type name: string, (optional, never None)
   :arg remove_active:

      remove_active

   :type remove_active: boolean, (optional)

   :file: `startup\bl_operators\presets.py\:71 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\presets.py$71>`_

.. function:: cycles_sampling_preset_add(name="", remove_active=False)

   Add a Sampling Preset

   :arg name:

      Name, Name of the preset, used to make the path name

   :type name: string, (optional, never None)
   :arg remove_active:

      remove_active

   :type remove_active: boolean, (optional)

   :file: `startup\bl_operators\presets.py\:71 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\presets.py$71>`_

.. function:: opengl(animation=False, sequencer=False, write_still=False, view_context=True)

   OpenGL render active viewport

   :arg animation:

      Animation, Render files from the animation range of this scene

   :type animation: boolean, (optional)
   :arg sequencer:

      Sequencer, Render using the sequencer's OpenGL display

   :type sequencer: boolean, (optional)
   :arg write_still:

      Write Image, Save rendered the image to the output path (used only when animation is disabled)

   :type write_still: boolean, (optional)
   :arg view_context:

      View Context, Use the current 3D view for rendering, else use scene settings

   :type view_context: boolean, (optional)

.. function:: play_rendered_anim()

   Play back rendered frames/movies using an external player

   :file: `startup\bl_operators\screen_play_rendered_anim.py\:76 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\screen_play_rendered_anim.py$76>`_

.. function:: preset_add(name="", remove_active=False)

   Add or remove a Render Preset

   :arg name:

      Name, Name of the preset, used to make the path name

   :type name: string, (optional, never None)
   :arg remove_active:

      remove_active

   :type remove_active: boolean, (optional)

   :file: `startup\bl_operators\presets.py\:71 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\presets.py$71>`_

.. function:: render(animation=False, write_still=False, use_viewport=False, layer="", scene="")

   Render active scene

   :arg animation:

      Animation, Render files from the animation range of this scene

   :type animation: boolean, (optional)
   :arg write_still:

      Write Image, Save rendered the image to the output path (used only when animation is disabled)

   :type write_still: boolean, (optional)
   :arg use_viewport:

      Use 3D Viewport, When inside a 3D viewport, use layers and camera of the viewport

   :type use_viewport: boolean, (optional)
   :arg layer:

      Render Layer, Single render layer to re-render (used only when animation is disabled)

   :type layer: string, (optional, never None)
   :arg scene:

      Scene, Scene to render, current scene if not specified

   :type scene: string, (optional, never None)

.. function:: shutter_curve_preset(shape='SMOOTH')

   Set shutter curve

   :arg shape:

      Mode

   :type shape: enum in ['SHARP', 'SMOOTH', 'MAX', 'LINE', 'ROUND', 'ROOT'], (optional)

.. function:: view_cancel()

   Cancel show render view

.. function:: view_show()

   Toggle show render view

