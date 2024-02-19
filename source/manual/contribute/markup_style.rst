.. highlight:: rst

******************
Markup Style Guide
******************

.. Editor's Note:
   ::
   There are many detailed conventions, e.g:
   ::
   - When definition lists/bullet-points are used.
   - Word-ordering in filenames.
   - How text is wrapped.
   - The number of spaces between lines.
   - When it is/is not okay to add in Unicode characters.
   - Should comments on a page be above or below titles :)
   ::
   Having a lot of detailed text on this page is off-putting to new contributors,
   so please avoid making this page into a wall-of-text,
   many conventions can be noticed along the way by reading existing text.

This page covers the conventions for writing and use of the reStructuredText (RST) markup syntax.

Conventions
===========

- Three (3) space indentation.
- Lines should be less than 120 characters long.
- Use *italics* for *button/menu names*.

Other loose conventions:

- Avoid Unicode characters.
- Avoid heavily wrapped text
   (i.e. sentences can have their own lines).

Headings
========

.. code-block:: rst

   #################
     Document Part
   #################

   ================
   Document Chapter
   ================ 

   Document Section
   ++++++++++++++++

   Document Subsection
   -------------------

   Document Subsubsection
   ^^^^^^^^^^^^^^^^^^^^^^

   Document Paragraph
   """"""""""""""""""

.. important::
   *Parts* should only be used for contents or index pages. Each ``.rst`` file should only have one chapter heading (``=``) per file - top heading.

Text Styling
============

See the `overview on ReStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`__ for more information on how to style the various elements of the documentation and on how to add lists, tables, pictures and code blocks. The `Sphinx reference <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`__ provides more insight into additional constructs.

.. tip::
   Do not manually format/break lines in ``.rst`` files; use your editor's *wrap text* functionality. 80 characters is standard line length for computer files.

The following are useful markups for text styling::

   *italic*
   **bold**
   ``literal``

Interface Elements
==================

- ``:kbd:`LMB``` - keyboard and mouse shortcuts.
- ``*Mirror*`` - interface labels.
- ``:menuselection:`3D Viewport --> Add --> Mesh --> Monkey``` - menus.

Code Samples
============

There is support for syntax highlighting if the programming language is provided, and line numbers can be optionally shown with the ``:linenos:`` option::

   .. code-block:: python
      :linenos:

      import bpy
      def some_function():
          ...

Images
======

Figures are used to place images::

   .. figure:: /images/interface_window-system_splash_current.png

      Image caption

For consistency, and since it would be good to ensure that screenshots are all of similar size when floated next to text, writers should take screenshots in the following manner:

#. Prepare the area you would like to capture making sure to *use the default theme and setting*. (In some cases you may not want to use the default settings e.g. if some options are hidden behind a checkbox.)
#. Zoom to the maximum zoom level (hold :kbd:`NumpadPlus` or :kbd:`Ctrl-MMB` or similar).
#. Zoom out eight zoom levels (:kbd:`NumpadMinus` -- eight times).
#. In some cases you will want to leave a small margin around the thing you are trying to capture. This should be around 30px but does not have to be exact.

This can be applied to several parts of the interface but might not work for all cases.

If really needed, use additinal *directives* for image formatting::

   .. figure:: /images/Logic_Nodes/once_node.png
      :align: right
      :width: 215
      :alt: Once Node (placeholder if .png image file is missing)

Files
-----

No Caps, No Gaps
   Lower case filenames underscore between words.
Sort Usefully
   Order naming with specific identifiers at the end.
Format
   Use ``.png`` for images that have solid colors such as screenshots of the Blender interface, and ``.jpg`` for images with a high amount of color variance, such as sample renders and photographs.

   Do not use animated ``.gif`` files, these are hard to maintain, can be distracting and are usually large in file size. Instead use a video if needed (see `Videos`_ below).
Location
   Place the images in the ``manual/images`` folder, and use subfolders, if needed.
Naming
   For naming files use dashes to separate chapters and sections, and use underscore to connect sections that are two or more words, i.e. for image files:
   
   ``chapter-subsection-sub_subsection-id.png``:

   - ``interface-splash-current.png``
   - ``interface-undo_redo-last.png``
   - ``interface-undo_redo-repeat_history-menu.png``

   Do not use special characters or spaces!

Usage Guides
------------

- Avoid specifying the resolution of the image, so that the theme can handle the images consistently and provide the best layout across different screen sizes.
- When documenting a panel or section of the UI, it is better to use a single image that shows all of the relevant areas (rather than multiple images for each icon or button) placed at the top of the section you are writing, and then explain the features in the order that they appear in the image.

  .. note::
     It is important that the manual can be maintained long term. UI and tool options change, so try to avoid having a lot of images (when they are not especially necessary). Otherwise, this becomes too much of a maintenance burden.

Videos
======

.. note::
   This is from Blender manual. It might not be suitable for *UPBGE-Docs* developers.

Videos can be embedded from Blender's self-hosted `PeerTube <https://joinpeertube.org/>`__ instance, which can be found at `video.blender.org <https://video.blender.org/>`__. To embed a video use the following directive::

   .. peertube:: ID

The ``ID`` is found in the video's URL, e.g.:

ID for ``https://video.blender.org/videos/watch/47448bc1-0cc0-4bd1-b6c8-9115d8f7e08c``

is ``47448bc1-0cc0-4bd1-b6c8-9115d8f7e08c``.

To get a new video uploaded, contact a `Documentation Project Administrator <https://projects.blender.org/blender/documentation>`__.

Usage Guides
------------

- Avoid adding videos that rely on voice or words, as this is difficult to translate.
- Do not embed video tutorials as a means of explaining a feature, the writing itself should explain it adequately. (Though you may include a link to the video at the bottom of the page under the heading ``Tutorials``.)

Useful Constructs
=================

- ``|BLENDER_VERSION|`` - Resolves to the current Blender version.
- ``:abbr:`SSAO (Screen Space Ambient Occlusion)``` -
  Abbreviations display the full text as a tooltip for the reader.
  
   :abbr:`Hover mouse over here (This is example of abbreviation)`

- ``:term:`Manifold``` - Links to an entry in the :doc:`Glossary </manual/glossary/index>`.

Cross References and Linkage
============================

You can link to another part of the Manual with folder path::

   :doc:`The Title </section/path/to/file>`

To link to a specific section in another file (or the same one), explicit labels are available::

   .. _explicit-label:           ["link to this" directive, single _underscore]

   (section or image which needs to be referenced)

   Some text :ref:`Optional Title <explicit-label>`.  ["link from this" directive]

.. important::
   Explicit labels should immediatelly preceed the title. I.e.::

      .. _explicit label:

      .. figure:: images/path-to-image.png
      
      =====
      Title
      =====

   will not work. Should be::
   
      .. figure:: images/path-to-image.png

      .. _explicit label:

      =====
      Title
      =====
   
Linking to a title in the *same file*::

   Titles are Targets
   ==================

   Body text.

   Implicit references, like `Titles are Targets`_ [single underscore_]

Linking to the outside world::

   `Blender Website <https://www.blender.org>`__ [double underscore__]

Context Sensitive Manual Access
-------------------------------

It is possible to link to a specific part of the manual from inside the Blender by opening the context menu (right click) of a property or operator and selecting *Online Manual*. In order for this to work, this needs to be accounted for in the documentation. To link a property or operator to a specific part of the manual you need to add an external reference link tag whose ID matches Blender's RNA tag. The easiest way to find out what is the tag for a property, is to open the context menu of the property/operator and select *Online Python Reference* to extract the tag from the URL. Some examples of how this looks in the RST document are given below::

   .. _bpy.types.FluidDomainSettings.use_fractions:

   Fractional Obstacles
      Enables finer resolution in fluid / obstacle regions (second order obstacles)...

      .. _bpy.types.FluidDomainSettings.fractions_distance:

      Obstacle Distance
         Determines how far apart fluid and obstacles are...

For an operator::

   .. _bpy.ops.curve.subdivide:

   Subdivide
   =========

Further Reading
===============

To learn more about reStructuredText, see:

`Sphinx RST Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`__
   Good basic introduction.
`reStructuredText Markup <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html>`__
   Verbose reStructuredText cheat-sheet.
