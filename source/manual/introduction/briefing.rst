
*********
Briefing
*********

History
-------

The **Uchronia Project Blender Game Engine** (UPBGE) is a `Blender <https://www.blender.org/>`__'s builtin tool for 
real-time projects, from architectural visualizations and simulations to games.

Originally a fork from the Blender Foundation's `Blender Game Engine <https://en.wikipedia.org/wiki/Blender_Game_Engine>`__, 
became indepent with the Blender Foundation's announcement of BGE's removal and 
replacement with a new Interactive Engine. With this independency, the UPBGE's developers 
have freedom to change and add features that could not be changed before (because the 
possibility of an official Blender merge, now discarded).

Features
--------

UPBGE have lots of `new features <https://github.com/UPBGE/blender/wiki/Release-notes>`__, 
improvements and bugs fixed that BGE haven't. Some features that UPBGE supports are:

- Realtime advanced physics powered by `Bullet <https://github.com/bulletphysics/bullet3>`__, including rigid bodies, soft bodies, obstacle simulation and path finding.
- Fully integrated audio engine powered by `OpenAL <https://www.openal.org/>`__ and `SDL <https://www.libsdl.org/>`__, supporting 3D sound and sound effects.
- Easy and straightforward visual logic system.
- Powerful `Python <https://www.python.org/>`__ language bindings, allowing support to even more libraries through the use of `PyPI <https://pypi.org/>`__.
- Development process entirely inside Blender, without needing to import/export assets.
- Execution of game in Blender's viewport (for fast previewing) or on an standalone executable.
- Blender's `Linked Libraries <https://docs.blender.org/manual/en/dev/data_system/linked_libraries.html>`__ feature, allowing to organize projects in multiple blend files.
- OpenGL custom shaders for visual effects and post processing.
- Fake or realtime reflections setting directly through the interface.

Development
-----------

UPBGE is maintained by a group of developers in their spare time and its community. You 
can contribute to UPBGE if you code in C++ or Python: just `open a pull request <https://github.com/UPBGE/blender/pulls>`__, 
submit your changes and wait for the reviewers. Also, even if you don't code, you can 
contribute by submiting bug reports, feature requests and participating discussions 
`on issues <https://github.com/UPBGE/blender/issues>`__.