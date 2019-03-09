Scene Operators
===============

.. module:: bpy.ops.scene

.. function:: delete()

   Delete active scene

.. function:: freestyle_add_edge_marks_to_keying_set()

   Add the data paths to the Freestyle Edge Mark property of selected edges to the active keying set

   :file: `startup\bl_operators\freestyle.py\:144 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\freestyle.py$144>`_

.. function:: freestyle_add_face_marks_to_keying_set()

   Add the data paths to the Freestyle Face Mark property of selected polygons to the active keying set

   :file: `startup\bl_operators\freestyle.py\:175 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\freestyle.py$175>`_

.. function:: freestyle_alpha_modifier_add(type='ALONG_STROKE')

   Add an alpha transparency modifier to the line style associated with the active lineset

   :arg type:

      Type

   :type type: enum in ['ALONG_STROKE', 'CREASE_ANGLE', 'CURVATURE_3D', 'DISTANCE_FROM_CAMERA', 'DISTANCE_FROM_OBJECT', 'MATERIAL', 'NOISE', 'TANGENT'], (optional)

.. function:: freestyle_color_modifier_add(type='ALONG_STROKE')

   Add a line color modifier to the line style associated with the active lineset

   :arg type:

      Type

   :type type: enum in ['ALONG_STROKE', 'CREASE_ANGLE', 'CURVATURE_3D', 'DISTANCE_FROM_CAMERA', 'DISTANCE_FROM_OBJECT', 'MATERIAL', 'NOISE', 'TANGENT'], (optional)

.. function:: freestyle_fill_range_by_selection(type='COLOR', name="")

   Fill the Range Min/Max entries by the min/max distance between selected mesh objects and the source object

   :arg type:

      Type, Type of the modifier to work on

      * ``COLOR`` Color, Color modifier type.
      * ``ALPHA`` Alpha, Alpha modifier type.
      * ``THICKNESS`` Thickness, Thickness modifier type.

   :type type: enum in ['COLOR', 'ALPHA', 'THICKNESS'], (optional)
   :arg name:

      Name, Name of the modifier to work on

   :type name: string, (optional, never None)

   :file: `startup\bl_operators\freestyle.py\:53 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\freestyle.py$53>`_

.. function:: freestyle_geometry_modifier_add(type='2D_OFFSET')

   Add a stroke geometry modifier to the line style associated with the active lineset

   :arg type:

      Type

   :type type: enum in ['2D_OFFSET', '2D_TRANSFORM', 'BACKBONE_STRETCHER', 'BEZIER_CURVE', 'BLUEPRINT', 'GUIDING_LINES', 'PERLIN_NOISE_1D', 'PERLIN_NOISE_2D', 'POLYGONIZATION', 'SAMPLING', 'SIMPLIFICATION', 'SINUS_DISPLACEMENT', 'SPATIAL_NOISE', 'TIP_REMOVER'], (optional)

.. function:: freestyle_lineset_add()

   Add a line set into the list of line sets

.. function:: freestyle_lineset_copy()

   Copy the active line set to a buffer

.. function:: freestyle_lineset_move(direction='UP')

   Change the position of the active line set within the list of line sets

   :arg direction:

      Direction, Direction to move the active line set towards

   :type direction: enum in ['UP', 'DOWN'], (optional)

.. function:: freestyle_lineset_paste()

   Paste the buffer content to the active line set

.. function:: freestyle_lineset_remove()

   Remove the active line set from the list of line sets

.. function:: freestyle_linestyle_new()

   Create a new line style, reusable by multiple line sets

.. function:: freestyle_modifier_copy()

   Duplicate the modifier within the list of modifiers

.. function:: freestyle_modifier_move(direction='UP')

   Move the modifier within the list of modifiers

   :arg direction:

      Direction, Direction to move the chosen modifier towards

   :type direction: enum in ['UP', 'DOWN'], (optional)

.. function:: freestyle_modifier_remove()

   Remove the modifier from the list of modifiers

.. function:: freestyle_module_add()

   Add a style module into the list of modules

.. function:: freestyle_module_move(direction='UP')

   Change the position of the style module within in the list of style modules

   :arg direction:

      Direction, Direction to move the chosen style module towards

   :type direction: enum in ['UP', 'DOWN'], (optional)

.. function:: freestyle_module_open(filepath="", make_internal=True)

   Open a style module file

   :arg filepath:

      filepath

   :type filepath: string, (optional, never None)
   :arg make_internal:

      Make internal, Make module file internal after loading

   :type make_internal: boolean, (optional)

   :file: `startup\bl_operators\freestyle.py\:219 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\freestyle.py$219>`_

.. function:: freestyle_module_remove()

   Remove the style module from the stack

.. function:: freestyle_stroke_material_create()

   Create Freestyle stroke material for testing

.. function:: freestyle_thickness_modifier_add(type='ALONG_STROKE')

   Add a line thickness modifier to the line style associated with the active lineset

   :arg type:

      Type

   :type type: enum in ['ALONG_STROKE', 'CALLIGRAPHY', 'CREASE_ANGLE', 'CURVATURE_3D', 'DISTANCE_FROM_CAMERA', 'DISTANCE_FROM_OBJECT', 'MATERIAL', 'NOISE', 'TANGENT'], (optional)

.. function:: new(type='NEW')

   Add new scene by type

   :arg type:

      Type

      * ``NEW`` New, Add new scene.
      * ``EMPTY`` Copy Settings, Make a copy without any objects.
      * ``LINK_OBJECTS`` Link Objects, Link to the objects from the current scene.
      * ``LINK_OBJECT_DATA`` Link Object Data, Copy objects linked to data from the current scene.
      * ``FULL_COPY`` Full Copy, Make a full copy of the current scene.

   :type type: enum in ['NEW', 'EMPTY', 'LINK_OBJECTS', 'LINK_OBJECT_DATA', 'FULL_COPY'], (optional)

.. function:: render_layer_add()

   Add a render layer

.. function:: render_layer_remove()

   Remove the selected render layer

.. function:: render_view_add()

   Add a render view

.. function:: render_view_remove()

   Remove the selected render view

.. function:: units_length_preset_add(name="", remove_active=False)

   Add or remove length units preset

   :arg name:

      Name, Name of the preset, used to make the path name

   :type name: string, (optional, never None)
   :arg remove_active:

      remove_active

   :type remove_active: boolean, (optional)

   :file: `startup\bl_operators\presets.py\:71 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\presets.py$71>`_

