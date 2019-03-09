Freestyle Types (freestyle.types)
=================================

.. module:: freestyle.types

This module contains core classes of the Freestyle Python API,
including data types of view map components (0D and 1D elements), base
classes for user-defined line stylization rules (predicates,
functions, chaining iterators, and stroke shaders), and operators.

Class hierarchy:

- :class:`BBox`
- :class:`BinaryPredicate0D`
- :class:`BinaryPredicate1D`
- :class:`Id`
- :class:`Interface0D`

  - :class:`CurvePoint`

    - :class:`StrokeVertex`

  - :class:`SVertex`
  - :class:`ViewVertex`

    - :class:`NonTVertex`
    - :class:`TVertex`

- :class:`Interface1D`

  - :class:`Curve`

    - :class:`Chain`

  - :class:`FEdge`

    - :class:`FEdgeSharp`
    - :class:`FEdgeSmooth`

  - :class:`Stroke`
  - :class:`ViewEdge`

- :class:`Iterator`

  - :class:`AdjacencyIterator`
  - :class:`CurvePointIterator`
  - :class:`Interface0DIterator`
  - :class:`SVertexIterator`
  - :class:`StrokeVertexIterator`
  - :class:`ViewEdgeIterator`

    - :class:`ChainingIterator`

  - :class:`orientedViewEdgeIterator`

- :class:`Material`
- :class:`Noise`
- :class:`Operators`
- :class:`SShape`
- :class:`StrokeAttribute`
- :class:`StrokeShader`
- :class:`UnaryFunction0D`

  - :class:`UnaryFunction0DDouble`
  - :class:`UnaryFunction0DEdgeNature`
  - :class:`UnaryFunction0DFloat`
  - :class:`UnaryFunction0DId`
  - :class:`UnaryFunction0DMaterial`
  - :class:`UnaryFunction0DUnsigned`
  - :class:`UnaryFunction0DVec2f`
  - :class:`UnaryFunction0DVec3f`
  - :class:`UnaryFunction0DVectorViewShape`
  - :class:`UnaryFunction0DViewShape`

- :class:`UnaryFunction1D`

  - :class:`UnaryFunction1DDouble`
  - :class:`UnaryFunction1DEdgeNature`
  - :class:`UnaryFunction1DFloat`
  - :class:`UnaryFunction1DUnsigned`
  - :class:`UnaryFunction1DVec2f`
  - :class:`UnaryFunction1DVec3f`
  - :class:`UnaryFunction1DVectorViewShape`
  - :class:`UnaryFunction1DVoid`

- :class:`UnaryPredicate0D`
- :class:`UnaryPredicate1D`
- :class:`ViewMap`
- :class:`ViewShape`
- :class:`IntegrationType`
- :class:`MediumType`
- :class:`Nature`

.. class:: AdjacencyIterator

   Class hierarchy: :class:`Iterator` > :class:`AdjacencyIterator`
   
   Class for representing adjacency iterators used in the chaining
   process.  An AdjacencyIterator is created in the increment() and
   decrement() methods of a :class:`ChainingIterator` and passed to the
   traverse() method of the ChainingIterator.
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __init__(brother)
   
      Copy constructor.
   
      :arg brother: An AdjacencyIterator object.
      :type brother: :class:`AdjacencyIterator`
   
   .. method:: __init__(vertex, restrict_to_selection=True, restrict_to_unvisited=True)
   
      Builds a AdjacencyIterator object.
   
      :arg vertex: The vertex which is the next crossing.
      :type vertex: :class:`ViewVertex`
      :arg restrict_to_selection: Indicates whether to force the chaining
         to stay within the set of selected ViewEdges or not.
      :type restrict_to_selection: bool
      :arg restrict_to_unvisited: Indicates whether a ViewEdge that has
         already been chained must be ignored ot not.
      :type restrict_to_unvisited: bool

   .. attribute:: is_incoming

      True if the current ViewEdge is coming towards the iteration vertex, and
      False otherwise.
      
      :type: bool


   .. attribute:: object

      The ViewEdge object currently pointed to by this iterator.
      
      :type: :class:`ViewEdge`




.. class:: BBox

   Class for representing a bounding box.
   
   .. method:: __init__()
   
      Default constructor.



.. class:: BinaryPredicate0D

   Base class for binary predicates working on :class:`Interface0D`
   objects.  A BinaryPredicate0D is typically an ordering relation
   between two Interface0D objects.  The predicate evaluates a relation
   between the two Interface0D instances and returns a boolean value (true
   or false).  It is used by invoking the __call__() method.
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __call__(inter1, inter2)
   
      Must be overload by inherited classes.  It evaluates a relation
      between two Interface0D objects.
   
      :arg inter1: The first Interface0D object.
      :type inter1: :class:`Interface0D`
      :arg inter2: The second Interface0D object.
      :type inter2: :class:`Interface0D`
      :return: True or false.
      :rtype: bool

   .. attribute:: name

      The name of the binary 0D predicate.
      
      :type: str




.. class:: BinaryPredicate1D

   Base class for binary predicates working on :class:`Interface1D`
   objects.  A BinaryPredicate1D is typically an ordering relation
   between two Interface1D objects.  The predicate evaluates a relation
   between the two Interface1D instances and returns a boolean value (true
   or false).  It is used by invoking the __call__() method.
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __call__(inter1, inter2)
   
      Must be overload by inherited classes. It evaluates a relation
      between two Interface1D objects.
   
      :arg inter1: The first Interface1D object.
      :type inter1: :class:`Interface1D`
      :arg inter2: The second Interface1D object.
      :type inter2: :class:`Interface1D`
      :return: True or false.
      :rtype: bool

   .. attribute:: name

      The name of the binary 1D predicate.
      
      :type: str




.. class:: Chain

   Class hierarchy: :class:`Interface1D` > :class:`Curve` > :class:`Chain`
   
   Class to represent a 1D elements issued from the chaining process.  A
   Chain is the last step before the :class:`Stroke` and is used in the
   Splitting and Creation processes.
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __init__(brother)
   
      Copy constructor.
   
      :arg brother: A Chain object.
      :type brother: :class:`Chain`
   
   .. method:: __init__(id)
   
      Builds a chain from its Id.
   
      :arg id: An Id object.
      :type id: :class:`Id`

   .. method:: push_viewedge_back(viewedge, orientation)
   
      Adds a ViewEdge at the end of the Chain.
   
      :arg viewedge: The ViewEdge that must be added.
      :type viewedge: :class:`ViewEdge`
      :arg orientation: The orientation with which the ViewEdge must be
         processed.
      :type orientation: bool


   .. method:: push_viewedge_front(viewedge, orientation)
   
      Adds a ViewEdge at the beginning of the Chain.
   
      :arg viewedge: The ViewEdge that must be added.
      :type viewedge: :class:`ViewEdge`
      :arg orientation: The orientation with which the ViewEdge must be
         processed.
      :type orientation: bool




.. class:: ChainingIterator

   Class hierarchy: :class:`Iterator` > :class:`ViewEdgeIterator` > :class:`ChainingIterator`
   
   Base class for chaining iterators.  This class is designed to be
   overloaded in order to describe chaining rules.  It makes the
   description of chaining rules easier.  The two main methods that need
   to overloaded are traverse() and init().  traverse() tells which
   :class:`ViewEdge` to follow, among the adjacent ones.  If you specify
   restriction rules (such as "Chain only ViewEdges of the selection"),
   they will be included in the adjacency iterator (i.e, the adjacent
   iterator will only stop on "valid" edges).
   
   .. method:: __init__(restrict_to_selection=True, restrict_to_unvisited=True, begin=None, orientation=True)
   
      Builds a Chaining Iterator from the first ViewEdge used for
      iteration and its orientation.
   
      :arg restrict_to_selection: Indicates whether to force the chaining
         to stay within the set of selected ViewEdges or not.
      :type restrict_to_selection: bool
      :arg restrict_to_unvisited: Indicates whether a ViewEdge that has
         already been chained must be ignored ot not.
      :type restrict_to_unvisited: bool
      :arg begin: The ViewEdge from which to start the chain.
      :type begin: :class:`ViewEdge` or None
      :arg orientation: The direction to follow to explore the graph.  If
         true, the direction indicated by the first ViewEdge is used.
      :type orientation: bool
   
   .. method:: __init__(brother)
   
      Copy constructor.
   
      :arg brother: 
      :type brother: ChainingIterator

   .. method:: init()
   
      Initializes the iterator context.  This method is called each
      time a new chain is started.  It can be used to reset some
      history information that you might want to keep.


   .. method:: traverse(it)
   
      This method iterates over the potential next ViewEdges and returns
      the one that will be followed next.  Returns the next ViewEdge to
      follow or None when the end of the chain is reached.
   
      :arg it: The iterator over the ViewEdges adjacent to the end vertex
         of the current ViewEdge.  The adjacency iterator reflects the
         restriction rules by only iterating over the valid ViewEdges.
      :type it: :class:`AdjacencyIterator`
      :return: Returns the next ViewEdge to follow, or None if chaining ends.
      :rtype: :class:`ViewEdge` or None


   .. attribute:: is_incrementing

      True if the current iteration is an incrementation.
      
      :type: bool


   .. attribute:: next_vertex

      The ViewVertex that is the next crossing.
      
      :type: :class:`ViewVertex`


   .. attribute:: object

      The ViewEdge object currently pointed by this iterator.
      
      :type: :class:`ViewEdge`




.. class:: Curve

   Class hierarchy: :class:`Interface1D` > :class:`Curve`
   
   Base class for curves made of CurvePoints.  :class:`SVertex` is the
   type of the initial curve vertices.  A :class:`Chain` is a
   specialization of a Curve.
   
   .. method:: __init__()
   
      Default Constructor.
   
   .. method:: __init__(brother)
   
      Copy Constructor.
   
      :arg brother: A Curve object.
      :type brother: :class:`Curve`
   
   .. method:: __init__(id)
   
      Builds a Curve from its Id.
   
      :arg id: An Id object.
      :type id: :class:`Id`

   .. method:: push_vertex_back(vertex)
   
      Adds a single vertex at the end of the Curve.
   
      :arg vertex: A vertex object.
      :type vertex: :class:`SVertex` or :class:`CurvePoint`


   .. method:: push_vertex_front(vertex)
   
      Adds a single vertex at the front of the Curve.
   
      :arg vertex: A vertex object.
      :type vertex: :class:`SVertex` or :class:`CurvePoint`


   .. attribute:: is_empty

      True if the Curve doesn't have any Vertex yet.
      
      :type: bool


   .. attribute:: segments_size

      The number of segments in the polyline constituting the Curve.
      
      :type: int




.. class:: CurvePoint

   Class hierarchy: :class:`Interface0D` > :class:`CurvePoint`
   
   Class to represent a point of a curve.  A CurvePoint can be any point
   of a 1D curve (it doesn't have to be a vertex of the curve).  Any
   :class:`Interface1D` is built upon ViewEdges, themselves built upon
   FEdges.  Therefore, a curve is basically a polyline made of a list of
   :class:`SVertex` objects.  Thus, a CurvePoint is built by linearly
   interpolating two :class:`SVertex` instances.  CurvePoint can be used
   as virtual points while querying 0D information along a curve at a
   given resolution.
   
   .. method:: __init__()
   
      Defult constructor.
   
   .. method:: __init__(brother)
   
      Copy constructor.
   
      :arg brother: A CurvePoint object.
      :type brother: :class:`CurvePoint`
   
   .. method:: __init__(first_vertex, second_vertex, t2d)
   
      Builds a CurvePoint from two SVertex objects and an interpolation parameter.
   
      :arg first_vertex: The first SVertex.
      :type first_vertex: :class:`SVertex`
      :arg second_vertex: The second SVertex.
      :type second_vertex: :class:`SVertex`
      :arg t2d: A 2D interpolation parameter used to linearly interpolate
                first_vertex and second_vertex.
      :type t2d: float
   
   .. method:: __init__(first_point, second_point, t2d)
   
      Builds a CurvePoint from two CurvePoint objects and an interpolation
      parameter.
   
      :arg first_point: The first CurvePoint.
      :type first_point: :class:`CurvePoint`
      :arg second_point: The second CurvePoint.
      :type second_point: :class:`CurvePoint`
      :arg t2d: The 2D interpolation parameter used to linearly interpolate
                first_point and second_point.
      :type t2d: float

   .. attribute:: fedge

      Gets the FEdge for the two SVertices that given CurvePoints consists out of.
      A shortcut for CurvePoint.first_svertex.get_fedge(CurvePoint.second_svertex).
      
      :type: :class:`FEdge`


   .. attribute:: first_svertex

      The first SVertex upon which the CurvePoint is built.
      
      :type: :class:`SVertex`


   .. attribute:: second_svertex

      The second SVertex upon which the CurvePoint is built.
      
      :type: :class:`SVertex`


   .. attribute:: t2d

      The 2D interpolation parameter.
      
      :type: float




.. class:: CurvePointIterator

   Class hierarchy: :class:`Iterator` > :class:`CurvePointIterator`
   
   Class representing an iterator on a curve.  Allows an iterating
   outside initial vertices.  A CurvePoint is instanciated and returned
   through the .object attribute.
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __init__(brother)
   
      Copy constructor.
   
      :arg brother: A CurvePointIterator object.
      :type brother: :class:`CurvePointIterator`
   
   .. method:: __init__(step=0.0)
   
      Builds a CurvePointIterator object.
   
      :arg step: A resampling resolution with which the curve is resampled.
         If zero, no resampling is done (i.e., the iterator iterates over
         initial vertices).
      :type step: float

   .. attribute:: object

      The CurvePoint object currently pointed by this iterator.
      
      :type: :class:`CurvePoint`


   .. attribute:: t

      The curvilinear abscissa of the current point.
      
      :type: float


   .. attribute:: u

      The point parameter at the current point in the stroke (0 <= u <= 1).
      
      :type: float




.. class:: FEdge

   Class hierarchy: :class:`Interface1D` > :class:`FEdge`
   
   Base Class for feature edges.  This FEdge can represent a silhouette,
   a crease, a ridge/valley, a border or a suggestive contour.  For
   silhouettes, the FEdge is oriented so that the visible face lies on
   the left of the edge.  For borders, the FEdge is oriented so that the
   face lies on the left of the edge.  An FEdge can represent an initial
   edge of the mesh or runs across a face of the initial mesh depending
   on the smoothness or sharpness of the mesh.  This class is specialized
   into a smooth and a sharp version since their properties slightly vary
   from one to the other.
   
   .. method:: FEdge()
   
      Default constructor.
   
   .. method:: FEdge(brother)
   
      Copy constructor.
   
      :arg brother: An FEdge object.
      :type brother: :class:`FEdge`
   
   .. method:: FEdge(first_vertex, second_vertex)
   
      Builds an FEdge going from the first vertex to the second.
   
      :arg first_vertex: The first SVertex.
      :type first_vertex: :class:`SVertex`
      :arg second_vertex: The second SVertex.
      :type second_vertex: :class:`SVertex`

   .. attribute:: first_svertex

      The first SVertex constituting this FEdge.
      
      :type: :class:`SVertex`


   .. attribute:: id

      The Id of this FEdge.
      
      :type: :class:`Id`


   .. attribute:: is_smooth

      True if this FEdge is a smooth FEdge.
      
      :type: bool


   .. attribute:: nature

      The nature of this FEdge.
      
      :type: :class:`Nature`


   .. attribute:: next_fedge

      The FEdge following this one in the ViewEdge.  The value is None if
      this FEdge is the last of the ViewEdge.
      
      :type: :class:`FEdge`


   .. attribute:: previous_fedge

      The FEdge preceding this one in the ViewEdge.  The value is None if
      this FEdge is the first one of the ViewEdge.
      
      :type: :class:`FEdge`


   .. attribute:: second_svertex

      The second SVertex constituting this FEdge.
      
      :type: :class:`SVertex`


   .. attribute:: viewedge

      The ViewEdge to which this FEdge belongs to.
      
      :type: :class:`ViewEdge`




.. class:: FEdgeSharp

   Class hierarchy: :class:`Interface1D` > :class:`FEdge` > :class:`FEdgeSharp`
   
   Class defining a sharp FEdge.  A Sharp FEdge corresponds to an initial
   edge of the input mesh.  It can be a silhouette, a crease or a border.
   If it is a crease edge, then it is borded by two faces of the mesh.
   Face a lies on its right whereas Face b lies on its left.  If it is a
   border edge, then it doesn't have any face on its right, and thus Face
   a is None.
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __init__(brother)
   
      Copy constructor.
   
      :arg brother: An FEdgeSharp object.
      :type brother: :class:`FEdgeSharp`
   
   .. method:: __init__(first_vertex, second_vertex)
   
      Builds an FEdgeSharp going from the first vertex to the second.
   
      :arg first_vertex: The first SVertex object.
      :type first_vertex: :class:`SVertex`
      :arg second_vertex: The second SVertex object.
      :type second_vertex: :class:`SVertex`

   .. attribute:: face_mark_left

      The face mark of the face lying on the left of the FEdge.
      
      :type: bool


   .. attribute:: face_mark_right

      The face mark of the face lying on the right of the FEdge.  If this FEdge
      is a border, it has no face on the right and thus this property is set to
      false.
      
      :type: bool


   .. attribute:: material_index_left

      The index of the material of the face lying on the left of the FEdge.
      
      :type: int


   .. attribute:: material_index_right

      The index of the material of the face lying on the right of the FEdge.
      If this FEdge is a border, it has no Face on its right and therefore
      no material.
      
      :type: int


   .. attribute:: material_left

      The material of the face lying on the left of the FEdge.
      
      :type: :class:`Material`


   .. attribute:: material_right

      The material of the face lying on the right of the FEdge.  If this FEdge
      is a border, it has no Face on its right and therefore no material.
      
      :type: :class:`Material`


   .. attribute:: normal_left

      The normal to the face lying on the left of the FEdge.
      
      :type: :class:`mathutils.Vector`


   .. attribute:: normal_right

      The normal to the face lying on the right of the FEdge.  If this FEdge
      is a border, it has no Face on its right and therefore no normal.
      
      :type: :class:`mathutils.Vector`




.. class:: FEdgeSmooth

   Class hierarchy: :class:`Interface1D` > :class:`FEdge` > :class:`FEdgeSmooth`
   
   Class defining a smooth edge.  This kind of edge typically runs across
   a face of the input mesh.  It can be a silhouette, a ridge or valley,
   a suggestive contour.
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __init__(brother)
   
      Copy constructor.
   
      :arg brother: An FEdgeSmooth object.
      :type brother: :class:`FEdgeSmooth`
   
   .. method:: __init__(first_vertex, second_vertex)
   
      Builds an FEdgeSmooth going from the first to the second.
   
      :arg first_vertex: The first SVertex object.
      :type first_vertex: :class:`SVertex`
      :arg second_vertex: The second SVertex object.
      :type second_vertex: :class:`SVertex`

   .. attribute:: face_mark

      The face mark of the face that this FEdge is running across.
      
      :type: bool


   .. attribute:: material

      The material of the face that this FEdge is running across.
      
      :type: :class:`Material`


   .. attribute:: material_index

      The index of the material of the face that this FEdge is running across.
      
      :type: int


   .. attribute:: normal

      The normal of the face that this FEdge is running across.
      
      :type: :class:`mathutils.Vector`




.. class:: Id

   Class for representing an object Id.
   
   .. method:: __init__(first=0, second=0)
   
      Build the Id from two numbers.
   
      :arg first: The first number.
      :type first: int
      :arg second: The second number.
      :type second: int
   
   .. method:: __init__(brother)
   
      Copy constructor.
   
      :arg brother: An Id object.
      :type brother: :class:`Id`

   .. attribute:: first

      The first number constituting the Id.
      
      :type: int


   .. attribute:: second

      The second number constituting the Id.
      
      :type: int




.. class:: IntegrationType

   Class hierarchy: int > :class:`IntegrationType`
   
   Different integration methods that can be invoked to integrate into a
   single value the set of values obtained from each 0D element of an 1D
   element:
   
   * IntegrationType.MEAN: The value computed for the 1D element is the
     mean of the values obtained for the 0D elements.
   * IntegrationType.MIN: The value computed for the 1D element is the
     minimum of the values obtained for the 0D elements.
   * IntegrationType.MAX: The value computed for the 1D element is the
     maximum of the values obtained for the 0D elements.
   * IntegrationType.FIRST: The value computed for the 1D element is the
     first of the values obtained for the 0D elements.
   * IntegrationType.LAST: The value computed for the 1D element is the
     last of the values obtained for the 0D elements.



.. class:: Interface0D

   Base class for any 0D element.
   
   .. method:: __init__()
   
      Default constructor.

   .. method:: get_fedge(inter)
   
      Returns the FEdge that lies between this 0D element and the 0D
      element given as the argument.
   
      :arg inter: A 0D element.
      :type inter: :class:`Interface0D`
      :return: The FEdge lying between the two 0D elements.
      :rtype: :class:`FEdge`


   .. attribute:: id

      The Id of this 0D element.
      
      :type: :class:`Id`


   .. attribute:: name

      The string of the name of this 0D element.
      
      :type: str


   .. attribute:: nature

      The nature of this 0D element.
      
      :type: :class:`Nature`


   .. attribute:: point_2d

      The 2D point of this 0D element.
      
      :type: :class:`mathutils.Vector`


   .. attribute:: point_3d

      The 3D point of this 0D element.
      
      :type: :class:`mathutils.Vector`


   .. attribute:: projected_x

      The X coordinate of the projected 3D point of this 0D element.
      
      :type: float


   .. attribute:: projected_y

      The Y coordinate of the projected 3D point of this 0D element.
      
      :type: float


   .. attribute:: projected_z

      The Z coordinate of the projected 3D point of this 0D element.
      
      :type: float




.. class:: Interface0DIterator

   Class hierarchy: :class:`Iterator` > :class:`Interface0DIterator`
   
   Class defining an iterator over Interface0D elements.  An instance of
   this iterator is always obtained from a 1D element.
   
   .. method:: __init__(brother)
   
      Copy constructor.
   
      :arg brother: An Interface0DIterator object.
      :type brother: :class:`Interface0DIterator`
   
   .. method:: __init__(it)
   
      Construct a nested Interface0DIterator that can be the argument of
      a Function0D.
   
      :arg it: An iterator object to be nested.
      :type it: :class:`SVertexIterator`, :class:`CurvePointIterator`, or
         :class:`StrokeVertexIterator`

   .. attribute:: at_last

      True if the interator points to the last valid element.
      For its counterpart (pointing to the first valid element), use it.is_begin.
      
      :type: bool


   .. attribute:: object

      The 0D object currently pointed to by this iterator.  Note that the object
      may be an instance of an Interface0D subclass. For example if the iterator
      has been created from the `vertices_begin()` method of the :class:`Stroke`
      class, the .object property refers to a :class:`StrokeVertex` object.
      
      :type: :class:`Interface0D` or one of its subclasses.


   .. attribute:: t

      The curvilinear abscissa of the current point.
      
      :type: float


   .. attribute:: u

      The point parameter at the current point in the 1D element (0 <= u <= 1).
      
      :type: float




.. class:: Interface1D

   Base class for any 1D element.
   
   .. method:: __init__()
   
      Default constructor.

   .. method:: points_begin(t=0.0)
   
      Returns an iterator over the Interface1D points, pointing to the
      first point. The difference with vertices_begin() is that here we can
      iterate over points of the 1D element at a any given sampling.
      Indeed, for each iteration, a virtual point is created.
   
      :arg t: A sampling with which we want to iterate over points of
         this 1D element.
      :type t: float
      :return: An Interface0DIterator pointing to the first point.
      :rtype: :class:`Interface0DIterator`


   .. method:: points_end(t=0.0)
   
      Returns an iterator over the Interface1D points, pointing after the
      last point. The difference with vertices_end() is that here we can
      iterate over points of the 1D element at a given sampling.  Indeed,
      for each iteration, a virtual point is created.
   
      :arg t: A sampling with which we want to iterate over points of
         this 1D element.
      :type t: float
      :return: An Interface0DIterator pointing after the last point.
      :rtype: :class:`Interface0DIterator`


   .. method:: vertices_begin()
   
      Returns an iterator over the Interface1D vertices, pointing to the
      first vertex.
   
      :return: An Interface0DIterator pointing to the first vertex.
      :rtype: :class:`Interface0DIterator`


   .. method:: vertices_end()
   
      Returns an iterator over the Interface1D vertices, pointing after
      the last vertex.
   
      :return: An Interface0DIterator pointing after the last vertex.
      :rtype: :class:`Interface0DIterator`


   .. attribute:: id

      The Id of this Interface1D.
      
      :type: :class:`Id`


   .. attribute:: length_2d

      The 2D length of this Interface1D.
      
      :type: float


   .. attribute:: name

      The string of the name of the 1D element.
      
      :type: str


   .. attribute:: nature

      The nature of this Interface1D.
      
      :type: :class:`Nature`


   .. attribute:: time_stamp

      The time stamp of the 1D element, mainly used for selection.
      
      :type: int




.. class:: Iterator

   Base class to define iterators.
   
   .. method:: __init__()
   
      Default constructor.

   .. method:: decrement()
   
      Makes the iterator point the previous element.


   .. method:: increment()
   
      Makes the iterator point the next element.


   .. attribute:: is_begin

      True if the interator points the first element.
      
      :type: bool


   .. attribute:: is_end

      True if the interator points the last element.
      
      :type: bool


   .. attribute:: name

      The string of the name of this iterator.
      
      :type: str




.. class:: Material

   Class defining a material.
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __init__(brother)
   
      Copy constructor.
   
      :arg brother: A Material object.
      :type brother: :class:`Material`
   
   .. method:: __init__(line, diffuse, ambient, specular, emission, shininess, priority)
   
      Builds a Material from its line, diffuse, ambient, specular, emissive
      colors, a shininess coefficient and line color priority.
   
      :arg line: The line color.
      :type line: :class:`mathutils.Vector`, list or tuple of 4 float values
      :arg diffuse: The diffuse color.
      :type diffuse: :class:`mathutils.Vector`, list or tuple of 4 float values
      :arg ambient: The ambient color.
      :type ambient: :class:`mathutils.Vector`, list or tuple of 4 float values
      :arg specular: The specular color.
      :type specular: :class:`mathutils.Vector`, list or tuple of 4 float values
      :arg emission: The emissive color.
      :type emission: :class:`mathutils.Vector`, list or tuple of 4 float values
      :arg shininess: The shininess coefficient.
      :type shininess: float
      :arg priority: The line color priority.
      :type priority: int

   .. attribute:: ambient

      RGBA components of the ambient color of the material.
      
      :type: :class:`mathutils.Color`


   .. attribute:: diffuse

      RGBA components of the diffuse color of the material.
      
      :type: :class:`mathutils.Vector`


   .. attribute:: emission

      RGBA components of the emissive color of the material.
      
      :type: :class:`mathutils.Color`


   .. attribute:: line

      RGBA components of the line color of the material.
      
      :type: :class:`mathutils.Vector`


   .. attribute:: priority

      Line color priority of the material.
      
      :type: int


   .. attribute:: shininess

      Shininess coefficient of the material.
      
      :type: float


   .. attribute:: specular

      RGBA components of the specular color of the material.
      
      :type: :class:`mathutils.Vector`




.. class:: MediumType

   Class hierarchy: int > :class:`MediumType`
   
   The different blending modes available to similate the interaction
   media-medium:
   
   * Stroke.DRY_MEDIUM: To simulate a dry medium such as Pencil or Charcoal.
   * Stroke.HUMID_MEDIUM: To simulate ink painting (color substraction blending).
   * Stroke.OPAQUE_MEDIUM: To simulate an opaque medium (oil, spray...).



.. class:: Nature

   Class hierarchy: int > :class:`Nature`
   
   Different possible natures of 0D and 1D elements of the ViewMap.
   
   Vertex natures:
   
   * Nature.POINT: True for any 0D element.
   * Nature.S_VERTEX: True for SVertex.
   * Nature.VIEW_VERTEX: True for ViewVertex.
   * Nature.NON_T_VERTEX: True for NonTVertex.
   * Nature.T_VERTEX: True for TVertex.
   * Nature.CUSP: True for CUSP.
   
   Edge natures:
   
   * Nature.NO_FEATURE: True for non feature edges (always false for 1D
     elements of the ViewMap).
   * Nature.SILHOUETTE: True for silhouettes.
   * Nature.BORDER: True for borders.
   * Nature.CREASE: True for creases.
   * Nature.RIDGE: True for ridges.
   * Nature.VALLEY: True for valleys.
   * Nature.SUGGESTIVE_CONTOUR: True for suggestive contours.
   * Nature.MATERIAL_BOUNDARY: True for edges at material boundaries.
   * Nature.EDGE_MARK: True for edges having user-defined edge marks.



.. class:: Noise

   Class to provide Perlin noise functionalities.
   
   .. method:: __init__(seed = -1)
   
      Builds a Noise object.  Seed is an optional argument.  The seed value is used
      as a seed for random number generation if it is equal to or greater than zero;
      otherwise, time is used as a seed.
   
      :arg seed: Seed for random number generation.
      :type seed: int

   Undocumented


   .. method:: smoothNoise1(v)
   
      Returns a smooth noise value for a 1D element.
   
      :arg v: One-dimensional sample point.
      :type v: float
      :return: A smooth noise value.
      :rtype: float


   .. method:: smoothNoise2(v)
   
      Returns a smooth noise value for a 2D element.
   
      :arg v: Two-dimensional sample point.
      :type v: :class:`mathutils.Vector`, list or tuple of 2 real numbers
      :return: A smooth noise value.
      :rtype: float


   .. method:: smoothNoise3(v)
   
      Returns a smooth noise value for a 3D element.
   
      :arg v: Three-dimensional sample point.
      :type v: :class:`mathutils.Vector`, list or tuple of 3 real numbers
      :return: A smooth noise value.
      :rtype: float


   .. method:: turbulence1(v, freq, amp, oct=4)
   
      Returns a noise value for a 1D element.
   
      :arg v: One-dimensional sample point.
      :type v: float
      :arg freq: Noise frequency.
      :type freq: float
      :arg amp: Amplitude.
      :type amp: float
      :arg oct: Number of octaves.
      :type oct: int
      :return: A noise value.
      :rtype: float


   .. method:: turbulence2(v, freq, amp, oct=4)
   
      Returns a noise value for a 2D element.
   
      :arg v: Two-dimensional sample point.
      :type v: :class:`mathutils.Vector`, list or tuple of 2 real numbers
      :arg freq: Noise frequency.
      :type freq: float
      :arg amp: Amplitude.
      :type amp: float
      :arg oct: Number of octaves.
      :type oct: int
      :return: A noise value.
      :rtype: float


   .. method:: turbulence3(v, freq, amp, oct=4)
   
      Returns a noise value for a 3D element.
   
      :arg v: Three-dimensional sample point.
      :type v: :class:`mathutils.Vector`, list or tuple of 3 real numbers
      :arg freq: Noise frequency.
      :type freq: float
      :arg amp: Amplitude.
      :type amp: float
      :arg oct: Number of octaves.
      :type oct: int
      :return: A noise value.
      :rtype: float


   Undocumented




.. class:: NonTVertex

   Class hierarchy: :class:`Interface0D` > :class:`ViewVertex` > :class:`NonTVertex`
   
   View vertex for corners, cusps, etc. associated to a single SVertex.
   Can be associated to 2 or more view edges.
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __init__(svertex)
   
      Build a NonTVertex from a SVertex.
   
      :arg svertex: An SVertex object.
      :type svertex: :class:`SVertex`

   .. attribute:: svertex

      The SVertex on top of which this NonTVertex is built.
      
      :type: :class:`SVertex`




.. class:: Operators

   Class defining the operators used in a style module.  There are five
   types of operators: Selection, chaining, splitting, sorting and
   creation.  All these operators are user controlled through functors,
   predicates and shaders that are taken as arguments.

   .. staticmethod:: bidirectional_chain(it, pred)
   
      Builds a set of chains from the current set of ViewEdges.  Each
      ViewEdge of the current list potentially starts a new chain.  The
      chaining operator then iterates over the ViewEdges of the ViewMap
      using the user specified iterator.  This operator iterates both using
      the increment and decrement operators and is therefore bidirectional.
      This operator works with a ChainingIterator which contains the
      chaining rules.  It is this last one which can be told to chain only
      edges that belong to the selection or not to process twice a ViewEdge
      during the chaining.  Each time a ViewEdge is added to a chain, its
      chaining time stamp is incremented.  This allows you to keep track of
      the number of chains to which a ViewEdge belongs to.
   
      :arg it: The ChainingIterator on the ViewEdges of the ViewMap.  It
         contains the chaining rule.
      :type it: :class:`ChainingIterator`
      :arg pred: The predicate on the ViewEdge that expresses the
         stopping condition.
      :type pred: :class:`UnaryPredicate1D`
   
   .. staticmethod:: bidirectional_chain(it)
   
      The only difference with the above bidirectional chaining algorithm
      is that we don't need to pass a stopping criterion.  This might be
      desirable when the stopping criterion is already contained in the
      iterator definition.  Builds a set of chains from the current set of
      ViewEdges.  Each ViewEdge of the current list potentially starts a new
      chain.  The chaining operator then iterates over the ViewEdges of the
      ViewMap using the user specified iterator.  This operator iterates
      both using the increment and decrement operators and is therefore
      bidirectional.  This operator works with a ChainingIterator which
      contains the chaining rules.  It is this last one which can be told to
      chain only edges that belong to the selection or not to process twice
      a ViewEdge during the chaining.  Each time a ViewEdge is added to a
      chain, its chaining time stamp is incremented.  This allows you to
      keep track of the number of chains to which a ViewEdge belongs to.
   
      :arg it: The ChainingIterator on the ViewEdges of the ViewMap.  It
         contains the chaining rule.
      :type it: :class:`ChainingIterator`

   .. staticmethod:: chain(it, pred, modifier)
   
      Builds a set of chains from the current set of ViewEdges.  Each
      ViewEdge of the current list starts a new chain.  The chaining
      operator then iterates over the ViewEdges of the ViewMap using the
      user specified iterator.  This operator only iterates using the
      increment operator and is therefore unidirectional.
   
      :arg it: The iterator on the ViewEdges of the ViewMap. It contains
         the chaining rule.
      :type it: :class:`ViewEdgeIterator`
      :arg pred: The predicate on the ViewEdge that expresses the
         stopping condition.
      :type pred: :class:`UnaryPredicate1D`
      :arg modifier: A function that takes a ViewEdge as argument and
         that is used to modify the processed ViewEdge state (the
         timestamp incrementation is a typical illustration of such a
         modifier).
      :type modifier: :class:`UnaryFunction1DVoid`
   
   .. staticmethod:: chain(it, pred)
   
      Builds a set of chains from the current set of ViewEdges.  Each
      ViewEdge of the current list starts a new chain.  The chaining
      operator then iterates over the ViewEdges of the ViewMap using the
      user specified iterator.  This operator only iterates using the
      increment operator and is therefore unidirectional.  This chaining
      operator is different from the previous one because it doesn't take
      any modifier as argument.  Indeed, the time stamp (insuring that a
      ViewEdge is processed one time) is automatically managed in this
      case.
   
      :arg it: The iterator on the ViewEdges of the ViewMap. It contains
         the chaining rule. 
      :type it: :class:`ViewEdgeIterator`
      :arg pred: The predicate on the ViewEdge that expresses the
         stopping condition.
      :type pred: :class:`UnaryPredicate1D`

   .. staticmethod:: create(pred, shaders)
   
      Creates and shades the strokes from the current set of chains.  A
      predicate can be specified to make a selection pass on the chains.
   
      :arg pred: The predicate that a chain must verify in order to be
         transform as a stroke.
      :type pred: :class:`UnaryPredicate1D`
      :arg shaders: The list of shaders used to shade the strokes.
      :type shaders: list of :class:`StrokeShader` objects

   .. staticmethod:: get_chain_from_index(i)
   
      Returns the Chain at the index in the current set of Chains.
   
      :arg i: index (0 <= i < Operators.get_chains_size()).
      :type i: int
      :return: The Chain object.
      :rtype: :class:`Chain`

   .. staticmethod:: get_chains_size()
   
      Returns the number of Chains.
   
      :return: The number of Chains.
      :rtype: int

   .. staticmethod:: get_stroke_from_index(i)
   
      Returns the Stroke at the index in the current set of Strokes.
   
      :arg i: index (0 <= i < Operators.get_strokes_size()).
      :type i: int
      :return: The Stroke object.
      :rtype: :class:`Stroke`

   .. staticmethod:: get_strokes_size()
   
      Returns the number of Strokes.
   
      :return: The number of Strokes.
      :rtype: int

   .. staticmethod:: get_view_edges_size()
   
      Returns the number of ViewEdges.
   
      :return: The number of ViewEdges.
      :rtype: int

   .. staticmethod:: get_viewedge_from_index(i)
   
      Returns the ViewEdge at the index in the current set of ViewEdges.
   
      :arg i: index (0 <= i < Operators.get_view_edges_size()).
      :type i: int
      :return: The ViewEdge object.
      :rtype: :class:`ViewEdge`

   .. staticmethod:: recursive_split(func, pred_1d, sampling=0.0)
   
      Splits the current set of chains in a recursive way.  We process the
      points of each chain (with a specified sampling) to find the point
      minimizing a specified function.  The chain is split in two at this
      point and the two new chains are processed in the same way.  The
      recursivity level is controlled through a predicate 1D that expresses
      a stopping condition on the chain that is about to be processed.
   
      :arg func: The Unary Function evaluated at each point of the chain.
        The splitting point is the point minimizing this function.
      :type func: :class:`UnaryFunction0DDouble`
      :arg pred_1d: The Unary Predicate expressing the recursivity stopping
         condition.  This predicate is evaluated for each curve before it
         actually gets split.  If pred_1d(chain) is true, the curve won't be
         split anymore.
      :type pred_1d: :class:`UnaryPredicate1D`
      :arg sampling: The resolution used to sample the chain for the
         predicates evaluation. (The chain is not actually resampled, a
         virtual point only progresses along the curve using this
         resolution.)
      :type sampling: float
   
   .. staticmethod:: recursive_split(func, pred_0d, pred_1d, sampling=0.0)
   
      Splits the current set of chains in a recursive way.  We process the
      points of each chain (with a specified sampling) to find the point
      minimizing a specified function.  The chain is split in two at this
      point and the two new chains are processed in the same way.  The user
      can specify a 0D predicate to make a first selection on the points
      that can potentially be split.  A point that doesn't verify the 0D
      predicate won't be candidate in realizing the min.  The recursivity
      level is controlled through a predicate 1D that expresses a stopping
      condition on the chain that is about to be processed.
   
      :arg func: The Unary Function evaluated at each point of the chain.
         The splitting point is the point minimizing this function.
      :type func: :class:`UnaryFunction0DDouble`
      :arg pred_0d: The Unary Predicate 0D used to select the candidate
         points where the split can occur.  For example, it is very likely
         that would rather have your chain splitting around its middle
         point than around one of its extremities.  A 0D predicate working
         on the curvilinear abscissa allows to add this kind of constraints.
      :type pred_0d: :class:`UnaryPredicate0D`
      :arg pred_1d: The Unary Predicate expressing the recursivity stopping
         condition. This predicate is evaluated for each curve before it
         actually gets split.  If pred_1d(chain) is true, the curve won't be
         split anymore.
      :type pred_1d: :class:`UnaryPredicate1D`
      :arg sampling: The resolution used to sample the chain for the
         predicates evaluation. (The chain is not actually resampled; a
         virtual point only progresses along the curve using this
         resolution.)
      :type sampling: float

   .. staticmethod:: reset(delete_strokes=True)
   
      Resets the line stylization process to the initial state.  The results of
      stroke creation are accumulated if **delete_strokes** is set to False.
   
      :arg delete_strokes: Delete the strokes that are currently stored.
      :type delete_strokes: bool

   .. staticmethod:: select(pred)
   
      Selects the ViewEdges of the ViewMap verifying a specified
      condition.
   
      :arg pred: The predicate expressing this condition.
      :type pred: :class:`UnaryPredicate1D`

   .. staticmethod:: sequential_split(starting_pred, stopping_pred, sampling=0.0)
   
      Splits each chain of the current set of chains in a sequential way.
      The points of each chain are processed (with a specified sampling)
      sequentially. Each time a user specified starting condition is
      verified, a new chain begins and ends as soon as a user-defined
      stopping predicate is verified. This allows chains overlapping rather
      than chains partitioning. The first point of the initial chain is the
      first point of one of the resulting chains. The splitting ends when
      no more chain can start.
   
      :arg starting_pred: The predicate on a point that expresses the
         starting condition.
      :type starting_pred: :class:`UnaryPredicate0D`
      :arg stopping_pred: The predicate on a point that expresses the
         stopping condition.
      :type stopping_pred: :class:`UnaryPredicate0D`
      :arg sampling: The resolution used to sample the chain for the
         predicates evaluation. (The chain is not actually resampled;
         a virtual point only progresses along the curve using this
         resolution.)
      :type sampling: float
   
   .. staticmethod:: sequential_split(pred, sampling=0.0)
   
      Splits each chain of the current set of chains in a sequential way.
      The points of each chain are processed (with a specified sampling)
      sequentially and each time a user specified condition is verified,
      the chain is split into two chains.  The resulting set of chains is a
      partition of the initial chain
   
      :arg pred: The predicate on a point that expresses the splitting
         condition.
      :type pred: :class:`UnaryPredicate0D`
      :arg sampling: The resolution used to sample the chain for the
         predicate evaluation. (The chain is not actually resampled; a
         virtual point only progresses along the curve using this
         resolution.)
      :type sampling: float

   .. staticmethod:: sort(pred)
   
      Sorts the current set of chains (or viewedges) according to the
      comparison predicate given as argument.
   
      :arg pred: The binary predicate used for the comparison.
      :type pred: :class:`BinaryPredicate1D`



.. class:: SShape

   Class to define a feature shape.  It is the gathering of feature
   elements from an identified input shape.
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __init__(brother)
   
      Copy constructor.
   
      :arg brother: An SShape object.
      :type brother: :class:`SShape`

   .. method:: add_edge(edge)
   
      Adds an FEdge to the list of FEdges.
   
      :arg edge: An FEdge object.
      :type edge: :class:`FEdge`


   .. method:: add_vertex(vertex)
   
      Adds an SVertex to the list of SVertex of this Shape.  The SShape
      attribute of the SVertex is also set to this SShape.
   
      :arg vertex: An SVertex object.
      :type vertex: :class:`SVertex`


   .. method:: compute_bbox()
   
      Compute the bbox of the SShape.


   .. attribute:: bbox

      The bounding box of the SShape.
      
      :type: :class:`BBox`


   .. attribute:: edges

      The list of edges constituting this SShape.
      
      :type: List of :class:`FEdge` objects


   .. attribute:: id

      The Id of this SShape.
      
      :type: :class:`Id`


   .. attribute:: name

      The name of the SShape.
      
      :type: str


   .. attribute:: vertices

      The list of vertices constituting this SShape.
      
      :type: List of :class:`SVertex` objects




.. class:: SVertex

   Class hierarchy: :class:`Interface0D` > :class:`SVertex`
   
   Class to define a vertex of the embedding.
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __init__(brother)
   
      Copy constructor.
   
      :arg brother: A SVertex object.
      :type brother: :class:`SVertex`
   
   .. method:: __init__(point_3d, id)
   
      Builds a SVertex from 3D coordinates and an Id.
   
      :arg point_3d: A three-dimensional vector.
      :type point_3d: :class:`mathutils.Vector`
      :arg id: An Id object.
      :type id: :class:`Id`

   .. method:: add_fedge(fedge)
   
      Add an FEdge to the list of edges emanating from this SVertex.
   
      :arg fedge: An FEdge.
      :type fedge: :class:`FEdge`


   .. method:: add_normal(normal)
   
      Adds a normal to the SVertex's set of normals.  If the same normal
      is already in the set, nothing changes.
   
      :arg normal: A three-dimensional vector.
      :type normal: :class:`mathutils.Vector`, list or tuple of 3 real numbers


   .. attribute:: curvatures

      Curvature information expressed in the form of a seven-element tuple
      (K1, e1, K2, e2, Kr, er, dKr), where K1 and K2 are scalar values
      representing the first (maximum) and second (minimum) principal
      curvatures at this SVertex, respectively; e1 and e2 are
      three-dimensional vectors representing the first and second principal
      directions, i.e. the directions of the normal plane where the
      curvature takes its maximum and minimum values, respectively; and Kr,
      er and dKr are the radial curvature, radial direction, and the
      derivative of the radial curvature at this SVertex, respectively.
      
      :type: tuple


   .. attribute:: id

      The Id of this SVertex.
      
      :type: :class:`Id`


   .. attribute:: normals

      The normals for this Vertex as a list.  In a sharp surface, an SVertex
      has exactly one normal.  In a smooth surface, an SVertex can have any
      number of normals.
      
      :type: list of :class:`mathutils.Vector` objects


   .. attribute:: normals_size

      The number of different normals for this SVertex.
      
      :type: int


   .. attribute:: point_2d

      The projected 3D coordinates of the SVertex.
      
      :type: :class:`mathutils.Vector`


   .. attribute:: point_3d

      The 3D coordinates of the SVertex.
      
      :type: :class:`mathutils.Vector`


   .. attribute:: viewvertex

      If this SVertex is also a ViewVertex, this property refers to the
      ViewVertex, and None otherwise.
      
      :type: :class:`ViewVertex`




.. class:: SVertexIterator

   Class hierarchy: :class:`Iterator` > :class:`SVertexIterator`
   
   Class representing an iterator over :class:`SVertex` of a
   :class:`ViewEdge`.  An instance of an SVertexIterator can be obtained
   from a ViewEdge by calling verticesBegin() or verticesEnd().
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __init__(brother)
   
      Copy constructor.
   
      :arg brother: An SVertexIterator object.
      :type brother: :class:`SVertexIterator`
   
   .. method:: __init__(vertex, begin, previous_edge, next_edge, t)
   
      Build an SVertexIterator that starts iteration from an SVertex
      object v.
   
      :arg vertex: The SVertex from which the iterator starts iteration.
      :type vertex: :class:`SVertex`
      :arg begin: The first SVertex of a ViewEdge.
      :type begin: :class:`SVertex`
      :arg previous_edge: The previous FEdge coming to vertex.
      :type previous_edge: :class:`FEdge`
      :arg next_edge: The next FEdge going out from vertex.
      :type next_edge: :class:`FEdge`
      :arg t: The curvilinear abscissa at vertex.
      :type t: float

   .. attribute:: object

      The SVertex object currently pointed by this iterator.
      
      :type: :class:`SVertex`


   .. attribute:: t

      The curvilinear abscissa of the current point.
      
      :type: float


   .. attribute:: u

      The point parameter at the current point in the 1D element (0 <= u <= 1).
      
      :type: float




.. class:: Stroke

   Class hierarchy: :class:`Interface1D` > :class:`Stroke`
   
   Class to define a stroke.  A stroke is made of a set of 2D vertices
   (:class:`StrokeVertex`), regularly spaced out.  This set of vertices
   defines the stroke's backbone geometry.  Each of these stroke vertices
   defines the stroke's shape and appearance at this vertex position.
   
   .. method:: Stroke()
   
      Default constructor
   
   .. method:: Stroke(brother)
   
      Copy constructor

   .. method:: compute_sampling(n)
   
      Compute the sampling needed to get N vertices.  If the
      specified number of vertices is less than the actual number of
      vertices, the actual sampling value is returned. (To remove Vertices,
      use the RemoveVertex() method of this class.)
   
      :arg n: The number of stroke vertices we eventually want
         in our Stroke.
      :type n: int
      :return: The sampling that must be used in the Resample(float)
         method.
      :rtype: float


   .. method:: insert_vertex(vertex, next)
   
      Inserts the StrokeVertex given as argument into the Stroke before the
      point specified by next.  The length and curvilinear abscissa are
      updated consequently.
   
      :arg vertex: The StrokeVertex to insert in the Stroke.
      :type vertex: :class:`StrokeVertex`
      :arg next: A StrokeVertexIterator pointing to the StrokeVertex
         before which vertex must be inserted.
      :type next: :class:`StrokeVertexIterator`


   .. method:: remove_all_vertices()
   
      Removes all vertices from the Stroke.


   .. method:: remove_vertex(vertex)
   
      Removes the StrokeVertex given as argument from the Stroke. The length
      and curvilinear abscissa are updated consequently.
   
      :arg vertex: the StrokeVertex to remove from the Stroke.
      :type vertex: :class:`StrokeVertex`


   .. method:: resample(n)
   
      Resamples the stroke so that it eventually has N points.  That means
      it is going to add N-vertices_size, where vertices_size is the
      number of points we already have.  If vertices_size >= N, no
      resampling is done.
   
      :arg n: The number of vertices we eventually want in our stroke.
      :type n: int
   
   .. method:: resample(sampling)
   
      Resamples the stroke with a given sampling.  If the sampling is
      smaller than the actual sampling value, no resampling is done.
   
      :arg sampling: The new sampling value.
      :type sampling: float


   .. method:: stroke_vertices_begin(t=0.0)
   
      Returns a StrokeVertexIterator pointing on the first StrokeVertex of
      the Stroke. One can specify a sampling value to resample the Stroke
      on the fly if needed.
   
      :arg t: The resampling value with which we want our Stroke to be
         resampled.  If 0 is specified, no resampling is done.
      :type t: float
      :return: A StrokeVertexIterator pointing on the first StrokeVertex.
      :rtype: :class:`StrokeVertexIterator`


   .. method:: stroke_vertices_end()
   
      Returns a StrokeVertexIterator pointing after the last StrokeVertex
      of the Stroke.
   
      :return: A StrokeVertexIterator pointing after the last StrokeVertex.
      :rtype: :class:`StrokeVertexIterator`


   .. method:: stroke_vertices_size()
   
      Returns the number of StrokeVertex constituting the Stroke.
   
      :return: The number of stroke vertices.
      :rtype: int


   .. method:: update_length()
   
      Updates the 2D length of the Stroke.


   .. attribute:: id

      The Id of this Stroke.
      
      :type: :class:`Id`


   .. attribute:: length_2d

      The 2D length of the Stroke.
      
      :type: float


   .. attribute:: medium_type

      The MediumType used for this Stroke.
      
      :type: :class:`MediumType`


   .. attribute:: texture_id

      The ID of the texture used to simulate th marks system for this Stroke.
      
      :type: int


   .. attribute:: tips

      True if this Stroke uses a texture with tips, and false otherwise.
      
      :type: bool




.. class:: StrokeAttribute

   Class to define a set of attributes associated with a :class:`StrokeVertex`.
   The attribute set stores the color, alpha and thickness values for a Stroke
   Vertex.
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __init__(brother)
   
      Copy constructor.
   
      :arg brother: A StrokeAttribute object.
      :type brother: :class:`StrokeAttribute`
   
   .. method:: __init__(red, green, blue, alpha, thickness_right, thickness_left)
   
      Build a stroke vertex attribute from a set of parameters.
   
      :arg red: Red component of a stroke color.
      :type red: float
      :arg green: Green component of a stroke color.
      :type green: float
      :arg blue: Blue component of a stroke color.
      :type blue: float
      :arg alpha: Alpha component of a stroke color.
      :type alpha: float
      :arg thickness_right: Stroke thickness on the right.
      :type thickness_right: float
      :arg thickness_left: Stroke thickness on the left.
      :type thickness_left: float
   
   .. method:: __init__(attribute1, attribute2, t)
   
      Interpolation constructor. Build a StrokeAttribute from two
      StrokeAttribute objects and an interpolation parameter.
   
      :arg attribute1: The first StrokeAttribute object.
      :type attribute1: :class:`StrokeAttribute`
      :arg attribute2: The second StrokeAttribute object.
      :type attribute2: :class:`StrokeAttribute`
      :arg t: The interpolation parameter (0 <= t <= 1).
      :type t: float

   .. method:: get_attribute_real(name)
   
      Returns an attribute of float type.
   
      :arg name: The name of the attribute.
      :type name: str
      :return: The attribute value.
      :rtype: float


   .. method:: get_attribute_vec2(name)
   
      Returns an attribute of two-dimensional vector type.
   
      :arg name: The name of the attribute.
      :type name: str
      :return: The attribute value.
      :rtype: :class:`mathutils.Vector`


   .. method:: get_attribute_vec3(name)
   
      Returns an attribute of three-dimensional vector type.
   
      :arg name: The name of the attribute.
      :type name: str
      :return: The attribute value.
      :rtype: :class:`mathutils.Vector`


   .. method:: has_attribute_real(name)
   
      Checks whether the attribute name of float type is available.
   
      :arg name: The name of the attribute.
      :type name: str
      :return: True if the attribute is availbale.
      :rtype: bool


   .. method:: has_attribute_vec2(name)
   
      Checks whether the attribute name of two-dimensional vector type
      is available.
   
      :arg name: The name of the attribute.
      :type name: str
      :return: True if the attribute is availbale.
      :rtype: bool


   .. method:: has_attribute_vec3(name)
   
      Checks whether the attribute name of three-dimensional vector
      type is available.
   
      :arg name: The name of the attribute.
      :type name: str
      :return: True if the attribute is availbale.
      :rtype: bool


   .. method:: set_attribute_real(name, value)
   
      Adds a user-defined attribute of float type.  If there is no
      attribute of the given name, it is added.  Otherwise, the new value
      replaces the old one.
   
      :arg name: The name of the attribute.
      :type name: str
      :arg value: The attribute value.
      :type value: float


   .. method:: set_attribute_vec2(name, value)
   
      Adds a user-defined attribute of two-dimensional vector type.  If
      there is no attribute of the given name, it is added.  Otherwise,
      the new value replaces the old one.
   
      :arg name: The name of the attribute.
      :type name: str
      :arg value: The attribute value.
      :type value: :class:`mathutils.Vector`, list or tuple of 2 real numbers


   .. method:: set_attribute_vec3(name, value)
   
      Adds a user-defined attribute of three-dimensional vector type.
      If there is no attribute of the given name, it is added.
      Otherwise, the new value replaces the old one.
   
      :arg name: The name of the attribute.
      :type name: str
      :arg value: The attribute value.
      :type value: :class:`mathutils.Vector`, list or tuple of 3 real numbers


   .. attribute:: alpha

      Alpha component of the stroke color.
      
      :type: float


   .. attribute:: color

      RGB components of the stroke color.
      
      :type: :class:`mathutils.Color`


   .. attribute:: thickness

      Right and left components of the stroke thickness.
      The right (left) component is the thickness on the right (left) of the vertex
      when following the stroke.
      
      :type: :class:`mathutils.Vector`


   .. attribute:: visible

      The visibility flag.  True if the StrokeVertex is visible.
      
      :type: bool




.. class:: StrokeShader

   Base class for stroke shaders.  Any stroke shader must inherit from
   this class and overload the shade() method.  A StrokeShader is
   designed to modify stroke attributes such as thickness, color,
   geometry, texture, blending mode, and so on.  The basic way for this
   operation is to iterate over the stroke vertices of the :class:`Stroke`
   and to modify the :class:`StrokeAttribute` of each vertex.  Here is a
   code example of such an iteration::
   
     it = ioStroke.strokeVerticesBegin()
     while not it.is_end:
         att = it.object.attribute
         ## perform here any attribute modification
         it.increment()
   
   .. method:: __init__()
   
      Default constructor.

   .. method:: shade(stroke)
   
      The shading method.  Must be overloaded by inherited classes.
   
      :arg stroke: A Stroke object.
      :type stroke: :class:`Stroke`


   .. attribute:: name

      The name of the stroke shader.
      
      :type: str




.. class:: StrokeVertex

   Class hierarchy: :class:`Interface0D` > :class:`CurvePoint` > :class:`StrokeVertex`
   
   Class to define a stroke vertex.
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __init__(brother)
   
      Copy constructor.
   
      :arg brother: A StrokeVertex object.
      :type brother: :class:`StrokeVertex`
   
   .. method:: __init__(first_vertex, second_vertex, t3d)
   
      Build a stroke vertex from 2 stroke vertices and an interpolation
      parameter.
   
      :arg first_vertex: The first StrokeVertex.
      :type first_vertex: :class:`StrokeVertex`
      :arg second_vertex: The second StrokeVertex.
      :type second_vertex: :class:`StrokeVertex`
      :arg t3d: An interpolation parameter.
      :type t3d: float
   
   .. method:: __init__(point)
   
      Build a stroke vertex from a CurvePoint
   
      :arg point: A CurvePoint object.
      :type point: :class:`CurvePoint`
   
   .. method:: __init__(svertex)
   
      Build a stroke vertex from a SVertex
   
      :arg svertex: An SVertex object.
      :type svertex: :class:`SVertex`
   
   .. method:: __init__(svertex, attribute)
   
      Build a stroke vertex from an SVertex and a StrokeAttribute object.
   
      :arg svertex: An SVertex object.
      :type svertex: :class:`SVertex`
      :arg attribute: A StrokeAttribute object.
      :type attribute: :class:`StrokeAttribute`

   .. attribute:: attribute

      StrokeAttribute for this StrokeVertex.
      
      :type: :class:`StrokeAttribute`


   .. attribute:: curvilinear_abscissa

      Curvilinear abscissa of this StrokeVertex in the Stroke.
      
      :type: float


   .. attribute:: point

      2D point coordinates.
      
      :type: :class:`mathutils.Vector`


   .. attribute:: stroke_length

      Stroke length (it is only a value retained by the StrokeVertex,
      and it won't change the real stroke length).
      
      :type: float


   .. attribute:: u

      Curvilinear abscissa of this StrokeVertex in the Stroke.
      
      :type: float




.. class:: StrokeVertexIterator

   Class hierarchy: :class:`Iterator` > :class:`StrokeVertexIterator`
   
   Class defining an iterator designed to iterate over the
   :class:`StrokeVertex` of a :class:`Stroke`.  An instance of a
   StrokeVertexIterator can be obtained from a Stroke by calling
   iter(), stroke_vertices_begin() or stroke_vertices_begin().  It is iterating
   over the same vertices as an :class:`Interface0DIterator`.  The difference
   resides in the object access: an Interface0DIterator only allows
   access to an Interface0D while one might need to access the
   specialized StrokeVertex type.  In this case, one should use a
   StrokeVertexIterator.  To call functions of the UnaryFuntion0D type,
   a StrokeVertexIterator can be converted to an Interface0DIterator by
   by calling Interface0DIterator(it).
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __init__(brother)
   
      Copy constructor.
   
      :arg brother: A StrokeVertexIterator object.
      :type brother: :class:`StrokeVertexIterator`

   .. method:: decremented()
   
      Returns a copy of a decremented StrokeVertexIterator.
   
      :return: A StrokeVertexIterator pointing the previous StrokeVertex.
      :rtype: :class:`StrokeVertexIterator`


   .. method:: incremented()
   
      Returns a copy of an incremented StrokeVertexIterator.
   
      :return: A StrokeVertexIterator pointing the next StrokeVertex.
      :rtype: :class:`StrokeVertexIterator`


   .. method:: reversed()
   
      Returns a StrokeVertexIterator that traverses stroke vertices in the
      reversed order.
   
      :return: A StrokeVertexIterator traversing stroke vertices backward.
      :rtype: :class:`StrokeVertexIterator`


   .. attribute:: at_last

      True if the interator points to the last valid element.
      For its counterpart (pointing to the first valid element), use it.is_begin.
      
      :type: bool


   .. attribute:: object

      The StrokeVertex object currently pointed to by this iterator.
      
      :type: :class:`StrokeVertex`


   .. attribute:: t

      The curvilinear abscissa of the current point.
      
      :type: float


   .. attribute:: u

      The point parameter at the current point in the stroke (0 <= u <= 1).
      
      :type: float




.. class:: TVertex

   Class hierarchy: :class:`Interface0D` > :class:`ViewVertex` > :class:`TVertex`
   
   Class to define a T vertex, i.e. an intersection between two edges.
   It points towards two SVertex and four ViewEdges.  Among the
   ViewEdges, two are front and the other two are back.  Basically a
   front edge hides part of a back edge.  So, among the back edges, one
   is of invisibility N and the other of invisibility N+1.
   
   .. method:: __init__()
   
      Default constructor.

   .. method:: get_mate(viewedge)
   
      Returns the mate edge of the ViewEdge given as argument.  If the
      ViewEdge is frontEdgeA, frontEdgeB is returned.  If the ViewEdge is
      frontEdgeB, frontEdgeA is returned.  Same for back edges.
   
      :arg viewedge: A ViewEdge object.
      :type viewedge: :class:`ViewEdge`
      :return: The mate edge of the given ViewEdge.
      :rtype: :class:`ViewEdge`


   .. method:: get_svertex(fedge)
   
      Returns the SVertex (among the 2) belonging to the given FEdge.
   
      :arg fedge: An FEdge object.
      :type fedge: :class:`FEdge`
      :return: The SVertex belonging to the given FEdge.
      :rtype: :class:`SVertex`


   .. attribute:: back_svertex

      The SVertex that is further away from the viewpoint.
      
      :type: :class:`SVertex`


   .. attribute:: front_svertex

      The SVertex that is closer to the viewpoint.
      
      :type: :class:`SVertex`


   .. attribute:: id

      The Id of this TVertex.
      
      :type: :class:`Id`




.. class:: UnaryFunction0D

   Base class for Unary Functions (functors) working on
   :class:`Interface0DIterator`.  A unary function will be used by
   invoking __call__() on an Interface0DIterator.  In Python, several
   different subclasses of UnaryFunction0D are used depending on the
   types of functors' return values.  For example, you would inherit from
   a :class:`UnaryFunction0DDouble` if you wish to define a function that
   returns a double value.  Available UnaryFunction0D subclasses are:
   
   * :class:`UnaryFunction0DDouble`
   * :class:`UnaryFunction0DEdgeNature`
   * :class:`UnaryFunction0DFloat`
   * :class:`UnaryFunction0DId`
   * :class:`UnaryFunction0DMaterial`
   * :class:`UnaryFunction0DUnsigned`
   * :class:`UnaryFunction0DVec2f`
   * :class:`UnaryFunction0DVec3f`
   * :class:`UnaryFunction0DVectorViewShape`
   * :class:`UnaryFunction0DViewShape`

   .. attribute:: name

      The name of the unary 0D function.
      
      :type: str




.. class:: UnaryFunction0DDouble

   Class hierarchy: :class:`UnaryFunction0D` > :class:`UnaryFunction0DDouble`
   
   Base class for unary functions (functors) that work on
   :class:`Interface0DIterator` and return a float value.
   
   .. method:: __init__()
   
      Default constructor.



.. class:: UnaryFunction0DEdgeNature

   Class hierarchy: :class:`UnaryFunction0D` > :class:`UnaryFunction0DEdgeNature`
   
   Base class for unary functions (functors) that work on
   :class:`Interface0DIterator` and return a :class:`Nature` object.
   
   .. method:: __init__()
   
      Default constructor.



.. class:: UnaryFunction0DFloat

   Class hierarchy: :class:`UnaryFunction0D` > :class:`UnaryFunction0DFloat`
   
   Base class for unary functions (functors) that work on
   :class:`Interface0DIterator` and return a float value.
   
   .. method:: __init__()
   
      Default constructor.



.. class:: UnaryFunction0DId

   Class hierarchy: :class:`UnaryFunction0D` > :class:`UnaryFunction0DId`
   
   Base class for unary functions (functors) that work on
   :class:`Interface0DIterator` and return an :class:`Id` object.
   
   .. method:: __init__()
   
      Default constructor.



.. class:: UnaryFunction0DMaterial

   Class hierarchy: :class:`UnaryFunction0D` > :class:`UnaryFunction0DMaterial`
   
   Base class for unary functions (functors) that work on
   :class:`Interface0DIterator` and return a :class:`Material` object.
   
   .. method:: __init__()
   
      Default constructor.



.. class:: UnaryFunction0DUnsigned

   Class hierarchy: :class:`UnaryFunction0D` > :class:`UnaryFunction0DUnsigned`
   
   Base class for unary functions (functors) that work on
   :class:`Interface0DIterator` and return an int value.
   
   .. method:: __init__()
   
      Default constructor.



.. class:: UnaryFunction0DVec2f

   Class hierarchy: :class:`UnaryFunction0D` > :class:`UnaryFunction0DVec2f`
   
   Base class for unary functions (functors) that work on
   :class:`Interface0DIterator` and return a 2D vector.
   
   .. method:: __init__()
   
      Default constructor.



.. class:: UnaryFunction0DVec3f

   Class hierarchy: :class:`UnaryFunction0D` > :class:`UnaryFunction0DVec3f`
   
   Base class for unary functions (functors) that work on
   :class:`Interface0DIterator` and return a 3D vector.
   
   .. method:: __init__()
   
      Default constructor.



.. class:: UnaryFunction0DVectorViewShape

   Class hierarchy: :class:`UnaryFunction0D` > :class:`UnaryFunction0DVectorViewShape`
   
   Base class for unary functions (functors) that work on
   :class:`Interface0DIterator` and return a list of :class:`ViewShape`
   objects.
   
   .. method:: __init__()
   
      Default constructor.



.. class:: UnaryFunction0DViewShape

   Class hierarchy: :class:`UnaryFunction0D` > :class:`UnaryFunction0DViewShape`
   
   Base class for unary functions (functors) that work on
   :class:`Interface0DIterator` and return a :class:`ViewShape` object.
   
   .. method:: __init__()
   
      Default constructor.



.. class:: UnaryFunction1D

   Base class for Unary Functions (functors) working on
   :class:`Interface1D`.  A unary function will be used by invoking
   __call__() on an Interface1D.  In Python, several different subclasses
   of UnaryFunction1D are used depending on the types of functors' return
   values.  For example, you would inherit from a
   :class:`UnaryFunction1DDouble` if you wish to define a function that
   returns a double value.  Available UnaryFunction1D subclasses are:
   
   * :class:`UnaryFunction1DDouble`
   * :class:`UnaryFunction1DEdgeNature`
   * :class:`UnaryFunction1DFloat`
   * :class:`UnaryFunction1DUnsigned`
   * :class:`UnaryFunction1DVec2f`
   * :class:`UnaryFunction1DVec3f`
   * :class:`UnaryFunction1DVectorViewShape`
   * :class:`UnaryFunction1DVoid`

   .. attribute:: name

      The name of the unary 1D function.
      
      :type: str




.. class:: UnaryFunction1DDouble

   Class hierarchy: :class:`UnaryFunction1D` > :class:`UnaryFunction1DDouble`
   
   Base class for unary functions (functors) that work on
   :class:`Interface1D` and return a float value.
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __init__(integration_type)
   
      Builds a unary 1D function using the integration method given as
      argument.
   
      :arg integration_type: An integration method.
      :type integration_type: :class:`IntegrationType`

   .. attribute:: integration_type

      The integration method.
      
      :type: :class:`IntegrationType`




.. class:: UnaryFunction1DEdgeNature

   Class hierarchy: :class:`UnaryFunction1D` > :class:`UnaryFunction1DEdgeNature`
   
   Base class for unary functions (functors) that work on
   :class:`Interface1D` and return a :class:`Nature` object.
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __init__(integration_type)
   
      Builds a unary 1D function using the integration method given as
      argument.
   
      :arg integration_type: An integration method.
      :type integration_type: :class:`IntegrationType`

   .. attribute:: integration_type

      The integration method.
      
      :type: :class:`IntegrationType`




.. class:: UnaryFunction1DFloat

   Class hierarchy: :class:`UnaryFunction1D` > :class:`UnaryFunction1DFloat`
   
   Base class for unary functions (functors) that work on
   :class:`Interface1D` and return a float value.
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __init__(integration_type)
   
      Builds a unary 1D function using the integration method given as
      argument.
   
      :arg integration_type: An integration method.
      :type integration_type: :class:`IntegrationType`

   .. attribute:: integration_type

      The integration method.
      
      :type: :class:`IntegrationType`




.. class:: UnaryFunction1DUnsigned

   Class hierarchy: :class:`UnaryFunction1D` > :class:`UnaryFunction1DUnsigned`
   
   Base class for unary functions (functors) that work on
   :class:`Interface1D` and return an int value.
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __init__(integration_type)
   
      Builds a unary 1D function using the integration method given as
      argument.
   
      :arg integration_type: An integration method.
      :type integration_type: :class:`IntegrationType`

   .. attribute:: integration_type

      The integration method.
      
      :type: :class:`IntegrationType`




.. class:: UnaryFunction1DVec2f

   Class hierarchy: :class:`UnaryFunction1D` > :class:`UnaryFunction1DVec2f`
   
   Base class for unary functions (functors) that work on
   :class:`Interface1D` and return a 2D vector.
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __init__(integration_type)
   
      Builds a unary 1D function using the integration method given as
      argument.
   
      :arg integration_type: An integration method.
      :type integration_type: :class:`IntegrationType`

   .. attribute:: integration_type

      The integration method.
      
      :type: :class:`IntegrationType`




.. class:: UnaryFunction1DVec3f

   Class hierarchy: :class:`UnaryFunction1D` > :class:`UnaryFunction1DVec3f`
   
   Base class for unary functions (functors) that work on
   :class:`Interface1D` and return a 3D vector.
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __init__(integration_type)
   
      Builds a unary 1D function using the integration method given as
      argument.
   
      :arg integration_type: An integration method.
      :type integration_type: :class:`IntegrationType`

   .. attribute:: integration_type

      The integration method.
      
      :type: :class:`IntegrationType`




.. class:: UnaryFunction1DVectorViewShape

   Class hierarchy: :class:`UnaryFunction1D` > :class:`UnaryFunction1DVectorViewShape`
   
   Base class for unary functions (functors) that work on
   :class:`Interface1D` and return a list of :class:`ViewShape`
   objects.
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __init__(integration_type)
   
      Builds a unary 1D function using the integration method given as
      argument.
   
      :arg integration_type: An integration method.
      :type integration_type: :class:`IntegrationType`

   .. attribute:: integration_type

      The integration method.
      
      :type: :class:`IntegrationType`




.. class:: UnaryFunction1DVoid

   Class hierarchy: :class:`UnaryFunction1D` > :class:`UnaryFunction1DVoid`
   
   Base class for unary functions (functors) working on
   :class:`Interface1D`.
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __init__(integration_type)
   
      Builds a unary 1D function using the integration method given as
      argument.
   
      :arg integration_type: An integration method.
      :type integration_type: :class:`IntegrationType`

   .. attribute:: integration_type

      The integration method.
      
      :type: :class:`IntegrationType`




.. class:: UnaryPredicate0D

   Base class for unary predicates that work on
   :class:`Interface0DIterator`.  A UnaryPredicate0D is a functor that
   evaluates a condition on an Interface0DIterator and returns true or
   false depending on whether this condition is satisfied or not.  The
   UnaryPredicate0D is used by invoking its __call__() method.  Any
   inherited class must overload the __call__() method.
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __call__(it)
   
      Must be overload by inherited classes.
   
      :arg it: The Interface0DIterator pointing onto the Interface0D at
         which we wish to evaluate the predicate.
      :type it: :class:`Interface0DIterator`
      :return: True if the condition is satisfied, false otherwise.
      :rtype: bool

   .. attribute:: name

      The name of the unary 0D predicate.
      
      :type: str




.. class:: UnaryPredicate1D

   Base class for unary predicates that work on :class:`Interface1D`.  A
   UnaryPredicate1D is a functor that evaluates a condition on a
   Interface1D and returns true or false depending on whether this
   condition is satisfied or not.  The UnaryPredicate1D is used by
   invoking its __call__() method.  Any inherited class must overload the
   __call__() method.
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __call__(inter)
   
      Must be overload by inherited classes.
   
      :arg inter: The Interface1D on which we wish to evaluate the predicate.
      :type inter: :class:`Interface1D`
      :return: True if the condition is satisfied, false otherwise.
      :rtype: bool

   .. attribute:: name

      The name of the unary 1D predicate.
      
      :type: str




.. class:: ViewEdge

   Class hierarchy: :class:`Interface1D` > :class:`ViewEdge`
   
   Class defining a ViewEdge.  A ViewEdge in an edge of the image graph.
   it connects two :class:`ViewVertex` objects.  It is made by connecting
   a set of FEdges.
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __init__(brother)
   
      Copy constructor.
   
      :arg brother: A ViewEdge object.
      :type brother: :class:`ViewEdge`

   .. method:: update_fedges()
   
      Sets Viewedge to this for all embedded fedges.


   .. attribute:: chaining_time_stamp

      The time stamp of this ViewEdge.
      
      :type: int


   .. attribute:: first_fedge

      The first FEdge that constitutes this ViewEdge.
      
      :type: :class:`FEdge`


   .. attribute:: first_viewvertex

      The first ViewVertex.
      
      :type: :class:`ViewVertex`


   .. attribute:: id

      The Id of this ViewEdge.
      
      :type: :class:`Id`


   .. attribute:: is_closed

      True if this ViewEdge forms a closed loop.
      
      :type: bool


   .. attribute:: last_fedge

      The last FEdge that constitutes this ViewEdge.
      
      :type: :class:`FEdge`


   .. attribute:: last_viewvertex

      The second ViewVertex.
      
      :type: :class:`ViewVertex`


   .. attribute:: nature

      The nature of this ViewEdge.
      
      :type: :class:`Nature`


   .. attribute:: occludee

      The shape that is occluded by the ViewShape to which this ViewEdge
      belongs to.  If no object is occluded, this property is set to None.
      
      :type: :class:`ViewShape`


   .. attribute:: qi

      The quantitative invisibility.
      
      :type: int


   .. attribute:: viewshape

      The ViewShape to which this ViewEdge belongs to.
      
      :type: :class:`ViewShape`




.. class:: ViewEdgeIterator

   Class hierarchy: :class:`Iterator` > :class:`ViewEdgeIterator`
   
   Base class for iterators over ViewEdges of the :class:`ViewMap` Graph.
   Basically the increment() operator of this class should be able to
   take the decision of "where" (on which ViewEdge) to go when pointing
   on a given ViewEdge.
   
   .. method:: __init__(begin=None, orientation=True)
   
      Builds a ViewEdgeIterator from a starting ViewEdge and its
      orientation.
   
      :arg begin: The ViewEdge from where to start the iteration.
      :type begin: :class:`ViewEdge` or None
      :arg orientation: If true, we'll look for the next ViewEdge among
         the ViewEdges that surround the ending ViewVertex of begin.  If
         false, we'll search over the ViewEdges surrounding the ending
         ViewVertex of begin.
      :type orientation: bool
   
   .. method:: __init__(brother)
   
      Copy constructor.
   
      :arg brother: A ViewEdgeIterator object.
      :type brother: :class:`ViewEdgeIterator`

   .. method:: change_orientation()
   
      Changes the current orientation.


   .. attribute:: begin

      The first ViewEdge used for the iteration.
      
      :type: :class:`ViewEdge`


   .. attribute:: current_edge

      The ViewEdge object currently pointed by this iterator.
      
      :type: :class:`ViewEdge`


   .. attribute:: object

      The ViewEdge object currently pointed by this iterator.
      
      :type: :class:`ViewEdge`


   .. attribute:: orientation

      The orientation of the pointed ViewEdge in the iteration.
      If true, the iterator looks for the next ViewEdge among those ViewEdges
      that surround the ending ViewVertex of the "begin" ViewEdge.  If false,
      the iterator searches over the ViewEdges surrounding the ending ViewVertex
      of the "begin" ViewEdge.
      
      :type: bool




.. class:: ViewMap

   Class defining the ViewMap.
   
   .. method:: __init__()
   
      Default constructor.

   .. method:: get_closest_fedge(x, y)
   
      Gets the FEdge nearest to the 2D point specified as arguments.
   
      :arg x: X coordinate of a 2D point.
      :type x: float
      :arg y: Y coordinate of a 2D point.
      :type y: float
      :return: The FEdge nearest to the specified 2D point.
      :rtype: :class:`FEdge`


   .. method:: get_closest_viewedge(x, y)
   
      Gets the ViewEdge nearest to the 2D point specified as arguments.
   
      :arg x: X coordinate of a 2D point.
      :type x: float
      :arg y: Y coordinate of a 2D point.
      :type y: float
      :return: The ViewEdge nearest to the specified 2D point.
      :rtype: :class:`ViewEdge`


   .. attribute:: scene_bbox

      The 3D bounding box of the scene.
      
      :type: :class:`BBox`




.. class:: ViewShape

   Class gathering the elements of the ViewMap (i.e., :class:`ViewVertex`
   and :class:`ViewEdge`) that are issued from the same input shape.
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __init__(brother)
   
      Copy constructor.
   
      :arg brother: A ViewShape object.
      :type brother: :class:`ViewShape`
   
   .. method:: __init__(sshape)
   
      Builds a ViewShape from an SShape.
   
      :arg sshape: An SShape object.
      :type sshape: :class:`SShape`

   .. method:: add_edge(edge)
   
      Adds a ViewEdge to the list of ViewEdge objects.
   
      :arg edge: A ViewEdge object.
      :type edge: :class:`ViewEdge`


   .. method:: add_vertex(vertex)
   
      Adds a ViewVertex to the list of the ViewVertex objects.
   
      :arg vertex: A ViewVertex object.
      :type vertex: :class:`ViewVertex`


   .. attribute:: edges

      The list of ViewEdge objects contained in this ViewShape.
      
      :type: List of :class:`ViewEdge` objects


   .. attribute:: id

      The Id of this ViewShape.
      
      :type: :class:`Id`


   .. attribute:: library_path

      The library path of the ViewShape.
      
      :type: str, or None if the ViewShape is not part of a library


   .. attribute:: name

      The name of the ViewShape.
      
      :type: str


   .. attribute:: sshape

      The SShape on top of which this ViewShape is built.
      
      :type: :class:`SShape`


   .. attribute:: vertices

      The list of ViewVertex objects contained in this ViewShape.
      
      :type: List of :class:`ViewVertex` objects




.. class:: ViewVertex

   Class hierarchy: :class:`Interface0D` > :class:`ViewVertex`
   
   Class to define a view vertex.  A view vertex is a feature vertex
   corresponding to a point of the image graph, where the characteristics
   of an edge (e.g., nature and visibility) might change.  A
   :class:`ViewVertex` can be of two kinds: A :class:`TVertex` when it
   corresponds to the intersection between two ViewEdges or a
   :class:`NonTVertex` when it corresponds to a vertex of the initial
   input mesh (it is the case for vertices such as corners for example).
   Thus, this class can be specialized into two classes, the
   :class:`TVertex` class and the :class:`NonTVertex` class.

   .. method:: edges_begin()
   
      Returns an iterator over the ViewEdges that goes to or comes from
      this ViewVertex pointing to the first ViewEdge of the list. The
      orientedViewEdgeIterator allows to iterate in CCW order over these
      ViewEdges and to get the orientation for each ViewEdge
      (incoming/outgoing).
   
      :return: An orientedViewEdgeIterator pointing to the first ViewEdge.
      :rtype: :class:`orientedViewEdgeIterator`


   .. method:: edges_end()
   
      Returns an orientedViewEdgeIterator over the ViewEdges around this
      ViewVertex, pointing after the last ViewEdge.
   
      :return: An orientedViewEdgeIterator pointing after the last ViewEdge.
      :rtype: :class:`orientedViewEdgeIterator`


   .. method:: edges_iterator(edge)
   
      Returns an orientedViewEdgeIterator pointing to the ViewEdge given
      as argument.
   
      :arg edge: A ViewEdge object.
      :type edge: :class:`ViewEdge`
      :return: An orientedViewEdgeIterator pointing to the given ViewEdge.
      :rtype: :class:`orientedViewEdgeIterator`


   .. attribute:: nature

      The nature of this ViewVertex.
      
      :type: :class:`Nature`




.. class:: orientedViewEdgeIterator

   Class hierarchy: :class:`Iterator` > :class:`orientedViewEdgeIterator`
   
   Class representing an iterator over oriented ViewEdges around a
   :class:`ViewVertex`.  This iterator allows a CCW iteration (in the image
   plane).  An instance of an orientedViewEdgeIterator can only be
   obtained from a ViewVertex by calling edges_begin() or edges_end().
   
   .. method:: __init__()
   
      Default constructor.
   
   .. method:: __init__(iBrother)
   
      Copy constructor.
   
      :arg iBrother: An orientedViewEdgeIterator object.
      :type iBrother: :class:`orientedViewEdgeIterator`

   .. attribute:: object

      The oriented ViewEdge (i.e., a tuple of the pointed ViewEdge and a boolean
      value) currently pointed to by this iterator. If the boolean value is true,
      the ViewEdge is incoming.
      
      :type: (:class:`ViewEdge`, bool)




