View2D Operators
================

.. module:: bpy.ops.view2d

.. function:: ndof()

   Use a 3D mouse device to pan/zoom the view

.. function:: pan(deltax=0, deltay=0)

   Pan the view

   :arg deltax:

      Delta X

   :type deltax: int in [-inf, inf], (optional)
   :arg deltay:

      Delta Y

   :type deltay: int in [-inf, inf], (optional)

.. function:: reset()

   Reset the view

.. function:: scroll_down(deltax=0, deltay=0, page=False)

   Scroll the view down

   :arg deltax:

      Delta X

   :type deltax: int in [-inf, inf], (optional)
   :arg deltay:

      Delta Y

   :type deltay: int in [-inf, inf], (optional)
   :arg page:

      Page, Scroll down one page

   :type page: boolean, (optional)

.. function:: scroll_left(deltax=0, deltay=0)

   Scroll the view left

   :arg deltax:

      Delta X

   :type deltax: int in [-inf, inf], (optional)
   :arg deltay:

      Delta Y

   :type deltay: int in [-inf, inf], (optional)

.. function:: scroll_right(deltax=0, deltay=0)

   Scroll the view right

   :arg deltax:

      Delta X

   :type deltax: int in [-inf, inf], (optional)
   :arg deltay:

      Delta Y

   :type deltay: int in [-inf, inf], (optional)

.. function:: scroll_up(deltax=0, deltay=0, page=False)

   Scroll the view up

   :arg deltax:

      Delta X

   :type deltax: int in [-inf, inf], (optional)
   :arg deltay:

      Delta Y

   :type deltay: int in [-inf, inf], (optional)
   :arg page:

      Page, Scroll up one page

   :type page: boolean, (optional)

.. function:: scroller_activate()

   Scroll view by mouse click and drag

.. function:: smoothview(xmin=0, xmax=0, ymin=0, ymax=0)

   Undocumented

   :arg xmin:

      X Min

   :type xmin: int in [-inf, inf], (optional)
   :arg xmax:

      X Max

   :type xmax: int in [-inf, inf], (optional)
   :arg ymin:

      Y Min

   :type ymin: int in [-inf, inf], (optional)
   :arg ymax:

      Y Max

   :type ymax: int in [-inf, inf], (optional)

.. function:: zoom(deltax=0.0, deltay=0.0)

   Zoom in/out the view

   :arg deltax:

      Delta X

   :type deltax: float in [-inf, inf], (optional)
   :arg deltay:

      Delta Y

   :type deltay: float in [-inf, inf], (optional)

.. function:: zoom_border(xmin=0, xmax=0, ymin=0, ymax=0, zoom_out=False)

   Zoom in the view to the nearest item contained in the border

   :arg xmin:

      X Min

   :type xmin: int in [-inf, inf], (optional)
   :arg xmax:

      X Max

   :type xmax: int in [-inf, inf], (optional)
   :arg ymin:

      Y Min

   :type ymin: int in [-inf, inf], (optional)
   :arg ymax:

      Y Max

   :type ymax: int in [-inf, inf], (optional)
   :arg zoom_out:

      Zoom Out

   :type zoom_out: boolean, (optional)

.. function:: zoom_in(zoomfacx=0.0, zoomfacy=0.0)

   Zoom in the view

   :arg zoomfacx:

      Zoom Factor X

   :type zoomfacx: float in [-inf, inf], (optional)
   :arg zoomfacy:

      Zoom Factor Y

   :type zoomfacy: float in [-inf, inf], (optional)

.. function:: zoom_out(zoomfacx=0.0, zoomfacy=0.0)

   Zoom out the view

   :arg zoomfacx:

      Zoom Factor X

   :type zoomfacx: float in [-inf, inf], (optional)
   :arg zoomfacy:

      Zoom Factor Y

   :type zoomfacy: float in [-inf, inf], (optional)

