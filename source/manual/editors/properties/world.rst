
*****
World
*****

.. figure:: /images/game-engine_world_panel.png

   BGE World panel.

World settings enable you to set some basic effects which affect all scenes throughout your
game, so giving it a feeling of unity and continuity. These include ambient light,
depth effects (mist) and global physics settings. These effects are a limited subset of
the more extensive range of effects available with the Blender internal or Cycles renderer.

.. tip::

   While world settings offer a simple way of adding effects to a scene,
   compositing nodes are often preferred, though more complex to master,
   for the additional control and options they offer.
   For example, filtering the Z value (distance from camera) or normals (direction of surfaces)
   through compositing nodes can further increase the depth and spatial clarity of a scene.


World
=====

These two color settings allow you to set some general lighting effects for your game.

Horizon Color
   The RGB color at the horizon;
   i.e. the color and intensity of any areas in the scene which are not filled explicitly.
Ambient Color
   Ambient light mimics an overall background illumination obtained from diffusing surfaces.
   Its general color and intensity are set by these controls.


Environmental Lighting
======================

Environment light provides light coming from all directions.

Light is calculated with a ray-traced method which is the same as that used by Ambient Occlusion.
The difference is that Environment lighting takes into account the "ambient" parameter of the material
shading settings, which indicates the amount of ambient light/color that that material receives.

Also, you can choose the environment color source (white, sky color, sky texture) and the light energy.

Energy
   Defines the strength of environment light.
Environment Color
   Defines where the color of the environment light comes from.

Using both settings simultaneously produces better global lighting.

It is good for mimicking the sky in outdoor lighting. Environment lighting can be fairly noisy at times.


Mist
====

Mist can greatly enhance the illusion of depth in your rendering.
To create mist, Blender makes objects farther away more transparent (decreasing their Alpha value)
so that they mix more of the background color with the object color.
With Mist enabled, the further the object is away from the camera the less its alpha value will be.

Mist
   Toggles mist on and off.
Falloff
   Sets the shape of the falloff of the mist.
Start
   The starting distance of the mist effect. No misting will take place for objects closer than this distance.
Depth
   The depth at which the opacity of objects falls to zero.
Minimum intensity
   Overall minimum intensity of the mist.
