Freestyle Functions (freestyle.functions)
=========================================

.. module:: freestyle.functions

This module contains functions operating on vertices (0D elements) and
polylines (1D elements).  The module is also intended to be a
collection of examples for function definition in Python.

User-defined functions inherit one of the following base classes,
depending on the object type (0D or 1D) to operate on and the return
value type:

- :class:`freestyle.types.UnaryFunction0DDouble`
- :class:`freestyle.types.UnaryFunction0DEdgeNature`
- :class:`freestyle.types.UnaryFunction0DFloat`
- :class:`freestyle.types.UnaryFunction0DId`
- :class:`freestyle.types.UnaryFunction0DMaterial`
- :class:`freestyle.types.UnaryFunction0DUnsigned`
- :class:`freestyle.types.UnaryFunction0DVec2f`
- :class:`freestyle.types.UnaryFunction0DVec3f`
- :class:`freestyle.types.UnaryFunction0DVectorViewShape`
- :class:`freestyle.types.UnaryFunction0DViewShape`
- :class:`freestyle.types.UnaryFunction1DDouble`
- :class:`freestyle.types.UnaryFunction1DEdgeNature`
- :class:`freestyle.types.UnaryFunction1DFloat`
- :class:`freestyle.types.UnaryFunction1DUnsigned`
- :class:`freestyle.types.UnaryFunction1DVec2f`
- :class:`freestyle.types.UnaryFunction1DVec3f`
- :class:`freestyle.types.UnaryFunction1DVectorViewShape`
- :class:`freestyle.types.UnaryFunction1DVoid`

.. class:: ChainingTimeStampF1D

   Class hierarchy: :class:`freestyle.types.UnaryFunction1D` > :class:`freestyle.types.UnaryFunction1DVoid` > :class:`ChainingTimeStampF1D`
   
   .. method:: __init__()
   
      Builds a ChainingTimeStampF1D object.
   
   .. method:: __call__(inter)
   
      Sets the chaining time stamp of the Interface1D.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`



.. class:: Curvature2DAngleF0D

   Class hierarchy: :class:`freestyle.types.UnaryFunction0D` > :class:`freestyle.types.UnaryFunction0DDouble` > :class:`Curvature2DAngleF0D`
   
   .. method:: __init__()
   
      Builds a Curvature2DAngleF0D object.
   
   .. method:: __call__(it)
   
      Returns a real value giving the 2D curvature (as an angle) of the 1D
      element to which the :class:`freestyle.types.Interface0D` pointed by
      the Interface0DIterator belongs.  The 2D curvature is evaluated at the
      Interface0D.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: The 2D curvature of the 1D element evaluated at the
         pointed Interface0D.
      :rtype: float



.. class:: Curvature2DAngleF1D

   Class hierarchy: :class:`freestyle.types.UnaryFunction1D` > :class:`freestyle.types.UnaryFunction1DDouble` > :class:`Curvature2DAngleF1D`
   
   .. method:: __init__(integration_type=IntegrationType.MEAN)
   
      Builds a Curvature2DAngleF1D object.
   
      :arg integration_type: The integration method used to compute a single value
         from a set of values.
      :type integration_type: :class:`freestyle.types.IntegrationType`
   
   .. method:: __call__(inter)
   
      Returns the 2D curvature as an angle for an Interface1D.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: The 2D curvature as an angle.
      :rtype: float



.. class:: CurveMaterialF0D

   A replacement of the built-in MaterialF0D for stroke creation.
   MaterialF0D does not work with Curves and Strokes.  Line color
   priority is used to pick one of the two materials at material
   boundaries.
   
   Notes: expects instances of CurvePoint to be iterated over
          can return None if no fedge can be found



.. class:: CurveNatureF0D

   Class hierarchy: :class:`freestyle.types.UnaryFunction0D` > :class:`freestyle.types.UnaryFunction0DEdgeNature` > :class:`CurveNatureF0D`
   
   .. method:: __init__()
   
      Builds a CurveNatureF0D object.
   
   .. method:: __call__(it)
   
      Returns the :class:`freestyle.types.Nature` of the 1D element the
      Interface0D pointed by the Interface0DIterator belongs to.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: The nature of the 1D element to which the pointed Interface0D
         belongs.
      :rtype: :class:`freestyle.types.Nature`



.. class:: CurveNatureF1D

   Class hierarchy: :class:`freestyle.types.UnaryFunction1D` > :class:`freestyle.types.UnaryFunction1DEdgeNature` > :class:`CurveNatureF1D`
   
   .. method:: __init__(integration_type=IntegrationType.MEAN)
   
      Builds a CurveNatureF1D object.
   
      :arg integration_type: The integration method used to compute a single value
         from a set of values.
      :type integration_type: :class:`freestyle.types.IntegrationType`
   
   .. method:: __call__(inter)
   
      Returns the nature of the Interface1D (silhouette, ridge, crease, and
      so on).  Except if the Interface1D is a
      :class:`freestyle.types.ViewEdge`, this result might be ambiguous.
      Indeed, the Interface1D might result from the gathering of several 1D
      elements, each one being of a different nature.  An integration
      method, such as the MEAN, might give, in this case, irrelevant
      results.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: The nature of the Interface1D.
      :rtype: :class:`freestyle.types.Nature`



.. class:: DensityF0D

   Class hierarchy: :class:`freestyle.types.UnaryFunction0D` > :class:`freestyle.types.UnaryFunction0DDouble` > :class:`DensityF0D`
   
   .. method:: __init__(sigma=2.0)
   
      Builds a DensityF0D object.
   
      :arg sigma: The gaussian sigma value indicating the X value for
         which the gaussian function is 0.5.  It leads to the window size
         value (the larger, the smoother).
      :type sigma: float
   
   .. method:: __call__(it)
   
      Returns the density of the (result) image evaluated at the
      :class:`freestyle.types.Interface0D` pointed by the
      Interface0DIterator. This density is evaluated using a pixels square
      window around the evaluation point and integrating these values using
      a gaussian.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: The density of the image evaluated at the pointed
         Interface0D.
      :rtype: float



.. class:: DensityF1D

   Class hierarchy: :class:`freestyle.types.UnaryFunction1D` > :class:`freestyle.types.UnaryFunction1DDouble` > :class:`DensityF1D`
   
   .. method:: __init__(sigma=2.0, integration_type=IntegrationType.MEAN, sampling=2.0)
   
      Builds a DensityF1D object.
   
      :arg sigma: The sigma used in DensityF0D and determining the window size
         used in each density query.
      :type sigma: float
      :arg integration_type: The integration method used to compute a single value
         from a set of values.
      :type integration_type: :class:`freestyle.types.IntegrationType`
      :arg sampling: The resolution used to sample the chain: the
         corresponding 0D function is evaluated at each sample point and
         the result is obtained by combining the resulting values into a
         single one, following the method specified by integration_type.
      :type sampling: float
   
   .. method:: __call__(inter)
   
      Returns the density evaluated for an Interface1D. The density is
      evaluated for a set of points along the Interface1D (using the
      :class:`freestyle.functions.DensityF0D` functor) with a user-defined
      sampling and then integrated into a single value using a user-defined
      integration method.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: The density evaluated for an Interface1D.
      :rtype: float



.. class:: GetCompleteViewMapDensityF1D

   Class hierarchy: :class:`freestyle.types.UnaryFunction1D` > :class:`freestyle.types.UnaryFunction1DDouble` > :class:`GetCompleteViewMapDensityF1D`
   
   .. method:: __init__(level, integration_type=IntegrationType.MEAN, sampling=2.0)
   
      Builds a GetCompleteViewMapDensityF1D object.
   
      :arg level: The level of the pyramid from which the pixel must be
         read.
      :type level: int
      :arg integration_type: The integration method used to compute a single value
         from a set of values.
      :type integration_type: :class:`freestyle.types.IntegrationType`
      :arg sampling: The resolution used to sample the chain: the
         corresponding 0D function is evaluated at each sample point and
         the result is obtained by combining the resulting values into a
         single one, following the method specified by integration_type.
      :type sampling: float
   
   .. method:: __call__(inter)
   
      Returns the density evaluated for an Interface1D in the complete
      viewmap image.  The density is evaluated for a set of points along the
      Interface1D (using the
      :class:`freestyle.functions.ReadCompleteViewMapPixelF0D` functor) and
      then integrated into a single value using a user-defined integration
      method.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: The density evaluated for the Interface1D in the complete
         viewmap image.
      :rtype: float



.. class:: GetCurvilinearAbscissaF0D

   Class hierarchy: :class:`freestyle.types.UnaryFunction0D` > :class:`freestyle.types.UnaryFunction0DFloat` > :class:`GetCurvilinearAbscissaF0D`
   
   .. method:: __init__()
   
      Builds a GetCurvilinearAbscissaF0D object.
   
   .. method:: __call__(it)
   
      Returns the curvilinear abscissa of the
      :class:`freestyle.types.Interface0D` pointed by the
      Interface0DIterator in the context of its 1D element.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: The curvilinear abscissa of the pointed Interface0D.
      :rtype: float



.. class:: GetDirectionalViewMapDensityF1D

   Class hierarchy: :class:`freestyle.types.UnaryFunction1D` > :class:`freestyle.types.UnaryFunction1DDouble` > :class:`GetDirectionalViewMapDensityF1D`
   
   .. method:: __init__(orientation, level, integration_type=IntegrationType.MEAN, sampling=2.0)
   
      Builds a GetDirectionalViewMapDensityF1D object.
   
      :arg orientation: The number of the directional map we must work
         with.
      :type orientation: int
      :arg level: The level of the pyramid from which the pixel must be
         read.
      :type level: int
      :arg integration_type: The integration method used to compute a single value
         from a set of values.
      :type integration_type: :class:`freestyle.types.IntegrationType`
      :arg sampling: The resolution used to sample the chain: the
         corresponding 0D function is evaluated at each sample point and
         the result is obtained by combining the resulting values into a
         single one, following the method specified by integration_type.
      :type sampling: float
   
   .. method:: __call__(inter)
   
      Returns the density evaluated for an Interface1D in of the steerable
      viewmaps image.  The direction telling which Directional map to choose
      is explicitly specified by the user.  The density is evaluated for a
      set of points along the Interface1D (using the
      :class:`freestyle.functions.ReadSteerableViewMapPixelF0D` functor) and
      then integrated into a single value using a user-defined integration
      method.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: the density evaluated for an Interface1D in of the
         steerable viewmaps image.
      :rtype: float



.. class:: GetOccludeeF0D

   Class hierarchy: :class:`freestyle.types.UnaryFunction0D` > :class:`freestyle.types.UnaryFunction0DViewShape` > :class:`GetOccludeeF0D`
   
   .. method:: __init__()
   
      Builds a GetOccludeeF0D object.
   
   .. method:: __call__(it)
   
      Returns the :class:`freestyle.types.ViewShape` that the Interface0D
      pointed by the Interface0DIterator occludes.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: The ViewShape occluded by the pointed Interface0D.
      :rtype: :class:`freestyle.types.ViewShape`



.. class:: GetOccludeeF1D

   Class hierarchy: :class:`freestyle.types.UnaryFunction1D` > :class:`freestyle.types.UnaryFunction1DVectorViewShape` > :class:`GetOccludeeF1D`
   
   .. method:: __init__()
   
      Builds a GetOccludeeF1D object.
   
   .. method:: __call__(inter)
   
      Returns a list of occluded shapes covered by this Interface1D.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: A list of occluded shapes covered by the Interface1D.
      :rtype: list of :class:`freestyle.types.ViewShape` objects



.. class:: GetOccludersF0D

   Class hierarchy: :class:`freestyle.types.UnaryFunction0D` > :class:`freestyle.types.UnaryFunction0DVectorViewShape` > :class:`GetOccludersF0D`
   
   .. method:: __init__()
   
      Builds a GetOccludersF0D object.
   
   .. method:: __call__(it)
   
      Returns a list of :class:`freestyle.types.ViewShape` objects occluding the
      :class:`freestyle.types.Interface0D` pointed by the Interface0DIterator.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: A list of ViewShape objects occluding the pointed
         Interface0D.
      :rtype: list of :class:`freestyle.types.ViewShape` objects



.. class:: GetOccludersF1D

   Class hierarchy: :class:`freestyle.types.UnaryFunction1D` > :class:`freestyle.types.UnaryFunction1DVectorViewShape` > :class:`GetOccludersF1D`
   
   .. method:: __init__()
   
      Builds a GetOccludersF1D object.
   
   .. method:: __call__(inter)
   
      Returns a list of occluding shapes that cover this Interface1D.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: A list of occluding shapes that cover the Interface1D.
      :rtype: list of :class:`freestyle.types.ViewShape` objects



.. class:: GetParameterF0D

   Class hierarchy: :class:`freestyle.types.UnaryFunction0D` > :class:`freestyle.types.UnaryFunction0DFloat` > :class:`GetParameterF0D`
   
   .. method:: __init__()
   
      Builds a GetParameterF0D object.
   
   .. method:: __call__(it)
   
      Returns the parameter of the :class:`freestyle.types.Interface0D`
      pointed by the Interface0DIterator in the context of its 1D element.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: The parameter of an Interface0D.
      :rtype: float



.. class:: GetProjectedXF0D

   Class hierarchy: :class:`freestyle.types.UnaryFunction0D` > :class:`freestyle.types.UnaryFunction0DDouble` > :class:`GetProjectedXF0D`
   
   .. method:: __init__()
   
      Builds a GetProjectedXF0D object.
   
   .. method:: __call__(it)
   
      Returns the X 3D projected coordinate of the :class:`freestyle.types.Interface0D`
      pointed by the Interface0DIterator.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: The X 3D projected coordinate of the pointed Interface0D.
      :rtype: float



.. class:: GetProjectedXF1D

   Class hierarchy: :class:`freestyle.types.UnaryFunction1D` > :class:`freestyle.types.UnaryFunction1DDouble` > :class:`GetProjectedXF1D`
   
   .. method:: __init__(integration_type=IntegrationType.MEAN)
   
      Builds a GetProjectedXF1D object.
   
      :arg integration_type: The integration method used to compute a single value
         from a set of values. 
      :type integration_type: :class:`freestyle.types.IntegrationType`
   
   .. method:: __call__(inter)
   
      Returns the projected X 3D coordinate of an Interface1D.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: The projected X 3D coordinate of an Interface1D.
      :rtype: float



.. class:: GetProjectedYF0D

   Class hierarchy: :class:`freestyle.types.UnaryFunction0D` > :class:`freestyle.types.UnaryFunction0DDouble` > :class:`GetProjectedYF0D`
   
   .. method:: __init__()
   
      Builds a GetProjectedYF0D object.
   
   .. method:: __call__(it)
   
      Returns the Y 3D projected coordinate of the :class:`freestyle.types.Interface0D`
      pointed by the Interface0DIterator.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: The Y 3D projected coordinate of the pointed Interface0D.
      :rtype: float



.. class:: GetProjectedYF1D

   Class hierarchy: :class:`freestyle.types.UnaryFunction1D` > :class:`freestyle.types.UnaryFunction1DDouble` > :class:`GetProjectedYF1D`
   
   .. method:: __init__(integration_type=IntegrationType.MEAN)
   
      Builds a GetProjectedYF1D object.
   
      :arg integration_type: The integration method used to compute a single value
         from a set of values. 
      :type integration_type: :class:`freestyle.types.IntegrationType`
   
   .. method:: __call__(inter)
   
      Returns the projected Y 3D coordinate of an Interface1D.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: The projected Y 3D coordinate of an Interface1D.
      :rtype: float



.. class:: GetProjectedZF0D

   Class hierarchy: :class:`freestyle.types.UnaryFunction0D` > :class:`freestyle.types.UnaryFunction0DDouble` > :class:`GetProjectedZF0D`
   
   .. method:: __init__()
   
      Builds a GetProjectedZF0D object.
   
   .. method:: __call__(it)
   
      Returns the Z 3D projected coordinate of the :class:`freestyle.types.Interface0D`
      pointed by the Interface0DIterator.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: The Z 3D projected coordinate of the pointed Interface0D.
      :rtype: float



.. class:: GetProjectedZF1D

   Class hierarchy: :class:`freestyle.types.UnaryFunction1D` > :class:`freestyle.types.UnaryFunction1DDouble` > :class:`GetProjectedZF1D`
   
   .. method:: __init__(integration_type=IntegrationType.MEAN)
   
      Builds a GetProjectedZF1D object.
   
      :arg integration_type: The integration method used to compute a single value
         from a set of values. 
      :type integration_type: :class:`freestyle.types.IntegrationType`
   
   .. method:: __call__(inter)
   
      Returns the projected Z 3D coordinate of an Interface1D.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: The projected Z 3D coordinate of an Interface1D.
      :rtype: float



.. class:: GetShapeF0D

   Class hierarchy: :class:`freestyle.types.UnaryFunction0D` > :class:`freestyle.types.UnaryFunction0DViewShape` > :class:`GetShapeF0D`
   
   .. method:: __init__()
   
      Builds a GetShapeF0D object.
   
   .. method:: __call__(it)
   
      Returns the :class:`freestyle.types.ViewShape` containing the
      Interface0D pointed by the Interface0DIterator.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: The ViewShape containing the pointed Interface0D.
      :rtype: :class:`freestyle.types.ViewShape`



.. class:: GetShapeF1D

   Class hierarchy: :class:`freestyle.types.UnaryFunction1D` > :class:`freestyle.types.UnaryFunction1DVectorViewShape` > :class:`GetShapeF1D`
   
   .. method:: __init__()
   
      Builds a GetShapeF1D object.
   
   .. method:: __call__(inter)
   
      Returns a list of shapes covered by this Interface1D.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: A list of shapes covered by the Interface1D.
      :rtype: list of :class:`freestyle.types.ViewShape` objects



.. class:: GetSteerableViewMapDensityF1D

   Class hierarchy: :class:`freestyle.types.UnaryFunction1D` > :class:`freestyle.types.UnaryFunction1DDouble` > :class:`GetSteerableViewMapDensityF1D`
   
   .. method:: __init__(level, integration_type=IntegrationType.MEAN, sampling=2.0)
   
      Builds a GetSteerableViewMapDensityF1D object.
   
      :arg level: The level of the pyramid from which the pixel must be
         read.
      :type level: int
      :arg integration_type: The integration method used to compute a single value
         from a set of values.
      :type integration_type: :class:`freestyle.types.IntegrationType`
      :arg sampling: The resolution used to sample the chain: the
         corresponding 0D function is evaluated at each sample point and
         the result is obtained by combining the resulting values into a
         single one, following the method specified by integration_type.
      :type sampling: float
   
   .. method:: __call__(inter)
   
      Returns the density of the ViewMap for a given Interface1D.  The
      density of each :class:`freestyle.types.FEdge` is evaluated in the
      proper steerable :class:`freestyle.types.ViewMap` depending on its
      orientation.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: The density of the ViewMap for a given Interface1D.
      :rtype: float



.. class:: GetViewMapGradientNormF0D

   Class hierarchy: :class:`freestyle.types.UnaryFunction0D` > :class:`freestyle.types.UnaryFunction0DFloat` > :class:`GetViewMapGradientNormF0D`
   
   .. method:: __init__(level)
   
      Builds a GetViewMapGradientNormF0D object.
   
      :arg level: The level of the pyramid from which the pixel must be
         read.
      :type level: int
   
   .. method:: __call__(it)
   
      Returns the norm of the gradient of the global viewmap density
      image.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: The norm of the gradient of the global viewmap density
         image.
      :rtype: float



.. class:: GetViewMapGradientNormF1D

   Class hierarchy: :class:`freestyle.types.UnaryFunction1D` > :class:`freestyle.types.UnaryFunction1DDouble` > :class:`GetViewMapGradientNormF1D`
   
   .. method:: __init__(level, integration_type=IntegrationType.MEAN, sampling=2.0)
   
      Builds a GetViewMapGradientNormF1D object.
   
      :arg level: The level of the pyramid from which the pixel must be
         read.
      :type level: int
      :arg integration_type: The integration method used to compute a single value
         from a set of values.
      :type integration_type: :class:`freestyle.types.IntegrationType`
      :arg sampling: The resolution used to sample the chain: the
         corresponding 0D function is evaluated at each sample point and
         the result is obtained by combining the resulting values into a
         single one, following the method specified by integration_type.
      :type sampling: float
   
   .. method:: __call__(inter)
   
      Returns the density of the ViewMap for a given Interface1D.  The
      density of each :class:`freestyle.types.FEdge` is evaluated in the
      proper steerable :class:`freestyle.types.ViewMap` depending on its
      orientation.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: The density of the ViewMap for a given Interface1D.
      :rtype: float



.. class:: GetXF0D

   Class hierarchy: :class:`freestyle.types.UnaryFunction0D` > :class:`freestyle.types.UnaryFunction0DDouble` > :class:`GetXF0D`
   
   .. method:: __init__()
   
      Builds a GetXF0D object.
   
   .. method:: __call__(it)
   
      Returns the X 3D coordinate of the :class:`freestyle.types.Interface0D` pointed by
      the Interface0DIterator.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: The X 3D coordinate of the pointed Interface0D.
      :rtype: float



.. class:: GetXF1D

   Class hierarchy: :class:`freestyle.types.UnaryFunction1D` > :class:`freestyle.types.UnaryFunction1DDouble` > :class:`GetXF1D`
   
   .. method:: __init__(integration_type=IntegrationType.MEAN)
   
      Builds a GetXF1D object.
   
      :arg integration_type: The integration method used to compute a single value
         from a set of values.
      :type integration_type: :class:`freestyle.types.IntegrationType`
   
   .. method:: __call__(inter)
   
      Returns the X 3D coordinate of an Interface1D.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: The X 3D coordinate of the Interface1D.
      :rtype: float



.. class:: GetYF0D

   Class hierarchy: :class:`freestyle.types.UnaryFunction0D` > :class:`freestyle.types.UnaryFunction0DDouble` > :class:`GetYF0D`
   
   .. method:: __init__()
   
      Builds a GetYF0D object.
   
   .. method:: __call__(it)
   
      Returns the Y 3D coordinate of the :class:`freestyle.types.Interface0D` pointed by
      the Interface0DIterator.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: The Y 3D coordinate of the pointed Interface0D.
      :rtype: float



.. class:: GetYF1D

   Class hierarchy: :class:`freestyle.types.UnaryFunction1D` > :class:`freestyle.types.UnaryFunction1DDouble` > :class:`GetYF1D`
   
   .. method:: __init__(integration_type=IntegrationType.MEAN)
   
      Builds a GetYF1D object.
   
      :arg integration_type: The integration method used to compute a single value
         from a set of values.
      :type integration_type: :class:`freestyle.types.IntegrationType`
   
   .. method:: __call__(inter)
   
      Returns the Y 3D coordinate of an Interface1D.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: The Y 3D coordinate of the Interface1D.
      :rtype: float



.. class:: GetZF0D

   Class hierarchy: :class:`freestyle.types.UnaryFunction0D` > :class:`freestyle.types.UnaryFunction0DDouble` > :class:`GetZF0D`
   
   .. method:: __init__()
   
      Builds a GetZF0D object.
   
   .. method:: __call__(it)
   
      Returns the Z 3D coordinate of the :class:`freestyle.types.Interface0D` pointed by
      the Interface0DIterator.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: The Z 3D coordinate of the pointed Interface0D.
      :rtype: float



.. class:: GetZF1D

   Class hierarchy: :class:`freestyle.types.UnaryFunction1D` > :class:`freestyle.types.UnaryFunction1DDouble` > :class:`GetZF1D`
   
   .. method:: __init__(integration_type=IntegrationType.MEAN)
   
      Builds a GetZF1D object.
   
      :arg integration_type: The integration method used to compute a single value
         from a set of values.
      :type integration_type: :class:`freestyle.types.IntegrationType`
   
   .. method:: __call__(inter)
   
      Returns the Z 3D coordinate of an Interface1D.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: The Z 3D coordinate of the Interface1D.
      :rtype: float



.. class:: IncrementChainingTimeStampF1D

   Class hierarchy: :class:`freestyle.types.UnaryFunction1D` > :class:`freestyle.types.UnaryFunction1DVoid` > :class:`IncrementChainingTimeStampF1D`
   
   .. method:: __init__()
   
      Builds an IncrementChainingTimeStampF1D object.
   
   .. method:: __call__(inter)
   
      Increments the chaining time stamp of the Interface1D.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`



.. class:: LocalAverageDepthF0D

   Class hierarchy: :class:`freestyle.types.UnaryFunction0D` > :class:`freestyle.types.UnaryFunction0DDouble` > :class:`LocalAverageDepthF0D`
   
   .. method:: __init__(mask_size=5.0)
   
      Builds a LocalAverageDepthF0D object.
   
      :arg mask_size: The size of the mask.
      :type mask_size: float
   
   .. method:: __call__(it)
   
      Returns the average depth around the
      :class:`freestyle.types.Interface0D` pointed by the
      Interface0DIterator.  The result is obtained by querying the depth
      buffer on a window around that point.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: The average depth around the pointed Interface0D.
      :rtype: float



.. class:: LocalAverageDepthF1D

   Class hierarchy: :class:`freestyle.types.UnaryFunction1D` > :class:`freestyle.types.UnaryFunction1DDouble` > :class:`LocalAverageDepthF1D`
   
   .. method:: __init__(sigma, integration_type=IntegrationType.MEAN)
   
      Builds a LocalAverageDepthF1D object.
   
      :arg sigma: The sigma used in DensityF0D and determining the window
         size used in each density query.
      :type sigma: float
      :arg integration_type: The integration method used to compute a single value
         from a set of values.
      :type integration_type: :class:`freestyle.types.IntegrationType`
   
   .. method:: __call__(inter)
   
      Returns the average depth evaluated for an Interface1D.  The average
      depth is evaluated for a set of points along the Interface1D (using
      the :class:`freestyle.functions.LocalAverageDepthF0D` functor) with a
      user-defined sampling and then integrated into a single value using a
      user-defined integration method.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: The average depth evaluated for the Interface1D.
      :rtype: float



.. class:: MaterialF0D

   Class hierarchy: :class:`freestyle.types.UnaryFunction0D` > :class:`freestyle.types.UnaryFunction0DMaterial` > :class:`MaterialF0D`
   
   .. method:: __init__()
   
      Builds a MaterialF0D object.
   
   .. method:: __call__(it)
   
      Returns the material of the object evaluated at the
      :class:`freestyle.types.Interface0D` pointed by the
      Interface0DIterator.  This evaluation can be ambiguous (in the case of
      a :class:`freestyle.types.TVertex` for example.  This functor tries to
      remove this ambiguity using the context offered by the 1D element to
      which the Interface0DIterator belongs to and by arbitrary choosing the
      material of the face that lies on its left when following the 1D
      element if there are two different materials on each side of the
      point.  However, there still can be problematic cases, and the user
      willing to deal with this cases in a specific way should implement its
      own getMaterial functor.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: The material of the object evaluated at the pointed
         Interface0D.
      :rtype: :class:`freestyle.types.Material`



.. class:: Normal2DF0D

   Class hierarchy: :class:`freestyle.types.UnaryFunction0D` > :class:`freestyle.types.UnaryFunction0DVec2f` > :class:`Normal2DF0D`
   
   .. method:: __init__()
   
      Builds a Normal2DF0D object.
   
   .. method:: __call__(it)
   
      Returns a two-dimensional vector giving the normalized 2D normal to
      the 1D element to which the :class:`freestyle.types.Interface0D`
      pointed by the Interface0DIterator belongs.  The normal is evaluated
      at the pointed Interface0D.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: The 2D normal of the 1D element evaluated at the pointed
         Interface0D.
      :rtype: :class:`mathutils.Vector`



.. class:: Normal2DF1D

   Class hierarchy: :class:`freestyle.types.UnaryFunction1D` > :class:`freestyle.types.UnaryFunction1DVec2f` > :class:`Normal2DF1D`
   
   .. method:: __init__(integration_type=IntegrationType.MEAN)
   
      Builds a Normal2DF1D object.
   
      :arg integration_type: The integration method used to compute a single value
         from a set of values.
      :type integration_type: :class:`freestyle.types.IntegrationType`
   
   .. method:: __call__(inter)
   
      Returns the 2D normal for the Interface1D.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: The 2D normal for the Interface1D.
      :rtype: :class:`mathutils.Vector`



.. class:: Orientation2DF1D

   Class hierarchy: :class:`freestyle.types.UnaryFunction1D` > :class:`freestyle.types.UnaryFunction1DVec2f` > :class:`Orientation2DF1D`
   
   .. method:: __init__(integration_type=IntegrationType.MEAN)
   
      Builds an Orientation2DF1D object.
   
      :arg integration_type: The integration method used to compute a single value
         from a set of values.
      :type integration_type: :class:`freestyle.types.IntegrationType`
   
   .. method:: __call__(inter)
   
      Returns the 2D orientation of the Interface1D.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: The 2D orientation of the Interface1D.
      :rtype: :class:`mathutils.Vector`



.. class:: Orientation3DF1D

   Class hierarchy: :class:`freestyle.types.UnaryFunction1D` > :class:`freestyle.types.UnaryFunction1DVec3f` > :class:`Orientation3DF1D`
   
   .. method:: __init__(integration_type=IntegrationType.MEAN)
   
      Builds an Orientation3DF1D object.
   
      :arg integration_type: The integration method used to compute a single value
         from a set of values.
      :type integration_type: :class:`freestyle.types.IntegrationType`
   
   .. method:: __call__(inter)
   
      Returns the 3D orientation of the Interface1D.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: The 3D orientation of the Interface1D.
      :rtype: :class:`mathutils.Vector`



.. class:: QuantitativeInvisibilityF0D

   Class hierarchy: :class:`freestyle.types.UnaryFunction0D` > :class:`freestyle.types.UnaryFunction0DUnsigned` > :class:`QuantitativeInvisibilityF0D`
   
   .. method:: __init__()
   
      Builds a QuantitativeInvisibilityF0D object.
   
   .. method:: __call__(it)
   
      Returns the quantitative invisibility of the
      :class:`freestyle.types.Interface0D` pointed by the
      Interface0DIterator.  This evaluation can be ambiguous (in the case of
      a :class:`freestyle.types.TVertex` for example).  This functor tries
      to remove this ambiguity using the context offered by the 1D element
      to which the Interface0D belongs to.  However, there still can be
      problematic cases, and the user willing to deal with this cases in a
      specific way should implement its own getQIF0D functor.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: The quantitative invisibility of the pointed Interface0D.
      :rtype: int



.. class:: QuantitativeInvisibilityF1D

   Class hierarchy: :class:`freestyle.types.UnaryFunction1D` > :class:`freestyle.types.UnaryFunction1DUnsigned` > :class:`QuantitativeInvisibilityF1D`
   
   .. method:: __init__(integration_type=IntegrationType.MEAN)
   
      Builds a QuantitativeInvisibilityF1D object.
   
      :arg integration_type: The integration method used to compute a single value
         from a set of values.
      :type integration_type: :class:`freestyle.types.IntegrationType`
   
   .. method:: __call__(inter)
   
      Returns the Quantitative Invisibility of an Interface1D element. If
      the Interface1D is a :class:`freestyle.types.ViewEdge`, then there is
      no ambiguity concerning the result.  But, if the Interface1D results
      of a chaining (chain, stroke), then it might be made of several 1D
      elements of different Quantitative Invisibilities.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: The Quantitative Invisibility of the Interface1D.
      :rtype: int



.. class:: ReadCompleteViewMapPixelF0D

   Class hierarchy: :class:`freestyle.types.UnaryFunction0D` > :class:`freestyle.types.UnaryFunction0DFloat` > :class:`ReadCompleteViewMapPixelF0D`
   
   .. method:: __init__(level)
   
      Builds a ReadCompleteViewMapPixelF0D object.
   
      :arg level: The level of the pyramid from which the pixel must be
         read.
      :type level: int
   
   .. method:: __call__(it)
   
      Reads a pixel in one of the level of the complete viewmap.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: A pixel in one of the level of the complete viewmap.
      :rtype: float



.. class:: ReadMapPixelF0D

   Class hierarchy: :class:`freestyle.types.UnaryFunction0D` > :class:`freestyle.types.UnaryFunction0DFloat` > :class:`ReadMapPixelF0D`
   
   .. method:: __init__(map_name, level)
   
      Builds a ReadMapPixelF0D object.
   
      :arg map_name: The name of the map to be read.
      :type map_name: str
      :arg level: The level of the pyramid from which the pixel must be
         read.
      :type level: int
   
   .. method:: __call__(it)
   
      Reads a pixel in a map.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: A pixel in a map.
      :rtype: float



.. class:: ReadSteerableViewMapPixelF0D

   Class hierarchy: :class:`freestyle.types.UnaryFunction0D` > :class:`freestyle.types.UnaryFunction0DFloat` > :class:`ReadSteerableViewMapPixelF0D`
   
   .. method:: __init__(orientation, level)
   
      Builds a ReadSteerableViewMapPixelF0D object.
   
      :arg orientation: The integer belonging to [0, 4] indicating the
         orientation (E, NE, N, NW) we are interested in.
      :type orientation: int
      :arg level: The level of the pyramid from which the pixel must be
         read.
      :type level: int
   
   .. method:: __call__(it)
   
      Reads a pixel in one of the level of one of the steerable viewmaps.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: A pixel in one of the level of one of the steerable viewmaps.
      :rtype: float



.. class:: ShapeIdF0D

   Class hierarchy: :class:`freestyle.types.UnaryFunction0D` > :class:`freestyle.types.UnaryFunction0DId` > :class:`ShapeIdF0D`
   
   .. method:: __init__()
   
      Builds a ShapeIdF0D object.
   
   .. method:: __call__(it)
   
      Returns the :class:`freestyle.types.Id` of the Shape the
      :class:`freestyle.types.Interface0D` pointed by the
      Interface0DIterator belongs to. This evaluation can be ambiguous (in
      the case of a :class:`freestyle.types.TVertex` for example).  This
      functor tries to remove this ambiguity using the context offered by
      the 1D element to which the Interface0DIterator belongs to. However,
      there still can be problematic cases, and the user willing to deal
      with this cases in a specific way should implement its own
      getShapeIdF0D functor.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: The Id of the Shape the pointed Interface0D belongs to.
      :rtype: :class:`freestyle.types.Id`



.. class:: TimeStampF1D

   Class hierarchy: :class:`freestyle.types.UnaryFunction1D` > :class:`freestyle.types.UnaryFunction1DVoid` > :class:`TimeStampF1D`
   
   .. method:: __init__()
   
      Builds a TimeStampF1D object.
   
   .. method:: __call__(inter)
   
      Returns the time stamp of the Interface1D.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`



.. class:: VertexOrientation2DF0D

   Class hierarchy: :class:`freestyle.types.UnaryFunction0D` > :class:`freestyle.types.UnaryFunction0DVec2f` > :class:`VertexOrientation2DF0D`
   
   .. method:: __init__()
   
      Builds a VertexOrientation2DF0D object.
   
   .. method:: __call__(it)
   
      Returns a two-dimensional vector giving the 2D oriented tangent to the
      1D element to which the :class:`freestyle.types.Interface0D` pointed
      by the Interface0DIterator belongs.  The 2D oriented tangent is
      evaluated at the pointed Interface0D.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: The 2D oriented tangent to the 1D element evaluated at the
         pointed Interface0D.
      :rtype: :class:`mathutils.Vector`



.. class:: VertexOrientation3DF0D

   Class hierarchy: :class:`freestyle.types.UnaryFunction0D` > :class:`freestyle.types.UnaryFunction0DVec3f` > :class:`VertexOrientation3DF0D`
   
   .. method:: __init__()
   
      Builds a VertexOrientation3DF0D object.
   
   .. method:: __call__(it)
   
      Returns a three-dimensional vector giving the 3D oriented tangent to
      the 1D element to which the :class:`freestyle.types.Interface0D`
      pointed by the Interface0DIterator belongs.  The 3D oriented tangent
      is evaluated at the pointed Interface0D.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: The 3D oriented tangent to the 1D element evaluated at the
         pointed Interface0D.
      :rtype: :class:`mathutils.Vector`



.. class:: ZDiscontinuityF0D

   Class hierarchy: :class:`freestyle.types.UnaryFunction0D` > :class:`freestyle.types.UnaryFunction0DDouble` > :class:`ZDiscontinuityF0D`
   
   .. method:: __init__()
   
      Builds a ZDiscontinuityF0D object.
   
   .. method:: __call__(it)
   
      Returns a real value giving the distance between the
      :class:`freestyle.types.Interface0D` pointed by the
      Interface0DIterator and the shape that lies behind (occludee).  This
      distance is evaluated in the camera space and normalized between 0 and
      1.  Therefore, if no object is occluded by the shape to which the
      Interface0D belongs to, 1 is returned.
   
      :arg it: An Interface0DIterator object.
      :type it: :class:`freestyle.types.Interface0DIterator`
      :return: The normalized distance between the pointed Interface0D
         and the occludee.
      :rtype: float



.. class:: ZDiscontinuityF1D

   Class hierarchy: :class:`freestyle.types.UnaryFunction1D` > :class:`freestyle.types.UnaryFunction1DDouble` > :class:`ZDiscontinuityF1D`
   
   .. method:: __init__(integration_type=IntegrationType.MEAN)
   
      Builds a ZDiscontinuityF1D object.
   
      :arg integration_type: The integration method used to compute a single value
         from a set of values.
      :type integration_type: :class:`freestyle.types.IntegrationType`
   
   .. method:: __call__(inter)
   
      Returns a real value giving the distance between an Interface1D
      and the shape that lies behind (occludee).  This distance is
      evaluated in the camera space and normalized between 0 and 1.
      Therefore, if no object is occluded by the shape to which the
      Interface1D belongs to, 1 is returned.
   
      :arg inter: An Interface1D object.
      :type inter: :class:`freestyle.types.Interface1D`
      :return: The normalized distance between the Interface1D and the occludee.
      :rtype: float



.. class:: pyCurvilinearLengthF0D




.. class:: pyDensityAnisotropyF0D

   Estimates the anisotropy of density.



.. class:: pyDensityAnisotropyF1D




.. class:: pyGetInverseProjectedZF1D




.. class:: pyGetSquareInverseProjectedZF1D




.. class:: pyInverseCurvature2DAngleF0D




.. class:: pyViewMapGradientNormF0D




.. class:: pyViewMapGradientNormF1D




.. class:: pyViewMapGradientVectorF0D

   Returns the gradient vector for a pixel.
   
   .. method:: __init__(self, level)
   
      Builds a pyViewMapGradientVectorF0D object.
   
      :arg level: the level at which to compute the gradient
      :type level: int



