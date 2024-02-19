.. _python_components_getting_started_character_controller_templates:

==============================
Character Controller Templates
==============================

These templates were created to help UPBGE users to create games or any kind of interactive things that requests a Character Controller. Easy to use, easy to attach to your project.

.. figure:: /images/Python_Components/Fig-08.png

To use, just select it from template label at script editor and you're done! You can use this template in your projects, even for commercial projects. You only need to give credits to Guilherme Teres Nunes (UnidayStudio) for this. It's very easy to use: Just load this script into your .blend file through template label (or paste it in the same folder that your .blend is), select the object that you want, and attach the script into the object's components using **Register Component** button.

Character Controller Component
------------------------------

This component will serve as a **Character Controller** for your game. With this, you can easly made an object move using :kbd:`W`, :kbd:`A`, :kbd:`S`, :kbd:`D`, run with :kbd:`LSHIFT` and Jump with :kbd:`SPACE`.
You simply have to create a capsule for your character, set the physics type to "Character" and attach this Component to them. It's very simple to configure:

.. figure:: /images/Python_Components/Fig-09.png
   :align: right

   Character Controller component

* **Activate**: If you want this component running.

* **Walk Speed**: The character's walk speed.
  
* **Run Speed**: The character's run speed.

* **Max Jumps**: The character's max jumps. Set to :kbd:`0` if you don't want the character to jump.

* **Static Jump Direction**: If you want to make your character jump in a static direction, activate "Static Jump Direction". It means that, if the player wasn't moving when he pressed Space, the character will jump up and the player will not be able to change this during the jump. The same for when he was moving when pressed Space. The jump direction will be the character direction when the player press space.

* **Static Jump Rotation**: Exactly like the Jump Direction, but for the character rotation.

* **Avoid Sliding**: If your character object have Collision Bounds activated, I'd recommend to enable the "Avoid Sliding" option. If so, the component will avoid the character from sliding on ramps.

* **Smooth Character Movement**: You can make the movement gets more smooth by increasing this value (:kbd:`0.0` to :kbd:`1.0`).

* **Make Object Invisible**: Makes the object invisible ingame (useful if you attach this component to a capsule object that have a armature inside).

First Person Camera Component
-----------------------------

This component was created to be attached to your camera and to give you a great mouselook control. Very useful for First Person games.

To use, add a camera in your scene, parent it into your character capsule (you can use the Character controller Component on it), and attach this Component to the camera. Don't forgot to position the camera in a place near the "head" of your character.

You can configure the mouse sensibility, invert :kbd:`X` or :kbd:`Y` axis and enable/disable the camera rotation limit. It's very simple to configure:

.. figure:: /images/Python_Components/Fig-10.png
   :align: right

   First Person Camera component

* **Activate**: If you want this component running.

* **Mouse Sensibility**: The mouse sensibility.

* **Invert Mouse X Axis**: To invert the mouselook on the :kbd:`X` axis.

* **Invert Mouse Y Axis**: To invert the mouselook on the :kbd:`Y` axis.

* **Limit Camera Rotation**: Limits the camera rotation on the :kbd:`X` local axis. Very useful for First Person games to avoid the camera from flip upside down.

Third Person Camera Component
-----------------------------

This component was created to be attached to your camera to give you a great third person mouselook control. Very useful for Adventure games, RPGs, Open Worlds, or any kind of games that may require a third person camera.

To use, add a camera in your scene, parent it into your character capsule (you can use the Character controller Component on it), and attach this Component to the camera. And you're done! The component will do the rest for you. :)

You can configure the mouse sensibility, invert :kbd:`X` or :kbd:`Y` axis and enable/disable the camera rotation limit. It's very simple to configure:

.. figure:: /images/Python_Components/Fig-11.png
   :align: right

   Third Person Camera component

* **Activate**: If you want this component running.

* **Mouse Sensibility**: The mouse sensibility.

* **Invert Mouse X Axis**: To invert the mouselook on the :kbd:`X` axis.

* **Invert Mouse Y Axis**: To invert the mouselook on the :kbd:`Y` axis.

* **Camera Height**: The height that you want your camera to be (consider height zero = the center of your character).

* **Camera Distance**: How far from the character that you want your camera to be.

* **Camera Crab (Side)**: You can make the camera stay on the side of your character, if you want. Just adjust this variable.

* **Camera Collision**: If you want your camera to have collision (to prevent the camera from traversing walls).

  * **Camera Collision Property**: The property that you want your camera to avoid (if you want the camera to avoid all the objects, leave this blank).

* **Align Player to View**: You can define when you want the player (character) to look at the camera view direction: Never, just when the player moves or always.

* **Align Player Smooth**: How smooth you want the player to look at the camera direction. :kbd:`0` means no smooth and :kbd:`1` means maximum smooth possible.

By using this Component, you can also call some functions using python (from other components) to help you: setCameraAlign(type), setCameraPos(x,y,z), alignPlayerToView(), getCameraView(). Take a look at the implementation to see how these functions works.

Simple Animator Component
-------------------------

This component will automatically align the armature to the move direction of your character, runs the right animations accordding to the speed and if the character is on air or not.

To use, attach this component to the armature of your character. It's important that the armature is parented with an capsule object with physics type equals to Character. It's very simple to configure:

.. figure:: /images/Python_Components/Fig-12.png
   :align: right

   Simple Animator component

* **Activate**: If you want this component running.

* **Max Walk Speed**: Define the max speed that you want while executing the walk animation. After this speed, the character will start interpolating the run animation. (Read the notes at the end).

* **Max Run Speed**: Define the max speed that you want while executing the run animation. After this speed, the animation will not change.

* **Suspend Children's Physics**: Enable this if you want to remove all the physics from the armature's childrens (recursive). Useful to avoid these childrens to collide with the player capsule, causing a physics bug.

* **Align To Move Direction**: Enable this if you want to make you character faces the direction that the player is going.
  
* **Align Smooth**: How smooth you want to align the character with the direction. 0 Means no smooth and 1 means max smooth.

* **Idle Animation**: Define the name of the Idle (stopped) animation, the frame start and frame end.

* **Walk Animation**: Define the name of the Walk animation, the frame start and frame end.
* **Run Animation**: Define the name of the Run animation, the frame start and frame end.

* **Jump Up Animation**: Define the name of the Jump Up animation, the frame start and frame end.

* **Jump Down Animation**: Define the name of the Jump Down animation, the frame start and frame end. The Jump animations should be divided in two: Jump Up and Jump Down. The first one will be executed when the character is going up. The second, whe the character is falling. Both should be loop animations.

.. note::
   The anim interpolation/transition between idle-walk and walk-run according to the speed is not implemented yet.
