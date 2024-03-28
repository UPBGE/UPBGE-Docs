.. _bpy.types.Filter2DActuator:

==============================
Filter 2D Actuator
==============================

.. seealso::
   See the Python reference of this logic brick in :class:`SCA_2DFilterActuator`.

The *Filter 2D Actuator* adds image filters, that apply on final render of objects. There are several 2D filters each listed below. Most are self-explanatory, however, some are special and will be described in detail later.

-  Custom Filter
-  Invert
-  Sepia
-  Gray Scale
-  Prewitt
-  Sobel
-  Laplacian
-  Erosion
-  Dilation
-  Sharpen
-  Blur
-  Motion Blur (currently not working)
-  Remove Filter
-  Disable Filter
-  Enable Filter

.. figure:: /images/logic_bricks/actuators/logic-actuators-types-filter_2d-filter_2d.png

   Filter 2D actuator

Properties
++++++++++++++++++++++++++++++

Filter 2D Type
   Selects the type of 2D filter to use. All 2D filters are rendered with fragment shaders so your hardware must support fragment shaders. Several of the filters are called "built-in filters", these are: Blur, Sharpen, Dilation, Erosion, Laplacian, Sobel, Prewitt, Gray Scale, Sepia, and Invert. There are however some filters that work differently from the ones above and are described separately.

   .. figure:: /images/logic_bricks/actuators/logic-actuators-types-filter_2d-built_in_filters.png

      Built-in Filters

Pass Number
   The pass number for the filter to use.

Details of special filters are described below.

Enable/Disable Filters
------------------------------

There are two filters which can be used to either *Enable* or *Disable* other filters.

To enable/disable a filter on a specific pass:

#. Create appropriate sensor(s) and controller(s).
#. Create a *2D Filter* actuator.
#. Select either *Enable Filter* or *Disable Filter* depending on what you want to do.
#. Set the pass number you want to disable the filter on it.

Removing Filters
------------------------------

The *Remove Filter* is used to remove other 2D filters.

To remove a filter on a specific pass:

#. Create appropriate sensor(s) and controller(s).
#. Create a *2D Filter* actuator.
#. Select *Remove Filter*.
#. Set the pass number you want to remove the filter from it.

Custom Filters
++++++++++++++++++++++++++++++

Custom filters give you the ability to define your own 2D filter using GLSL. Its usage is the same as built-in filters, but you must select *Custom Filter* in *2D Filter* actuator, then write shader program into the Text Editor, and then place shader script name on actuator.

.. figure:: /images/logic_bricks/actuators/logic-actuators-types-filter_2d-custom_filter.png

   2D Filters: Custom Filter

FXAA Antialiasing Example:

.. figure:: /images/logic_bricks/actuators/logic-actuators-types-filter_2d-custom_filter1.png

   Custom Filter: FXAA Antialiasing Filter

At *Text Editor* under Templates / OpenGL Shading Language there is a FXAA antialiasing filter that can be used as a *Custom Filter*. Once opened in the *Text Editor* can be used in the *2D Filter* actuator under *Custom Filter* option.

Examples
++++++++++++++++++++++++++++++

Built-in Filters
------------------------------

.. list-table::

   * - .. figure:: /images/logic_bricks/actuators/logic-actuators-types-filter_2d-sepia_render_full.jpg

          Sepia Filter

     - .. figure:: /images/logic_bricks/actuators/logic-actuators-types-filter_2d-sobel_render_full.jpg

          Sobel Filter
