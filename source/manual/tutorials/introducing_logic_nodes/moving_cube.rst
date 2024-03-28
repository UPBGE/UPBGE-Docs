.. _ln-moving_cube:

==============================
Moving A Cube
==============================

See :ref:`logic_node_editor-index` for *node* basics.

Moving an object requires input from user, processing this input, and applying movement to object. To run the game, a *Camera* object is also required.

- Add 4 :ref:`ln-keyboard_key` nodes, and assign :kbd:`A` for left, :kbd:`D` for right, :kbd:`W` for forward, and :kbd:`S` for backward movement.

- Add 2 :ref:`ln-math` nodes, set both to ``Subtract``, and connect 2 above nodes to each :ln:`Math` node, i.e. :kbd:`A` and :kbd:`D` nodes to one :ln:`Math` node, :kbd:`W` and :kbd:`S` to the other :ln:`Math` node.

- Next add a :ref:`ln-combine_xy`, connect above :ln:`Math` nodes to ``X`` and ``Y`` input sockets.

- Connect to :ref:`ln-vector_math` ``Vector 1`` socket, set ``Normalize`` property from dropdown menu.

- Connect the ``Result`` output to another :ln:`Vector Math` node > ``Vector 1`` socket. Set property to ``Scale``.
   
   .. tip::
      Either add new node, or select existing one > :kbd:`Shift-D` to duplicate > move with mouse > :kbd:`LMB` to 'land' it. Keep mouse cursor close to the node while duplicating.

- Add :ref:`ln-float` node, set value to ``0.1``, and connect it to the last :ln:`Vector Math` node, ``Scale`` input. This will determine movement *speed* for the object.

- Add :ref:`ln-apply_movement` node; output from above :ln:`Vector Math` node goes into ``Vector`` input. Check ``Local`` box, and in the *Object* input select an object to move, i.e. *Cube*.

- Last, add :ref:`ln-on_update` node, and connect to above :ln:`Apply Movement` > ``Condition`` socket. 

Alright, now we apply this *logic tree* to an object.

- Select (or add) any object, in *Logic Nodes Editor* select all nodes (:kbd:`A`), and in :menuselection:`N-panel > Dashboard > Administration` click :menuselection:`Apply To Selected` button.

If the game does not run as expected, also click :menuselection:`Force Compile`.

Logic tree should look like this:

.. figure:: /images/tutorials/introducing_logic_nodes/15_move_object.png
   :figwidth: 100%
   :align: center

   Logic tree for moving an object with keyboard

Run the game, use the keyboard keys we set in first step to move the Cube.

If object is moving in wrong direction, either swap keys in :ln:`Keyboard Key` nodes (i.e. ``A`` > ``D`` and ``D`` > ``A``), or swap ``A`` and ``B`` inputs in :ln:`Math` node.
