.. _contribute-writing_style:

===================
Writing Style Guide
===================

In order to maintain a consistent writing style within the manual, please keep this page in mind and only deviate from it when you have a good reason to do so.

Primary Goals
-------------

User Focused
   While some areas of computer graphics are highly technical, this manual shall be kept understandable by non-technical users.

Complete
   The manual aims to provide detailed functional description of all features, tools and options in UPBGE. This does not mean we have to document every small detail. The manual should provide information on what a feature is, how to use it, and its purpose.
    
Concise
   Computer graphics is a vast field, there are many rules, exceptions to the rules, and interesting details. Expanding into details can add unnecessary content, so keep the text concise and relevant to the topic at hand.
   
Maintainable
   Try to write content that will not have to be redone the moment some small change is made. This helps a small documentation community to maintain the manual.

Content Guidelines
------------------

Rules of thumb:

* **Spell checking** is *strongly* recommended.

* Use **American English** (i.e. modeling and not modelling, color and not colour) also for formatting numbers (i.e. 2,718.28 and not 2 718,28).

* Take care about grammar, appropriate wording and use simple English.

* Keep sentences short and clear, resulting in text that is easy to read, objective and to the point.

* Including *why or how an option might be useful* is a good idea.

* If you are unsure about how a feature works, ask a developer or someone else.

To be avoided:

* Avoid writing in *first person* perspective, about yourself or your own opinions.
   
* Avoid weasel words and being unnecessarily vague, i.e.:
   | "Reloading the file will probably fix the problem"
   | "Most people do not use this option because ..."

* Avoid including specific details such as:  
   | “UPBGE has 23 different kinds of modifiers.”
   | “Enabling previews adds 65536 bytes to the size of each blend-file (unless it is compressed).”
   | These details are not useful for users to memorize and they become quickly outdated.

* Avoid documenting bugs.
   Issues that are known to the developers and are not going to be resolved before the next release can be documented as *Known Limitations*.

* Avoid product placements, i.e. unnecessarily promoting software or hardware brands. Keep content vendor-neutral where possible.

* Avoid technical explanations about the mathematical/algorithmic implementation of a feature - keep it simple.
   
* Avoid repetition of large portions of text.
   Simply explain it once, and from then on refer to that explanation. For general terminology, consider defining a ``:term:`` in the glossary.

* Avoid enumerations of similar options, such as listing every preset or every frame rate in a ``select menu``.
   Such lists are only showing what is **already obvious** in the interface and end up being a lot of text to read and maintain.

* Avoid documenting changes in UPBGE between releases.
   That is what the release notes are for. We only need to document the current state of documentation.

* Unless a unit or a value is obscure and unpredictable, there is no need to mention it.

* Do not simply copy the tooltips from UPBGE.
   People will come to the manual to learn more than what is provided by the UI.

* Use a *TODO* comment (which is not shown in the HTML page, but useful for other editors):

.. parsed-literal::
   .. TODO:: how does this tool work \? ask Joe.

Glossary
--------

This section is specifically about the *Glossary* section, where we define common terms in *Blender/UPBGE* and computer graphics.

*Terms* are added with ``:term:`` syntax, explained in :doc:`Markup Style Guide </manual/contribute/markup_style>`.

Rules of thumb:

* Define the term before providing any further information.

* Avoid using constructs such as “it is” or “xyz is” before the definition.

* Avoid repeating the term immediately or using it in the definition.

* Avoid adding terms not found in UPBGE/Blender’s interface or manual.

* Avoid overly long entries. If an explanation of a complex term is needed, supplement with external links.

* Avoid duplicating documentation; if explaining the term is the primary focus of another section of the manual (e.g. if the term is the name of a tool), either just link to that section, or avoid creating a glossary entry entirely.

* URL references are to be added at the end, formatted as follows, e.g:

.. parsed-literal::
   See also \`OpenGL <https://en.wikipedia.org/wiki/OpenGL>`__ on Wikipedia.

Examples
--------

This entry:

.. parsed-literal::
   Displacement Mapping
      Uses a grayscale heightmap, like Bump Mapping,
      but the image is used to physically move the vertices of the mesh at render time.
      This is of course only useful if the mesh has large amounts of vertices.

would be written like this instead, putting a definition first:

.. parsed-literal::
   Displacement Mapping
      A method for distorting vertices based on an image.
      Similar to Bump Mapping, but instead operates on the mesh's actual geometry.
      This relies on the mesh having enough geometry.

This entry:

.. parsed-literal::
   Doppler Effect
      The Doppler effect is the change in pitch that occurs
      when a sound has a velocity relative to the listener.

would be written like this, avoiding the immediate repetition of the term:

.. parsed-literal::
   Doppler Effect
      Perceived change in pitch that occurs
      when the source of a sound is moving relative to the listener.

This entry:

.. parsed-literal::
   Curve
      It is a class of objects.
      In Blender there are Bézier curves and NURBS curves.

would be written like this, avoiding the “it is”:

.. parsed-literal::
   Curve
      A type of object defined in terms of a line interpolated between Control Vertices.
      Available types of curves include Bézier and NURBS.



