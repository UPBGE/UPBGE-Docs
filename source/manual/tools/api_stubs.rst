*********
API Stubs
*********


What Are They?
==============

Python is a dynamically-typed language, but that doesn't mean you can't have
such quality-of-life features like auto-completion or type information for APIs,
which all modern IDEs provide.

The only reason you can't have them for Blender or UPBGE projects is that the
relevant modules(namely, `bpy.*` and `bge.*`) are only available inside Blender.

There are two possible options to deal with this problem. Firstly, you can
`build Blender as a Python module <https://wiki.blender.org/wiki/Building_Blender/Other/BlenderAsPyModule>`__,
which would give your IDE the most accurate and up-to-date API information as possible.

But it's not always easy to build Blender from source, especially if you are not
familiar with the task. In this case, using API stubs, or a "fake module" could be
a good alternative.

fake-bpy-module
===============

There is an open-source project named `fake-bpy-module <https://github.com/nutti/fake-bpy-module>`__
which provides a stub for Blender's Python API.

Once you install it via pip (or any other package manager you may prefer), you can
configure the IDE of your choice as described in the project page.

After that, you can enjoy nice auto-completion and type information for most of the
Blender's Python API.

One thing to remember, by the way, is that you need to match the version of
`fake-bpy-module` to that of Blender on which your UPBGE installation is based. For
UPBGE 0.2.5, you need to install `fake-bpy-module-2.79`, for example.

At the time of the writing, there is no fake-bpy-module for Blender 2.90, which
UPBGE 0.3.0 supports. Before the new version of the module is released, you may want
to install `fake-bpy-module-2.83` instead, as it is the closest version to 2.90.

fake-bge-module
===============

There is also `fake-bge-module <https://github.com/nutti/fake-bge-module>`__, which
supports UPBGE's Python API as its Blender counterpart does for Blender's core API.

The usage instruction almost the same as the other module which you can read from
the project's homepage. There is only a version for UPBGE 0.2.5 at the moment, but
it should work for newer versions as well for the most part.

Caveats
=======

There is one crucial caveat with providing type hints
(`PEP-484 <https://www.python.org/dev/peps/pep-0484/>`__) for UPBGE API, however.

Due to `an issue <https://github.com/UPBGE/upbge/issues/1240>`__ regarding how the
module initializes itself, you cannot reference BGE types(e.g. `KX_Camera`) other
than `KX_Component` in your game component.

Auto-completion and type information should work regardless of the problem.
Still, it certainly limits the benefits of such features provided by `fake-bge-module`,
o better be resolved sooner than later.
