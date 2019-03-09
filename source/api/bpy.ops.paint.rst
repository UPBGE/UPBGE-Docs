Paint Operators
===============

.. module:: bpy.ops.paint

.. function:: add_simple_uvs()

   Add cube map uvs on mesh

.. function:: add_texture_paint_slot(type='DIFFUSE_COLOR', name="Untitled", width=1024, height=1024, color=(0.0, 0.0, 0.0, 1.0), alpha=True, generated_type='BLANK', float=False)

   Add a texture paint slot

   :arg type:

      Type, Merge method to use

   :type type: enum in ['DIFFUSE_COLOR', 'DIFFUSE_INTENSITY', 'ALPHA', 'TRANSLUCENCY', 'SPECULAR_COLOR', 'SPECULAR_INTENSITY', 'SPECULAR_HARDNESS', 'AMBIENT', 'EMIT', 'MIRROR_COLOR', 'RAYMIRROR', 'NORMAL', 'WARP', 'DISPLACE'], (optional)
   :arg name:

      Name, Image data-block name

   :type name: string, (optional, never None)
   :arg width:

      Width, Image width

   :type width: int in [1, inf], (optional)
   :arg height:

      Height, Image height

   :type height: int in [1, inf], (optional)
   :arg color:

      Color, Default fill color

   :type color: float array of 4 items in [0, inf], (optional)
   :arg alpha:

      Alpha, Create an image with an alpha channel

   :type alpha: boolean, (optional)
   :arg generated_type:

      Generated Type, Fill the image with a grid for UV map testing

      * ``BLANK`` Blank, Generate a blank image.
      * ``UV_GRID`` UV Grid, Generated grid to test UV mappings.
      * ``COLOR_GRID`` Color Grid, Generated improved UV grid to test UV mappings.

   :type generated_type: enum in ['BLANK', 'UV_GRID', 'COLOR_GRID'], (optional)
   :arg float:

      32 bit Float, Create image with 32 bit floating point bit depth

   :type float: boolean, (optional)

.. function:: brush_colors_flip()

   Toggle foreground and background brush colors

.. function:: brush_select(paint_mode='ACTIVE', sculpt_tool='BLOB', vertex_paint_tool='MIX', weight_paint_tool='MIX', texture_paint_tool='DRAW', toggle=False, create_missing=False)

   Select a paint mode's brush by tool type

   :arg paint_mode:

      Paint Mode

      * ``ACTIVE`` Current, Set brush for active paint mode.
      * ``SCULPT`` Sculpt.
      * ``VERTEX_PAINT`` Vertex Paint.
      * ``WEIGHT_PAINT`` Weight Paint.
      * ``TEXTURE_PAINT`` Texture Paint.

   :type paint_mode: enum in ['ACTIVE', 'SCULPT', 'VERTEX_PAINT', 'WEIGHT_PAINT', 'TEXTURE_PAINT'], (optional)
   :arg sculpt_tool:

      Sculpt Tool

   :type sculpt_tool: enum in ['BLOB', 'CLAY', 'CLAY_STRIPS', 'CREASE', 'DRAW', 'FILL', 'FLATTEN', 'GRAB', 'INFLATE', 'LAYER', 'MASK', 'NUDGE', 'PINCH', 'ROTATE', 'SCRAPE', 'SIMPLIFY', 'SMOOTH', 'SNAKE_HOOK', 'THUMB'], (optional)
   :arg vertex_paint_tool:

      Vertex Paint Tool

      * ``MIX`` Mix, Use mix blending mode while painting.
      * ``ADD`` Add, Use add blending mode while painting.
      * ``SUB`` Subtract, Use subtract blending mode while painting.
      * ``MUL`` Multiply, Use multiply blending mode while painting.
      * ``BLUR`` Blur, Blur the color with surrounding values.
      * ``LIGHTEN`` Lighten, Use lighten blending mode while painting.
      * ``DARKEN`` Darken, Use darken blending mode while painting.
      * ``AVERAGE`` Average, Use average blending mode while painting.
      * ``SMEAR`` Smear, Use smear blending mode while painting.
      * ``COLORDODGE`` Color Dodge, Use color dodge blending mode while painting.
      * ``DIFFERENCE`` Difference, Use difference blending mode while painting.
      * ``SCREEN`` Screen, Use screen blending mode while painting.
      * ``HARDLIGHT`` Hardlight, Use hardlight blending mode while painting.
      * ``OVERLAY`` Overlay, Use overlay blending mode while painting.
      * ``SOFTLIGHT`` Softlight, Use softlight blending mode while painting.
      * ``EXCLUSION`` Exclusion, Use exclusion blending mode while painting.
      * ``LUMINOCITY`` Luminocity, Use luminocity blending mode while painting.
      * ``SATURATION`` Saturation, Use saturation blending mode while painting.
      * ``HUE`` Hue, Use hue blending mode while painting.
      * ``ERASE_ALPHA`` Erase Alpha, Erase alpha while painting.
      * ``ADD_ALPHA`` Add Alpha, Add alpha while painting.

   :type vertex_paint_tool: enum in ['MIX', 'ADD', 'SUB', 'MUL', 'BLUR', 'LIGHTEN', 'DARKEN', 'AVERAGE', 'SMEAR', 'COLORDODGE', 'DIFFERENCE', 'SCREEN', 'HARDLIGHT', 'OVERLAY', 'SOFTLIGHT', 'EXCLUSION', 'LUMINOCITY', 'SATURATION', 'HUE', 'ERASE_ALPHA', 'ADD_ALPHA'], (optional)
   :arg weight_paint_tool:

      Weight Paint Tool

      * ``MIX`` Mix, Use mix blending mode while painting.
      * ``ADD`` Add, Use add blending mode while painting.
      * ``SUB`` Subtract, Use subtract blending mode while painting.
      * ``MUL`` Multiply, Use multiply blending mode while painting.
      * ``BLUR`` Blur, Blur the color with surrounding values.
      * ``LIGHTEN`` Lighten, Use lighten blending mode while painting.
      * ``DARKEN`` Darken, Use darken blending mode while painting.
      * ``AVERAGE`` Average, Use average blending mode while painting.
      * ``SMEAR`` Smear, Use smear blending mode while painting.
      * ``COLORDODGE`` Color Dodge, Use color dodge blending mode while painting.
      * ``DIFFERENCE`` Difference, Use difference blending mode while painting.
      * ``SCREEN`` Screen, Use screen blending mode while painting.
      * ``HARDLIGHT`` Hardlight, Use hardlight blending mode while painting.
      * ``OVERLAY`` Overlay, Use overlay blending mode while painting.
      * ``SOFTLIGHT`` Softlight, Use softlight blending mode while painting.
      * ``EXCLUSION`` Exclusion, Use exclusion blending mode while painting.
      * ``LUMINOCITY`` Luminocity, Use luminocity blending mode while painting.
      * ``SATURATION`` Saturation, Use saturation blending mode while painting.
      * ``HUE`` Hue, Use hue blending mode while painting.
      * ``ERASE_ALPHA`` Erase Alpha, Erase alpha while painting.
      * ``ADD_ALPHA`` Add Alpha, Add alpha while painting.

   :type weight_paint_tool: enum in ['MIX', 'ADD', 'SUB', 'MUL', 'BLUR', 'LIGHTEN', 'DARKEN', 'AVERAGE', 'SMEAR', 'COLORDODGE', 'DIFFERENCE', 'SCREEN', 'HARDLIGHT', 'OVERLAY', 'SOFTLIGHT', 'EXCLUSION', 'LUMINOCITY', 'SATURATION', 'HUE', 'ERASE_ALPHA', 'ADD_ALPHA'], (optional)
   :arg texture_paint_tool:

      Texture Paint Tool

   :type texture_paint_tool: enum in ['DRAW', 'SOFTEN', 'SMEAR', 'CLONE', 'FILL', 'MASK'], (optional)
   :arg toggle:

      Toggle, Toggle between two brushes rather than cycling

   :type toggle: boolean, (optional)
   :arg create_missing:

      Create Missing, If the requested brush type does not exist, create a new brush

   :type create_missing: boolean, (optional)

.. function:: delete_texture_paint_slot()

   Delete selected texture paint slot

.. function:: face_select_all(action='TOGGLE')

   Change selection for all faces

   :arg action:

      Action, Selection action to execute

      * ``TOGGLE`` Toggle, Toggle selection for all elements.
      * ``SELECT`` Select, Select all elements.
      * ``DESELECT`` Deselect, Deselect all elements.
      * ``INVERT`` Invert, Invert selection of all elements.

   :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

.. function:: face_select_hide(unselected=False)

   Hide selected faces

   :arg unselected:

      Unselected, Hide unselected rather than selected objects

   :type unselected: boolean, (optional)

.. function:: face_select_linked()

   Select linked faces

.. function:: face_select_linked_pick(deselect=False)

   Select linked faces under the cursor

   :arg deselect:

      Deselect, Deselect rather than select items

   :type deselect: boolean, (optional)

.. function:: face_select_reveal(select=True)

   Reveal hidden faces

   :arg select:

      Select

   :type select: boolean, (optional)

.. function:: grab_clone(delta=(0.0, 0.0))

   Move the clone source image

   :arg delta:

      Delta, Delta offset of clone image in 0.0..1.0 coordinates

   :type delta: float array of 2 items in [-inf, inf], (optional)

.. function:: hide_show(action='HIDE', area='INSIDE', xmin=0, xmax=0, ymin=0, ymax=0)

   Hide/show some vertices

   :arg action:

      Action, Whether to hide or show vertices

      * ``HIDE`` Hide, Hide vertices.
      * ``SHOW`` Show, Show vertices.

   :type action: enum in ['HIDE', 'SHOW'], (optional)
   :arg area:

      Area, Which vertices to hide or show

      * ``OUTSIDE`` Outside, Hide or show vertices outside the selection.
      * ``INSIDE`` Inside, Hide or show vertices inside the selection.
      * ``ALL`` All, Hide or show all vertices.
      * ``MASKED`` Masked, Hide or show vertices that are masked (minimum mask value of 0.5).

   :type area: enum in ['OUTSIDE', 'INSIDE', 'ALL', 'MASKED'], (optional)
   :arg xmin:

      X Min

   :type xmin: int in [-inf, inf], (optional)
   :arg xmax:

      X Max

   :type xmax: int in [-inf, inf], (optional)
   :arg ymin:

      Y Min

   :type ymin: int in [-inf, inf], (optional)
   :arg ymax:

      Y Max

   :type ymax: int in [-inf, inf], (optional)

.. function:: image_from_view(filepath="")

   Make an image from the current 3D view for re-projection

   :arg filepath:

      File Path, Name of the file

   :type filepath: string, (optional, never None)

.. function:: image_paint(stroke=None, mode='NORMAL')

   Paint a stroke into the image

   :arg stroke:

      Stroke

   :type stroke: :class:`bpy_prop_collection` of :class:`OperatorStrokeElement`, (optional)
   :arg mode:

      Stroke Mode, Action taken when a paint stroke is made

      * ``NORMAL`` Normal, Apply brush normally.
      * ``INVERT`` Invert, Invert action of brush for duration of stroke.
      * ``SMOOTH`` Smooth, Switch brush to smooth mode for duration of stroke.

   :type mode: enum in ['NORMAL', 'INVERT', 'SMOOTH'], (optional)

.. function:: mask_flood_fill(mode='VALUE', value=0.0)

   Fill the whole mask with a given value, or invert its values

   :arg mode:

      Mode

      * ``VALUE`` Value, Set mask to the level specified by the 'value' property.
      * ``VALUE_INVERSE`` Value Inverted, Set mask to the level specified by the inverted 'value' property.
      * ``INVERT`` Invert, Invert the mask.

   :type mode: enum in ['VALUE', 'VALUE_INVERSE', 'INVERT'], (optional)
   :arg value:

      Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked

   :type value: float in [0, 1], (optional)

.. function:: mask_lasso_gesture(path=None, mode='VALUE', value=1.0)

   Add mask within the lasso as you move the brush

   :arg path:

      Path

   :type path: :class:`bpy_prop_collection` of :class:`OperatorMousePath`, (optional)
   :arg mode:

      Mode

      * ``VALUE`` Value, Set mask to the level specified by the 'value' property.
      * ``VALUE_INVERSE`` Value Inverted, Set mask to the level specified by the inverted 'value' property.
      * ``INVERT`` Invert, Invert the mask.

   :type mode: enum in ['VALUE', 'VALUE_INVERSE', 'INVERT'], (optional)
   :arg value:

      Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked

   :type value: float in [0, 1], (optional)

.. function:: project_image(image='')

   Project an edited render from the active camera back onto the object

   :arg image:

      Image

   :type image: enum in [], (optional)

.. function:: sample_color(location=(0, 0), merged=False, palette=False)

   Use the mouse to sample a color in the image

   :arg location:

      Location

   :type location: int array of 2 items in [0, inf], (optional)
   :arg merged:

      Sample Merged, Sample the output display color

   :type merged: boolean, (optional)
   :arg palette:

      Add to Palette

   :type palette: boolean, (optional)

.. function:: texture_paint_toggle()

   Toggle texture paint mode in 3D view

.. function:: vert_select_all(action='TOGGLE')

   Change selection for all vertices

   :arg action:

      Action, Selection action to execute

      * ``TOGGLE`` Toggle, Toggle selection for all elements.
      * ``SELECT`` Select, Select all elements.
      * ``DESELECT`` Deselect, Deselect all elements.
      * ``INVERT`` Invert, Invert selection of all elements.

   :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

.. function:: vert_select_ungrouped(extend=False)

   Select vertices without a group

   :arg extend:

      Extend, Extend the selection

   :type extend: boolean, (optional)

.. function:: vertex_color_brightness_contrast(brightness=0.0, contrast=0.0)

   Adjust vertex color brightness/contrast

   :arg brightness:

      Brightness

   :type brightness: float in [-100, 100], (optional)
   :arg contrast:

      Contrast

   :type contrast: float in [-100, 100], (optional)

.. function:: vertex_color_dirt(blur_strength=1.0, blur_iterations=1, clean_angle=3.14159, dirt_angle=0.0, dirt_only=False)

   Undocumented

   :arg blur_strength:

      Blur Strength, Blur strength per iteration

   :type blur_strength: float in [0.01, 1], (optional)
   :arg blur_iterations:

      Blur Iterations, Number of times to blur the colors (higher blurs more)

   :type blur_iterations: int in [0, 40], (optional)
   :arg clean_angle:

      Highlight Angle, Less than 90 limits the angle used in the tonal range

   :type clean_angle: float in [0, 3.14159], (optional)
   :arg dirt_angle:

      Dirt Angle, Less than 90 limits the angle used in the tonal range

   :type dirt_angle: float in [0, 3.14159], (optional)
   :arg dirt_only:

      Dirt Only, Don't calculate cleans for convex areas

   :type dirt_only: boolean, (optional)

   :file: `startup\bl_operators\vertexpaint_dirt.py\:178 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\vertexpaint_dirt.py$178>`_

.. function:: vertex_color_from_weight()

   Convert active weight into gray scale vertex colors

.. function:: vertex_color_hsv(h=0.5, s=1.0, v=1.0)

   Adjust vertex color HSV values

   :arg h:

      Hue

   :type h: float in [0, 1], (optional)
   :arg s:

      Saturation

   :type s: float in [0, 2], (optional)
   :arg v:

      Value

   :type v: float in [0, 2], (optional)

.. function:: vertex_color_invert()

   Invert RGB values

.. function:: vertex_color_levels(offset=0.0, gain=1.0)

   Adjust levels of vertex colors

   :arg offset:

      Offset, Value to add to colors

   :type offset: float in [-1, 1], (optional)
   :arg gain:

      Gain, Value to multiply colors by

   :type gain: float in [0, inf], (optional)

.. function:: vertex_color_set()

   Fill the active vertex color layer with the current paint color

.. function:: vertex_color_smooth()

   Smooth colors across vertices

.. function:: vertex_paint(stroke=None, mode='NORMAL')

   Paint a stroke in the active vertex color layer

   :arg stroke:

      Stroke

   :type stroke: :class:`bpy_prop_collection` of :class:`OperatorStrokeElement`, (optional)
   :arg mode:

      Stroke Mode, Action taken when a paint stroke is made

      * ``NORMAL`` Normal, Apply brush normally.
      * ``INVERT`` Invert, Invert action of brush for duration of stroke.
      * ``SMOOTH`` Smooth, Switch brush to smooth mode for duration of stroke.

   :type mode: enum in ['NORMAL', 'INVERT', 'SMOOTH'], (optional)

.. function:: vertex_paint_toggle()

   Toggle the vertex paint mode in 3D view

.. function:: weight_from_bones(type='AUTOMATIC')

   Set the weights of the groups matching the attached armature's selected bones, using the distance between the vertices and the bones

   :arg type:

      Type, Method to use for assigning weights

      * ``AUTOMATIC`` Automatic, Automatic weights from bones.
      * ``ENVELOPES`` From Envelopes, Weights from envelopes with user defined radius.

   :type type: enum in ['AUTOMATIC', 'ENVELOPES'], (optional)

.. function:: weight_gradient(type='LINEAR', xstart=0, xend=0, ystart=0, yend=0, cursor=1002)

   Draw a line to apply a weight gradient to selected vertices

   :arg type:

      Type

   :type type: enum in ['LINEAR', 'RADIAL'], (optional)
   :arg xstart:

      X Start

   :type xstart: int in [-inf, inf], (optional)
   :arg xend:

      X End

   :type xend: int in [-inf, inf], (optional)
   :arg ystart:

      Y Start

   :type ystart: int in [-inf, inf], (optional)
   :arg yend:

      Y End

   :type yend: int in [-inf, inf], (optional)
   :arg cursor:

      Cursor, Mouse cursor style to use during the modal operator

   :type cursor: int in [0, inf], (optional)

.. function:: weight_paint(stroke=None, mode='NORMAL')

   Paint a stroke in the current vertex group's weights

   :arg stroke:

      Stroke

   :type stroke: :class:`bpy_prop_collection` of :class:`OperatorStrokeElement`, (optional)
   :arg mode:

      Stroke Mode, Action taken when a paint stroke is made

      * ``NORMAL`` Normal, Apply brush normally.
      * ``INVERT`` Invert, Invert action of brush for duration of stroke.
      * ``SMOOTH`` Smooth, Switch brush to smooth mode for duration of stroke.

   :type mode: enum in ['NORMAL', 'INVERT', 'SMOOTH'], (optional)

.. function:: weight_paint_toggle()

   Toggle weight paint mode in 3D view

.. function:: weight_sample()

   Use the mouse to sample a weight in the 3D view

.. function:: weight_sample_group(group='DEFAULT')

   Select one of the vertex groups available under current mouse position

   :arg group:

      Keying Set, The Keying Set to use

   :type group: enum in ['DEFAULT'], (optional)

.. function:: weight_set()

   Fill the active vertex group with the current paint weight

