.. |socket-multi| image:: /images/editors/logic_nodes/lne-socket-multi.png

.. |socket-bool| image:: /images/editors/logic_nodes/lne-socket-bool.png

.. |socket-dict| image:: /images/editors/logic_nodes/lne-socket-dict.png

.. |socket-float| image:: /images/editors/logic_nodes/lne-socket-float.png

.. |socket-integer| image:: /images/editors/logic_nodes/lne-socket-integer.png

.. |socket-list| image:: /images/editors/logic_nodes/lne-socket-list.png

.. |socket-material| image:: /images/editors/logic_nodes/lne-socket-material.png

.. |socket-object| image:: /images/editors/logic_nodes/lne-socket-object.png

.. |socket-sound| image:: /images/editors/logic_nodes/lne-socket-sound.png

.. |socket-string| image:: /images/editors/logic_nodes/lne-socket-string.png

.. |socket-vector| image:: /images/editors/logic_nodes/lne-socket-vector.png

.. |socket-file| image:: /images/editors/logic_nodes/lne-socket-file.png

.. |socket-geometry| image:: /images/editors/logic_nodes/lne-socket-geometry.png

.. _lne-additional_details:

==============================
Additional Details
==============================

N-panel Tabs
++++++++++++++++++++++++++++++

After new *logic tree* is added, :kbd:`N`-panel includes:

-  ``Group`` - add a group socket or a panel;

-  ``Node`` - set node name in ``Label`` field, change color, and see Properties;

-  ``Tool`` - active tool for i.e. selection;

-  ``View`` - manage :ref:`Annotations <fps-annotations>`;

-  ``Dashboard`` - main access point to Logic Node Editor functionality - apply logic tree to node, use a tree template, see properties;

-  ``Custom Nodes`` - add user created custom nodes;

-  ``Help & Documentation`` - update ``Uplogic`` module, access UPBGE manual and API.

RMB Context
++++++++++++++++++++++++++++++

With mouse inside Logic Node Editor, :kbd:`RMB` context has two versions:

1. No node selected - add, paste, find node, cut and mute links; for a fast workflow, use the hotkeys.

.. figure:: /images/editors/logic_nodes/15-rmb_no_selection.png
   :figwidth: 40%
   :align: center

   RMB context with no node selected

2. Node selected - copy, paste etc. Use the hotkeys, if you dare.

.. figure:: /images/editors/logic_nodes/16-rmb_node_selected.png
   :figwidth: 65%
   :align: center

   RMB context with node selected

Put some *Logic Nodes* into the editor (any will do for testing), connect them, and:

-  :kbd:`LMB-select` them > :kbd:`Shift-J` to put them all into a frame; keep ``Frame`` selected > ``Node`` tab > add text into ``Label`` field > :kbd:`Enter`.

-  :kbd:`Ctrl-RMB-drag` over a noodle (aka *link*) to delete it/cut the link.

-  Also useful for learning/testing/debugging are :kbd:`M` > mute nodes, and for final packed design :kbd:`Ctrl-H` > hide unused sockets, or even :kbd:`H` > collapse the nodes. 

Test other hotkeys as per figures above.

Socket Type by Colors
++++++++++++++++++++++++++++++

.. hlist::
   :columns: 3

   -  |socket-multi| - :socket:`multi`

   -  |socket-bool| - :socket:`bool`
   
   -  |socket-dict| - :socket:`dict`
   
   -  |socket-float| - :socket:`float`
   
   -  |socket-integer| - :socket:`integer`
   
   -  |socket-list| - :socket:`list`
   
   -  |socket-material| - :socket:`material` 
   
   -  |socket-object| - :socket:`object`
   
   -  |socket-sound| - :socket:`sound`
   
   -  |socket-string| - :socket:`string`
   
   -  |socket-vector| - :socket:`vector`
   
   -  |socket-file| - :socket:`file`

   -  |socket-geometry| - :socket:`geometry`
