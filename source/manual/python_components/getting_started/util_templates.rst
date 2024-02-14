.. _python_components_getting_started_util_templates:

===============
Utils Templates
===============

These templates were created to help UPBGE users to create games or any kind of interactive things. Easy to use, easy to attach to your project.

..
   figure:: /images/Python_Components/Fig-17.png


To use, just select it from template label at script editor and you're done! You can use this template in your projects, even for commercial projects. You only need to give credits to Guilherme Teres Nunes (UnidayStudio) for this. It's very easy to use: Just load this script into your .blend file through template label (or paste it in the same folder that your .blend is), select the object that you want, and attach the script into the object's components using **Register Component** button.

Sound Speaker Component
-----------------------

This component will serve as an sound Speaker for your game. With this, you can easly control 3D sound, volume. Unfortunatelly, the sounds needs to be mono to make the 3D sound works. You can convert your sound to mono using windows CMD like this: '> ffmpeg -i Sound.wav -ac 1 SoundMono.wav' 
It's very simple to configure:

.. figure:: /images/Python_Components/Fig-18.png
   :align: left

   Sound Speaker component

* **Sound File**: The file name, example: "Assets/DoorMono.wav".
* **Loop Sound**: If you want the sound to loop or just play once.
* **Volume**: The Volume.
* **Pitch**: The Pitch.
* **3D Sound**: If you want the sound to be 3D.
* **Min Distance**: If 3D Sound is enabled, the sound will have the max volume if the listener is at this distance or minor.
* **Max Distance**: If 3D Sound is enabled, the sound will volume down until zero when the listener reach this distance.
* **Delete Object After End**: If enabled, the object will be deleted at the end of the sound (if Loop Sound equals to false).

|

Minimap Component
-----------------

This component will spawn a minimap based on the camera (which owns the component) view. Add this component to a camera and position it on top of your character. 
To configure, take a look at the values:

.. figure:: /images/Python_Components/Fig-19.png
   :align: left

   Minimap component

* **Camera Type**: You can choose between Perspertive or Ortographic camera.
* **Camera Height**: Define the height that you want your minimap camera to be. If you don't want the component to modify this, just set to :kbd:`0`.
* **Minimap Position**: The position of the center of the minimap on the screen (values goes from :kbd:`0` to :kbd:`1`).
* **Minimap Size**: The size of the minimap (values goes from :kbd:`0` to :kbd:`1`).
* **Follow Object**: You can define an object for the minimap to follow (like the player). Leave it empty if you don't want.
* **Rotate on Z axis**: If you defined a Follow Object, you can also makes the minimap rotates on the :kbd:`Z` axis according to the follow object's rotation.
