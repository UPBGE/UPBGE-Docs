==============================
Moving A Cube
==============================

In this tutorial, we'll learn how to move an object using a Python controller in UPBGE. This builds upon the basic concepts introduced earlier.

Setting Up the Scene
+++++++++++++++++++

1. Create a cube in your scene.
2. Add a **Keyboard** sensor and connect it to a **Python** controller.
3. Assign a new script to the controller.

Writing the Movement Script
++++++++++++++++++++++++++

Here's a simple script to move the cube when a key is pressed:

.. code-block:: python

   import bge

   # Get the current controller and its owner (the cube)
   controller = bge.logic.getCurrentController()
   owner = controller.owner

   # Get the keyboard input
   keyboard = bge.logic.keyboard

   # Check if the "W" key is pressed
   if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.WKEY]:
       owner.worldPosition.x += 0.1  # Move right
   elif bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.SKEY]:
       owner.worldPosition.x -= 0.1  # Move left

   # Add similar checks for other keys (A, D, etc.) as needed

Explanation:
- The script checks for keyboard input and updates the cube's position accordingly.
- You can extend this to include movement along the Y or Z axes.

.. note::
   Make sure to enable the keyboard sensor in the Logic Bricks editor and set it to detect the desired keys.
