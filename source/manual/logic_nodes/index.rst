.. _ln-index:

===========
Logic Nodes
===========

.. toctree::
   :maxdepth: 2
   :hidden:
   
   introduction
   events/index
   game/index
   input/index
   values/index
   animation/index
   lights/index
   nodes/index
   objects/index
   scene/index
   sound/index
   logic/index
   math/index
   physics/index
   python/index
   raycasts/index
   time/index
   data/index
   file/index
   network/index
   render/index
   ui/index
   utility/index

This page lists all available *Logic Nodes* in this chapter. There are 6 categories in *Logic Editor* :menuselection:`Add` menu, separated into sub- and sub-sub-menus (click the line to toggle-expand):

.. collapse:: Events  | |  Game  | |  Input  | |  Values

   * :ref:`ln-events-index`
      * On Init
      * On Update
      * On Next Frame
      * On Value Changed To
      * On Value Changed
      * Once
      * **Custom**
         * Receive Event
         * Send Event
   * :ref:`ln-game-index`
      * Load Blender File
      * Load Game
      * Quit Game
      * Restart Game
      * Save Game
   * :ref:`ln-input-index`
      * **Mouse**
         * Mouse Button
         * Mouse Moved
         * Mouse Over
         * Mouse Status
         * Cursor Visibility
         * Set Cursor Position
         * Mouse Look
      * **Keyboard**
         * Keyboard Key
         * Keyboard Active
         * Key Code
         * Key Logger
      * **Gamepad**
         * Gamepad Button
         * Gamepad Sticks
         * Gamepad Active
         * Gamepad Vibrate
         * Gamepad Look
      * **VR**
         * VR Headset
         * VR Controller
   * :ref:`ln-values-index`
      * Boolean
      * Float
      * Integer
      * String
      * **Vector**
         * Color RGB
         * Color RGBA
         * Separate XY
         * Separate XYZ
         * Combine XY
         * Combine XYZ
         * Combine XYZW
         * Euler
         * Resize Vector
      * **Properties**
         * Get Tree Property
         * Set Tree Property
         * Get Object Property
         * Set Object Property
         * Object Has Property
         * Toggle Object Property
         * Modify Object Property
         * Evaluate Object Property
         * Copy Property From Object
         * Get Global Property
         * Set Global Property
      * Random Value
      * Invert
      * Formatted String
      * File Path
      * Store Value
      * Value Switch
      * Value Switch List
      * Value Switch List Compare ( x )

|

.. collapse:: Animation  | |  Lights  | |  Nodes  | |  Objects  | |  Scene  | |  Sound

   * :ref:`ln-animation-index`
      * Play Animation
      * Stop Animation
      * Set Animation Frame
      * Animation Status
      * **Armature / Rig**
         * Bone Status
         * Set Bone Position
      * **Bone Constraints**
         * Set Attribute
         * Set Influence
         * Set Target
   * :ref:`ln-lights-index`
      * Get Light Color
      * Set Light Color
      * Get Light Power
      * Set Light Power
      * Set Light Shadow
      * Make Light Unique
   * :ref:`ln-nodes-index`
      * **Materials**
         * Get Node
         * Play Sequence
         * Get Socket Value
         * Set Socket
         * Get Node Value
         * Set Node Value
      * **Geometry**
         * Get Socket Value
         * Set Socket
         * Get Node Value
         * Set Node Value
      * **Groups**
         * Get Socket Value
         * Set Socket
         * Get Node Value
         * Set Node Value
   * :ref:`ln-objects-index`
      * **Get Attribute**
         * Get World Position
         * Get World Orientation
         * Get World Linear Velocity
         * Get World Angular Velocity
         * Get World Transform
         * Get Local Position
         * Get Local Orientation
         * Get Local Linear Velocity
         * Get Local Angular Velocity
         * Get Local Transform
         * Get Name
         * Get Scale
         * Get Color
      * **Set Attribute**
         * Set World Position
         * Set World Orientation
         * Set World Linear Velocity
         * Set World Angular Velocity
         * Set World Transform
         * Set Local Position
         * Set Local Orientation
         * Set Local Linear Velocity
         * Set Local Angular Velocity
         * Set Local Transform
         * Set Scale
         * Set Color
      * **Transformation**
         * Apply Movement
         * Apply Rotation
         * Apply Force
         * Apply Torque
         * Apply Impulse
         * Align Axis To Vector
         * Follow Path
         * Move To
         * Move To With Navmesh
         * Rotate To
         * Slow Follow
      * **Object Data**
         * Get Axis Vector
         * Get Object ID
         * Get Vertices
         * Replace Mesh
         * Set Constraint Attribute
      * **Curves**
         * Get Curve Points
         * Set Curve Points
      * Add Object
      * Remove Object
      * Set Visibility
      * Get Object
      * Get Child By Index
      * Get Child By Name
      * Get Parent
      * Set Parent
      * Remove Parent
      * Set Material
      * Send Message
      * Spawn Pool
   * :ref:`ln-scene-index`
      * **Camera**
         * Active Camera
         * Set Camera
         * Set FOV
         * Set Orthographic Scale
         * World To Screen
         * Screen To World
      * **Post FX**
         * Add Filter
         * Remove Filter
         * Set Filter State
         * Toggle Filter
      * **Collections**
         * Get Collection
         * Get Object Names
         * Get Objects
         * Set Collection Visibility
         * Set Overlay Collection
         * Remove Overlay Collection
      * Get Scene
      * Set Scene
      * Get Gravity
      * Set Gravity
      * Get Timescale
      * Set Timescale
   * :ref:`ln-sound-index` 
      * Start Sound
      * Start Speaker
      * Pause Sound
      * Resume Sound
      * Stop Sound
      * Stop All Sounds

|

.. collapse:: Logic  | |  Math  | |  Physics  | |  Python  | |  Raycasts  | |  Time

   * AI ( TODO )
   * :ref:`ln-logic-index`
      * **Trees**
         * Start Logic Tree
         * Run Logic Tree
         * Stop Logic Tree
         * Add Logic Tree To Object
         * Logic Tree Status
      * **Bricks**
         * Get Sensor Value
         * Set Sensor Value
         * Get Actuator Value
         * Set Actuator Value
         * Controller Status
         * Sensor Positive
      * Gate
      * Branch
      * Gate List
      * Is None
      * Not None
   * :ref:`ln-math-index`
      * Math
      * Vector Math
      * **Vectors**
         * Check Angle
         * Vector Rotate
         * Absolute Vector
         * XYZ To Matrix
         * Matrix To XYZ
      * Interpolate
      * Absolute
      * Clamp
      * Compare
      * Formula
      * Map Range
      * Treshold
      * Ranged Treshold
      * Limit Range
      * Within Range
   * :ref:`ln-physics-index`
      * **Vehicle**
         * Create New Vehicle
         * Accelerate
         * Brake
         * Set Vehicle Attribute
         * Steer
      * **Character**
         * Walk
         * Jump
         * Get Physics Info
         * Set Jump Force
         * Set Max Jumps
         * Set Velocity
      * Collision
      * Set Collision Group
      * Set Collision Mask
      * Add Constraint
      * Remove Constraint
      * Set Physics
      * Set Gravity
      * Set Dynamics
      * Set Rigid Body
   * :ref:`ln-python-index`
      * Run Python Code
      * Get Instance Attribute
      * Set Object Attribute
      * Typecast Value
   * :ref:`ln-raycasts-index`
      * Raycast
      * Mouse Ray
      * Camera Ray
      * Projectile Ray
   * :ref:`ln-time-index`
      * Time Data
      * Delta Factor
      * Delay
      * Timer
      * Pulsify
      * Barrier

|

.. collapse:: Data  | |  File  | |  Network

   * :ref:`ln-data-index`
      * **List**
         * New List
         * List From Items
         * Append
         * Extend
         * Remove Index
         * Remove Value
         * Get List Index
         * Set List Index
         * Get Random List Item
         * Duplicate
      * **Dict**
         * New Dictionary
         * Dictionary From Items
         * Get Dictionary Key
         * Set Dictionary Key
         * Remove Dictionary Key
      * **Variables**
         * Load Variable
         * Save Variable
         * Remove Variable
         * Load Variable Dict
         * Save Variable Dict
         * Clear Variables
         * List Saved Variables
      * Load Scene
      * Load File Content
   * :ref:`ln-file-index`
      * Get Font
      * Get Image
      * Get Sound
   * :ref:`ln-network-index`
      * LAN Server
      * LAN Client
      * Rebuild Data
      * Send Data
      * Serialize Data

|

.. collapse:: Render  | |  UI

   * :ref:`ln-render-index`
      * **EEVEE**
         * Set Ambient Occlusion
         * Set Bloom
         * Set Exposure
         * Set Gamma
         * Set SSR
         * Set Volumetric Light
      * Get Fullscreen
      * Set Fullscreen
      * Get Resolution
      * Set Resolution
      * Get VSync
      * Set VSync
      * Show Framerate
      * Show Profile
   * :ref:`ln-ui-index`
      * **Widgets**
         * Create Canvas
         * Create Layout
         * Create Button
         * Create Label
         * Create Image
         * Crate Slider
      * Add Widget
      * Get Widget Atrribute
      * Set Widget Attribute
      * Set Custom Cursor

|

.. collapse:: Utility

   * :ref:`ln-utility-index`
      * Print
      * Draw
   
-----

.. note::

   The sub-menu *Layout* is not a particular part of Logic Nodes - those are tools for organizing and connecting, and are common feature for all *node editors*.

.. figure:: /images/logic_nodes/ln-noodles.png
   :align: center 
   :scale: 60%
   :alt: Logic Noodles
   
   Logic Noodles
