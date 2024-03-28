.. _2d_scroller-player_movement:

==============================
2. Player Movement
==============================

From the game logic perspective, player can do few movements:

-  It can walk/run, either to the left, or to the right, relative to the screen space.

-  It can jump up.

-  It can fall off the rock into the void.

For this reason, we need to know what state/movement a player is in. We need properties to keep those states updated while the game is running.

-  With player selected, first add :menuselection:`Properties > Game > Game Properties > Add Game Property`, name it ``running``, leave default type ``Float``, and also default value ``0.0``. Save often.

-  In *Logic Node Editor*, add new node tree, name it ``player_2d_movement``, and set 'Fake User'.

-  Next add :ln:`Get Object Property`, ``Object`` > ``player``, and ``Property`` > ``running``.

-  Connect above node ``Property Value`` socket into :ln:`Math` > ``A`` socket, set ``B`` to ``0.20``, set ``Operation`` > ``Multiply``.

-  Connect :ln:`Math` ``Result`` > :ln:`Combine XYZ` ``Y`` socket, leave ``X`` and ``Z`` at default value (``0.0``).

-  Below :ln:`Combine XYZ` node add :ln:`Get Attribute - World Position`, and ``Object`` > ``player``.

-  Next add :ln:`Vector Math`, connect :ln:`Combine XYZ` ``Vector`` > ``Vector 1``, :ln:`World Position` > ``Vector 2``, ``Operation`` > ``Add``.

-  Above :ln:`Vector Math` add :ln:`On Update`, next :ln:`Rotate To`, connect ``Out`` > ``Condition`` (*red* to *red* socket), and ``Result`` > ``Target`` (*blue* to *blue* socket).

-  Next add :ln:`Walk`, and above it :ln:`Set Attribute - World Position`; :ln:`Rotate To` ``Done`` > ``Condition`` - both nodes, :ln:`Combine XYZ` ``Vector`` > :ln:`Walk` ``Vector``, uncheck :ln:`Set World Position` ``Y`` and ``Z``, both nodes ``Object`` > ``player``, also uncheck :ln:`Walk` ``Local``.

-  For organizing purpose, select all > :kbd:`Ctrl-J` to put all into a frame, with frame still selected > :menuselection:`N-panel > Node > Node > Label` > ``Change player rotation based on 'running' property``.

This part is done.

.. figure:: /images/tutorials/introducing_logic_nodes/2d_side_scroller/ln-2d-player_movement-1.png
   :figwidth: 100%
   :align: center

   Player movement setup - rotation part

Next we add collision detection - if player falls into the void, when it collides with *Bedrock* object, it will be 'teleported' back to the beginning. This is the sole purpose of Bedrock object.

-  First we need to add a property to *Bedrock* object > select it in :menuselection:`Outliner`, then :menuselection:`Add Game Property`, same as we did above for the player; name it ``bedrock``, leave the rest as default.

.. figure:: /images/tutorials/introducing_logic_nodes/2d_side_scroller/ln-2d-bedrock.png
   :figwidth: 60%
   :align: center

   Bedrock property

-  In *Logic Node Editor*, under *Player movement* frame, add :ln:`Collision`, and :ln:`Set Attribute - World Position` - it makes sense, doesn't it, because when player will fall into the void, and touch (collide) with the *Bedrock*, we will reset its position, otherwise player would keep falling deeper and deeper into the void - forever.

-  Set :ln:`Collision` ``Property`` > ``bedrock``, check ``Continuous``, connect ``On Collision`` output to :ln:`Set World Position` > ``Condition``, and last node ``Object`` > ``player``.

Done. Simple as that.

.. figure:: /images/tutorials/introducing_logic_nodes/2d_side_scroller/ln-2d-player_movement-2.png
   :figwidth: 60%
   :align: center

   Reset player position nodes setup

In case you need to 'teleport' player somewhere else than at the beginning, change :ln:`Set World Position` ``Value`` fields (from top to bottom - X, Y, Z). This is used in case when player manages to advance to some 'checkpoint' inside the level, but it fails to make it to the end - it is 'teleported' to last 'checkpoint'.

If you run the game, not much will happen - the game is not yet functional. We need to add more functionality to the player. And ``Apply To Selected`` all logic trees to player, of course.
