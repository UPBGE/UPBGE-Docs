.. _lne-first_example:

==============================
A First Example
==============================

Activating the Logic Nodes Add-on
+++++++++++++++++++++++++++++++++

The *Logic Nodes* add-on comes pre-installed in UPB eGE 0.3+. If not already, it needs to be activated:

* :menuselection:`Edit -> Preferences -> Add-ons`

.. figure:: /images/editors/logic_nodes/01_edit_menu_prefs.png
   :figwidth: 100%
   :align: center

   Navigate to Preferences

There, *search/filter* for ``logic``, and check the box for *Logic Nodes+*.

.. figure:: /images/editors/logic_nodes/02_prefs_filter_logic.png
   :figwidth: 100%
   :align: center

   Search for 'logic' and check the box

Click the little arrow, next to the check box, to expand the *Logic Nodes+* add-on menu, and in the :menuselection:`Preferences` click :menuselection:`Install or Update Uplogic Module` button.

.. figure:: /images/editors/logic_nodes/03_prefs_addons_ln_unfold.png
   :figwidth: 90%
   :align: center

   Install or Update Uplogic Module

.. important::
   This same :menuselection:`Preferences` menu can be used to report a bug > click :menuselection:`Report a Bug` button (internet connection is required). The default web browser will open ``github.com`` web page. There, click :menuselection:`New issue` button, and follow the instructions. 

Houston, the eagle has landed. We're good to go.

.. _lne-system_console:

System Console
++++++++++++++++++++++++++++++

UPBGE uses system console/terminal to print info and error messages. To see those messages:

Windows users:

* :menuselection:`Window --> Toggle System Console` menu.

Linux and Mac users:

* start UPBGE via console/terminal - navigate to blender executable file, and run::
   ``./blender``

.. figure:: /images/editors/logic_nodes/00_terminal_run.png
   :figwidth: 100%
   :align: center

   Run UPBGE on Linux or Mac terminal
.. _lntut-first_example:

We will print some text to the console when a keyboard key is pressed. This is the "Hello World" example for the Logic Nodes.

.. _lntut-creating_new_logic_tree:

Creating a New Logic Tree
++++++++++++++++++++++++++++++

Now let's get started. First we need to create a logic tree. Switch the *Editor Type* to the :menuselection:`Logic Node Editor`.

.. figure:: /images/editors/logic_nodes/04_editor.png
   :figwidth: 50%
   :align: center

   Select Logic Node Editor

This editor is similar to the *Shader Editor* or *Geometry Node Editor*. Click on :menuselection:`New` and a new empty tree (named *Logic Node Editor* by default) will be created.

.. figure:: /images/editors/logic_nodes/05_new_ln_tree.png
   :figwidth: 100%
   :align: center

   Click New button

.. figure:: /images/editors/logic_nodes/06_n_panel_dashboard.png
   :figwidth: 100%
   :align: center

   New empty Node Tree with side Dashboard

Adding Nodes
++++++++++++++++++++++++++++++

With mouse cursor inside *Logic Node Editor*, press :kbd:`Shift-A`, or click :menuselection:`Add` button in top header. This will pop-up a menu with all available *Logic Nodes*, organized in sub-menus. Go ahead and take a look at what is available.

.. figure:: /images/editors/logic_nodes/07_add_key_node.png
   :figwidth: 100%
   :align: center

   Available Logic Nodes in Add menu

For this example, we're looking for two nodes: :ref:`ln-keyboard_key` and :ref:`ln-print` node. Easiest way to add nodes:

* press :kbd:`Shift-A` hotkey, to invoke adding a node;
* **immediately** after that start typing, i.e. ``print`` - UPBGE is smart and will search for it;
* if accidentally wrong node is selected, press :kbd:`ESC` to cancel, and repeat.

.. figure:: /images/editors/logic_nodes/08_search_print_node.png
   :figwidth: 100%
   :align: center

   Editor searches for node

.. tip::
   Beside finding the node, *Search* pop-up also shows in which *menu/sub-menu* the nodes are.

:ln:`Keyboard Key` node is a node of the **condition** type. These nodes do not actually do anything in-game; they either provide a condition, or can be used to check for a more complex set of conditions.

:ln:`Print` node is an **action** type node. These nodes actually do something. They move objects, change properties, add constraints etc. - you name it.

Those two nodes need to be connected together. The :ln:`Keyboard Key` node has an *If Pressed* output socket, colored red. Connect it (click-and-drag) to the *Condition* input socket of the :ln:`Print` node and enter "Hello World" in the text box at the bottom, next to *Value* input socket (blue sockets are for *strings*). Also, if not already, look at the :ln:`Keyboard Key` node and you'll see that it expects user to choose a key. Click the bottom field and press :kbd:`SPACE` key, which will set that key as selected one. It should look something like this now:

.. figure:: /images/editors/logic_nodes/09_nodes_connected.png
   :figwidth: 100%
   :align: center

   Logic Nodes added and connected

Applying Logic Trees
++++++++++++++++++++++++++++++

Once done, all that's left is to apply the tree to an object. Logic trees work the following way:

* each tree can be applied to as many objects as you want;
* meaning it is executed by each object it is applied to, separately.

Example: if this tree is attached to 4 objects and user presses :kbd:`SPACE` key **once**, the message would be printed 4 times, once for each object.

To apply a tree to a cube, first a cube is added; select it and press :menuselection:`Apply To Selected` button, in the *Dashboard* tab of side *N-panel*. Press :kbd:`N` to toggle *N-panel*, if it is hidden.

.. figure:: /images/editors/logic_nodes/10_apply_to_selected.png
   :figwidth: 100%
   :align: center

   Apply logic tree to selected object

.. warning::
   Be careful, trees can be applied to multiple objects at once!

To see which objects have been applied with a *Logic Node* tree, scroll down the *Dashboard* tab, and check the *Tree applied to:* sub-panel at the bottom.

.. figure:: /images/editors/logic_nodes/11_tree_applied_to.png
   :figwidth: 100%
   :align: center

   Objects with applied Logic Node tree

If needed, sub-panels can be rearranged:

* for easier rearranging, first collapse sub-panels - click small arrow next to the sub-panel title;
* click-and-drag top-right icon (4 by 2 dots) of sub-panel.

.. figure:: /images/editors/logic_nodes/12_rearange_n_sub_panel.png
   :figwidth: 100%
   :align: center

   Collapsed and rearranged N-panel sub-panels

What is left now is to run our example \'game\':

* in *Render* panel of a *Properties* editor, click :menuselection:`Embedded Start` or :menuselection:`Standalone Start` (hotkey is :kbd:`P`) - the \'game\' shall start;
* with \'game\' running, press :kbd:`SPACE` (or whichever keyboard key is assigned in :ln:`Keyboard Key` node) once;

.. figure:: /images/editors/logic_nodes/13_embedded_start.png
   :figwidth: 100%
   :align: center

   Start the game in Render panel

Finally check the system console - it should have our message printed:

-  once if logic tree was applied to one object;
-  twice if logic tree was applied to two objects;
-  four times if logic tree was applied to two objects, and :kbd:`SPACE` was pressed twice etc.

.. figure:: /images/editors/logic_nodes/14_terminal_output.png
   :figwidth: 100%
   :align: center

   System console/terminal output

.. note::
   See :ref:`lne-system_console` for more info.
   
   The :ln:`Print` node prints to the system console only, not to the Python interactive console. This is a feature of Blender and is not changeable.

Press :kbd:`ESC` key to end the \'game\'.
