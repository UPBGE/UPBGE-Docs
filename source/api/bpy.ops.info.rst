Info Operators
==============

.. module:: bpy.ops.info

.. function:: report_copy()

   Copy selected reports to Clipboard

.. function:: report_delete()

   Delete selected reports

.. function:: report_replay()

   Replay selected reports

.. function:: reports_display_update()

   Update the display of reports in Blender UI (internal use)

.. function:: select_all_toggle()

   Select or deselect all reports

.. function:: select_border(xmin=0, xmax=0, ymin=0, ymax=0, deselect=False, extend=True)

   Toggle border selection

   :arg xmin:

      X Min

   :type xmin: int in [-inf, inf], (optional)
   :arg xmax:

      X Max

   :type xmax: int in [-inf, inf], (optional)
   :arg ymin:

      Y Min

   :type ymin: int in [-inf, inf], (optional)
   :arg ymax:

      Y Max

   :type ymax: int in [-inf, inf], (optional)
   :arg deselect:

      Deselect, Deselect rather than select items

   :type deselect: boolean, (optional)
   :arg extend:

      Extend, Extend selection instead of deselecting everything first

   :type extend: boolean, (optional)

.. function:: select_pick(report_index=0)

   Select reports by index

   :arg report_index:

      Report, Index of the report

   :type report_index: int in [0, inf], (optional)

