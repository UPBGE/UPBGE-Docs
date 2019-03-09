freestyle.utils submodule (freestyle.utils.ContextFunctions)
============================================================

.. module:: freestyle.utils.ContextFunctions

The Blender Freestyle.ContextFunctions submodule

.. method:: get_border()

   Returns the border.

   :return: A tuple of 4 numbers (xmin, ymin, xmax, ymax).
   :rtype: tuple


.. method:: get_canvas_height()

   Returns the canvas height.

   :return: The canvas height.
   :rtype: int


.. method:: get_canvas_width()

   Returns the canvas width.

   :return: The canvas width.
   :rtype: int


.. function:: get_selected_fedge()

   Returns the selected FEdge.

   :return: The selected FEdge.
   :rtype: :class:`FEdge`


.. function:: get_time_stamp()

   Returns the system time stamp.

   :return: The system time stamp.
   :rtype: int


.. function:: load_map(file_name, map_name, num_levels=4, sigma=1.0)

   Loads an image map for further reading.

   :arg file_name: The name of the image file.
   :type file_name: str
   :arg map_name: The name that will be used to access this image.
   :type map_name: str
   :arg num_levels: The number of levels in the map pyramid
      (default = 4).  If num_levels == 0, the complete pyramid is
      built.
   :type num_levels: int
   :arg sigma: The sigma value of the gaussian function.
   :type sigma: float


.. function:: read_complete_view_map_pixel(level, x, y)

   Reads a pixel in the complete view map.

   :arg level: The level of the pyramid in which we wish to read the
      pixel.
   :type level: int
   :arg x: The x coordinate of the pixel we wish to read.  The origin
      is in the lower-left corner.
   :type x: int
   :arg y: The y coordinate of the pixel we wish to read.  The origin
      is in the lower-left corner.
   :type y: int
   :return: The floating-point value stored for that pixel.
   :rtype: float


.. function:: read_directional_view_map_pixel(orientation, level, x, y)

   Reads a pixel in one of the oriented view map images.

   :arg orientation: The number telling which orientation we want to
      check.
   :type orientation: int
   :arg level: The level of the pyramid in which we wish to read the
      pixel.
   :type level: int
   :arg x: The x coordinate of the pixel we wish to read.  The origin
      is in the lower-left corner.
   :type x: int
   :arg y: The y coordinate of the pixel we wish to read.  The origin
      is in the lower-left corner.
   :type y: int
   :return: The floating-point value stored for that pixel.
   :rtype: float


.. function:: read_map_pixel(map_name, level, x, y)

   Reads a pixel in a user-defined map.

   :arg map_name: The name of the map.
   :type map_name: str
   :arg level: The level of the pyramid in which we wish to read the
      pixel.
   :type level: int
   :arg x: The x coordinate of the pixel we wish to read.  The origin
      is in the lower-left corner.
   :type x: int
   :arg y: The y coordinate of the pixel we wish to read.  The origin
      is in the lower-left corner.
   :type y: int
   :return: The floating-point value stored for that pixel.
   :rtype: float


