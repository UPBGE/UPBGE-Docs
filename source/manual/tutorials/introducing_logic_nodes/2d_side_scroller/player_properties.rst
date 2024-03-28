.. _2d_scroller-player_properties:

==============================
3. Player Properties
==============================

Previously we added a single property to the player - ``running``. In this chapter we will add some more properties, and use them with the game logic.

First, let's add game properties to player.

-  :menuselection:`Add Game Property` > ``grounded`` > ``Float`` > ``0.0`` (default values), ``falling`` > ``Timer`` > ``0.0``, ``jumped`` > ``Boolean`` > unchecked, ``landed`` > ``Boolean`` > unchecked, ``start_falling`` > ``Boolean`` > unchecked.

.. figure:: /images/tutorials/introducing_logic_nodes/2d_side_scroller/ln-2d-player_properties-added_properties.png
   :figwidth: 60%
   :align: center

   Added player game properties

-  Next we add new logic tree, name it ``player_2d_properties``. Be kindly informed, this logic tree is a bit larger than previous ones. Did you remember to set 'Fake User'?

.. tip::
   It is recommended to switch to 'fullscreen area/window' mode - mouse over *Logic Node Editor* > :kbd:`Ctrl-Space` (toggle fullscreen).

From left to right:

-  First we add :ln:`Float`, set its value ``Float`` > ``0.1``. If player is on the ground, this value will be used.

-  Below it add :ln:`Get Physics Info`, ``Object`` > ``player``. This node will provide physics data for player.

-  Next add :ln:`Value Switch`, connect :ln:`Float` to top ``Type/Value`` input (second input socket from top), set bottom ``Type/Value`` to ``Float`` > ``0.03``, and :ln:`Get Physics Info` ``On Ground`` > ``A if True, else B`` (top conditional input).

.. figure:: /images/tutorials/introducing_logic_nodes/2d_side_scroller/ln-2d-player_properties-1.png
   :figwidth: 60%
   :align: center

   Player properties - first chunk of nodes

Approximately four node heights higher, we will start second nodes chunk. From now on, unless indicated otherwise, all ``Object`` fields should be set to ``player``, and this will not be indicated for each node explicitly. Also previous node will be not named, just its output, for a sake of simplicity, except in case of ambiguity. If unclear, refer to relevant image, usually below the text.

-  Add :ln:`Get Object Property`, ``Property`` > ``start_falling``.

-  Add :ln:`On Value Changed To`, ``Property Value`` > ``Value``, ``Bool`` checked.

-  Add :ln:`Set Object Property`, ``Result`` > ``Condition``, ``Property`` > ``falling``, ``Float`` > ``0.0``.

This is one row. Below it add another row.

-  :ln:`On Value Changed To`, ``Bool`` checked > ``Value`` of :ln:`On Value Changed`, ``If Changed`` > ``Condition`` of :ln:`Set Object Property`, ``Property`` > ``landed``, ``New`` > bottom most input socket.

Copy last row one row below.

-  :ln:`On Value Changed To` ``Bool`` uncheck, :ln:`Set Object Property` ``Property`` > ``start_falling``.

One row lower:

-  :ln:`Get Object Property` ``Property`` > ``Grounded``, below it add :ln:`Value Switch`, bottom field ``Float`` > ``0.0``, next one above ``Float`` > ``1.0``, connect ``On Ground`` > ``A if True, else B``.

-  Add :ln:`Interpolate`, ``Property Value`` > ``From``, ``Result`` > ``To``, ``Factor`` > ``0.3``.

-  Above :ln:`Interpolate` add :ln:`On Update`, ``Out`` > ``Condition`` of :ln:`Set Object Property`, ``Property`` > ``Grounded``.

-  Also connect ``On Ground`` > *On take off* & *When landed* (left-most, see image below) ``Value`` sockets. Use *Reroute* utility, if you desire so.

.. tip::
   Using *Reroute* utility

   :kbd:`Shift-RMB` over existing noodle, and you get *Reroute* socket for free. :kbd:`LMB` the noodle from it just the same as you would from output socket, drag it to input socket. To move it around - :kbd:`LMB`-select it, :kbd:`G` to grab, move with mouse, :kbd:`LMB` to 'land it' wherever you wish. :kbd:`Shift-Tab` to toggle grid snapping.
   
.. figure:: /images/tutorials/introducing_logic_nodes/2d_side_scroller/ln-2d-player_properties-2.png
   :figwidth: 100%
   :align: center

   Second chunk of nodes

One but last chunk. This one is for player walking. Same as before - from left to right, below existing noodle soup, sorry, group.

-  Add 2 x :ln:`Keyboard Key`, one below the other, :kbd:`A` for left, :kbd:`D` for right movement.

-  :ln:`Gate`, ``Gate Type`` > ``Or``, connect the red dots.

-  Below it, add :ln:`Value Switch`, bottom field ``Float`` > ``1.0``, field above ``Float`` > ``-1.0``, ``If Pressed`` ``A`` > ``A if True, else B``.

-  Add/duplicate :ln:`Value Switch`, :ln:`Gate` ``Result`` > ``A if True, else B``, ``Result`` > next (middle) socket, bottom socket ``Float`` > ``0.0``.

-  Above last node add :ln:`Get Object Property`, ``Property`` > ``running``.

-  Next :ln:`Interpolate`, ``Property Value`` > ``From``, ``Result`` > ``To``, first :ln:`Value Switch`` > ``Factor``.

-  At the end, :ln:`Set Object Property`, from above :ln:`On Update` > ``Condition``, ``Property`` > ``running``, ``Value`` > bottom input socket.

.. figure:: /images/tutorials/introducing_logic_nodes/2d_side_scroller/ln-2d-player_properties-3.png
   :figwidth: 100%
   :align: center

   One-but-last chunk of nodes

Ignore left yellow arrow in above image, this connection is not from ``On Ground``.

And the last chunk, this one for jumping.

-  :ln:`Keyboard Key`, ``Space`` for jumping.

-  :ln:`Gate`, above :ln:`Get Physics Info` ``On Ground`` > ``Condition A``, ``If Pressed`` > ``Condition B``.

-  :ln:`Jump`, ``Result`` > ``Condition``.

-  :ln:`On Value Changed`, ``Done`` > ``Value``.

-  Yes, last one, :ln:`Set Object Property`, ``If Changed`` > ``Condition``, ``New`` > bottom-most input socket.

Yes, finally, we are done with this logic tree.

.. figure:: /images/tutorials/introducing_logic_nodes/2d_side_scroller/ln-2d-player_properties-4.png
   :figwidth: 100%
   :align: center

   The last chunk

Next we add player animations, so it will look like it is walking.
