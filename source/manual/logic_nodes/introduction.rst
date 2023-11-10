.. _logic_nodes-introduction:

============
Introduction
============

As an alternative to Python scripts and Logic Bricks, Logic Nodes try to provide an intuitive and versatile
way to create game logic. They are designed to support rapid prototyping, enabling artists and game designers
to quickly test and even fully implement features.

Logic Nodes use a visual approach to programming, allowing developers to skip learning a programming language and
the engine's API to get their game done. With a set of over 250 nodes, close to all functionalitiy is
covered, including calling custom scripts and referencing logic bricks to make full use of UPBGE's power.

------------
Logic Trees
------------

*Logic Trees* are different from *Logic Bricks*, as they are not directly bound to an object.
They can be created, edited and compiled without any object in the scene. To be executed though,
they need to be applied to at least one object (or called through another tree, but more on
that later). Now the difference between being bound and being applied to an object is that
multiple objects can have the same *Logic Tree* applied to them, while *Logic Bricks* are unique
for each object.

Basically, *Logic Node Trees* work just as *Material Node Trees* do, you add nodes, connect them
to one another and something happens. One difference would be that with a material, you always
try to route all of your nodes back to the *Material Output* at some point. This is not the case
with Logic Nodes. You can have a lot of smaller patches within a single tree which will be
executed, regardless if they're connected or not. As there's no such thing as an "Output" Node,
each part of the tree is evaluated "as is".

------------
Logic Nodes
------------

The system is built around *Nodes*, and each Node has *Sockets* that can be connected to the
Sockets of other nodes. Normally the code isn't very picky and will try to work with whatever comes
its way, meaning that you can try to combine different types of Sockets without having to fear a
complete crash.

It is generally advised to try to keep Logic Trees as small as possible to keep the performance high.
You would for example use the "Formula" Node for more complex equations instead of putting multiple
"Math" nodes together.

----------
Global Variables
----------

With the Logic Node Addon also comes the ability to create and read global variables. They work very
similarly to Properties, but again they are not bound to an object, but to the scene. These variables
are intended to be used to store data about the world like time, temperature, etc. or game settings,
though they can just as well be used for player or entity data that wouldn't really make sense on an
object.

------------
Architecture
------------

Under the hood, Logic Nodes are actually generating Python scripts to be executed by the game engine.
These scripts can be loaded in two ways:

- Applied as :doc:`Logic Bricks </manual/logic/introduction>` or
- applied as a :doc:`Python Component </manual/python_components/introduction>`

Applying a tree using Logic Bricks generates the necessary bricks on the selected object to execute the tree.
This method gives you full access to Logic Brick functionality, which can be very useful when trying to work
with object-specific behavior.

Using the Component method has the advantage of being tidier. The generated component will have options for
executing the tree only at startup and for executing the tree only when a certain property is set. Using
this method will prevent you from accessing Logic Bricks directly, but you can still access them via custom
Python calls.

.. warning::

   Due to the way Logic Nodes *currently* work, they are the most performance-heavy way to create logic.
