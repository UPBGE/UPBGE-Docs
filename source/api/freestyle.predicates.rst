Freestyle Predicates (freestyle.predicates)
===========================================

.. module:: freestyle.predicates

This module contains predicates operating on vertices (0D elements)
and polylines (1D elements).  It is also intended to be a collection
of examples for predicate definition in Python.

User-defined predicates inherit one of the following base classes,
depending on the object type (0D or 1D) to operate on and the arity
(unary or binary):

- :class:`freestyle.types.BinaryPredicate0D`
- :class:`freestyle.types.BinaryPredicate1D`
- :class:`freestyle.types.UnaryPredicate0D`
- :class:`freestyle.types.UnaryPredicate1D`

.. class:: AndBP1D




.. class:: AndUP1D




.. class:: ContourUP1D

   Class hierarchy: :class:`freestyle.types.UnaryPredicate1D` > :class:`ContourUP1D`
   
   .. method:: __call__(inter)
   
      Returns true if the Interface1D is a contour.  An Interface1D is a
      contour if it is borded by a different shape on each of its sides.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: True if the Interface1D is a contour, false otherwise.
      :rtype: bool



.. class:: DensityLowerThanUP1D

   Class hierarchy: :class:`freestyle.types.UnaryPredicate1D` > :class:`DensityLowerThanUP1D`
   
   .. method:: __init__(threshold, sigma=2.0)
   
      Builds a DensityLowerThanUP1D object.
   
      :arg threshold: The value of the threshold density.  Any Interface1D
         having a density lower than this threshold will match.
      :type threshold: float
      :arg sigma: The sigma value defining the density evaluation window
         size used in the :class:`freestyle.functions.DensityF0D` functor.
      :type sigma: float
   
   .. method:: __call__(inter)
   
      Returns true if the density evaluated for the Interface1D is less
      than a user-defined density value.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: True if the density is lower than a threshold.
      :rtype: bool



.. class:: EqualToChainingTimeStampUP1D

   Class hierarchy: :class:`freestyle.types.UnaryPredicate1D` > :class:`freestyle.types.EqualToChainingTimeStampUP1D`
   
   .. method:: __init__(ts)
   
      Builds a EqualToChainingTimeStampUP1D object.
   
      :arg ts: A time stamp value.
      :type ts: int
   
   .. method:: __call__(inter)
   
      Returns true if the Interface1D's time stamp is equal to a certain
      user-defined value.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: True if the time stamp is equal to a user-defined value.
      :rtype: bool



.. class:: EqualToTimeStampUP1D

   Class hierarchy: :class:`freestyle.types.UnaryPredicate1D` > :class:`EqualToTimeStampUP1D`
   
   .. method:: __init__(ts)
   
      Builds a EqualToTimeStampUP1D object.
   
      :arg ts: A time stamp value.
      :type ts: int
   
   .. method:: __call__(inter)
   
      Returns true if the Interface1D's time stamp is equal to a certain
      user-defined value.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: True if the time stamp is equal to a user-defined value.
      :rtype: bool



.. class:: ExternalContourUP1D

   Class hierarchy: :class:`freestyle.types.UnaryPredicate1D` > :class:`ExternalContourUP1D`
   
   .. method:: __call__(inter)
   
      Returns true if the Interface1D is an external contour.  An
      Interface1D is an external contour if it is borded by no shape on
      one of its sides.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: True if the Interface1D is an external contour, false
         otherwise.
      :rtype: bool



.. class:: FalseBP1D

   Class hierarchy: :class:`freestyle.types.BinaryPredicate1D` > :class:`FalseBP1D`
   
   .. method:: __call__(inter1, inter2)
   
      Always returns false.
   
      :arg inter1: The first Interface1D object.
      :type inter1: :class:`freestyle.types.Interface1D`
      :arg inter2: The second Interface1D object.
      :type inter2: :class:`freestyle.types.Interface1D`
      :return: False.
      :rtype: bool



.. class:: FalseUP0D

   Class hierarchy: :class:`freestyle.types.UnaryPredicate0D` > :class:`FalseUP0D`
   
   .. method:: __call__(it)
   
      Always returns false.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: False.
      :rtype: bool



.. class:: FalseUP1D

   Class hierarchy: :class:`freestyle.types.UnaryPredicate1D` > :class:`FalseUP1D`
   
   .. method:: __call__(inter)
   
      Always returns false.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: False.
      :rtype: bool



.. class:: Length2DBP1D

   Class hierarchy: :class:`freestyle.types.BinaryPredicate1D` > :class:`Length2DBP1D`
   
   .. method:: __call__(inter1, inter2)
   
      Returns true if the 2D length of inter1 is less than the 2D length
      of inter2.
   
      :arg inter1: The first Interface1D object.
      :type inter1: :class:`freestyle.types.Interface1D`
      :arg inter2: The second Interface1D object.
      :type inter2: :class:`freestyle.types.Interface1D`
      :return: True or false.
      :rtype: bool



.. class:: MaterialBP1D

   Checks whether the two supplied ViewEdges have the same material.



.. class:: NotBP1D




.. class:: NotUP1D




.. class:: ObjectNamesUP1D




.. class:: OrBP1D




.. class:: OrUP1D




.. class:: QuantitativeInvisibilityRangeUP1D




.. class:: QuantitativeInvisibilityUP1D

   Class hierarchy: :class:`freestyle.types.UnaryPredicate1D` > :class:`QuantitativeInvisibilityUP1D`
   
   .. method:: __init__(qi=0)
   
      Builds a QuantitativeInvisibilityUP1D object.
   
      :arg qi: The Quantitative Invisibility you want the Interface1D to
         have.
      :type qi: int
   
   .. method:: __call__(inter)
   
      Returns true if the Quantitative Invisibility evaluated at an
      Interface1D, using the
      :class:`freestyle.functions.QuantitativeInvisibilityF1D` functor,
      equals a certain user-defined value.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: True if Quantitative Invisibility equals a user-defined
         value.
      :rtype: bool



.. class:: SameShapeIdBP1D

   Class hierarchy: :class:`freestyle.types.BinaryPredicate1D` > :class:`SameShapeIdBP1D`
   
   .. method:: __call__(inter1, inter2)
   
      Returns true if inter1 and inter2 belong to the same shape.
   
      :arg inter1: The first Interface1D object.
      :type inter1: :class:`freestyle.types.Interface1D`
      :arg inter2: The second Interface1D object.
      :type inter2: :class:`freestyle.types.Interface1D`
      :return: True or false.
      :rtype: bool



.. class:: ShapeUP1D

   Class hierarchy: :class:`freestyle.types.UnaryPredicate1D` > :class:`ShapeUP1D`
   
   .. method:: __init__(first, second=0)
   
      Builds a ShapeUP1D object.
   
      :arg first: The first Id component.
      :type first: int
      :arg second: The second Id component.
      :type second: int
   
   .. method:: __call__(inter)
   
      Returns true if the shape to which the Interface1D belongs to has the
      same :class:`freestyle.types.Id` as the one specified by the user.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: True if Interface1D belongs to the shape of the
         user-specified Id.
      :rtype: bool



.. class:: TrueBP1D

   Class hierarchy: :class:`freestyle.types.BinaryPredicate1D` > :class:`TrueBP1D`
   
   .. method:: __call__(inter1, inter2)
   
      Always returns true.
   
      :arg inter1: The first Interface1D object.
      :type inter1: :class:`freestyle.types.Interface1D`
      :arg inter2: The second Interface1D object.
      :type inter2: :class:`freestyle.types.Interface1D`
      :return: True.
      :rtype: bool



.. class:: TrueUP0D

   Class hierarchy: :class:`freestyle.types.UnaryPredicate0D` > :class:`TrueUP0D`
   
   .. method:: __call__(it)
   
      Always returns true.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: True.
      :rtype: bool



.. class:: TrueUP1D

   Class hierarchy: :class:`freestyle.types.UnaryPredicate1D` > :class:`TrueUP1D`
   
   .. method:: __call__(inter)
   
      Always returns true.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: True.
      :rtype: bool



.. class:: ViewMapGradientNormBP1D

   Class hierarchy: :class:`freestyle.types.BinaryPredicate1D` > :class:`ViewMapGradientNormBP1D`
   
   .. method:: __init__(level, integration_type=IntegrationType.MEAN, sampling=2.0)
   
      Builds a ViewMapGradientNormBP1D object.
   
      :arg level: The level of the pyramid from which the pixel must be
         read.
      :type level: int
      :arg integration_type: The integration method used to compute a single value
         from a set of values.
      :type integration_type: :class:`freestyle.types.IntegrationType`
      :arg sampling: The resolution used to sample the chain:
         GetViewMapGradientNormF0D is evaluated at each sample point and
         the result is obtained by combining the resulting values into a
         single one, following the method specified by integration_type.
      :type sampling: float
   
   .. method:: __call__(inter1, inter2)
   
      Returns true if the evaluation of the Gradient norm Function is
      higher for inter1 than for inter2.
   
      :arg inter1: The first Interface1D object.
      :type inter1: :class:`freestyle.types.Interface1D`
      :arg inter2: The second Interface1D object.
      :type inter2: :class:`freestyle.types.Interface1D`
      :return: True or false.
      :rtype: bool



.. class:: WithinImageBoundaryUP1D

   Class hierarchy: :class:`freestyle.types.UnaryPredicate1D` > :class:`WithinImageBoundaryUP1D`
   
   .. method:: __init__(xmin, ymin, xmax, ymax)
   
      Builds an WithinImageBoundaryUP1D object.
   
      :arg xmin: X lower bound of the image boundary.
      :type xmin: float
      :arg ymin: Y lower bound of the image boundary.
      :type ymin: float
      :arg xmax: X upper bound of the image boundary.
      :type xmax: float
      :arg ymax: Y upper bound of the image boundary.
      :type ymax: float
   
   .. method:: __call__(inter)
   
      Returns true if the Interface1D intersects with image boundary.



.. class:: pyBackTVertexUP0D

   Check whether an Interface0DIterator references a TVertex and is
   the one that is hidden (inferred from the context).



.. class:: pyClosedCurveUP1D




.. class:: pyDensityFunctorUP1D




.. class:: pyDensityUP1D




.. class:: pyDensityVariableSigmaUP1D




.. class:: pyHighDensityAnisotropyUP1D




.. class:: pyHighDirectionalViewMapDensityUP1D




.. class:: pyHighSteerableViewMapDensityUP1D




.. class:: pyHighViewMapDensityUP1D




.. class:: pyHighViewMapGradientNormUP1D




.. class:: pyHigherCurvature2DAngleUP0D




.. class:: pyHigherLengthUP1D




.. class:: pyHigherNumberOfTurnsUP1D




.. class:: pyIsInOccludersListUP1D




.. class:: pyIsOccludedByIdListUP1D




.. class:: pyIsOccludedByItselfUP1D




.. class:: pyIsOccludedByUP1D




.. class:: pyLengthBP1D




.. class:: pyLowDirectionalViewMapDensityUP1D




.. class:: pyLowSteerableViewMapDensityUP1D




.. class:: pyNFirstUP1D




.. class:: pyNatureBP1D




.. class:: pyNatureUP1D




.. class:: pyParameterUP0D




.. class:: pyParameterUP0DGoodOne




.. class:: pyProjectedXBP1D




.. class:: pyProjectedYBP1D




.. class:: pyShapeIdListUP1D




.. class:: pyShapeIdUP1D




.. class:: pyShuffleBP1D




.. class:: pySilhouetteFirstBP1D




.. class:: pyUEqualsUP0D




.. class:: pyVertexNatureUP0D




.. class:: pyViewMapGradientNormBP1D




.. class:: pyZBP1D




.. class:: pyZDiscontinuityBP1D




.. class:: pyZSmallerUP1D




