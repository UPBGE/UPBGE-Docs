==============================
Using Linked Libraries In Game
==============================

*Linked Library* is a Blender feature that allows referencing a datablock from another 
blend file into the current one, allowing easier manipulation of common assets and better 
project management, as you only need to edit the original file to update all the 
references. UPBGE supports this Blender feature, specially group instances, which ones 
are fairly well integrated through Python. This tutorial aims to show how to use linked 
libraries, group instances and manage the links.

---------------
Before We Start
---------------

To proceed with this tutorial, we need some base files first. On a directory, save three 
empty blend files: *game.blend* (which will contain the references from the libraries), 
*lib_character.blend* (which will contain the actual model of our character) and 
*lib_scenery.blend* (which will contain the actual model of our ground). We'll edit the 
file *game.blend* later, first we must create the contents of our libraries. 

lib_character.blend
   Add an Monkey object, add it to a group (:kbd:`Ctrl-G`) and rename the group to `player`.

lib_scenery.blend
   Add an Plane, scale it by 5 (so it have the size of 10x10), add it to a group 
   (:kbd:`Ctrl-G`) and rename the group to `ground`.

Both files should be set up somewhat like this:

.. figure:: /images/tutorials-linked_libraries-base_files_1.png
   
   Split view of the two files.

------------------
Linking The Groups
------------------

Now, we'll create a blend file named *game.blend* on the same directory as our previous 
files. In this file, we'll do the following procedures:

- Go to the *File* menu, click the option *Link*.
- Select the either *lib_character.blend* or *lib_scenery.blend*.
- Select the option *Group*.
- Select the corresponding group and double click it / click *Link from Library*.

.. figure:: /images/tutorials-linked_libraries-linking_1.png
   
   Linking procedures diagram.
   
If everything went right, you should see in the *3D Viewport* the group instances added. 
They are not editable as they are only :ref:`datablock-empty` objects referencing groups 
from the original files.

With the instances added, all you have to do is place them with the desired 
transformations, and if you need to edit all the placed instances, just edit the original 
file to update all the references. Pretty handy, isn't it?

------------------
Managing the Links
------------------

If you rename or move any of your libraries to another folder, you will face a common 
problem: broken links. There are several ways to deal with this problem, and this section 
will present you the use of the *Outliner* to manage links (and :ref:`datablock-index`).

