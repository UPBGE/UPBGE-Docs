.. _python_components_getting_started_top_down_templates:

==================
Top Down Templates
==================

This template was created to help UPBGE users to create games or any kind of interactive thing that request a Top Down Controller. Easy to use, easy to attach to your project.

.. figure:: /images/Python_Components/Fig-13.png


To use, just select it from template label at script editor and you're done! You can use this template in your projects, even for commercial projects. You only need to give credits to Guilherme Teres Nunes (UnidayStudio) for this. It's very easy to use: Just load this script into your .blend file through template label (or paste it in the same folder that your .blend is), select the object that you want, and attach the script into the object's components using **Register Component** button.

Mouse Camera Drag Component
---------------------------

This component will allow the player to move the camera (or other objects) by simple holding a mouse button (you decide what button) and dragging the mouse around. Very useful for top down games. It will also allow the player to move the camera (or other objects) by pressing :kbd:`W`, :kbd:`A`, :kbd:`S`, :kbd:`D` keys. There is some configuration to help you adapting this logic to better fit in your project. If you want to drag the camera in a vertial way, to create a side scroller game, for example, you can easly change the "Up Axis" to allow this. You can attach this component into your camera or into other objects.
It's very simple to configure:

.. figure:: /images/Python_Components/Fig-14.png
   :align: left

   Mouse Camera Drag component

* **Show Mouse**: Enable if you want to show the mouse
* **Mouse Movement**: Enable if you want to activate the mouse drag logic
* **Mouse Button**: Which mouse button you want to use
* **Keyboard Movement**: Enable if you want to move the object using :kbd:`W`, :kbd:`A`, :kbd:`S`, :kbd:`D`
* **Up Axis**: Select the :kbd:`UP` axis.
* **Local Movement**: Local or Global movement? You decide!
* **Mouse Sensibility**: The mouse sensibility!
* **Keyboard Speed**: If you enabled the Keyboard Movement, control the speed here!
* **Limit Area**: You can limit the area that the object can stay by playing around with this values. If you don't want, just set to :kbd:`0`.

|

Mouse Point And Click Component
-------------------------------

This component will allow you to teleport an object right into the point that the player clicks. You can limit the scope of the clicks by adding a property. This feature is very useful for top down/point and click games, because you need a pivot to point where the player wants the character to go. 
It's very simple to configure:

.. figure:: /images/Python_Components/Fig-15.png
   :align: left

   Mouse Point and Click component

* **Activate**: Activate or deactivate the logic
* **Mouse Button**: Which mouse button you want to use
* **Align To Normal**: Enable if you want to align the object to the mouse over normal.
* **Property**: The property that you want to interact with (leave this blank if you want to interact with everything).

|

Object Chaser Component
-----------------------

This component will make the object chase a target (another object) when they have certain distance. Note that is necessary to have a navmesh in your scene. You can also change the Target object in realtime by calling the function setTarget(). 
It's very simple to configure:

.. figure:: /images/Python_Components/Fig-16.png
   :align: left

   Object Chaser component

* **Activate**: Activate or deactivate the logic.
* **Navmesh Name**: The name of your navmesh.
* **Target Object**: The name of your target.
* **Min Distance**: The minimum distance that you want the object from the target.
* **Tolerance Distance**: Once the object is already near the target, the extra tolerance distance that they can have before it starts chasing again.
* **Speed**: The speed of the object while chasing the target.
* **Front Axis**: The front Axis (put :kbd:`Y` axis if you don't know).
* **Up Axis**: The :kbd:`UP` Axis (put :kbd:`Z` if you don't know).
* **Smooth Turn**: To smooth the path following turns.
