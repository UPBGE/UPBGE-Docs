View3D Operators
================

.. module:: bpy.ops.view3d

.. function:: background_image_add(name="Image", filepath="", filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA')

   Add a new background image (Ctrl for Empty Object)

   :arg name:

      Name, Image name to assign

   :type name: string, (optional, never None)
   :arg filepath:

      File Path, Path to file

   :type filepath: string, (optional, never None)
   :arg filter_blender:

      Filter .blend files

   :type filter_blender: boolean, (optional)
   :arg filter_backup:

      Filter .blend files

   :type filter_backup: boolean, (optional)
   :arg filter_image:

      Filter image files

   :type filter_image: boolean, (optional)
   :arg filter_movie:

      Filter movie files

   :type filter_movie: boolean, (optional)
   :arg filter_python:

      Filter python files

   :type filter_python: boolean, (optional)
   :arg filter_font:

      Filter font files

   :type filter_font: boolean, (optional)
   :arg filter_sound:

      Filter sound files

   :type filter_sound: boolean, (optional)
   :arg filter_text:

      Filter text files

   :type filter_text: boolean, (optional)
   :arg filter_btx:

      Filter btx files

   :type filter_btx: boolean, (optional)
   :arg filter_collada:

      Filter COLLADA files

   :type filter_collada: boolean, (optional)
   :arg filter_alembic:

      Filter Alembic files

   :type filter_alembic: boolean, (optional)
   :arg filter_folder:

      Filter folders

   :type filter_folder: boolean, (optional)
   :arg filter_blenlib:

      Filter Blender IDs

   :type filter_blenlib: boolean, (optional)
   :arg filemode:

      File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file

   :type filemode: int in [1, 9], (optional)
   :arg relative_path:

      Relative Path, Select the file relative to the blend file

   :type relative_path: boolean, (optional)
   :arg show_multiview:

      Enable Multi-View

   :type show_multiview: boolean, (optional)
   :arg use_multiview:

      Use Multi-View

   :type use_multiview: boolean, (optional)
   :arg display_type:

      Display Type

      * ``DEFAULT`` Default, Automatically determine display type for files.
      * ``LIST_SHORT`` Short List, Display files as short list.
      * ``LIST_LONG`` Long List, Display files as a detailed list.
      * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.

   :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
   :arg sort_method:

      File sorting mode

      * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically.
      * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type.
      * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time.
      * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.

   :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)

.. function:: background_image_remove(index=0)

   Remove a background image from the 3D view

   :arg index:

      Index, Background image index to remove

   :type index: int in [0, inf], (optional)

.. function:: camera_to_view()

   Set camera view to active view

.. function:: camera_to_view_selected()

   Move the camera so selected objects are framed

.. function:: clear_render_border()

   Clear the boundaries of the border render and disable border render

.. function:: clip_border(xmin=0, xmax=0, ymin=0, ymax=0)

   Set the view clipping border

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

.. function:: copybuffer()

   Selected objects are saved in a temp file

.. function:: cursor3d()

   Set the location of the 3D cursor

.. function:: dolly(delta=0, mx=0, my=0)

   Dolly in/out in the view

   :arg delta:

      Delta

   :type delta: int in [-inf, inf], (optional)
   :arg mx:

      Zoom Position X

   :type mx: int in [0, inf], (optional)
   :arg my:

      Zoom Position Y

   :type my: int in [0, inf], (optional)

.. function:: edit_mesh_extrude_individual_move()

   Extrude individual elements and move

   :file: `startup\bl_operators\view3d.py\:36 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\view3d.py$36>`_

.. function:: edit_mesh_extrude_move_normal()

   Extrude and move along normals

   :file: `startup\bl_operators\view3d.py\:106 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\view3d.py$106>`_

.. function:: edit_mesh_extrude_move_shrink_fatten()

   Extrude and move along individual normals

   :file: `startup\bl_operators\view3d.py\:123 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\view3d.py$123>`_

.. function:: enable_manipulator(translate=False, rotate=False, scale=False)

   Enable the transform manipulator for use

   :arg translate:

      Translate, Enable the translate manipulator

   :type translate: boolean, (optional)
   :arg rotate:

      Rotate, Enable the rotate manipulator

   :type rotate: boolean, (optional)
   :arg scale:

      Scale, Enable the scale manipulator

   :type scale: boolean, (optional)

.. function:: fly()

   Interactively fly around the scene

.. function:: game_start()

   Start game engine

.. function:: layers(nr=1, extend=False, toggle=True)

   Toggle layer(s) visibility

   :arg nr:

      Number, The layer number to set, zero for all layers

   :type nr: int in [0, 20], (optional)
   :arg extend:

      Extend, Add this layer to the current view layers

   :type extend: boolean, (optional)
   :arg toggle:

      Toggle, Toggle the layer

   :type toggle: boolean, (optional)

.. function:: localview()

   Toggle display of selected object(s) separately and centered in view

.. function:: manipulator(constraint_axis=(False, False, False), constraint_orientation='GLOBAL', release_confirm=False, use_accurate=False, use_planar_constraint=False)

   Manipulate selected item by axis

   :arg constraint_axis:

      Constraint Axis

   :type constraint_axis: boolean array of 3 items, (optional)
   :arg constraint_orientation:

      Orientation, Transformation orientation

   :type constraint_orientation: enum in [], (optional)
   :arg release_confirm:

      Confirm on Release, Always confirm operation when releasing button

   :type release_confirm: boolean, (optional)
   :arg use_accurate:

      Accurate, Use accurate transformation

   :type use_accurate: boolean, (optional)
   :arg use_planar_constraint:

      Planar Constraint, Limit the transformation to the two axes that have not been clicked (translate/scale only)

   :type use_planar_constraint: boolean, (optional)

.. function:: move()

   Move the view

.. function:: navigate()

   Interactively navigate around the scene (uses the mode (walk/fly) preference)

.. function:: ndof_all()

   Pan and rotate the view with the 3D mouse

.. function:: ndof_orbit()

   Orbit the view using the 3D mouse

.. function:: ndof_orbit_zoom()

   Orbit and zoom the view using the 3D mouse

.. function:: ndof_pan()

   Pan the view with the 3D mouse

.. function:: object_as_camera()

   Set the active object as the active camera for this view or scene

.. function:: pastebuffer(autoselect=True, active_layer=True)

   Contents of copy buffer gets pasted

   :arg autoselect:

      Select, Select pasted objects

   :type autoselect: boolean, (optional)
   :arg active_layer:

      Active Layer, Put pasted objects on the active layer

   :type active_layer: boolean, (optional)

.. function:: properties()

   Toggle the properties region visibility

.. function:: render_border(xmin=0, xmax=0, ymin=0, ymax=0, camera_only=False)

   Set the boundaries of the border render and enable border render

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
   :arg camera_only:

      Camera Only, Set render border for camera view and final render only

   :type camera_only: boolean, (optional)

.. function:: rotate()

   Rotate the view

.. function:: ruler()

   Interactive ruler

.. function:: select(extend=False, deselect=False, toggle=False, center=False, enumerate=False, object=False, location=(0, 0))

   Activate/select item(s)

   :arg extend:

      Extend, Extend selection instead of deselecting everything first

   :type extend: boolean, (optional)
   :arg deselect:

      Deselect, Remove from selection

   :type deselect: boolean, (optional)
   :arg toggle:

      Toggle Selection, Toggle the selection

   :type toggle: boolean, (optional)
   :arg center:

      Center, Use the object center when selecting, in editmode used to extend object selection

   :type center: boolean, (optional)
   :arg enumerate:

      Enumerate, List objects under the mouse (object mode only)

   :type enumerate: boolean, (optional)
   :arg object:

      Object, Use object selection (editmode only)

   :type object: boolean, (optional)
   :arg location:

      Location, Mouse location

   :type location: int array of 2 items in [-inf, inf], (optional)

.. function:: select_border(xmin=0, xmax=0, ymin=0, ymax=0, deselect=False, extend=True)

   Select items using border selection

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
   :arg deselect:

      Deselect, Deselect rather than select items

   :type deselect: boolean, (optional)
   :arg extend:

      Extend, Extend selection instead of deselecting everything first

   :type extend: boolean, (optional)

.. function:: select_circle(x=0, y=0, radius=25, deselect=False)

   Select items using circle selection

   :arg x:

      X

   :type x: int in [-inf, inf], (optional)
   :arg y:

      Y

   :type y: int in [-inf, inf], (optional)
   :arg radius:

      Radius

   :type radius: int in [1, inf], (optional)
   :arg deselect:

      Deselect, Deselect rather than select items

   :type deselect: boolean, (optional)

.. function:: select_lasso(path=None, deselect=False, extend=True)

   Select items using lasso selection

   :arg path:

      Path

   :type path: :class:`bpy_prop_collection` of :class:`OperatorMousePath`, (optional)
   :arg deselect:

      Deselect, Deselect rather than select items

   :type deselect: boolean, (optional)
   :arg extend:

      Extend, Extend selection instead of deselecting everything first

   :type extend: boolean, (optional)

.. function:: select_menu(name='', toggle=False)

   Menu object selection

   :arg name:

      Object Name

   :type name: enum in [], (optional)
   :arg toggle:

      Toggle, Toggle selection instead of deselecting everything first

   :type toggle: boolean, (optional)

.. function:: select_or_deselect_all(extend=False, toggle=False, deselect=False, center=False, enumerate=False, object=False)

   Select element under the mouse, deselect everything is there's nothing under the mouse

   :arg extend:

      Extend, Extend selection instead of deselecting everything first

   :type extend: boolean, (optional)
   :arg toggle:

      Toggle, Toggle the selection

   :type toggle: boolean, (optional)
   :arg deselect:

      Deselect, Remove from selection

   :type deselect: boolean, (optional)
   :arg center:

      Center, Use the object center when selecting, in editmode used to extend object selection

   :type center: boolean, (optional)
   :arg enumerate:

      Enumerate, List objects under the mouse (object mode only)

   :type enumerate: boolean, (optional)
   :arg object:

      Object, Use object selection (editmode only)

   :type object: boolean, (optional)

   :file: `startup\bl_operators\view3d.py\:179 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup\bl_operators\view3d.py$179>`_

.. function:: smoothview()

   Undocumented

.. function:: snap_cursor_to_active()

   Snap cursor to active item

.. function:: snap_cursor_to_center()

   Snap cursor to the Center

.. function:: snap_cursor_to_grid()

   Snap cursor to nearest grid division

.. function:: snap_cursor_to_selected()

   Snap cursor to center of selected item(s)

.. function:: snap_selected_to_active()

   Snap selected item(s) to the active item

.. function:: snap_selected_to_cursor(use_offset=True)

   Snap selected item(s) to cursor

   :arg use_offset:

      Offset

   :type use_offset: boolean, (optional)

.. function:: snap_selected_to_grid()

   Snap selected item(s) to nearest grid division

.. function:: toggle_render()

   Toggle rendered shading mode of the viewport

.. function:: toolshelf()

   Toggles tool shelf display

.. function:: view_all(use_all_regions=False, center=False)

   View all objects in scene

   :arg use_all_regions:

      All Regions, View selected for all regions

   :type use_all_regions: boolean, (optional)
   :arg center:

      Center

   :type center: boolean, (optional)

.. function:: view_center_camera()

   Center the camera view

.. function:: view_center_cursor()

   Center the view so that the cursor is in the middle of the view

.. function:: view_center_lock()

   Center the view lock offset

.. function:: view_center_pick()

   Center the view to the Z-depth position under the mouse cursor

.. function:: view_lock_clear()

   Clear all view locking

.. function:: view_lock_to_active()

   Lock the view to the active object/bone

.. function:: view_orbit(angle=0.0, type='ORBITLEFT')

   Orbit the view

   :arg angle:

      Roll

   :type angle: float in [-inf, inf], (optional)
   :arg type:

      Orbit, Direction of View Orbit

      * ``ORBITLEFT`` Orbit Left, Orbit the view around to the Left.
      * ``ORBITRIGHT`` Orbit Right, Orbit the view around to the Right.
      * ``ORBITUP`` Orbit Up, Orbit the view Up.
      * ``ORBITDOWN`` Orbit Down, Orbit the view Down.

   :type type: enum in ['ORBITLEFT', 'ORBITRIGHT', 'ORBITUP', 'ORBITDOWN'], (optional)

.. function:: view_pan(type='PANLEFT')

   Pan the view

   :arg type:

      Pan, Direction of View Pan

      * ``PANLEFT`` Pan Left, Pan the view to the Left.
      * ``PANRIGHT`` Pan Right, Pan the view to the Right.
      * ``PANUP`` Pan Up, Pan the view Up.
      * ``PANDOWN`` Pan Down, Pan the view Down.

   :type type: enum in ['PANLEFT', 'PANRIGHT', 'PANUP', 'PANDOWN'], (optional)

.. function:: view_persportho()

   Switch the current view from perspective/orthographic projection

.. function:: view_roll(angle=0.0, type='ANGLE')

   Roll the view

   :arg angle:

      Roll

   :type angle: float in [-inf, inf], (optional)
   :arg type:

      Roll Angle Source, How roll angle is calculated

      * ``ANGLE`` Roll Angle, Roll the view using an angle value.
      * ``LEFT`` Roll Left, Roll the view around to the Left.
      * ``RIGHT`` Roll Right, Roll the view around to the Right.

   :type type: enum in ['ANGLE', 'LEFT', 'RIGHT'], (optional)

.. function:: view_selected(use_all_regions=False)

   Move the view to the selection center

   :arg use_all_regions:

      All Regions, View selected for all regions

   :type use_all_regions: boolean, (optional)

.. function:: viewnumpad(type='LEFT', align_active=False)

   Use a preset viewpoint

   :arg type:

      View, Preset viewpoint to use

      * ``LEFT`` Left, View From the Left.
      * ``RIGHT`` Right, View From the Right.
      * ``BOTTOM`` Bottom, View From the Bottom.
      * ``TOP`` Top, View From the Top.
      * ``FRONT`` Front, View From the Front.
      * ``BACK`` Back, View From the Back.
      * ``CAMERA`` Camera, View From the Active Camera.

   :type type: enum in ['LEFT', 'RIGHT', 'BOTTOM', 'TOP', 'FRONT', 'BACK', 'CAMERA'], (optional)
   :arg align_active:

      Align Active, Align to the active object's axis

   :type align_active: boolean, (optional)

.. function:: walk()

   Interactively walk around the scene

.. function:: zoom(delta=0, mx=0, my=0)

   Zoom in/out in the view

   :arg delta:

      Delta

   :type delta: int in [-inf, inf], (optional)
   :arg mx:

      Zoom Position X

   :type mx: int in [0, inf], (optional)
   :arg my:

      Zoom Position Y

   :type my: int in [0, inf], (optional)

.. function:: zoom_border(xmin=0, xmax=0, ymin=0, ymax=0, zoom_out=False)

   Zoom in the view to the nearest object contained in the border

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
   :arg zoom_out:

      Zoom Out

   :type zoom_out: boolean, (optional)

.. function:: zoom_camera_1_to_1()

   Match the camera to 1:1 to the render output

