==============================  
Moving A Cube  
==============================  

In this tutorial, we’ll move a cube in 3D space using Python, with full WASD controls and rotation.  

Setup:
++++++

1. Add a **Cube** to the scene.  
2. Add an **Always** sensor linked to a **Python Controller** (no other setup needed).  

Full Python Script:
+++++++++++++++++++

.. code-block:: python  

    import bge  
    from math import radians  

    def update_movement(owner, speed=0.1, rot_speed=1.0):  
        keyboard = bge.logic.keyboard  
        events = keyboard.events  

        # Movement (WASD)  
        move_vec = [0.0, 0.0, 0.0]  
        if events[bge.events.WKEY] == bge.logic.KX_INPUT_ACTIVE:  
            move_vec[1] += speed  # Forward (Y-axis)  
        if events[bge.events.SKEY] == bge.logic.KX_INPUT_ACTIVE:  
            move_vec[1] -= speed  # Backward  
        if events[bge.events.AKEY] == bge.logic.KX_INPUT_ACTIVE:  
            move_vec[0] -= speed  # Left (X-axis)  
        if events[bge.events.DKEY] == bge.logic.KX_INPUT_ACTIVE:  
            move_vec[0] += speed  # Right  

        # Apply movement relative to the cube’s rotation  
        owner.applyMovement(move_vec, local=True)  

        # Rotation (Q/E for yaw)  
        if events[bge.events.QKEY] == bge.logic.KX_INPUT_ACTIVE:  
            owner.applyRotation([0, 0, radians(rot_speed)], local=True)  
        if events[bge.events.EKEY] == bge.logic.KX_INPUT_ACTIVE:  
            owner.applyRotation([0, 0, radians(-rot_speed)], local=True)  

    # Main  
    controller = bge.logic.getCurrentController()  
    owner = controller.owner  
    update_movement(owner)  

Explanation:
++++++++++++

- **`applyMovement`**: Moves the cube relative to its local rotation (so "W" always moves forward).  
- **`applyRotation`**: Rotates around the Z-axis (yaw) with `Q`/`E`.  
- **No Logic Bricks setup**: All input is handled via Python.  

Extensions:
+++++++++++

- Add gravity with `owner.worldPosition.z -= 0.05`.  
- Use `bge.render.showMouse(True)` for mouse look.  
