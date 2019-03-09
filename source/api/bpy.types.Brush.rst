Brush(ID)
=========

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: Brush(ID)

   Brush data-block for storing brush settings for painting and sculpting

   .. attribute:: auto_smooth_factor

      Amount of smoothing to automatically apply to each stroke

      :type: float in [0, 1], default 0.0

   .. attribute:: blend

      Brush blending mode

      * ``MIX`` Mix, Use mix blending mode while painting.
      * ``ADD`` Add, Use add blending mode while painting.
      * ``SUB`` Subtract, Use subtract blending mode while painting.
      * ``MUL`` Multiply, Use multiply blending mode while painting.
      * ``LIGHTEN`` Lighten, Use lighten blending mode while painting.
      * ``DARKEN`` Darken, Use darken blending mode while painting.
      * ``ERASE_ALPHA`` Erase Alpha, Erase alpha while painting.
      * ``ADD_ALPHA`` Add Alpha, Add alpha while painting.
      * ``OVERLAY`` Overlay, Use overlay blending mode while painting.
      * ``HARDLIGHT`` Hard light, Use hard light blending mode while painting.
      * ``COLORBURN`` Color burn, Use color burn blending mode while painting.
      * ``LINEARBURN`` Linear burn, Use linear burn blending mode while painting.
      * ``COLORDODGE`` Color dodge, Use color dodge blending mode while painting.
      * ``SCREEN`` Screen, Use screen blending mode while painting.
      * ``SOFTLIGHT`` Soft light, Use softlight blending mode while painting.
      * ``PINLIGHT`` Pin light, Use pinlight blending mode while painting.
      * ``VIVIDLIGHT`` Vivid light, Use vividlight blending mode while painting.
      * ``LINEARLIGHT`` Linear light, Use linearlight blending mode while painting.
      * ``DIFFERENCE`` Difference, Use difference blending mode while painting.
      * ``EXCLUSION`` Exclusion, Use exclusion blending mode while painting.
      * ``HUE`` Hue, Use hue blending mode while painting.
      * ``SATURATION`` Saturation, Use saturation blending mode while painting.
      * ``LUMINOSITY`` Luminosity, Use luminosity blending mode while painting.
      * ``COLOR`` Color, Use color blending mode while painting.

      :type: enum in ['MIX', 'ADD', 'SUB', 'MUL', 'LIGHTEN', 'DARKEN', 'ERASE_ALPHA', 'ADD_ALPHA', 'OVERLAY', 'HARDLIGHT', 'COLORBURN', 'LINEARBURN', 'COLORDODGE', 'SCREEN', 'SOFTLIGHT', 'PINLIGHT', 'VIVIDLIGHT', 'LINEARLIGHT', 'DIFFERENCE', 'EXCLUSION', 'HUE', 'SATURATION', 'LUMINOSITY', 'COLOR'], default 'MIX'

   .. attribute:: blur_kernel_radius

      Radius of kernel used for soften and sharpen in pixels

      :type: int in [1, 10000], default 0

   .. attribute:: blur_mode

      :type: enum in ['BOX', 'GAUSSIAN'], default 'GAUSSIAN'

   .. data:: brush_capabilities

      Brush's capabilities

      :type: :class:`BrushCapabilities`, (readonly, never None)

   .. attribute:: clone_alpha

      Opacity of clone image display

      :type: float in [0, 1], default 0.0

   .. attribute:: clone_image

      Image for clone tool

      :type: :class:`Image`

   .. attribute:: clone_offset

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: color

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: crease_pinch_factor

      How much the crease brush pinches

      :type: float in [0, 1], default 0.666667

   .. attribute:: cursor_color_add

      Color of cursor when adding

      :type: float array of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. attribute:: cursor_color_subtract

      Color of cursor when subtracting

      :type: float array of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. attribute:: cursor_overlay_alpha

      :type: int in [0, 100], default 0

   .. data:: curve

      Editable falloff curve

      :type: :class:`CurveMapping`, (readonly, never None)

   .. attribute:: direction

      * ``ADD`` Add, Add effect of brush.
      * ``SUBTRACT`` Subtract, Subtract effect of brush.

      :type: enum in ['ADD', 'SUBTRACT'], default 'ADD'

   .. attribute:: falloff_angle

      Paint most on faces pointing towards the view according to this angle

      :type: float in [0, 1.5708], default 0.0

   .. attribute:: fill_threshold

      Threshold above which filling is not propagated

      :type: float in [0, 100], default 0.0

   .. attribute:: grad_spacing

      Spacing before brush gradient goes full circle

      :type: int in [1, 10000], default 0

   .. data:: gradient

      :type: :class:`ColorRamp`, (readonly)

   .. attribute:: gradient_fill_mode

      :type: enum in ['LINEAR', 'RADIAL'], default 'LINEAR'

   .. attribute:: gradient_stroke_mode

      :type: enum in ['PRESSURE', 'SPACING_REPEAT', 'SPACING_CLAMP'], default 'PRESSURE'

   .. attribute:: height

      Affectable height of brush (layer height for layer tool, i.e.)

      :type: float in [0, 1], default 0.5

   .. attribute:: icon_filepath

      File path to brush icon

      :type: string, default "", (never None)

   .. data:: image_paint_capabilities

      Brush's capabilities in image paint mode

      :type: :class:`ImapaintToolCapabilities`, (readonly, never None)

   .. attribute:: image_tool

      :type: enum in ['DRAW', 'SOFTEN', 'SMEAR', 'CLONE', 'FILL', 'MASK'], default 'DRAW'

   .. attribute:: jitter

      Jitter the position of the brush while painting

      :type: float in [0, 1000], default 0.0

   .. attribute:: jitter_absolute

      Jitter the position of the brush in pixels while painting

      :type: int in [0, 1000000], default 0

   .. attribute:: mask_overlay_alpha

      :type: int in [0, 100], default 0

   .. attribute:: mask_stencil_dimension

      Dimensions of mask stencil in viewport

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: mask_stencil_pos

      Position of mask stencil in viewport

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: mask_texture

      :type: :class:`Texture`

   .. data:: mask_texture_slot

      :type: :class:`BrushTextureSlot`, (readonly)

   .. attribute:: mask_tool

      :type: enum in ['DRAW', 'SMOOTH'], default 'DRAW'

   .. attribute:: normal_weight

      How much grab will pull vertexes out of surface during a grab

      :type: float in [0, 1], default 0.0

   .. attribute:: paint_curve

      Active Paint Curve

      :type: :class:`PaintCurve`

   .. attribute:: plane_offset

      Adjust plane on which the brush acts towards or away from the object surface

      :type: float in [-2, 2], default 0.0

   .. attribute:: plane_trim

      If a vertex is further away from offset plane than this, then it is not affected

      :type: float in [0, 1], default 0.5

   .. attribute:: rake_factor

      How much grab will follow cursor rotation

      :type: float in [0, 10], default 0.0

   .. attribute:: rate

      Interval between paints for Airbrush

      :type: float in [0.0001, 10000], default 0.0

   .. data:: sculpt_capabilities

      Brush's capabilities in sculpt mode

      :type: :class:`SculptToolCapabilities`, (readonly, never None)

   .. attribute:: sculpt_plane

      :type: enum in ['AREA', 'VIEW', 'X', 'Y', 'Z'], default 'AREA'

   .. attribute:: sculpt_tool

      :type: enum in ['BLOB', 'CLAY', 'CLAY_STRIPS', 'CREASE', 'DRAW', 'FILL', 'FLATTEN', 'GRAB', 'INFLATE', 'LAYER', 'MASK', 'NUDGE', 'PINCH', 'ROTATE', 'SCRAPE', 'SIMPLIFY', 'SMOOTH', 'SNAKE_HOOK', 'THUMB'], default 'BLOB'

   .. attribute:: secondary_color

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: sharp_threshold

      Threshold below which, no sharpening is done

      :type: float in [0, 100], default 0.0

   .. attribute:: size

      Radius of the brush in pixels

      :type: int in [1, 5000], default 0

   .. attribute:: smooth_stroke_factor

      Higher values give a smoother stroke

      :type: float in [0.5, 0.99], default 0.0

   .. attribute:: smooth_stroke_radius

      Minimum distance from last point before stroke continues

      :type: int in [10, 200], default 0

   .. attribute:: spacing

      Spacing between brush daubs as a percentage of brush diameter

      :type: int in [1, 1000], default 0

   .. attribute:: stencil_dimension

      Dimensions of stencil in viewport

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: stencil_pos

      Position of stencil in viewport

      :type: float array of 2 items in [-inf, inf], default (0.0, 0.0)

   .. attribute:: strength

      How powerful the effect of the brush is when applied

      :type: float in [0, 10], default 0.5

   .. attribute:: stroke_method

      * ``DOTS`` Dots, Apply paint on each mouse move step.
      * ``DRAG_DOT`` Drag Dot, Allows a single dot to be carefully positioned.
      * ``SPACE`` Space, Limit brush application to the distance specified by spacing.
      * ``AIRBRUSH`` Airbrush, Keep applying paint effect while holding mouse (spray).
      * ``ANCHORED`` Anchored, Keep the brush anchored to the initial location.
      * ``LINE`` Line, Draw a line with dabs separated according to spacing.
      * ``CURVE`` Curve, Define the stroke curve with a bezier curve (dabs are separated according to spacing).

      :type: enum in ['DOTS', 'DRAG_DOT', 'SPACE', 'AIRBRUSH', 'ANCHORED', 'LINE', 'CURVE'], default 'DOTS'

   .. attribute:: texture

      :type: :class:`Texture`

   .. attribute:: texture_overlay_alpha

      :type: int in [0, 100], default 0

   .. attribute:: texture_sample_bias

      Value added to texture samples

      :type: float in [-1, 1], default 0.0

   .. data:: texture_slot

      :type: :class:`BrushTextureSlot`, (readonly)

   .. attribute:: unprojected_radius

      Radius of brush in Blender units

      :type: float in [0.001, inf], default 0.0

   .. attribute:: use_accumulate

      Accumulate stroke daubs on top of each other

      :type: boolean, default False

   .. attribute:: use_adaptive_space

      Space daubs according to surface orientation instead of screen space

      :type: boolean, default False

   .. attribute:: use_airbrush

      Keep applying paint effect while holding mouse (spray)

      :type: boolean, default False

   .. attribute:: use_alpha

      When this is disabled, lock alpha while painting

      :type: boolean, default False

   .. attribute:: use_anchor

      Keep the brush anchored to the initial location

      :type: boolean, default False

   .. attribute:: use_cursor_overlay

      Show cursor in viewport

      :type: boolean, default False

   .. attribute:: use_cursor_overlay_override

      Don't show overlay during a stroke

      :type: boolean, default False

   .. attribute:: use_curve

      Define the stroke curve with a bezier curve. Dabs are separated according to spacing

      :type: boolean, default False

   .. attribute:: use_custom_icon

      Set the brush icon from an image file

      :type: boolean, default False

   .. attribute:: use_edge_to_edge

      Drag anchor brush from edge-to-edge

      :type: boolean, default False

   .. attribute:: use_frontface

      Brush only affects vertexes that face the viewer

      :type: boolean, default False

   .. attribute:: use_frontface_falloff

      Blend brush influence by how much they face the front

      :type: boolean, default False

   .. attribute:: use_gradient

      Use Gradient by utilizing a sampling method

      :type: boolean, default False

   .. attribute:: use_inverse_smooth_pressure

      Lighter pressure causes more smoothing to be applied

      :type: boolean, default False

   .. attribute:: use_line

      Draw a line with dabs separated according to spacing

      :type: boolean, default False

   .. attribute:: use_locked_size

      When locked brush stays same size relative to object; when unlocked brush size is given in pixels

      :type: boolean, default False

   .. attribute:: use_offset_pressure

      Enable tablet pressure sensitivity for offset

      :type: boolean, default False

   .. attribute:: use_original_normal

      When locked keep using normal of surface where stroke was initiated

      :type: boolean, default False

   .. attribute:: use_paint_image

      Use this brush in texture paint mode

      :type: boolean, default False

   .. attribute:: use_paint_sculpt

      Use this brush in sculpt mode

      :type: boolean, default False

   .. attribute:: use_paint_vertex

      Use this brush in vertex paint mode

      :type: boolean, default False

   .. attribute:: use_paint_weight

      Use this brush in weight paint mode

      :type: boolean, default False

   .. attribute:: use_persistent

      Sculpt on a persistent layer of the mesh

      :type: boolean, default False

   .. attribute:: use_plane_trim

      Enable Plane Trim

      :type: boolean, default False

   .. attribute:: use_pressure_jitter

      Enable tablet pressure sensitivity for jitter

      :type: boolean, default False

   .. attribute:: use_pressure_masking

      Pen pressure makes texture influence smaller

      :type: enum in ['NONE', 'RAMP', 'CUTOFF'], default 'NONE'

   .. attribute:: use_pressure_size

      Enable tablet pressure sensitivity for size

      :type: boolean, default False

   .. attribute:: use_pressure_spacing

      Enable tablet pressure sensitivity for spacing

      :type: boolean, default False

   .. attribute:: use_pressure_strength

      Enable tablet pressure sensitivity for strength

      :type: boolean, default False

   .. attribute:: use_primary_overlay

      Show texture in viewport

      :type: boolean, default False

   .. attribute:: use_primary_overlay_override

      Don't show overlay during a stroke

      :type: boolean, default False

   .. attribute:: use_projected

      Apply brush influence in 2D circle instead of a sphere

      :type: boolean, default False

   .. attribute:: use_relative_jitter

      Jittering happens in screen space, not relative to brush size

      :type: boolean, default False

   .. attribute:: use_restore_mesh

      Allow a single dot to be carefully positioned

      :type: boolean, default False

   .. attribute:: use_secondary_overlay

      Show texture in viewport

      :type: boolean, default False

   .. attribute:: use_secondary_overlay_override

      Don't show overlay during a stroke

      :type: boolean, default False

   .. attribute:: use_smooth_stroke

      Brush lags behind mouse and follows a smoother path

      :type: boolean, default False

   .. attribute:: use_space

      Limit brush application to the distance specified by spacing

      :type: boolean, default False

   .. attribute:: use_space_attenuation

      Automatically adjust strength to give consistent results for different spacings

      :type: boolean, default False

   .. attribute:: vertex_tool

      Brush blending mode

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

      :type: enum in ['MIX', 'ADD', 'SUB', 'MUL', 'BLUR', 'LIGHTEN', 'DARKEN', 'AVERAGE', 'SMEAR', 'COLORDODGE', 'DIFFERENCE', 'SCREEN', 'HARDLIGHT', 'OVERLAY', 'SOFTLIGHT', 'EXCLUSION', 'LUMINOCITY', 'SATURATION', 'HUE', 'ERASE_ALPHA', 'ADD_ALPHA'], default 'MIX'

   .. attribute:: weight

      Vertex weight when brush is applied

      :type: float in [0, 1], default 1.0

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
   * :class:`ID.name`
   * :class:`ID.users`
   * :class:`ID.use_fake_user`
   * :class:`ID.tag`
   * :class:`ID.is_updated`
   * :class:`ID.is_updated_data`
   * :class:`ID.is_library_indirect`
   * :class:`ID.library`
   * :class:`ID.preview`

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
   * :class:`ID.copy`
   * :class:`ID.user_clear`
   * :class:`ID.user_remap`
   * :class:`ID.make_local`
   * :class:`ID.user_of_id`
   * :class:`ID.animation_data_create`
   * :class:`ID.animation_data_clear`
   * :class:`ID.update_tag`

.. rubric:: References

.. hlist::
   :columns: 2

   * :mod:`bpy.context.brush`
   * :class:`BlendData.brushes`
   * :class:`BlendDataBrushes.new`
   * :class:`BlendDataBrushes.remove`
   * :class:`Paint.brush`

