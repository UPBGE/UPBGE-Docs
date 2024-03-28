.. _tools-api_stubs:

==============================
API Stubs
==============================

What Are They?
++++++++++++++++++++++++++++++

Python is a dynamically-typed language, but that doesn't mean you can't have such quality-of-life features like auto-completion or type information for APIs, which all modern IDEs provide.

The only reason you can't have them for UPBGE projects is that the relevant modules (namely, ``bpy.*`` and ``bge.*``) are only available inside UPBGE.

There are two possible options to deal with this problem. Firstly, you can `build UPBGE/Blender as a Python module <https://wiki.blender.org/wiki/Building_Blender/Other/BlenderAsPyModule>`__, which would give your IDE the most accurate and up-to-date API information as possible.

But it's not always easy to build UPBGE from source, especially if you are not familiar with the task. In this case, using API stubs could be a good alternative.

UPBGE-stubs
++++++++++++++++++++++++++++++

An utility to generate Python API stubs from documentation files in reStructuredText format called `BPY Stub Generator (bpystubgen) <https://github.com/mysticfall/bpystubgen>`__ can help us to get the UPBGE python API stubs.

The main usage of the program is to create Python API stubs from the documentation generated during the build process of UPBGE so that an IDE can provide autocompletion support and type hints for relevant modules like bpy or bge.

There are already a number of tools created with a similar goal in mind, notably `fake-bpy-module <https://github.com/nutti/fake-bpy-module>`__ and `fake-bge-module <https://github.com/nutti/fake-bge-module>`__ which can be a good alternative to this project.

However, ``bpystubgen`` has a few advantages over the others:

* It's very fast - some of those tools may take over an hour to generate the entire stubs for blender, but *bpystubgen* can do it under a minute (1,593 source documents).
* The generated stub modules preserve most of the source documentation, so you can use them as a manual as well.
* It generates pep-561 compliant stub modules, so it's safe to include them in your runtime module path.
* Along with its fast execution speed, the project also provides well-organised api and test suites to make it easier to fix bugs or improve the output quality.

Using UPBGE-stubs
++++++++++++++++++++++++++++++

If you just want to use the API stubs, you can install them from PyPI without having to generate them yourself. As for UPBGE, stubs are available for the 0.3 release, which you can install as follows:

.. code-block:: python
   
   pip install upbge-stubs==0.3.*

Once you install it via pip (or any other package manager you may prefer), you can configure the IDE of your choice as described in the project page `BPY Stub Generator (bpystubgen) <https://github.com/mysticfall/bpystubgen>`__.

After that, you can enjoy nice auto-completion and type information for most of the UPBGE's Python API.

Examples
++++++++++++++++++++++++++++++

.. figure:: /images/tools/tools-examples_1.png

   Auto-completion at work in PyCharm

.. figure:: /images/tools/tools-examples_2.png

   Pop-up documentation support in VSCode
