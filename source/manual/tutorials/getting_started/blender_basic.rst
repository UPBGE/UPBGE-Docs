====================
Blender/UPBGE Basics
====================

-------------
Blender/UPBGE
-------------

When you start Blender/UPBGE, you will be greeted with the splash screen. Although you can
customize all aspect of Blender/UPBGE, in this manual, we will assume you are using the
default Blender/UPBGE settings and shortcuts.

Clicking anywhere else to dismiss the splash screen, you are presented with an empty
workspace like this:

.. figure:: /images/Chapter1/Fig01-20.jpg

   Blender/UPBGE default workspace.

The Blender/UPBGE window is divided into Editors. Each Editor region can be resized, moved,
and changed to display a specific set of content. For now, let's focus on the default setup.

---------
Main Menu
---------

At the top of the screen is the main menu, which offers basic functionalities such as
Open, Save, and Help. Furthermore, the main menu controls the view for the rest of the
Blender/UPBGE window. The Render Engine option in the middle of the menu controls how the
interface is configured.

.. figure:: /images/Chapter1/Fig01-21.png
   :figwidth: 40%
   :align: left

   Selecting the Game Engine

By default, Cycles Render is selected. In this mode, the interface is configured for
doing 3D modeling, animation, and rendering with Cycles. But let's switch it to the
Blender Game mode. Click the drop-down menu and select Blender Game from the list.
This setting will unlock certain features that are not visible normally, and it also
hides features that are not available in the Blender game engine.

-----------
3D Viewport
-----------

Occupying the majority of the screen is a 3D Viewport. Here you can see the 3D world
you created and test the game. For now, feel free to explore the 3D Viewport by holding
down your middle mouse button over the 3D Viewport and dragging the mouse; the view should
rotate with the mouse movement. (Mac users can use the two-finger rotate gesture on the
trackpad) The default scene contains three objects: a cube, a camera, and a light.
To select one of the objects, right-click on it. The selected object is highlighted in yellow.

.. note:: **Basic Navigation Controls**

   Press and hold the middle mouse button to rotate the 3D view. Scroll the mouse
   wheel to zoom in the 3D view. Right-click to select a 3D object.
   Selected objects are highlighted in yellow.

.. figure:: /images/Chapter1/Fig01-23.png
   :figwidth: 25%
   :align: left

   Number pad keyboard layout.


Another common setup for the 3D Viewport is to split the view into four quadrants:
top view, side view, front view, and a perspective view. You can turn on Quad
view by pressing Ctrl+Alt+Q with the mouse over the 3D Viewport (see Figure 1.22).
Press the same key combination to go back to the single view.

To quickly snap to one of the predetermined views (side, top, front, and so on),
the number pad is the way to go.

--------
Outliner
--------

.. figure:: /images/Chapter1/Fig01-20b.png
   :figwidth: 33%
   :align: right

   Outliner

To the right of the screen are two editors. The top portion is the Outliner, which
contains a listing of all the data in the current Blender file. For a large project,
the Outliner is an indispensable tool for organizing your scene. For now, you can
safely ignore it.

-----------------
Properties Editor
-----------------

.. figure:: /images/Chapter1/Fig01-24.png
   :figwidth: 33%
   :align: right

   Properties Editor icons.

Under the Outliner on the right, you have the Properties Editor. Here you can access
global settings for the file, as well as settings for individual objects. This is one
of the most frequently used panels in Blender, after the 3D view perhaps. The *Properties Editor*
is context sensitive, which means it will automatically display different content, depending
on the object that is active. Take a closer look at the row of icons at the top of the *Properties Editor*,
as shown in Figure 1.24. These tabs organize the properties into groups,
with the more general settings on the left-most tab, and the more specific settings on the right.

--------
Timeline
--------

At the very bottom of the screen is a timeline window, which will be useful when you start making animations.

.. figure:: /images/Chapter1/Fig01-20c.png

   Timeline

-----------------------
Workspace Customization
-----------------------

The default screen, as described previously, is set up for general use. At some point,
it becomes necessary to change the screen layout to accomplish other tasks. To select a
different layout, use the Screens layout drop-down menu from the main menu.

Apart from the predefined screen layouts, you can customize the screen layout however
you like. You can either split an existing editor into two or merge two
adjacent editors together.

.. note:: **Editor, Region, and Area**

   A region within the Blender/UPBGE windows is called an *editor*. An editor displays
   a specific set of content and tools. Common areas include: *3D View*, *Properties Editor*,
   *UV/Image Editor*, and *Logic Brick Editor*.



Figure 1.25 shows one area split into two. You can do it by dragging the top corner
of the area to the right or bottom

.. figure:: /images/Chapter1/Fig01-25.png

   Area Splitting

To merge two adjacent areas into one is exactly the same as shown in Figure 1.25,
but it is done in reverse order. Optionally, you can click with the right mouse button
in the edge of the area you want to split or join, and select the option in the Area Options pop-up menu.

.. figure:: /images/Chapter1/Fig01-27.png
   :figwidth: 25%
   :align: left

   Editor selection.

Not only can you change the size and layout of the editor,
but the type of editor can also be changed. As you can see in Figure 1.27,
the left-most icon in the header can be used to change the editor type.

.. figure:: /images/Chapter1/Fig01-28.png
   :figwidth: 45%
   :align: right

   Dopesheet, Image Editor, and Logic Brick Editor.

Almost everything a studio needs to create the game is integrated into a single interface:
you can create the game, test the game, and play the game all from the same program.
This means that, as an artist, you can create a game in the shortest time possible,
without having to worry about importing and exporting files between different applications.
As a programmer, you won't have to switch back and forth between different software just
to test your code. Figure 1.28 shows some screenshots of different editors that you will
be using throughout the manual.

-------------------
More on the 3D View
-------------------

The 3D view is where you will spend most of your time, so let's take a look at it in a
bit more detail. You've already learned a few ways to navigate around the scene earlier
in this chapter, using both the mouse and the keyboard.

----------------------
Viewport Shading Modes
----------------------

.. figure:: /images/Chapter1/Fig01-29.png
   :figwidth: 25%
   :align: right

   Drawing Modes

Let's look at the four different Viewport Shading modes available in the 3D view.
They are used to change the way the scene is displayed onscreen. The four modes are:

- **Bounding Box** : Represents all objects as a wireframe boundary. Useful for when the scene gets really complex.
- **Wireframe** : Draws all objects as wireframe, which allows you to see through objects.
- **Solid** : Draws all objects as solid faces, which is commonly used when modeling.
- **Textured** : Draws all objects as solid faces, also with texture and accurate lighting. This is useful for previewing the scene.

The two most commonly used Shading modes are Wireframe and Solid. Therefore,
they are assigned to a keyboard toggle for easy access. Press the ``Z`` key to toggle
between Wireframe and Solid View modes. Additionally, you can Press ``Alt+Z`` to toggle
between Solid and Textured view modes.

.. note:: **Standing Out**

   Individual objects can also override the Viewport Shading mode
   via a setting under the Properties Editor > Object > Display > Type.


-------------
Editing Modes
-------------

To the left of the Shading mode selector is the Editing Mode selector.

- **Object Mode** : The default mode, which allows the manipulation of objects in the
scene as a whole. From this mode, you can select any of the objects in the scene,
and move, rotate, and scale them. In fact, almost everything apart from modeling
can be done from Object mode.
- **Edit Mode**: This mode can be seen as the counterpart to Object mode. It allows
you to edit the underlying geometry of the object. If you are modeling, you'll
probably want to be in Edit mode. For this reason, Edit mode is not available
when a non-editable object is selected (for example, a camera or light).

To switch between Object mode and Edit mode, press the tab key.

In addition to the two editing modes we just discussed, there are a few other modes that are less commonly used.

- **Sculpt Mode** : Only available for Mesh objects. Allows modifications to the mesh as if it were clay.
- **Vertex** , **Weight,** and **Texture Paint Mode** : Only available for Mesh objects.
These modes allow the assignment of color or weight to the mesh.
- **Pose Mode** : Is used to animate bones in an armature.

Edit mode and Object mode are by far the most commonly used editing modes, so we will
refrain from diving too deeply into the other modes for now.

------------------
Keyboard and Mouse
------------------

The joke is that to move an object in Blender, you have to press the ``G`` key,
which stands for "movinG." This gag stems from the fact that to a beginner,
many of the shortcuts in Blender/UPBGE seem counterintuitive. However, there
is a very good reason why "G" is preferred over "M." In this case, the ``G`` key can
be easily accessed on the keyboard by the left hand while the right hand is on the mouse.
Also, officially, G stands for Grab.

.. note:: **Think Different**

   By default, the Mac keyboard uses Command instead of Control as the default modifier key.
   So whenever you see ``Ctrl+Something`` in this book, mentally map it to Cmd
   if you are using a Jobsian product.

   Additionally, Blender/UPBGE has good support for multi-touch gestures on OS X.
   You can pinch to zoom, rotate to orbit around, and pan around.

Let's start with some shortcuts that work the way you would expect:

* **Ctrl + S:** Save File
* **Ctrl + O:** Open File
* **Ctrl + N:** New File
* **Ctrl + Z:** Undo
* **Ctrl + Shift + Z:** Redo
* **Ctrl + Q:** Close(Quit) Application

The above shortcuts work anywhere within Blender: they are effectively global. Unfortunately, the familiarity ends here.

To manipulate an object in the 3D view, generally you have to select it at first:

- **Right-click:** Select object
- **Shift + Right-click:** Extend selection to multiple objects
- **A:** Select all

All of the actions above are "reversible." If something is already selected, right-clicking
on it will deselect it. If all the objects are already selected, pressing ``A`` will deselect all.

Once an object is selected, you can start manipulating it. The keyboard shortcuts
below correspond to the three most basic transforms:

- **G:** Start Grabbing
- **S:** Start Scaling
- **R:** Start Rotating
- **Move mouse:** Carry out transform action
- **Left-click:** Confirm transformation
- **Enter:** Confirm transformation

Pressing one of the keys will start the transformation, and then you can move your mouse
to control the degree of the effect. To finalize the transformation, left-click the mouse or press Enter.

------
Search
------

.. figure:: /images/Chapter1/Fig01-30.png
   :figwidth: 30%
   :align: right

   The Search Box

The final tip that you will learn is the search functionality in Blender.
If you are unable to recall how to invoke a certain operation, whether through a button or
a keyboard shortcut, a quick way to find it is by using the search functionality.
Key in a few letters of what you are looking for, and the result should appear
as shown in Figure 1.30.

Tapping on the spacebar from anywhere will bring out a search box that contains a list of actions.

A word of caution, though: the current implementation of the search is not very
context-aware, so sometimes operations that are not permitted in the active context might show up.

------------------------
Blender/UPBGE Philosophy
------------------------

Blender/UPBGE is designed with certain philosophies in mind. Understanding these
will allow you to use Blender the way it is intended, which allows you to navigate
around Blender faster and work more efficiently.

Let the brainwashing begin!

---------
Interface
---------

Because Blender was originally created as an in-house software, its interface is
designed to maximize speed and efficiency for users who have mastered it. Since Blender 2.5,
a lot of work has been done to make the interface more user-friendly. That said, Blender is
probably unlike any other program you've used before, including other kinds of 3D software.
Luckily, the Blender interface is very consistent within the application. This means that
once you learn to do something, you'll be able to use it in another part of the program.

--------
Keyboard
--------

Because of the large number of commands Blender is capable of performing, invoking a
function through a quick tap on the keyboard is generally faster than using the mouse
to find the menu entry. As you follow through the rest of this section, pay special
attention to the shortcut keys that are used, because Blender is designed to let you
work fast once you learn the shortcuts.


Blender's keyboard shortcuts are optimized for a full-sized English QWERTY keyboard.
The number pad (which, unfortunately, is not present on many laptops) is used to quickly
navigate around the 3D scene. Laptop users usually have to press extra keys on their keyboard
(such as the Fn key or a toggle) in order to simulate a number pad key. As a solution,
go to File > User Preferences (Ctrl + Alt + U), then switch to Input tab and enable "Emulate Numpad"
option to use main 1 to 0 keys instead of Numpad keys. If you want this setting
remain permanently, click on the "Save User Settings" button.

.. figure:: /images/Chapter1/Fig01-30.png

   Emulate Numpad

.. figure:: /images/Chapter1/Fig01-31.png
   :figwidth: 20%
   :align: right

   3D Navigator.

Alternatively, Blender also has an add-on called "3D Navigation" that provides an
easier way to navigate around the world for people without a number pad. To enable
the 3D navigation plug-in to help you navigate around the 3D Viewport quickly,
go to File > User Preferences > Add-Ons, and turn on 3D Views: 3D Navigation. Then
you can switch views quickly from the 3D view's Toolshelf.

-----
Mouse
-----

Blender is designed for a three-button mouse: a mouse with two buttons and a
scroll wheel. Although there is an option to emulate the middle-mouse button
(when you click on the scroll wheel), this book will assume that you are working
with a three-button mouse for convenience.

.. note:: **How to Emulate a Three-Button Mouse**

   If you don't have a three-button mouse, you can use the Alt+Left mouse button
   combination to emulate the middle mouse button. To enable this feature,
   go to File > User Preferences > Input and turn on Emulate 3 Button Mouse.

-------
Context
-------

In Blender, the actions you can perform at any given time are limited to the
current state of Blender, also known collectively as the " context." For example,
certain operations can only be invoked when you have an object selected; the Property Editors
change, depending on which object is selected; the effect of the keyboard shortcuts even changes,
depending on where your mouse is positioned. This context-sensitive nature lets you focus on the
task at hand by only providing you with options that makes sense at the time. This is Blender's
way of preventing the interface from getting too cluttered.

The "context" usually refers to one or a combination of the following:

- **Active rendering engine:** Blender Render, Blender Games, and Cycles Render are the default three.
- **Active editor:** The active editor is defined as the window subdivision that the mouse
cursor is hovering over. Shortcut keys often have different effects, depending on which
editor the mouse is over.
- **Active object:** The active object is defined as the object that is most recently selected.
- **Selected object:** All the objects that have been selected (highlighted). Keep in mind
that there can be more than one selected object, but only one active object.
- **Editing mode:** Blender has six different modes of editing. Two of the most commonly
used are the Edit mode and the Object mode. In Object mode, you can manipulate objects as
a whole. In Edit mode, you can change the shape of a mesh. In each mode, there is a unique
set of tools and options at your disposal. You will learn about the other four modes
(Sculpt, Vertex Paint, Texture Paint, Weight Paint) in later chapters.

----------
Datablocks
----------

Often, a single Blender file contains hundreds of objects, each with different colors,
textures, and animations. How is all this organized?

Blender uses "data blocks" to represent content stored within a Blender file. Each
data block represents a collection of data or settings. Some common datablock types
you will encounter are Object datablock, Mesh datablock, Material datablock, Texture datablock,
and Image datablock.

.. figure:: /images/Chapter1/Fig01-32.png
   :figwidth: 30%
   :align: right

   Datablock hierarchy.

In order to reduce the apparent complexity of the program, Blender further organizes
data blocks into hierarchies. At the top level are scenes, which can have a number of
worlds, each of which can have any number of objects (objects can be a mesh, a light, a camera,
and so on). If the object is a mesh, then a Mesh datablock is attached to it. If the object is
a light, then a Light datablock is attached to the object.

An example of a datablock hierarchy chain is shown in Figure 1.32:
Scene > Object > Mesh > Material > Texture > Image


Throughout the Blender interface, you will run into many datablock managers.
They all look like Figure 1.33.

.. figure:: /images/Chapter1/Fig01-33.png
   :figwidth: 30%
   :align: left

   Datablock Sharing

Because datablocks can be shared, copied, and reused, large scenes can be managed
efficiently through the use of shared datablocks. Figure 1.33 shows a datablock
that has been shared by three "users," as denoted by the number next to its name.

----------------------
Parenting and Grouping
----------------------

Grouping and parenting both allow you to introduce some form of order to the scene
by setting up arbitrary relationships between different objects. But grouping and
parenting work in different ways.

Parenting is used to establish links between multiple objects so that basic
transformations like location, rotation, and scaling are propagated from the
parent to its children. This way, any transformation applied to the parent is
automatically applied to all the children. Parenting is a useful way to "glue"
different objects together so they behave as one.

To parent one object to another, simply select the object you want to be the child first.
If more than one object is to be a child, select all of them now. Lastly, select the
object that you want to be the parent. Then press Ctrl+P to set parent.

An object can only have one parent object, but a parent object can have many children.

Grouping can also be used to logically link objects in the scene together without
any transformation constraints to the objects. Unlike parenting, grouping does not
have a parent-child relationship; objects are simply members of a group.

Select all the objects you want to group. Then press Ctrl+G to add them to a new group.
You can also manage group membership from the Object Properties Editor.

Grouping, by itself, it not very useful. But groups can be quickly "instanced" as
group instances. Group Instance is a very useful way to create multiple copies of
objects without making actual copies of the objects. Grouping will also come in handy
for asset management, which will be discussed in the next chapter.

A single object can be in multiple groups. A group can have multiple objects.

----------------------
Backward Compatibility
----------------------

Blender is designed so that older files can be opened with newer versions of Blender.
But due to the rate that Blender matures, some unexpected behaviors are to be expected
when you least expect them.

Due to the Blender Python API change in Blender 2.5, old scripts written for 2.4x will
be broken in later versions of Blender. But by the time you are reading this, there
should be enough new content available for you to find.

------
Onward
------

This concludes the crash course on Blender and the game engine. By now,
you should have a cursory understanding of the function of a game engine and be
familiar with the Blender interface. In the next chapter, you will get your hands
dirty and build a simple game by following the step-by-step tutorial.
