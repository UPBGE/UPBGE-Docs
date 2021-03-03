===============
A First Example
===============

Here we will try print some text to the console when a key is pressed. This could
probably be called the "Hello World" example for the Logic Nodes.

---------------------------------
Activating the Logic Nodes Add-on
---------------------------------

The *Logic Nodes* add-on cames pre-installed in UPBGE 0.3+. To activate it you have
to go to ``Edit -> Preferences -> Add-ons`` and filter for Game Engine.
There, check the box for the Logic Nodes and you're good to go.

.. figure:: /images/Tutorials/Introducing_Logic_Nodes/tutorials-introducing-logic-nodes-01.png

   Activating Logic Nodes Add-on

-------------------------
Creating A New Logic Tree
-------------------------

Now, let's get started. First we will need to create a logic tree. For this, check
the view menu for a new editor called Logic Tree Editor (Should be under "General").

.. figure:: /images/Tutorials/Introducing_Logic_Nodes/tutorials-introducing-logic-nodes-02.png

   Set-up for Logic Nodes Editor

This editor is similar to the Shader Editor, so creating a new logic tree is the same as
creating a new Material. Just click on New and a new tree (named NodeTree by default)
should appear.

.. figure:: /images/Tutorials/Introducing_Logic_Nodes/tutorials-introducing-logic-nodes-03.png

   Logic Nodes Editor


.. figure:: /images/Tutorials/Introducing_Logic_Nodes/tutorials-introducing-logic-nodes-04.png

   Node Tree Created

------------
Adding Nodes
------------

Let's make something happen here. When you press :kbd:`Shift-A`, you'll notice that you
can add new nodes now. Go ahead, take a look at what's at your disposal.

.. figure:: /images/Tutorials/Introducing_Logic_Nodes/tutorials-introducing-logic-nodes-05.png

   Adding Logic Nodes

For this example, we're looking for two nodes: the ``Key Down`` node and the ``Print`` node.
If you can't find them, you can also search for those words.

The ``Key Down`` node is a node of the condition type. These nodes do not actually do anything in-game,
but they either provide a condition or can be used to check for a more complex set of conditions.

The ``Print`` node is an action type node. These nodes actually do something.
They move objects, change properties, add constraints, you name it.

Now we need to link the two together. The ``Key Down`` node has a Condition Socket,
they are colored red. Connect that to the condition socket of the ``Print`` node and enter "Hello World" in
the text box. Also, if you didn't already, look at the ``Key Down`` node and you'll see that it asks you
to choose a key. It should look something like this now:

.. figure:: /images/Tutorials/Introducing_Logic_Nodes/tutorials-introducing-logic-nodes-06.png

   Logic Nodes Added

--------------------
Applying Logic Trees
--------------------

Once you've done that, all that's left is to apply the tree to an object. Logic trees work the
following way: each tree can be applied to as many objects as you want, meaning it is executed
by each object it is applied to separately.

Example: If you attached this tree to 4 objects and pressed the key ONCE,
the message would be printed 4 times, once for each object.

To apply a tree to a cube, first add a cube, select it and press ``Apply to selected`` in the
logic tree editor under the ``Item`` tab.

.. warning::

   Be Careful, trees can be applied to multiple objects at once!

.. figure:: /images/Tutorials/Introducing_Logic_Nodes/tutorials-introducing-logic-nodes-07.png

   Applying Logic Tree

--------------
System Console
--------------
Now, Last step! Hit Window -> Toggle System Console (for Linux and Mac users: save the file
and start blender via console again), start your game and hit that key you entered before.
Quit the game, check the system console and there should be your message, printed as many times as you hit the key.

.. figure:: /images/Tutorials/Introducing_Logic_Nodes/tutorials-introducing-logic-nodes-08.png

   Console Output

This console is also the place where your errors will be printed if you are working in Debug Mode.

.. note::

   The ``Print`` node prints to the system console only, not to the python interactive console.
   Sadly this is not changable.
