.. _logic-introduction:

============
Introduction
============

What makes a game different than a movie? Let's see. In both you can find yourself buried in a
comfortable seat eating junk food and alienated from the world. And funny 3D goggles are not exclusive
to either. But what about interactivity? In a game you can control a player and interact with the
virtual (or real!) world and the game elements. The story can be dynamically created in front of your eyes.

Therefore, as a director and content creator you will play different roles in a movie or a game. In a movie,
for example, you have to direct the flow of the story, but for a game, you have to direct how the player
controls and experiences this flow. More than ever, it's time to narrow the gap between what technology can
deliver and what the public can experiment with and assimilate as part of their own nature. It is necessary
to give *all the power to the user*.

Traditionally, to design your game interaction in the past, you would have needed coding expertise and a highly
technical background. If, as a creative artist, any words such as technical, code, or programming scare
you, Have confidence! "Pure artists" are still scared with code. The idea here is not that they will no longer
be afraid of it. Instead, with the UPBGE they will not have to face their fears. *Logic Bricks* are an alternative
to hardcore coding, known to be "artists friendly" more. *Logic Bricks* is here to rescue you. *Logic Bricks* is a
visual set of tools responsible for integrating the game components together. By using *Logic Bricks*, you can
determine what to do after a mouse click, when to play an animation, how to move your character, and so on, as
shown in following picture.

.. figure:: /images/Logic/logic-logic-bricks-editor.png

   Logic Bricks Editor.

.. note::

   Logic Bricks is high level visual programming.

*Logic Bricks* system is the default "scripting" layer in the Game Engine.
Each *Game Object* in the game may store a collection of logical components (Logic Bricks)
which control its behavior within the scene. *Logic bricks* can be combined to perform
user-defined actions that determine the progression of the simulation.

------------
Logic Bricks
------------

The main part of *Logic Bricks* system can be set up through a graphical interface,
the Logic Bricks Editor, and therefore does not require detailed programming knowledge.
Logic is set up as blocks (or "bricks") which represent preprogrammed functions;
these can be tweaked and combined to create the game/application.

The *Logic Brick* system is composed of three main elements:
:doc:`Sensors </manual/logic/sensors/introduction>`,
:doc:`Controllers </manual/logic/controllers/introduction>` and
:doc:`Actuators </manual/logic/actuators/introduction>`. Sensors are an event system
used to trigger an action upon a specific event (for example, an object collides
with another object or the joystick is used). Once one or more sensors is triggered,
you can use a controller to control whether or not this set of events will produce
an event in the game (and which effect). Controllers work as logic pipes, evaluating
sensors through simple logic conditions, such as And, Or, and Not. Finally, when a
controller validates a set of sensors, it will activate an actuator. An actuator is
responsible for a specific action of the game (such as ending the game, moving an
object, and so on).

In this chapter, we'll cover sensors, controllers, and actuators in detail specifically,
how and when to use them. Additionally, you will learn about object game properties,
the State Machine system, how the interface works, and the architecture of the system
as a whole. As a system used to build new worlds, this is no place for do's and don'ts.
It will be up to you to find the best set of features that fits your project and
creativity. Nevertheless, when possible, we'll present suggestions of when and how
people have used the tools in the past, but you don't have to feel constrained by that.
Treat Logic Bricks as small Lego pieces and surprise us and yourself.

.. note::

   Logic Bricks are really easy and quick to use. You can make entire games with them with
   absolutely no need for coding.

----------
Properties
----------

:doc:`Properties </manual/logic/properties>` are like variables in other programming languages.
They are used to save and access data values either for the whole game (e.g. scores),
or for particular objects/players (e.g. names).
However, in the UPBGE, a property is associated with an object.
Properties can be of different types,
and are set up in a special area of the Logic Editor.

------
States
------

Another useful feature is object :doc:`States </manual/logic/states>`.
At any time while the simulation is running,
the object will process any logic which belongs to the current state of the object.
States can be used to define groups of behavior -- e.g. an actor object may be "sleeping", "awake" or "dead",
and its logic behavior may be different in each of these three states. The states of an object are set up,
displayed and edited in the Controller logic bricks for the object.

------------
Architecture
------------

The game engine was designed to revolve around game objects. Twenty years ago, when it was first developed, this
was a breakthrough design. The idea of having events controlled per object, as opposed to a central controller,
worked well for the early days of 3D engines. Nowadays, some people may advocate that controlling elements per object
is less scalable and more difficult to manage. That will be up to you to decide. Regardless of your thoughts on that
subject, the game engine still allows you to emulate a centralized controlling system, while giving autonomy to each
object to deal with its own business. Part of this flexibility is due to the hooked-up Python layer and the
Logic Brick system. Through the Python interface, you can replace or at least control most of the effects and logic
setups you create with Logic Bricks. With Logic Bricks, you can quickly set up a system that is easy to visualize,
implement, and test. The strength of the game engine comes from the trade-off between the two sibling systems.
A flexible design may lack features and performance compared to specific engines. Nevertheless, the different kinds
of applications you can prototype and develop quickly with the game engine make up for the compromise.

If you look at a level deep into the object structure, you will find that the architecture of the Logic Bricks
system is "controller-centric." It revolves around the controllers of the game because they are the ones to determine
what do to with the sensors and what actuators to activate. This doesn't have to be followed strictly, but based on
this design, you will want to keep your sensors and actuators to a minimum and optimize their usage with the
controllers. Actually, in order to optimize the performance, the game engine disables any sensor and actuator that
is unlinked to a controller or linked to a controller in a non-active state. This is one of the (many) reasons why
Python controllers are so popular. They allow you to replace the use of multiple sensors and actuators by direct
calls to their equivalents in the source code. The chapter :doc:`Python Scripting </manual/python/index>` is entirely
dedicated to that aspect of the game engine, and will complement the applications of Logic Bricks discussed in this chapter.
