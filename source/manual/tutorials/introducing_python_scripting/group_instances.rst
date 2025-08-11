==============================
Dealing With Group Instances
==============================

Learn to dynamically spawn and manage group instances.

Setup
+++++

1. Create a group named "Projectile"
2. Make sure it has a **Rigid Body** setup
3. Add **Always** + **Python Controller**

Spawning Script
++++++++++++++

.. code-block:: python

    import bge
    from random import uniform

    def spawn_projectiles(scene, owner):
        if bge.logic.keyboard.events[bge.events.SPACEKEY] == bge.logic.KX_INPUT_ACTIVE:
            # Random position near spawner
            pos = [uniform(-2, 2), uniform(-2, 2), 3]
            
            # Create instance
            new_obj = scene.addObject("Projectile", owner, 0)
            new_obj.worldPosition = pos
            
            # Apply physics force
            new_obj.applyForce([0, 0, -50], local=False)

    scene = bge.logic.getCurrentScene()
    controller = bge.logic.getCurrentController()
    owner = controller.owner
    spawn_projectiles(scene, owner)

Advanced Usage
+++++++++++++

- Object pooling for better performance
- Damage system on collision
- Particle trail effects
