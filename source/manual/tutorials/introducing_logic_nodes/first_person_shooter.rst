.. _lntut-first_person_camera:

==============================
First Person Shooter
==============================

In this tutorial we will:

-  Open .blend file with level assets - barrels and cubes, a brick walls, and a player with camera;

-  Use *Logic Nodes* to add :kbd:`W S A D` movement and a jump with some extras;

-  Upgrade with *Logic Nodes* into a FPS game;

.. figure:: /images/tutorials/introducing_logic_nodes/ln-fps-annotations.png
   :figwidth: 45%
   :align: right

   Placement options for Annotation tool

We will also learn few handy shortcuts on-the-go. Shall we?

Download/open :download:`level with assets </blends/logic_nodes/fps_ln_tutorial.blend>` .blend file. Follow the instructions precisely. :)

.. _fps-annotations:

-  :kbd:`Shift-Space` > :kbd:`D` for on-screen scribble tool, called *Annotation* in blenderland.

Annotation tool is useful for quick sketch, storyboard, and transferring ideas to collaborators. Also for annotations. He he he. Try all three :menuselection:`Placement` options for *Annotation* tool, rotate 3D viewport in-between, to see different placements of your scribbles. Go to :menuselection:`N-panel > View > Annotations` and select individual colors to be able to erase them. Or click :menuselection:`X` to delete all at once quickly. 

Ok, enough chit-chat - let's fight!

.. figure:: /images/tutorials/introducing_logic_nodes/ln-fps-player_hierarchy.png
   :figwidth: 50%
   :align: right

   Player as parent of many children

In :ref:`gs-outliner_editor` top > search for ``Player``.

Take a look of the *level* objects, particularly the hierarchy of *Player* object. Below *Player* object there is a bunch of other objects, being a *children* of *Player*, our main *Parent* object. Wherever *Player* goes, all children will follow. Also take a look at :ref:`gs-properties_editor` - under *Object* tab (orange square) there are *Relations* and *Collections* sub-panels, and close to the bottom, a *Viewport Display* sub-panel - under *Display As* a :menuselection:`Wire` is selected, and this is why *Player* looks underfed, sorry, wireframed. Since during the gameplay the *Player* is actually not visible, this will save some computer power. Not much though. :)

Of our main interest is a ``Head`` object, which is of type *Empty* object - those are commonly used as *Parent* object. In our case, *Head* is a parent of ``Camera`` object - this is the "eyes" of our player. No camera - no image on our screen.

Next, under the *Camera*, there is a ``Gun`` object, and this one has an ``Animation`` object with *Action* assigned to it.

Those are main building blocks of the game development, which we will incorporate into *Logic Nodes* workflow. Let the party begin!

Delete ``Text`` object (it was showing > :kbd:`W` to exit Annotation tool), we do not need it. Switch to *Logic Nodes* workspace (top-most header). Arrange the editors as you see fit, the one we will use most is *Logic Node Editor*.

.. tip::
   Both game and 3D model development require use of multiple editors at once. This can clutter the screen, particularly small one, quickly. To remedy this, few workflows are at our disposal.

   1. Dedicate each workspace, like default Blender startup file. In this case there are *workspaces*, which can be switched by clicking top-most header, in our example:

      :menuselection:`Layout | Logic Nodes | Animation | Scripting`

      There is also :menuselection:`+` tab, if you want to add another workspace. And you can assign hotkeys for switching previous/next workspace: :menuselection:`Edit > Preferences > Keymap` - search for ``Screen > Cycle Workspace``. Assign 2 keyboard keys, one for *previous* and one for *next* workspace.

   I trust you can figure out how to delete a workspace by yourself.

   2. Use Blender/UPBGE handy shortcut, :kbd:`Ctrl-Space`, which will toggle-maximize the editor window under the mouse cursor. This was a preferred workflow of now late Johnny Maccarony, world-known heavy consumer of *Logic Node noodles*.

In :ref:`Logic Node Editor <logic_node_editor-index>`, first create new logic tree, click ``Logic Node Editor``, rename to ``player``, and mark :ref:`dbl-protected` (Fake User); next add basic movement nodes, same as for :ref:`ln-moving_cube` chapter.

-  Add 5 :ref:`ln-keyboard_key` nodes, assign :kbd:`D A W S` keys for right/left and forward/backward movement, and :kbd:`Space` for jumping.

-  Add 2 :ref:`ln-math` nodes and connect with above 4 movement nodes.

-  Add :ref:`ln-apply_force` node, connect remaining :ln:`Keyboard Key` node ``If Pressed`` output socket to ``Condition`` input socket, add ``Player`` as object, set ``vector Z``  (up/down axis) to ``200.0`` - this much force will be applied. ``Local`` ? Judge yourself, or use time-tested very successful procedure - `trial & error`. Lucky you, just 2 options are available.

-  Add :ref:`ln-combine_xyz` node, connect above :ln:`Math` nodes. Leave `Z` at default `0.0` value.

-  Add :ref:`ln-vector_math` node, set to ``Normalize``, connect those 2 cute blue-ish dots.

-  Add another :ln:`Vector Math` node, set *Operation* to ``Scale``. This node will determine speed of the Player. Connect ``Result`` from above node to ``Vector 1`` input socket.

.. _fps-snap_ln:

.. tip::
   If you want nodes to be aligned, turn on *magnet* icon in top-right corner of *Logic Node Editor*, above N-panel. Nodes will now snap to invisible grid. Hotkey is :kbd:`Shift-Tab`.

.. figure:: /images/tutorials/introducing_logic_nodes/ln-fps-speed_property-apply_tree.png
   :width: 100%
   :align: center

   Add Game Property and Apply To Selected

Before we continue with nodes, we need to add *Game Property*. With *Player* selected:

-  In :menuselection:`Properties > Game > Game Properties`, click :menuselection:`Add Game Property`, name it ``speed``, leave default ``Float`` type, and set value to ``1.0``.

:menuselection:`Apply To Selected` - this will create ``NL__player`` game property, ``player`` object tree, and a :py:`nl_player.py` script. *NL/nl* stands for *node logic*.

Good job. Now we can continue with nodes.

-  Add :ref:`ln-get_object_property` node; if not already, select ``Game Property`` from dropdown, and in ``Property`` field type ``speed`` - this is the *speed* property that we just created above. Connect this node to ``Scale`` input socket of the last :ln:`Vector Math` node, and add ``Player`` as owner object - click :menuselection:`Object` and select from menu.

-  Add :ref:`ln-on_update` and a :ref:`ln-apply_movement` node - connect ``Out`` to ``Condition``, and last :ln:`Vector Math` into ``Vector``; also set ``Player`` as object, and yes, check ``Local``.

This is our node setup so far:

.. figure:: /images/tutorials/introducing_logic_nodes/ln-fps-setup_so_far.png
   :figwidth: 100%
   :align: center

   Player movement nodes setup so far

.. tip::
   Another very useful Blender habit to grow - almost all buttons & commands have option to ``Add to Quick Favorites`` or ``Assign Shortcut``:

   -  Go to :menuselection:`Properties > Render > Game Resolution`;

   -  Hover mouse over :menuselection:`Embedded Start` button, :ref:`RMB <about-mouse>` and select ``Add to Quick Favorites``.

   -  Use this tip whenever you find yourself using/repeating same actions over and over. It is a great time saver.

.. _fps-quick_favorites:

.. figure:: /images/tutorials/introducing_logic_nodes/ln-fps-quick_favorites.png
   :figwidth: 40%
   :align: right

   Q for Quick Favorites > E for Start

According to the Holy Blender Bible, Embedded Start can be invoked with hotkey :kbd:`P`, which seems to be not working in current UPBGE by default. So we added it into Quick Favorites, although we could as easily assign a `P` shortcut. We will now run game and test if node setup is working as expected. With mouse over :ref:`3D-Viewport <gs-3d_viewport>`:

:kbd:`Numpad 0 > Home > Q` will move into 'camera view' > zoom-in/maximize/center the camera view > open *Quick Favorites* menu; there, another hotkey is offered for the *Embedded Start* - this depends on various factors, and is recognizable by any of the letters being underscored - `E` in figure; in your case might be something else. Pressing that key should start the game. :kbd:`Esc` to end the game.

While the game is running, press movement keys and observe Player behavior.

-  First of all, it is moving way to fast > reduce the ``speed`` property; trial & error is the name of the game, until you find comfortable settings. `Hint` - halve the *speed* value for a start, and do not forget - Player should be selected in order to change its speed property.

-  Second of all, keys are wrong > fix them until character moves properly relative to pressed keys > :kbd:`W` forward; :kbd:`S` backward; :kbd:`A` left; :kbd:`D` right.

.. _fps-mouse_moves_head:

.. figure:: /images/tutorials/introducing_logic_nodes/ln-fps-mouse_moves_head.png
   :figwidth: 40%
   :align: right

   Mouse Look settings

If you're done fixing, let's continue.

-  Add :ref:`ln-mouse_look` and connect ``Out`` from :ln:`On Update` to ``Condition``, set ``Player`` as ``Object`` and ``Head`` as ``Head``. Run the game, test, if needed, adjust settings in :ln:`Mouse Look` node: ``Cap Up/Down`` will limit *Head* movement, ``Smoothing`` will smooth mouse moves.

.. _fps-value_switch:

Next we upgrade walking to run:

-  Add/duplicate :ln:`Keyboard Key` & :ln:`Math`, add :ref:`ln-value_switch`. The logic here is:

   -  When :kbd:`Shift` is pressed, add some *float* value to *speed*, and use resulting value for movement;

   -  If not pressed, use existing *speed* value.
  
Test the game, adjust values as you see fit.

.. figure:: /images/tutorials/introducing_logic_nodes/ln-fps-value_switch.png
   :figwidth: 80%
   :align: center

   Value Switch for running

Now it is time for some actions - we'll add gun shooting. Switch to :menuselection:`Animation` workspace, in the left editor/window > top-right, check :ref:`Shading <gs-viewport_shading>` options - little arrow at far right side will dropdown some setting, which you are free and advised to change.

.. tip::
   With object selected, you can 'focus' it with :kbd:`Numpad ,` (comma); this works in :menuselection:`3D Viewport`, :menuselection:`Outliner`, and other editors. Use this if you 'loose' the object from sight.

.. figure:: /images/tutorials/introducing_logic_nodes/ln-fps-action_editor.png
   :figwidth: 50%
   :align: right

   Action Editor context with action dots

-  Expand/enlarge bottom :menuselection:`Dope Sheet Editor`, select/expand ``Gun`` object (Outliner > Search if needed), and you shall see some orange dots in *Dope Sheet* - this is gun ``Action`` - when gun is fired, bullet pushes it back and up. Hit :kbd:`Space` to toggle animation playing. We need to attach this action to Player and connect it with an input.

-  Switch *Editing context* from :menuselection:`Dope Sheet` to :menuselection:`Action Editor` - name of our action is shown in the header > ``Shot``.

-  Back to :menuselection:`Logic Nodes` workspace (or modify workspace to include *Logic Node Editor* window/area). Add :ref:`ln-mouse_button`, :ref:`ln-pulsify`, :ref:`ln-stop_animation` and :ref:`ln-play_animation` nodes, connect them red-to-red dot.

-  ``Shot`` action is how long? Set :ln:`Play Animation` to ``Object`` > ``Gun``, and ``Action`` > ``Shot``, ``End`` > last action frame. Test the game, adjust settings.

Gun is moving when shooting now, but still needs to actually shoot something. And the sound is missing.

-  Add below :ref:`ln-active_camera`, :ref:`ln-get_world_position`, and :ref:`ln-get_axis_vector` - connect ``Camera`` to both :ln:`Get World Position` > ``Object``, and :ln:`Get Axis Vector` > ``Object``, set ``Axis`` > ``-Z Axis`` (object/player forward-facing direction).
   
   -  :ln:`Get Axis Vector` will take :ln:`Active Camera` orientation and feed it to :ln:`Raycast` for aiming direction.

   -  :ln:`Get World Position` will take :ln:`Active Camera` (player body/head) position and feed it to :ln:`Raycast` as shooting origin point/position.

-  Add :ref:`ln-raycast`, connect :ln:`Get World Position` > ``Origin``, :ln:`Get Axis Vector` > ``Aim``, and above :ln:`Stop Animation` > ``Condition``, check ``Custom Distance`` and ``Local``.

-  Add :ref:`ln-apply_impulse`, connect :ln:`Raycast` top two output sockets color-to-color, and ``Picked Point`` > ``Vector``, ``Ray Direction`` > ``Direction``.

-  Add :ref:`ln-draw` node, set to ``Cube``, connect :ln:`Apply Impulse` > ``Condition``, :ln:`Raycast` ``Picked Point`` > ``Origin``, set ``Width`` to something small, i.e. `0.02`, and check ``Use Volume Origin``.

   -  ``Cube`` will act as improvised bullet. In final game this bullet would probably best be hidden.

Done - test and adjust settings.
  
.. figure:: /images/tutorials/introducing_logic_nodes/ln-fps-shoot_nodes.png
   :figwidth: 90%
   :align: center

   Shot action nodes

.. figure:: /images/tutorials/introducing_logic_nodes/ln-fps-shot_sound.png
   :figwidth: 50%
   :align: right

   Shot audio clip node

Final touch:

-  Search/download 'machine gun shot single audio', a short sound clip, save to disk, somewhere close to our working *.blend* file.

-  Next to above :ln:`Play Animation` add :ref:`ln-start_sound`, set as ``2D Sample``, connect :ln:`Play Animation` ``Started`` > ``Condition``, ``Sound`` attribute > *folder* icon > load shot audio clip, *note* icon > load from dropdown. Test the game, take a break.

