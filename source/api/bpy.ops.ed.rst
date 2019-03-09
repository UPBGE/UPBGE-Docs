Ed Operators
============

.. module:: bpy.ops.ed

.. function:: flush_edits()

   Flush edit data from active editing modes

.. function:: redo()

   Redo previous action

.. function:: undo()

   Undo previous action

.. function:: undo_history(item=0)

   Redo specific action in history

   :arg item:

      Item

   :type item: int in [0, inf], (optional)

.. function:: undo_push(message="Add an undo step *function may be moved*")

   Add an undo state (internal use only)

   :arg message:

      Undo Message

   :type message: string, (optional, never None)

.. function:: undo_redo()

   Undo and redo previous action

