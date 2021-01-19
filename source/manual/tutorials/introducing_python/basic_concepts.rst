==============
Basic Concepts
==============

This tutorial will give you a quick introduction about how to use Python within the Game Engine. Basically, it will enable you to start with Python scripting avoiding typical errors and wrong paths.

When writing Python code for the UPBGE we recommend to keep the UPBGE Python API open as reference. You can find it here: `upbge.org/api <https://upbge.org/api/>`__

-------------------------------------------
If you don't know enough Python to begin...
-------------------------------------------
This tutorial is not a tutorial to teach you Python. If you don't know enough Python to begin with maybe worth trying to play with Python on the side, at least to cover the basics.

Maybe a lot to read, but at least they explain a bunch of things, you don’t have to rush... `https://www.techbeamers.com/python-tutorial-step-by-step <https://www.techbeamers.com/python-tutorial-step-by-step/>`__

And we mean, maybe Google explains better than us: `https://developers.google.com/edu/python/set-up <https://developers.google.com/edu/python/set-up/>`__ 

Just pick your poison. Take your time to read, really :-). If you go through with it, you’ll be ready to try your new spells on the UPBGE!

------------------------------
Logic Brick: Python Controller
------------------------------
PUT IMAGE

A Python controller is basically a logic brick that you can program using Python scripts.

If you look at how a controller usually behaves, they do pretty simple things:

- AND Controller: When all connected sensors are positive, activate all connected actuators.
- OR Controller: When one of the connected sensors is positive, activate all connected actuators.
- NAND Controller: When no connected sensor is positive, activate all connected actuators.
- XOR Controller: When only one of the connected sensors is positive, activate all, etc.
These are all basic logic gates, but what if you want more control?

Test if a sensor is positive, and actually check some values from it?

That’s when you use a Python controller:
PUT IMAGE
