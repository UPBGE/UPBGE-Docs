.. _2d_scroller-camera_movement:

==============================
1. Camera Movement
==============================

In 2d scroller games, camera is usually showing player from the side, and it moves perpendicularly together with the player. If you press :kbd:`Numpad 0` (zero - camera perspective), or :kbd:`Numpad 3`, you should see player from same perspective (press :kbd:`Numpad ,` (comma) to focus the player).

-  Add a new logic tree, name it 'player_2d_camera', and set 'Fake User'.

-  Next add, from left to right, :ln:`Get World Position`, set 'player' as Object - it will get player's position, so camera knows where to go, following the player.

-  Add :ln:`Separate XYZ` vector node, to separate 3D vector into separate XYZ coordinates from 'World Position'; connect the sockets.

-  Under above node, add 2 :ln:`Float` nodes - one will set camera distance from player, the other will set following speed. Select both 'Float' nodes, hit :kbd:`Ctrl-J` - this will group both nodes into a frame, for better organization. Rename top node to 'camera distance', and set value to i.e. ``30.0``; rename bottom one to 'slow camera', set value to i.e. ``0.15`` (with node selected - side :menuselection:`N-panel > Node > Label`). Also, with frame selected, rename it i.e. into 'camera custom', and also change frame color (below 'Label').

-  Next add :ln:`Math` node, set operation to ``Add``, connect ``X`` coordinate from :ln:`Separate XYZ` into ``A`` socket, and ``Float`` output socket from :ln:`camera distance` into ``B`` socket. This will get player's ``X`` position (horizontal) and set camera's ``X`` position accordingly.

-  Add another :ln:`Math` node under the first one, connect ``Z`` coordinate from :ln:`Separate XYZ` into ``A`` socket, and set ``B`` value to ``1.0``.

- Add :ln:`Combine XYZ` node, connect top :ln:`Math` node into ``X``, bottom :ln:`Math` node into ``Z``, and ``Y`` socket from :ln:`Separate XYZ` directly into ``Y`` socket.

-  Above first :ln:`Math` node, add :ln:`Active Camera`, next another :ln:`Get World Position` above :ln:`Combine XYZ`, and connect ``Camera`` as Object. 

-  Next add :ln:`Vector Math` node, set 'Operation' to ``Add``, connect :ln:`Get World Position` into top ``Vector 1`` socket, :ln:`Combine XYZ` into ``Vector 2`` socket.

-  Next add another :ln:`Vector Math`, set 'Operation' to ``Scale``, connect previous node into ``Vector 1``, and :ln:`slow follow` into ``Scale``.

-  Add :ln:`On Update` above last node, next :ln:`Set World Position` node; connect :ln:`On Update` into ``Condition`` socket, :ln:`Active Camera` as Object, and last :ln:`Vector Math` into ``Value`` socket.

-  With 'player' selected, :menuselection:`Apply To Selected`.

Done.

.. figure:: /images/tutorials/introducing_logic_nodes/2d_side_scroller/ln-2d-player_camera.png
   :figwidth: 100%
   :align: center

   2D player camera nodes setup
