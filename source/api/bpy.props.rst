Property Definitions (bpy.props)
================================

.. module:: bpy.props

This module defines properties to extend Blender's internal data. The result of these functions is used to assign properties to classes registered with Blender and can't be used directly.

.. note:: All parameters to these functions must be passed as keywords.

Assigning to Existing Classes
+++++++++++++++++++++++++++++

Custom properties can be added to any subclass of an :class:`ID`,
:class:`Bone` and :class:`PoseBone`.

These properties can be animated, accessed by the user interface and python
like Blender's existing properties.

.. literalinclude:: ..\examples\bpy.props.py
   :lines: 11-

Operator Example
++++++++++++++++

A common use of custom properties is for python based :class:`Operator` classes.

.. literalinclude:: ..\examples\bpy.props.1.py
   :lines: 7-

PropertyGroup Example
+++++++++++++++++++++

PropertyGroups can be used for collecting custom settings into one value
to avoid many individual settings mixed in together.

.. literalinclude:: ..\examples\bpy.props.2.py
   :lines: 8-

Collection Example
++++++++++++++++++

Custom properties can be added to any subclass of an :class:`ID`,
:class:`Bone` and :class:`PoseBone`.

.. literalinclude:: ..\examples\bpy.props.3.py
   :lines: 8-

Update Example
++++++++++++++

It can be useful to perform an action when a property is changed and can be
used to update other properties or synchronize with external data.

All properties define update functions except for CollectionProperty.

.. literalinclude:: ..\examples\bpy.props.4.py
   :lines: 10-

Get/Set Example
+++++++++++++++

Get/Set functions can be used for boolean, int, float, string and enum properties.
If these callbacks are defined the property will not be stored in the ID properties
automatically, instead the get/set functions will be called when the property is
read or written from the API.

.. literalinclude:: ..\examples\bpy.props.5.py
   :lines: 10-

.. function:: BoolProperty(name="", description="", default=False, options={'ANIMATABLE'}, tags={}, subtype='NONE', update=None, get=None, set=None)

   Returns a new boolean property definition.

   :arg name: Name used in the user interface.
   :type name: string
   :arg description: Text used for the tooltip and api documentation.
   :type description: string
   :arg options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
   :type options: set
   :arg tags: Enumerator of tags that are defined by parent class.
   :type tags: set
   :arg subtype: Enumerator in ['PIXEL', 'UNSIGNED', 'PERCENTAGE', 'FACTOR', 'ANGLE', 'TIME', 'DISTANCE', 'NONE'].
   :type subtype: string
   :arg update: Function to be called when this value is modified,
      This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
   :type update: function
   :arg get: Function to be called when this value is 'read',
      This function must take 1 value (self) and return the value of the property.
   :type get: function
   :arg set: Function to be called when this value is 'written',
      This function must take 2 values (self, value) and return None.
   :type set: function


.. function:: BoolVectorProperty(name="", description="", default=(False, False, False), options={'ANIMATABLE'}, tags={}, subtype='NONE', size=3, update=None, get=None, set=None)

   Returns a new vector boolean property definition.

   :arg name: Name used in the user interface.
   :type name: string
   :arg description: Text used for the tooltip and api documentation.
   :type description: string
   :arg default: sequence of booleans the length of *size*.
   :type default: sequence
   :arg options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
   :type options: set
   :arg tags: Enumerator of tags that are defined by parent class.
   :type tags: set
   :arg subtype: Enumerator in ['COLOR', 'TRANSLATION', 'DIRECTION', 'VELOCITY', 'ACCELERATION', 'MATRIX', 'EULER', 'QUATERNION', 'AXISANGLE', 'XYZ', 'COLOR_GAMMA', 'LAYER', 'NONE'].
   :type subtype: string
   :arg size: Vector dimensions in [1, 32].
   :type size: int
   :arg update: Function to be called when this value is modified,
      This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
   :type update: function
   :arg get: Function to be called when this value is 'read',
      This function must take 1 value (self) and return the value of the property.
   :type get: function
   :arg set: Function to be called when this value is 'written',
      This function must take 2 values (self, value) and return None.
   :type set: function


.. function:: CollectionProperty(type=None, name="", description="", options={'ANIMATABLE'}, tags={})

   Returns a new collection property definition.

   :arg type: A subclass of :class:`bpy.types.PropertyGroup` or :class:`bpy.types.ID`.
   :type type: class
   :arg name: Name used in the user interface.
   :type name: string
   :arg description: Text used for the tooltip and api documentation.
   :type description: string
   :arg options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
   :type options: set
   :arg tags: Enumerator of tags that are defined by parent class.
   :type tags: set


.. function:: EnumProperty(items, name="", description="", default=None, options={'ANIMATABLE'}, tags={}, update=None, get=None, set=None)

   Returns a new enumerator property definition.

   :arg items: sequence of enum items formatted:
      ``[(identifier, name, description, icon, number), ...]``.

      The first three elements of the tuples are mandatory.

      :identifier: The identifier is used for Python access.
      :name: Name for the interace.
      :description: Used for documentation and tooltips.
      :icon: An icon string identifier or integer icon value
         (e.g. returned by :class:`bpy.types.UILayout.icon`)
      :number: Unique value used as the identifier for this item (stored in file data).
         Use when the identifier may need to change. If the *ENUM_FLAG* option is used,
         the values are bitmasks and should be powers of two.

      When an item only contains 4 items they define ``(identifier, name, description, number)``.

      For dynamic values a callback can be passed which returns a list in
      the same format as the static list.
      This function must take 2 arguments ``(self, context)``, **context may be None**.

      .. warning::

         There is a known bug with using a callback,
         Python must keep a reference to the strings returned or Blender will misbehave
         or even crash.
   :type items: sequence of string tuples or a function
   :arg name: Name used in the user interface.
   :type name: string
   :arg description: Text used for the tooltip and api documentation.
   :type description: string
   :arg default: The default value for this enum, a string from the identifiers used in *items*.
      If the *ENUM_FLAG* option is used this must be a set of such string identifiers instead.
      WARNING: It shall not be specified (or specified to its default *None* value) for dynamic enums
      (i.e. if a callback function is given as *items* parameter).
   :type default: string or set
   :arg options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'ENUM_FLAG', 'LIBRARY_EDITABLE'].
   :type options: set
   :arg tags: Enumerator of tags that are defined by parent class.
   :type tags: set
   :arg update: Function to be called when this value is modified,
      This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
   :type update: function
   :arg get: Function to be called when this value is 'read',
      This function must take 1 value (self) and return the value of the property.
   :type get: function
   :arg set: Function to be called when this value is 'written',
      This function must take 2 values (self, value) and return None.
   :type set: function


.. function:: FloatProperty(name="", description="", default=0.0, min=sys.float_info.min, max=sys.float_info.max, soft_min=sys.float_info.min, soft_max=sys.float_info.max, step=3, precision=2, options={'ANIMATABLE'}, tags={}, subtype='NONE', unit='NONE', update=None, get=None, set=None)

   Returns a new float property definition.

   :arg name: Name used in the user interface.
   :type name: string
   :arg description: Text used for the tooltip and api documentation.
   :type description: string
   :arg min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
   :type min: float
   :arg max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
   :type max: float
   :arg soft_min: Soft minimum (>= *min*), user won't be able to drag the widget below this value in the UI.
   :type soft_min: float
   :arg soft_max: Soft maximum (<= *max*), user won't be able to drag the widget above this value in the UI.
   :type soft_max: float
   :arg step: Step of increment/decrement in UI, in [1, 100], defaults to 3 (WARNING: actual value is /100).
   :type step: int
   :arg precision: Maximum number of decimal digits to display, in [0, 6].
   :type precision: int
   :arg options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
   :type options: set
   :arg tags: Enumerator of tags that are defined by parent class.
   :type tags: set
   :arg subtype: Enumerator in ['PIXEL', 'UNSIGNED', 'PERCENTAGE', 'FACTOR', 'ANGLE', 'TIME', 'DISTANCE', 'NONE'].
   :type subtype: string
   :arg unit: Enumerator in ['NONE', 'LENGTH', 'AREA', 'VOLUME', 'ROTATION', 'TIME', 'VELOCITY', 'ACCELERATION'].
   :type unit: string
   :arg update: Function to be called when this value is modified,
      This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
   :type update: function
   :arg get: Function to be called when this value is 'read',
      This function must take 1 value (self) and return the value of the property.
   :type get: function
   :arg set: Function to be called when this value is 'written',
      This function must take 2 values (self, value) and return None.
   :type set: function


.. function:: FloatVectorProperty(name="", description="", default=(0.0, 0.0, 0.0), min=sys.float_info.min, max=sys.float_info.max, soft_min=sys.float_info.min, soft_max=sys.float_info.max, step=3, precision=2, options={'ANIMATABLE'}, tags={}, subtype='NONE', unit='NONE', size=3, update=None, get=None, set=None)

   Returns a new vector float property definition.

   :arg name: Name used in the user interface.
   :type name: string
   :arg description: Text used for the tooltip and api documentation.
   :type description: string
   :arg default: sequence of floats the length of *size*.
   :type default: sequence
   :arg min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
   :type min: float
   :arg max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
   :type max: float
   :arg soft_min: Soft minimum (>= *min*), user won't be able to drag the widget below this value in the UI.
   :type soft_min: float
   :arg soft_max: Soft maximum (<= *max*), user won't be able to drag the widget above this value in the UI.
   :type soft_max: float
   :arg options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
   :type options: set
   :arg tags: Enumerator of tags that are defined by parent class.
   :type tags: set
   :arg step: Step of increment/decrement in UI, in [1, 100], defaults to 3 (WARNING: actual value is /100).
   :type step: int
   :arg precision: Maximum number of decimal digits to display, in [0, 6].
   :type precision: int
   :arg subtype: Enumerator in ['COLOR', 'TRANSLATION', 'DIRECTION', 'VELOCITY', 'ACCELERATION', 'MATRIX', 'EULER', 'QUATERNION', 'AXISANGLE', 'XYZ', 'COLOR_GAMMA', 'LAYER', 'NONE'].
   :type subtype: string
   :arg unit: Enumerator in ['NONE', 'LENGTH', 'AREA', 'VOLUME', 'ROTATION', 'TIME', 'VELOCITY', 'ACCELERATION'].
   :type unit: string
   :arg size: Vector dimensions in [1, 32].
   :type size: int
   :arg update: Function to be called when this value is modified,
      This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
   :type update: function
   :arg get: Function to be called when this value is 'read',
      This function must take 1 value (self) and return the value of the property.
   :type get: function
   :arg set: Function to be called when this value is 'written',
      This function must take 2 values (self, value) and return None.
   :type set: function


.. function:: IntProperty(name="", description="", default=0, min=-2**31, max=2**31-1, soft_min=-2**31, soft_max=2**31-1, step=1, options={'ANIMATABLE'}, tags={}, subtype='NONE', update=None, get=None, set=None)

   Returns a new int property definition.

   :arg name: Name used in the user interface.
   :type name: string
   :arg description: Text used for the tooltip and api documentation.
   :type description: string
   :arg min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
   :type min: int
   :arg max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
   :type max: int
   :arg soft_max: Soft maximum (<= *max*), user won't be able to drag the widget above this value in the UI.
   :type soft_min: int
   :arg soft_min: Soft minimum (>= *min*), user won't be able to drag the widget below this value in the UI.
   :type soft_max: int
   :arg step: Step of increment/decrement in UI, in [1, 100], defaults to 1 (WARNING: unused currently!).
   :type step: int
   :arg options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
   :type options: set
   :arg tags: Enumerator of tags that are defined by parent class.
   :type tags: set
   :arg subtype: Enumerator in ['PIXEL', 'UNSIGNED', 'PERCENTAGE', 'FACTOR', 'ANGLE', 'TIME', 'DISTANCE', 'NONE'].
   :type subtype: string
   :arg update: Function to be called when this value is modified,
      This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
   :type update: function
   :arg get: Function to be called when this value is 'read',
      This function must take 1 value (self) and return the value of the property.
   :type get: function
   :arg set: Function to be called when this value is 'written',
      This function must take 2 values (self, value) and return None.
   :type set: function


.. function:: IntVectorProperty(name="", description="", default=(0, 0, 0), min=-2**31, max=2**31-1, soft_min=-2**31, soft_max=2**31-1, step=1, options={'ANIMATABLE'}, tags={}, subtype='NONE', size=3, update=None, get=None, set=None)

   Returns a new vector int property definition.

   :arg name: Name used in the user interface.
   :type name: string
   :arg description: Text used for the tooltip and api documentation.
   :type description: string
   :arg default: sequence of ints the length of *size*.
   :type default: sequence
   :arg min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
   :type min: int
   :arg max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
   :type max: int
   :arg soft_min: Soft minimum (>= *min*), user won't be able to drag the widget below this value in the UI.
   :type soft_min: int
   :arg soft_max: Soft maximum (<= *max*), user won't be able to drag the widget above this value in the UI.
   :type soft_max: int
   :arg step: Step of increment/decrement in UI, in [1, 100], defaults to 1 (WARNING: unused currently!).
   :type step: int
   :arg options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
   :type options: set
   :arg tags: Enumerator of tags that are defined by parent class.
   :type tags: set
   :arg subtype: Enumerator in ['COLOR', 'TRANSLATION', 'DIRECTION', 'VELOCITY', 'ACCELERATION', 'MATRIX', 'EULER', 'QUATERNION', 'AXISANGLE', 'XYZ', 'COLOR_GAMMA', 'LAYER', 'NONE'].
   :type subtype: string
   :arg size: Vector dimensions in [1, 32].
   :type size: int
   :arg update: Function to be called when this value is modified,
      This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
   :type update: function
   :arg get: Function to be called when this value is 'read',
      This function must take 1 value (self) and return the value of the property.
   :type get: function
   :arg set: Function to be called when this value is 'written',
      This function must take 2 values (self, value) and return None.
   :type set: function


.. function:: PointerProperty(type=None, name="", description="", options={'ANIMATABLE'}, tags={}, poll=None, update=None)

   Returns a new pointer property definition.

   :arg type: A subclass of :class:`bpy.types.PropertyGroup` or :class:`bpy.types.ID`.
   :type type: class
   :arg name: Name used in the user interface.
   :type name: string
   :arg description: Text used for the tooltip and api documentation.
   :type description: string
   :arg options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
   :type options: set
   :arg tags: Enumerator of tags that are defined by parent class.
   :type tags: set
   :arg poll: function to be called to determine whether an item is valid for this property.
              The function must take 2 values (self, object) and return Bool.
   :type poll: function
   :arg update: Function to be called when this value is modified,
      This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
   :type update: function


.. function:: RemoveProperty(cls, attr)

   Removes a dynamically defined property.

   :arg cls: The class containing the property (must be a positional argument).
   :type cls: type
   :arg attr: Property name (must be passed as a keyword).
   :type attr: string

.. note:: Typically this function doesn't need to be accessed directly.
   Instead use ``del cls.attr``


.. function:: StringProperty(name="", description="", default="", maxlen=0, options={'ANIMATABLE'}, tags={}, subtype='NONE', update=None, get=None, set=None)

   Returns a new string property definition.

   :arg name: Name used in the user interface.
   :type name: string
   :arg description: Text used for the tooltip and api documentation.
   :type description: string
   :arg default: initializer string.
   :type default: string
   :arg maxlen: maximum length of the string.
   :type maxlen: int
   :arg options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
   :type options: set
   :arg tags: Enumerator of tags that are defined by parent class.
   :type tags: set
   :arg subtype: Enumerator in ['FILE_PATH', 'DIR_PATH', 'FILE_NAME', 'BYTE_STRING', 'PASSWORD', 'NONE'].
   :type subtype: string
   :arg update: Function to be called when this value is modified,
      This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
   :type update: function
   :arg get: Function to be called when this value is 'read',
      This function must take 1 value (self) and return the value of the property.
   :type get: function
   :arg set: Function to be called when this value is 'written',
      This function must take 2 values (self, value) and return None.
   :type set: function


