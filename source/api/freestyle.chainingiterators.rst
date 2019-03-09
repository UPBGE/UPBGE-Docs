Freestyle Chaining Iterators (freestyle.chainingiterators)
==========================================================

.. module:: freestyle.chainingiterators

This module contains chaining iterators used for the chaining
operation to construct long strokes by concatenating feature edges
according to selected chaining rules.  The module is also intended to
be a collection of examples for defining chaining iterators in Python.

.. class:: ChainPredicateIterator

   Class hierarchy: :class:`freestyle.types.Iterator` >
   :class:`freestyle.types.ViewEdgeIterator` >
   :class:`freestyle.types.ChainingIterator` >
   :class:`ChainPredicateIterator`
   
   A "generic" user-controlled ViewEdge iterator.  This iterator is in
   particular built from a unary predicate and a binary predicate.
   First, the unary predicate is evaluated for all potential next
   ViewEdges in order to only keep the ones respecting a certain
   constraint.  Then, the binary predicate is evaluated on the current
   ViewEdge together with each ViewEdge of the previous selection.  The
   first ViewEdge respecting both the unary predicate and the binary
   predicate is kept as the next one.  If none of the potential next
   ViewEdge respects these two predicates, None is returned.
   
   .. method:: __init__(upred, bpred, restrict_to_selection=True, restrict_to_unvisited=True, begin=None, orientation=True)
   
      Builds a ChainPredicateIterator from a unary predicate, a binary
      predicate, a starting ViewEdge and its orientation.
   
      :arg upred: The unary predicate that the next ViewEdge must satisfy.
      :type upred: :class:`freestyle.types.UnaryPredicate1D`
      :arg bpred: The binary predicate that the next ViewEdge must
         satisfy together with the actual pointed ViewEdge.
      :type bpred: :class:`freestyle.types.BinaryPredicate1D`
      :arg restrict_to_selection: Indicates whether to force the chaining
         to stay within the set of selected ViewEdges or not.
      :type restrict_to_selection: bool
      :arg restrict_to_unvisited: Indicates whether a ViewEdge that has
         already been chained must be ignored ot not.
      :type restrict_to_unvisited: bool
      :arg begin: The ViewEdge from where to start the iteration.
      :type begin: :class:`freestyle.types.ViewEdge` or None
      :arg orientation: If true, we'll look for the next ViewEdge among
         the ViewEdges that surround the ending ViewVertex of begin.  If
         false, we'll search over the ViewEdges surrounding the ending
         ViewVertex of begin.
      :type orientation: bool
   
   .. method:: __init__(brother)
   
      Copy constructor.
   
      :arg brother: A ChainPredicateIterator object.
      :type brother: :class:`ChainPredicateIterator`



.. class:: ChainSilhouetteIterator

   Class hierarchy: :class:`freestyle.types.Iterator` >
   :class:`freestyle.types.ViewEdgeIterator` >
   :class:`freestyle.types.ChainingIterator` >
   :class:`ChainSilhouetteIterator`
   
   A ViewEdge Iterator used to follow ViewEdges the most naturally.  For
   example, it will follow visible ViewEdges of same nature.  As soon, as
   the nature or the visibility changes, the iteration stops (by setting
   the pointed ViewEdge to 0).  In the case of an iteration over a set of
   ViewEdge that are both Silhouette and Crease, there will be a
   precedence of the silhouette over the crease criterion.
   
   .. method:: __init__(restrict_to_selection=True, begin=None, orientation=True)
   
      Builds a ChainSilhouetteIterator from the first ViewEdge used for
      iteration and its orientation.
   
      :arg restrict_to_selection: Indicates whether to force the chaining
         to stay within the set of selected ViewEdges or not.
      :type restrict_to_selection: bool
      :arg begin: The ViewEdge from where to start the iteration.
      :type begin: :class:`freestyle.types.ViewEdge` or None
      :arg orientation: If true, we'll look for the next ViewEdge among
         the ViewEdges that surround the ending ViewVertex of begin.  If
         false, we'll search over the ViewEdges surrounding the ending
         ViewVertex of begin.
      :type orientation: bool
   
   .. method:: __init__(brother)
   
      Copy constructor.
   
      :arg brother: A ChainSilhouetteIterator object.
      :type brother: :class:`ChainSilhouetteIterator`



.. class:: pyChainSilhouetteIterator

   Natural chaining iterator that follows the edges of the same nature
   following the topology of objects, with decreasing priority for
   silhouettes, then borders, then suggestive contours, then all other edge
   types.  A ViewEdge is only chained once.

   .. method:: init()

   .. method:: traverse(iter)



.. class:: pyChainSilhouetteGenericIterator

   Natural chaining iterator that follows the edges of the same nature
   following the topology of objects, with decreasing priority for
   silhouettes, then borders, then suggestive contours, then all other
   edge types.
   
   .. method:: __init__(self, stayInSelection=True, stayInUnvisited=True)
   
      Builds a pyChainSilhouetteGenericIterator object.
   
      :arg stayInSelection: True if it is allowed to go out of the selection
      :type stayInSelection: bool
      :arg stayInUnvisited: May the same ViewEdge be chained twice
      :type stayInUnvisited: bool

   .. method:: init()

   .. method:: traverse(iter)



.. class:: pyExternalContourChainingIterator

   Chains by external contour

   .. method:: checkViewEdge(ve, orientation)

   .. method:: init()

   .. method:: traverse(iter)



.. class:: pySketchyChainSilhouetteIterator

   Natural chaining iterator with a sketchy multiple touch.  It chains the
   same ViewEdge multiple times to achieve a sketchy effect.
   
   .. method:: __init__(self, nRounds=3,stayInSelection=True)
   
      Builds a pySketchyChainSilhouetteIterator object.
   
      :arg nRounds: Number of times every Viewedge is chained.
      :type nRounds: int
      :arg stayInSelection: if False, edges outside of the selection can be chained.
      :type stayInSelection: bool

   .. method:: init()

   .. method:: make_sketchy(ve)

      Creates the skeychy effect by causing the chain to run from
      the start again. (loop over itself again)

   .. method:: traverse(iter)



.. class:: pySketchyChainingIterator

   Chaining iterator designed for sketchy style. It chains the same
   ViewEdge several times in order to produce multiple strokes per
   ViewEdge.

   .. method:: init()

   .. method:: traverse(iter)



.. class:: pyFillOcclusionsRelativeChainingIterator

   Chaining iterator that fills small occlusions
   
   .. method:: __init__(self, percent)
   
      Builds a pyFillOcclusionsRelativeChainingIterator object.
   
      :arg percent: The maximal length of the occluded part, expressed
          in a percentage of the total chain length.
      :type percent: float

   .. method:: init()

   .. method:: traverse(iter)



.. class:: pyFillOcclusionsAbsoluteChainingIterator

   Chaining iterator that fills small occlusions
   
   .. method:: __init__(self, length)
   
      Builds a pyFillOcclusionsAbsoluteChainingIterator object.
   
      :arg length: The maximum length of the occluded part in pixels.
      :type length: int

   .. method:: init()

   .. method:: traverse(iter)



.. class:: pyFillOcclusionsAbsoluteAndRelativeChainingIterator

   Chaining iterator that fills small occlusions regardless of the
   selection.
   
   .. method:: __init__(self, percent, l)
   
      Builds a pyFillOcclusionsAbsoluteAndRelativeChainingIterator object.
   
      :arg percent: The maximal length of the occluded part as a
          percentage of the total chain length.
      :type percent: float
      :arg l: Absolute length.
      :type l: float

   .. method:: init()

   .. method:: traverse(iter)



.. class:: pyFillQi0AbsoluteAndRelativeChainingIterator

   Chaining iterator that fills small occlusions regardless of the
   selection.
   
   .. method:: __init__(self, percent, l)
   
      Builds a pyFillQi0AbsoluteAndRelativeChainingIterator object.
   
      :arg percent: The maximal length of the occluded part as a
          percentage of the total chain length.
      :type percent: float
      :arg l: Absolute length.
      :type l: float

   .. method:: init()

   .. method:: traverse(iter)



.. class:: pyNoIdChainSilhouetteIterator

   Natural chaining iterator that follows the edges of the same nature
   following the topology of objects, with decreasing priority for
   silhouettes, then borders, then suggestive contours, then all other edge
   types.  It won't chain the same ViewEdge twice.
   
   .. method:: __init__(self, stayInSelection=True)
   
      Builds a pyNoIdChainSilhouetteIterator object.
   
      :arg stayInSelection: True if it is allowed to go out of the selection
      :type stayInSelection: bool

   .. method:: init()

   .. method:: traverse(iter)



