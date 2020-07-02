===================
Game Basic Concepts
===================

----
Game
----

So far, we have talked about 3D at length. But how does the game engine fit into? Well, a game engine simply takes the existing 3D assets and attaches a "brain" 
to them so the objects know how to respond to events. The "brain" can be in the form of logic bricks (which can perform different actions depending on the 
user input), scripts (which can extend the functionality of logic bricks), or other physical properties of an object (such as rigid body settings to make 
an object tumble and fall realistically).

.. figure:: /images/Chapter1/Fig01-19.jpg
   
   Game = Object + Logic.

A game engine is made up of many distinct components:

* **Rendering Engine** : Turns the 3D scene you've built (including models, lights, and camera) into an image to be displayed onscreen.
* **Physics** : Handles collisions and physical simulations of objects.
* **Logic/Scripting** : The brain behind a game, it reacts to the user input, makes decisions, and keeps track of what's going on in the game.
* **Sound** : Produces the audio events.

The above list is not meant to be exhaustive, but it should give you an idea of what a game engine does. The Blender game engine gives you a lot of control over each of these components, which you will learn one by one in later chapters.

.. topic:: **Quality vs. Performance**

   Making a video game is a constant balancing act between quality and performance. As artists, you want to make the virtual world as rich and detailed 
   as possible; on the other hand, you need to make sure the game can run smoothly for people who might not have top-of-the-line computers. Throughout the 
   process of game-making, you will run into cases where you have to make a decision whether to prioritize the visual quality or the performance of the game. 
   You will also learn tricks to achieve high-quality visual without compromising the performance, as well as how to optimize the game by identifying what 
   is slowing it down.
   
---------
Game Loop
---------

The game loop is something that every game or general software has: it consists of several 
processing steps and then, repeating it. To make it clear, think of a video player 
processing steps:

- It reads a portion of the video file from disk.
- It decodes the read file portion into a image.
- It shows the decoded image in the screen as a single frame.
- It repeats everything from the start.

Nevertheless, this article will present you how the game loop is built in UPBGE.
It is essential to know how it works: if you keep that in mind, it will explain a lot of 
mysterious behavior that you might discover.

.. figure:: /images/tutorials-getting_started-game_loop.png
   
   Game loop diagram.

Each cycle in the game loop represents a logical frame, also known as logic tick. 
It is the smallest time unit within your game. In each loop:

- The scenes are processed.
- The devices are checked for input.
- The final image is rendered.

It is important to know that the render part might be skipped if the last frame was 
spending too much processing time , resulting in lag. There is a limit on how much renders 
can be skipped (default = 5). If this limit exceeds, a render will take place regardless 
how long it takes. Such 'render' lags will result in 'logic' lags, making the game run 
slower than expected.

----------
Scene Loop
----------

.. figure:: /images/tutorials-getting_started-scene_loop.png
   
   Scene loop diagram.

This loop is a bit more complex. The scenes loop cycles through all active scenes 
performing the following steps for each scene:

- Logic processing
   This first step processes the logic of the game, be it visual or Python.
- Physics update
   The physics update will be done after the logic runs, but before the render is drawn.
- Sound playing
   The sound playing is put in the last step of the scene loop.

Once all these steps are taken for all active scenes, the main loop continues.

-----------
Logic Ticks
-----------

The logic processing works through frames called *logic ticks*. By default, a game 
running at 60 frames per second also can run 60 logic ticks per second. In practical 
examples:

- If I have a number 0 and increase it by 1 each frame, after 1 second its value 
  will be 60.

- If I have an object and move it 0.1 meters each frame, after 1 second it 
  should have been moved 6 meters.

In UPBGE you can control the logic tick intervals for each object by skipping a given ammount 
of ticks, allowing you to run logic at exact custom time intervals or optimize logic which 
doesn't need to run each frame. The following diagram shows how logic tick skipping work.

.. figure:: /images/tutorials-getting_started-logic_ticks_diagram.png
   
   Logic tick skipping diagram.

In the given diagram, where dark red is logic execution and grey is a interval:

1. No ticks skipped between logic ticks, the logic runs each game frame.
2. Skipping of 2 ticks between each logic execution.
3. Skipping of 6 ticks between each logic execution.

To understand how the game loop and logic triggering works is important for you to shape 
the way your logic will be made and understand internal behaviors that UPBGE may show.
