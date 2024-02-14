
*************
A Deeper Look
*************

Use Cases
=========

UPBGE allows you to create real-time interactive 3D applications or simulations. This 
allows you to create almost any type of interactive project, like architectural 
presentations, virtual prototypes for robotic projects, physics simulation projects, 
simple and complex games, and much more.

Much can be achieved through UPBGE by default, as it provides a blank canvas full of 
features to be used, and even more can be acomplished by extending these features 
according to your needs. 
For example, if you're working with robotics and needs to send or receive commands 
through a USB port, you can install the 
`PySerial <https://pypi.org/project/pyserial/>`__ Python module for use with UPBGE.
Or if you need a graphical feature that can't be acomplished through the default UPBGE's 
capabilities, you can write your own OpenGL shaders. 
The list goes on, and there's a big chance that the project you aim to can be brought to 
life with UPBGE, using its features and abilities to be extended.

Sample Games
============

Here are some examples of games made with BGE/UPBGE:

.. youtube:: yRBDkQbGpdg

``Game Name / Creator Name:`` Krum - Battle Arena by Haidme produced with BGE/UPBGE.

.. youtube:: ujLuhiCcwA8

``Game Name / Creator Name:`` Tomato Jones 2 by Haidme produced with BGE/UPBGE.

..
  .. youtube:: SQz3O8VFdOo

..
  ``Game Name / Creator Name:`` Highlands Test by Atomic Skill produced with UPBGE 0.2.5.

.. youtube:: FJfmLktYi7o

``Game Name / Creator Name:`` The Future's End by Mark Telles produced with UPBGE 0.2.5.

..
   .. youtube:: 3krdf9xRgw4

..
  ``Game Name / Creator Name:`` Spaceship Test by Atomic Skill produced with UPBGE 0.3.

.. youtube:: Ji9NO_gtvQU

``Game Name / Creator Name:`` GTA-like prototype by ThePajlok Studios produced with UPBGE 0.3.

Under The Hood
==============

UPBGE oversees a game loop, which processes logic, sound, physics and rendering 
simulations in sequential order. The engine is written in C++.

By default, the user has access to a powerful and high-level visual logic programming 
interface. The visual programming in UPBGE provides deep interaction with the simulation, 
and its functionality can be extended through Python scripting. It is designed to abstract 
the complex engine features into a simple user interface, which does not require experience 
with Programming.

UPBGE is closely integrated with the existing code base of Blender, which permits quick 
transitions between the traditional modeling feature set and game-specific functionality
provided by the program. In this sense, the UPBGE can be efficiently used in all areas of 
game design, from prototyping to final release.

UPBGE can simulate content within Blender, however it also includes the ability to export 
a binary run-time to Linux, MacOS, and MS-Windows.

There are a number of powerful libraries the UPBGE takes advantage of:

- `Audaspace <https://audaspace.github.io/>`__: A sound library for control of audio. Uses OpenAL or SDL.
- `Bullet <http://bulletphysics.org>`__: A physics engine featuring 3D collision detection, soft body dynamics and rigid body dynamics.
- `Detour <https://github.com/recastnavigation/recastnavigation>`__: A pathfinding and spatial reasoning toolkit.
- `Recast <https://github.com/recastnavigation/recastnavigation>`__: A state of the art navigation mesh construction tool set for games.

Project Development Process
===========================

When creating a game or simulation in UPBGE, there are four essential steps:

#. Create visual elements that can be rendered. Usually, 3D models.
#. Enable interaction within the scene using logic to enable custom behavior and 
   determine how it is invoked.
#. Create one (or more) camera to give a frustum from which to render the scene, and 
   modify the parameters to support the environment in which the game will be displayed, 
   such as VR rendering.
#. Launch the game, using the internal player or exporting a runtime to the appropriate platform.
