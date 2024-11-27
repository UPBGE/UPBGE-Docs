.. figure:: /images/logic_nodes/math/ln-tween_value.png
   :align: right
   :width: 245
   :alt: Tween Value Node

.. _ln-tween_value:

==============================
Tween Value
==============================

Move a value along a given curve over a set duration. This node can be used to map a linear value of 0-1 to a curve.

Add Point
   :kbd:`LMB` on curve.

Delete Point
   :kbd:`LMB`-select a point, below the graph is a row with point settings - click :menuselection:`X` to delete.

Change Point Location
   :kbd:`LMB`-drag the point to desired location on graph.

Point Settings
   In a row below the graph, click-select icon to change handle type, or change its position values (X Y coordinates).

Graph Options
   Above the graph are option icons - zoom in/out, use *Clipping* (will clamp output values between 0 and 1), use dropdown menu to *Reset View*, *Reset Curve* etc.

Parameters
++++++++++++++++++++++++++++++

Type
   A value type to process.

On Demand
   Automatically move right on the curve if the "Result" socket is being accessed.

Inputs
++++++++++++++++++++++++++++++

Forward
   Move right on the curve.

Back
   Move left on the curve.

From
   Starting tween value.

To
   Ending tween value.

Duration
   Duration of Tweening in seconds.

Outputs
++++++++++++++++++++++++++++++

Done
   *True* if node performed successfully, else *False*.

Reached
   *True* if the factor is either 0 or 1, else *False*.

Result
   Resulting tween value.

Factor
   Current X-Axis position.
