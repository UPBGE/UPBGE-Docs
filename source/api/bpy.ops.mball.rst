Mball Operators
===============

.. module:: bpy.ops.mball

.. function:: delete_metaelems()

   Delete selected metaelement(s)

.. function:: duplicate_metaelems()

   Duplicate selected metaelement(s)

.. function:: duplicate_move(MBALL_OT_duplicate_metaelems=None, TRANSFORM_OT_translate=None)

   Make copies of the selected metaelements and move them

   :arg MBALL_OT_duplicate_metaelems:

      Duplicate Metaelements, Duplicate selected metaelement(s)

   :type MBALL_OT_duplicate_metaelems: :class:`MBALL_OT_duplicate_metaelems`, (optional)
   :arg TRANSFORM_OT_translate:

      Translate, Translate (move) selected items

   :type TRANSFORM_OT_translate: :class:`TRANSFORM_OT_translate`, (optional)

.. function:: hide_metaelems(unselected=False)

   Hide (un)selected metaelement(s)

   :arg unselected:

      Unselected, Hide unselected rather than selected

   :type unselected: boolean, (optional)

.. function:: reveal_metaelems(select=True)

   Reveal all hidden metaelements

   :arg select:

      Select

   :type select: boolean, (optional)

.. function:: select_all(action='TOGGLE')

   Change selection of all meta elements

   :arg action:

      Action, Selection action to execute

      * ``TOGGLE`` Toggle, Toggle selection for all elements.
      * ``SELECT`` Select, Select all elements.
      * ``DESELECT`` Deselect, Deselect all elements.
      * ``INVERT`` Invert, Invert selection of all elements.

   :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)

.. function:: select_random_metaelems(percent=50.0, seed=0, action='SELECT')

   Randomly select metaelements

   :arg percent:

      Percent, Percentage of objects to select randomly

   :type percent: float in [0, 100], (optional)
   :arg seed:

      Random Seed, Seed for the random number generator

   :type seed: int in [0, inf], (optional)
   :arg action:

      Action, Selection action to execute

      * ``SELECT`` Select, Select all elements.
      * ``DESELECT`` Deselect, Deselect all elements.

   :type action: enum in ['SELECT', 'DESELECT'], (optional)

.. function:: select_similar(type='TYPE', threshold=0.1)

   Select similar metaballs by property types

   :arg type:

      Type

   :type type: enum in ['TYPE', 'RADIUS', 'STIFFNESS', 'ROTATION'], (optional)
   :arg threshold:

      Threshold

   :type threshold: float in [0, 1], (optional)

