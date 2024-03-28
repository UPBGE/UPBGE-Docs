.. figure:: /images/logic_nodes/physics/vehicle/ln-create_new_vehicle.png
   :align: right
   :width: 215
   :alt: Create New Vehicle Node

.. _ln-create_new_vehicle:

==============================
Create New Vehicle
==============================

Attaches a vehicle constraint to an object. This object will become the collider for the vehicle.

.. important::
   This node needs a specific object setup to work correctly. A vehicle needs to be ceated only once, otherwise the vehicle control nodes won't be able to address the correct constraint. Of course, there must be the collider object. This will be the object executing the tree. Parented directly to this collider must be all the wheels.

   The wheels must follow a naming convention:

   If ``FWheel`` appears somewhere in the wheels name, it will be a ``front`` mounted wheel.
   
   If ``RWheel`` appears somewhere in the wheels name, it will be a ``rear`` mounted wheel.

Wheels will be mounted in the position they are placed at, but the difference is that vehicle control nodes can be targeted to either front, rear or all wheels, which are accessed differently.

The collider may have any number of wheels. It may also have other children, as everything not named *FWheel* or *RWheel* will be ignored.

The node will return a vehicle constraint which can be used to drive the vehicle or modify its attributes. This constraint will also be automatically saved to the collider object and can be accessed via::

   # obj is the collider object
   vehicle_constraint = obj['_vconst']

Inputs
++++++++++++++++++++++++++++++

Condition
   If connected, condition must be fulfilled for node to activate.

Collider
   Object that will act as collider for vehicle.

Suspension
   Vehicle suspension height.

Stiffness
   Vehicle suspension stiffness, will determine how much vehicle `wiggles`.

Damping
   The rate at which suspension activity will subside.

Friction
   The grip of the wheel. Pavement would be a higher value than mud.

Wheel Modifier
   todo

Outputs
++++++++++++++++++++++++++++++

Done
   *True* if node performed successfully, else *False*.

Vehicle Constraint
   A vehicle constraint.

Wheels
   A list of wheel objects.
