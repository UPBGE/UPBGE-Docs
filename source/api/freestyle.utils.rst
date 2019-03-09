Freestyle Utilities (freestyle.utils)
=====================================

.. module:: freestyle.utils

This module contains helper functions used for Freestyle style module
writing.

.. toctree::
   :maxdepth: 1

   freestyle.utils.ContextFunctions.rst

.. function:: getCurrentScene()

   Returns the current scene.

   :return: The current scene.
   :rtype: :class:`bpy.types.Scene`


.. function:: integrate(func, it, it_end, integration_type)

   Returns a single value from a set of values evaluated at each 0D
   element of this 1D element.

   :arg func: The UnaryFunction0D used to compute a value at each
      Interface0D.
   :type func: :class:`UnaryFunction0D`
   :arg it: The Interface0DIterator used to iterate over the 0D
      elements of this 1D element. The integration will occur over
      the 0D elements starting from the one pointed by it.
   :type it: :class:`Interface0DIterator`
   :arg it_end: The Interface0DIterator pointing the end of the 0D
      elements of the 1D element.
   :type it_end: :class:`Interface0DIterator`
   :arg integration_type: The integration method used to compute a
      single value from a set of values.
   :type integration_type: :class:`IntegrationType`
   :return: The single value obtained for the 1D element.  The return
      value type is float if func is of the :class:`UnaryFunction0DDouble`
      or :class:`UnaryFunction0DFloat` type, and int if func is of the
      :class:`UnaryFunction0DUnsigned` type.
   :rtype: int or float


.. function:: angle_x_normal(it: Interface0DIterator)

   unsigned angle between a Point's normal and the X axis, in radians

.. function:: bound(lower, x, higher)

   Returns x bounded by a maximum and minimum value. Equivalent to:
       return min(max(x, lower), higher)

.. function:: bounding_box(stroke)

   Returns the maximum and minimum coordinates (the bounding box) of the stroke's vertices

.. function:: curvature_from_stroke_vertex(svert)

   The 3D curvature of an stroke vertex' underlying geometry
          The result is None or in the range [-inf, inf]

.. function:: find_matching_vertex(id, it)

   Finds the matching vertex, or returns None.

.. function:: get_chain_length(ve, orientation)

   Returns the 2d length of a given ViewEdge.

.. function:: get_object_name(stroke)

   Returns the name of the object that this stroke is drawn on.

.. function:: get_strokes()

   Get all strokes that are currently available

.. function:: get_test_stroke()

   Returns a static stroke object for testing 

.. function:: is_poly_clockwise(stroke)

   True if the stroke is orientated in a clockwise way, False otherwise

.. function:: iter_distance_along_stroke(stroke)

   Yields the absolute distance along the stroke up to the current vertex.

.. function:: iter_distance_from_camera(stroke, range_min, range_max, normfac)

   Yields the distance to the camera relative to the maximum
   possible distance for every stroke vertex, constrained by
   given minimum and maximum values.

.. function:: iter_distance_from_object(stroke, location, range_min, range_max, normfac)

   yields the distance to the given object relative to the maximum
   possible distance for every stroke vertex, constrained by
   given minimum and maximum values.

.. function:: iter_material_value(stroke, func, attribute)

   Yields a specific material attribute from the vertex' underlying material.

.. function:: iter_t2d_along_stroke(stroke)

   Yields the progress along the stroke.

.. function:: material_from_fedge(fe)

   get the diffuse rgba color from an FEdge

.. function:: normal_at_I0D(it: Interface0DIterator) -> Vector

   Normal at an Interface0D object. In contrast to Normal2DF0D this
          function uses the actual data instead of underlying Fedge objects.

.. function:: pairwise(iterable, types={<class 'Stroke'>, <class 'StrokeVertexIterator'>})

   Yields a tuple containing the previous and current object 

.. function:: rgb_to_bw(r, g, b)

   Method to convert rgb to a bw intensity value.

.. function:: simplify(points, tolerance)

   Simplifies a set of points

.. function:: stroke_curvature(it)

   Compute the 2D curvature at the stroke vertex pointed by the iterator 'it'.
   K = 1 / R
   where R is the radius of the circle going through the current vertex and its neighbors

.. function:: stroke_normal(stroke)

   Compute the 2D normal at the stroke vertex pointed by the iterator
   'it'.  It is noted that Normal2DF0D computes normals based on
   underlying FEdges instead, which is inappropriate for strokes when
   they have already been modified by stroke geometry modifiers.
   
   The returned normals are dynamic: they update when the
   vertex position (and therefore the vertex normal) changes.
   for use in geometry modifiers it is advised to
   cast this generator function to a tuple or list

.. function:: tripplewise(iterable)

   Yields a tuple containing the current object and its immediate neighbors 

.. class:: BoundingBox

   Object representing a bounding box consisting out of 2 2D vectors

   .. method:: inside(other)

      True if self inside other, False otherwise



.. class:: StrokeCollector

   Collects and Stores stroke objects

   .. method:: shade(stroke)



