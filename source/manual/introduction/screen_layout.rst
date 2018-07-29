
************************
Game Logic Screen Layout
************************

The design, construction, debugging and running of a game use a wide range of Blender functions.
To help with the process, Blender incorporates a suggested screen layout for setting up UPBGE 
games. This includes many already-familiar panels but also a new *Logic Editor* panel **(4)** 
concerned solely with UPBGE.

The diagram below shows this default *Game Logic* screen layout, together with the 
appropriate options for game setup/debug/running (these should be set up in the 
order shown).

.. figure:: /images/introduction-screen_layout-overview.jpg

   Game Logic Screen Layout.

.. rubric:: 1. Blender Game

Selected from the render engine menu.
This specifies that all output will be output by the real-time UPBGE renderer.
It also opens various other menu options such as the Game options (see below)
and a range of Properties for the UPBGE renderer properties (see below).

.. rubric:: 2. Game Logic

Layout selected from the list of screen layouts for various applications.
This includes many already-familiar panels (**Info**, **3D View**,
**Properties**, etc) but also a new **Logic Editor** panel concerned solely with UPBGE.

.. rubric:: 3. Game

.. figure:: /images/introduction-screen_layout-game.png

   Game options.

This menu gives various options for conditions for running UPBGE.
Note that this menu is only available when the render engine is set to Blender Game. 
All the options available at this menu are also available in the :doc:`Render tab of the 
Properties editor </manual/editors/properties/render>`. The main options are: 

   Start Game
      Run game in Game Engine (:kbd:`P` or :kbd:`Shift-P` when the mouse cursor is over the 3D View editor).
	  
   Show Debug Properties
      Show properties marked for debugging while game runs.
	  
   Show Framerate and Profile
      Show frame rate and profiling information while game runs.
	  
   Show Physics Visualization
      Show a visualization of physics bounds and interactions.
	  
   Auto Start
      Automatically start game at load time.

.. rubric:: 4. Logic Editor panel

The Logic Editor is where the :doc:`logic, properties and states </manual/logic/index>` 
are set up to control the behavior of the objects in the game. (The Logic Editor panel can 
also be displayed by selecting Logic Editor in the Display Editor menu, by pressing 
:kbd:`Shift-F2`, or by pressing :kbd:`Ctrl-Right`).

.. rubric:: 5. Properties

The Property panel of the screen is selected as usual from the main Information menu.
However, note that several sections of the Property panel are changed when the render engine
**(2)** is changed from Blender Render to Blender Game.
