Application Translations (bpy.app.translations)
===============================================

.. module:: bpy.app.translations

This object contains some data/methods regarding internationalization in Blender, and allows every py script
to feature translations for its own UI messages.

Intro
-----

.. warning::

   Most of this object should only be useful if you actually manipulate i18n stuff from Python.
   If you are a regular add-on, you should only bother about :const:`contexts` member,
   and the :func:`register`/:func:`unregister` functions! The :func:`pgettext` family of functions
   should only be used in rare, specific cases (like e.g. complex "composited" UI strings...).

| To add translations to your python script, you must define a dictionary formatted like that:
|    ``{locale: {msg_key: msg_translation, ...}, ...}``
| where:

- locale is either a lang iso code (e.g. ``fr``), a lang+country code (e.g. ``pt_BR``),
  a lang+variant code (e.g. ``sr@latin``), or a full code (e.g. ``uz_UZ@cyrilic``).
- msg_key is a tuple (context, org message) - use, as much as possible, the predefined :const:`contexts`.
- msg_translation is the translated message in given language!

Then, call ``bpy.app.translations.register(__name__, your_dict)`` in your ``register()`` function, and
``bpy.app.translations.unregister(__name__)`` in your ``unregister()`` one.

The ``Manage UI translations`` add-on has several functions to help you collect strings to translate, and
generate the needed python code (the translation dictionary), as well as optional intermediary po files
if you want some... See
`How to Translate Blender <https://wiki.blender.org/index.php/Dev:Doc/Process/Translate_Blender>`_ and
`Using i18n in Blender Code <https://wiki.blender.org/index.php/Dev:Source/Interface/Internationalization>`_
for more info.

Module References
-----------------


.. literalinclude:: ..\examples\bpy.app.translations.py
   :lines: 35-

.. attribute:: locale

   The actual locale currently in use (will always return a void string when Blender is built without internationalization support).


.. attribute:: locales

   All locales currently known by Blender (i.e. available as translations).


.. data:: contexts_C_to_py

   A readonly dict mapping contexts' C-identifiers to their py-identifiers.


.. data:: contexts

   constant value bpy.app.translations.contexts(default_real=None, default='*', operator_default='Operator', ui_events_keymaps='UI_Events_KeyMaps', plural='Plural', id_action='Action', id_armature='Armature', id_brush='Brush', id_camera='Camera', id_cachefile='CacheFile', id_curve='Curve', id_fs_linestyle='FreestyleLineStyle', id_gpencil='GPencil', id_group='Group', id_id='ID', id_image='Image', id_shapekey='Key', id_lamp='Lamp', id_library='Library', id_lattice='Lattice', id_mask='Mask', id_material='Material', ...)

.. method:: locale_explode(locale)

   Return all components and their combinations  of the given ISO locale string.

   >>> bpy.app.translations.locale_explode("sr_RS@latin")
   ("sr", "RS", "latin", "sr_RS", "sr@latin")

   For non-complete locales, missing elements will be None.

   :arg locale: The ISO locale string to explode.
   :type msgid: string
   :return: A tuple ``(language, country, variant, language_country, language@variant)``.


.. method:: pgettext(msgid, msgctxt)

   Try to translate the given msgid (with optional msgctxt).

   .. note::
       The ``(msgid, msgctxt)`` parameters order has been switched compared to gettext function, to allow
       single-parameter calls (context then defaults to BLT_I18NCONTEXT_DEFAULT).

   .. note::
       You should really rarely need to use this function in regular addon code, as all translation should be
       handled by Blender internal code. The only exception are string containing formatting (like "File: %r"),
       but you should rather use :func:`pgettext_iface`/:func:`pgettext_tip` in those cases!

   .. note::
       Does nothing when Blender is built without internationalization support (hence always returns ``msgid``).

   :arg msgid: The string to translate.
   :type msgid: string
   :arg msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
   :type msgctxt: string or None
   :return: The translated string (or msgid if no translation was found).


.. method:: pgettext_data(msgid, msgctxt)

   Try to translate the given msgid (with optional msgctxt), if new data name's translation is enabled.

   .. note::
       See :func:`pgettext` notes.

   :arg msgid: The string to translate.
   :type msgid: string
   :arg msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
   :type msgctxt: string or None
   :return: The translated string (or ``msgid`` if no translation was found).


.. method:: pgettext_iface(msgid, msgctxt)

   Try to translate the given msgid (with optional msgctxt), if labels' translation is enabled.

   .. note::
       See :func:`pgettext` notes.

   :arg msgid: The string to translate.
   :type msgid: string
   :arg msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
   :type msgctxt: string or None
   :return: The translated string (or msgid if no translation was found).


.. method:: pgettext_tip(msgid, msgctxt)

   Try to translate the given msgid (with optional msgctxt), if tooltips' translation is enabled.

   .. note::
       See :func:`pgettext` notes.

   :arg msgid: The string to translate.
   :type msgid: string
   :arg msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
   :type msgctxt: string or None
   :return: The translated string (or msgid if no translation was found).


.. method:: register(module_name, translations_dict)

   Registers an addon's UI translations.

   .. note::
       Does nothing when Blender is built without internationalization support.

   :arg module_name: The name identifying the addon.
   :type module_name: string
   :arg translations_dict: A dictionary built like that:
       ``{locale: {msg_key: msg_translation, ...}, ...}``
   :type translations_dict: dict


.. method:: unregister(module_name)

   Unregisters an addon's UI translations.

   .. note::
       Does nothing when Blender is built without internationalization support.

   :arg module_name: The name identifying the addon.
   :type module_name: string


