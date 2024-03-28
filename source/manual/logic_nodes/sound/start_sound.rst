.. figure:: /images/logic_nodes/sound/ln-start_sound.png
   :align: right
   :width: 265
   :alt: Start Sound Node

.. _ln-start_sound:

==============================
Start Sound
==============================

Parameters
++++++++++++++++++++++++++++++

Sound Type
   2D or 3D sound or sample; sample has additional 2 more inputs.

Update Running
   todo

Show Advanced Options
   If selected, additional inputs are activated.

Use Speaker
   If selected, *Position* is changed to *Object* field; enter object name or pick from list.

Inputs
++++++++++++++++++++++++++++++

Condition
   If connected, condition must be fulfilled for node to activate.

Position
   Vector position of the sound source.

Sound File
   Which file to play. Pick sound file from dropdown list, or load it with folder icon.

Use Occlusion
   todo

Loop Count
   How many times to play the sound.

Pitch
   Set pitch of the sound.

Volume
   A volume to set.

Ignore Timescale
   If checked, timescale will be ignored.

Attenuation
   Attenuation value of the sound. Only visible if *Show Advanced Options* is selected.

Reference Distance
   todo. Only visible if *Show Advanced Options* is selected.

Cone Inner / Outer
   Size of inner and outer sound cone. Only visible if *Show Advanced Options* is selected.

Cone Outer Volume
   Volume of outer cone. Only visible if *Show Advanced Options* is selected.
   
Outputs
++++++++++++++++++++++++++++++

On Start
   Start signal is emitted.

On Finish
   End signal is emitted.

Sound
   Resulting sound output.

Example
==============================

.. figure:: /images/logic_nodes/sound/ln-start_sound-example.png
   :align: center 
   :width: 80%
   :alt: Start Sound Node Example

|

Above example will play selected ``Sound File``, when mouse cursor enters the selected ``Object`` - a non-default ``Cube`` in this example.
