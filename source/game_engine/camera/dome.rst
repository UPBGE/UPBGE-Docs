
***********
Dome Camera
***********

This feature allows artists to visualize their interactive projects within an immersive dome environment.
In order to make it an extensible tool, we are supporting Fulldome, Truncated domes (front and rear),
Planetariums and domes with spherical mirrors.

.. tip::

   The Dome camera uses a multi-pass texture algorithm as developed by Paul Bourke and
   was implemented by Dalai Felinto with sponsorship from SAT -- Society for Arts and
   Technology within the SAT Metalab
   `immersion research program <http://paulbourke.net/miscellaneous/domemirror/BlenderiDome/>`__,
   that involves rendering the scene four times and placing the subsequent images
   onto a mesh designed especially such that the result,
   when viewed with an orthographic camera, is a fisheye projection.

.. note::

   Remember to use Blender in 'fullscreen mode' to get the maximum out of your projector.

   To accomplish that launch Blender with the command-line argument ``-W``.
   Also to get away of the top menu on Blender try to join all areas
   (buttons, 3D View, text, etc.) in a single one. Otherwise if you only maximize it (:kbd:`Ctrl-Up`)
   you cannot get the whole screen free to run your game
   (the top menu bar takes about 20 pixels).


Dome Camera Settings
====================

.. figure:: /images/game-engine_camera_dome_dome.png

Dome Type
   This menu allows you to select which type of dome camera to use.
   They are outlined below, along with their respective settings.

- `Fisheye Mode`_
- `Front-Truncated Dome Mode`_
- `Rear-Truncated Dome Mode`_
- `Cube Map Mode`_
- `Spherical Panoramic Mode`_

Available camera settings change depending on the selected Dome Type:

Resolution
   Sets the resolution of the Buffer. Decreasing this value increases speed, but decreases quality.
Tessellation
   This is the tessellation level of the mesh (not available in Cube Map mode).
Angle
   Sets the field of view of the dome in degrees, from 90 to 250. (Available in Fisheye and Truncated modes).
Tilt
   Set the camera rotation in the horizontal axis (available in Fisheye and Truncated modes).

`Warp Data Mesh`_
   Use a custom warp mesh data file.


Fisheye Mode
------------

An Orthogonal Fisheye view from 90° to 250° degrees.

- From 90° to 180° we are using four renders.
- From 181° to 250° we are using five renders.

.. figure:: /images/game-engine_camera_dome_fisheye.jpg

   Fisheye Mode.


Front-Truncated Dome Mode
-------------------------

Designed for truncated domes,
this mode aligns the fisheye image with the top of the window, while touching the sides.

- The Field of view goes from 90° to 250° degrees.
- From 90° to 180° we are using four renders.
- From 181° to 250° we are using five renders.

.. figure:: /images/game-engine_camera_dome_front-truncated.jpg

   Front Truncated Dome Mode.


Rear-Truncated Dome Mode
------------------------

Designed for truncated domes,
this mode aligns the fisheye image with the bottom of the window, while touching the sides.

- The Field of view goes from 90° to 250° degrees.
- From 90° to 180° we are using four renders.
- From 181° to 250° we are using five renders.

.. figure:: /images/game-engine_camera_dome_rear-truncated.jpg

   Rear Truncated Dome Mode.


Cube Map Mode
-------------

Cube Map mode can be used for pre-generate animated images for CubeMaps.

We are using six renders for that. The order of the images follows Blender internal EnvMap file format:
- First line: right, back, left.
- Second line: bottom, top, front.

.. figure:: /images/game-engine_camera_dome_envmap.jpg

   Environment Map Mode.


Spherical Panoramic Mode
------------------------

A full spherical panoramic mode.

- We are using six cameras here.
- The bottom and top start to get precision with *Definition* set to 5 or more.

.. figure:: /images/game-engine_camera_dome_panoramic.jpg

   Full Spherical Panoramic Mode.


Warp Data Mesh
--------------

Many projection environments require images that are not simple perspective projections that
are the norm for flat screen displays. Examples include geometry correction for cylindrical
displays and some new methods of projecting into planetarium domes or upright domes intended
for VR.

For more information on the mesh format see `Paul Bourke's article <http://paulbourke.net/dataformats/meshwarp/>`__.

.. figure:: /images/game-engine_camera_dome_warped.jpg

In order to produce those images, we are using a specific file format.

File template:

.. code-block:: none

   mode
   width height
   n0_x n0_y n0_u n0_v n0_i
   n1_x n1_y n1_u n1_v n1_i
   n2_x n1_y n2_u n2_v n2_i
   n3_x n3_y n3_u n3_v n3_i
   (...)


First line is the image type the mesh is support to be applied to:
``2 = rectangular``, ``1 = radial`` Next line has the mesh dimensions in
pixels. Rest of the lines are the nodes of the mesh.

Each line is compound of *x*, *y*, *u*, *v*, *i*. (x, y)
are the normalized screen coordinates, (u, v)
texture coordinates, *i* a multiplicative intensity factor.

*x* varies from negative screen aspect to positive screen aspect.
*y* varies from -1 to 1. *u* and *v* vary from 0 to 1.
*i* ranges from 0 to 1, if negative do not draw that mesh node.

#. You need to create the file and add it to the Text Editor in order to select it as your Warp Mesh data file.
#. Open the Text Editor :menuselection:`Editor Types --> Text Editor`.
#. Open your mesh data file (e.g. myDome.data) in the Text editor (:menuselection:`Text --> Open` or :kbd:`Alt-O`).
#. Go to Game Framing Settings :menuselection:`Editor Types --> Properties editor --> Scene`.
#. Enable Dome Mode.
#. Type filename in Warp Data field (e.g. myDome.data).

To create your own Warp Meshes an interactive tool called meshmapper is available as part of
`Paul Bourke's Warpplayer <http://paulbourke.net/miscellaneous/domemirror/warpplayer/>`__
software package (requires full version).


Examples
========

- `Spherical Mirror Dome 4×3 <https://wiki.blender.org/uploads/8/81/Dev-GameEngine-Dome-Standard_4x3.data>`__.
- `Truncated Dome 4×3 <https://wiki.blender.org/uploads/9/9b/Dev-GameEngine-Dome-Truncated_4x3.data>`__.
- `Sample Fullscreen File 4×3
  <https://wiki.blender.org/uploads/d/d4/Dev-GameEngine-Dome-Sample-FullScreen_4x3.data>`__.
- `Sample Fullbuffer File 4×3
  <https://wiki.blender.org/uploads/3/3d/Dev-GameEngine-Dome-Sample-FullBuffer_4x3.data>`__.

.. important::

   The viewport is calculated using the ratio of canvas width by canvas height.
   Therefore different screen sizes will require different warp mesh files. Also in order to get
   the correct ratio of your projector you need to use Blender in Fullscreen mode.
