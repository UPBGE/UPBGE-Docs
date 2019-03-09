KeyMapItem(bpy_struct)
======================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: KeyMapItem(bpy_struct)

   Item in a Key Map

   .. attribute:: active

      Activate or deactivate item

      :type: boolean, default False

   .. attribute:: alt

      Alt key pressed

      :type: boolean, default False

   .. attribute:: any

      Any modifier keys pressed

      :type: boolean, default False

   .. attribute:: ctrl

      Control key pressed

      :type: boolean, default False

   .. data:: id

      ID of the item

      :type: int in [-32768, 32767], default 0, (readonly)

   .. attribute:: idname

      Identifier of operator to call on input event

      :type: string, default "", (never None)

   .. data:: is_user_defined

      Is this keymap item user defined (doesn't just replace a builtin item)

      :type: boolean, default False, (readonly)

   .. data:: is_user_modified

      Is this keymap item modified by the user

      :type: boolean, default False, (readonly)

   .. attribute:: key_modifier

      Regular key pressed as a modifier

      * ``NONE`` .
      * ``LEFTMOUSE`` Left Mouse, LMB.
      * ``MIDDLEMOUSE`` Middle Mouse, MMB.
      * ``RIGHTMOUSE`` Right Mouse, RMB.
      * ``BUTTON4MOUSE`` Button4 Mouse, MB4.
      * ``BUTTON5MOUSE`` Button5 Mouse, MB5.
      * ``BUTTON6MOUSE`` Button6 Mouse, MB6.
      * ``BUTTON7MOUSE`` Button7 Mouse, MB7.
      * ``ACTIONMOUSE`` Action Mouse, MBA.
      * ``SELECTMOUSE`` Select Mouse, MBS.
      * ``PEN`` Pen.
      * ``ERASER`` Eraser.
      * ``MOUSEMOVE`` Mouse Move, MsMov.
      * ``INBETWEEN_MOUSEMOVE`` In-between Move, MsSubMov.
      * ``TRACKPADPAN`` Mouse/Trackpad Pan, MsPan.
      * ``TRACKPADZOOM`` Mouse/Trackpad Zoom, MsZoom.
      * ``MOUSEROTATE`` Mouse/Trackpad Rotate, MsRot.
      * ``WHEELUPMOUSE`` Wheel Up, WhUp.
      * ``WHEELDOWNMOUSE`` Wheel Down, WhDown.
      * ``WHEELINMOUSE`` Wheel In, WhIn.
      * ``WHEELOUTMOUSE`` Wheel Out, WhOut.
      * ``EVT_TWEAK_L`` Tweak Left, TwkL.
      * ``EVT_TWEAK_M`` Tweak Middle, TwkM.
      * ``EVT_TWEAK_R`` Tweak Right, TwkR.
      * ``EVT_TWEAK_A`` Tweak Action, TwkA.
      * ``EVT_TWEAK_S`` Tweak Select, TwkS.
      * ``A`` A.
      * ``B`` B.
      * ``C`` C.
      * ``D`` D.
      * ``E`` E.
      * ``F`` F.
      * ``G`` G.
      * ``H`` H.
      * ``I`` I.
      * ``J`` J.
      * ``K`` K.
      * ``L`` L.
      * ``M`` M.
      * ``N`` N.
      * ``O`` O.
      * ``P`` P.
      * ``Q`` Q.
      * ``R`` R.
      * ``S`` S.
      * ``T`` T.
      * ``U`` U.
      * ``V`` V.
      * ``W`` W.
      * ``X`` X.
      * ``Y`` Y.
      * ``Z`` Z.
      * ``ZERO`` 0.
      * ``ONE`` 1.
      * ``TWO`` 2.
      * ``THREE`` 3.
      * ``FOUR`` 4.
      * ``FIVE`` 5.
      * ``SIX`` 6.
      * ``SEVEN`` 7.
      * ``EIGHT`` 8.
      * ``NINE`` 9.
      * ``LEFT_CTRL`` Left Ctrl, CtrlL.
      * ``LEFT_ALT`` Left Alt, AltL.
      * ``LEFT_SHIFT`` Left Shift, ShiftL.
      * ``RIGHT_ALT`` Right Alt, AltR.
      * ``RIGHT_CTRL`` Right Ctrl, CtrlR.
      * ``RIGHT_SHIFT`` Right Shift, ShiftR.
      * ``OSKEY`` OS Key, Cmd.
      * ``GRLESS`` Grless.
      * ``ESC`` Esc.
      * ``TAB`` Tab.
      * ``RET`` Return, Enter.
      * ``SPACE`` Spacebar, Space.
      * ``LINE_FEED`` Line Feed.
      * ``BACK_SPACE`` Back Space, BkSpace.
      * ``DEL`` Delete, Del.
      * ``SEMI_COLON`` ;.
      * ``PERIOD`` ..
      * ``COMMA`` ,.
      * ``QUOTE`` ".
      * ``ACCENT_GRAVE`` \`.
      * ``MINUS`` -.
      * ``PLUS`` +.
      * ``SLASH`` /.
      * ``BACK_SLASH`` \\.
      * ``EQUAL`` =.
      * ``LEFT_BRACKET`` [.
      * ``RIGHT_BRACKET`` ].
      * ``LEFT_ARROW`` Left Arrow, ←.
      * ``DOWN_ARROW`` Down Arrow, ↓.
      * ``RIGHT_ARROW`` Right Arrow, →.
      * ``UP_ARROW`` Up Arrow, ↑.
      * ``NUMPAD_2`` Numpad 2, Pad2.
      * ``NUMPAD_4`` Numpad 4, Pad4.
      * ``NUMPAD_6`` Numpad 6, Pad6.
      * ``NUMPAD_8`` Numpad 8, Pad8.
      * ``NUMPAD_1`` Numpad 1, Pad1.
      * ``NUMPAD_3`` Numpad 3, Pad3.
      * ``NUMPAD_5`` Numpad 5, Pad5.
      * ``NUMPAD_7`` Numpad 7, Pad7.
      * ``NUMPAD_9`` Numpad 9, Pad9.
      * ``NUMPAD_PERIOD`` Numpad ., Pad..
      * ``NUMPAD_SLASH`` Numpad /, Pad/.
      * ``NUMPAD_ASTERIX`` Numpad \*, Pad\*.
      * ``NUMPAD_0`` Numpad 0, Pad0.
      * ``NUMPAD_MINUS`` Numpad -, Pad-.
      * ``NUMPAD_ENTER`` Numpad Enter, PadEnter.
      * ``NUMPAD_PLUS`` Numpad +, Pad+.
      * ``F1`` F1.
      * ``F2`` F2.
      * ``F3`` F3.
      * ``F4`` F4.
      * ``F5`` F5.
      * ``F6`` F6.
      * ``F7`` F7.
      * ``F8`` F8.
      * ``F9`` F9.
      * ``F10`` F10.
      * ``F11`` F11.
      * ``F12`` F12.
      * ``F13`` F13.
      * ``F14`` F14.
      * ``F15`` F15.
      * ``F16`` F16.
      * ``F17`` F17.
      * ``F18`` F18.
      * ``F19`` F19.
      * ``PAUSE`` Pause.
      * ``INSERT`` Insert, Ins.
      * ``HOME`` Home.
      * ``PAGE_UP`` Page Up, PgUp.
      * ``PAGE_DOWN`` Page Down, PgDown.
      * ``END`` End.
      * ``MEDIA_PLAY`` Media Play/Pause, >/\|\|.
      * ``MEDIA_STOP`` Media Stop, Stop.
      * ``MEDIA_FIRST`` Media First, \|<<.
      * ``MEDIA_LAST`` Media Last, >>\|.
      * ``TEXTINPUT`` Text Input, TxtIn.
      * ``WINDOW_DEACTIVATE`` Window Deactivate.
      * ``TIMER`` Timer, Tmr.
      * ``TIMER0`` Timer 0, Tmr0.
      * ``TIMER1`` Timer 1, Tmr1.
      * ``TIMER2`` Timer 2, Tmr2.
      * ``TIMER_JOBS`` Timer Jobs, TmrJob.
      * ``TIMER_AUTOSAVE`` Timer Autosave, TmrSave.
      * ``TIMER_REPORT`` Timer Report, TmrReport.
      * ``TIMERREGION`` Timer Region, TmrReg.
      * ``NDOF_MOTION`` NDOF Motion, NdofMov.
      * ``NDOF_BUTTON_MENU`` NDOF Menu, NdofMenu.
      * ``NDOF_BUTTON_FIT`` NDOF Fit, NdofFit.
      * ``NDOF_BUTTON_TOP`` NDOF Top, Ndof↑.
      * ``NDOF_BUTTON_BOTTOM`` NDOF Bottom, Ndof↓.
      * ``NDOF_BUTTON_LEFT`` NDOF Left, Ndof←.
      * ``NDOF_BUTTON_RIGHT`` NDOF Right, Ndof→.
      * ``NDOF_BUTTON_FRONT`` NDOF Front, NdofFront.
      * ``NDOF_BUTTON_BACK`` NDOF Back, NdofBack.
      * ``NDOF_BUTTON_ISO1`` NDOF Isometric 1, NdofIso1.
      * ``NDOF_BUTTON_ISO2`` NDOF Isometric 2, NdofIso2.
      * ``NDOF_BUTTON_ROLL_CW`` NDOF Roll CW, NdofRCW.
      * ``NDOF_BUTTON_ROLL_CCW`` NDOF Roll CCW, NdofRCCW.
      * ``NDOF_BUTTON_SPIN_CW`` NDOF Spin CW, NdofSCW.
      * ``NDOF_BUTTON_SPIN_CCW`` NDOF Spin CCW, NdofSCCW.
      * ``NDOF_BUTTON_TILT_CW`` NDOF Tilt CW, NdofTCW.
      * ``NDOF_BUTTON_TILT_CCW`` NDOF Tilt CCW, NdofTCCW.
      * ``NDOF_BUTTON_ROTATE`` NDOF Rotate, NdofRot.
      * ``NDOF_BUTTON_PANZOOM`` NDOF Pan/Zoom, NdofPanZoom.
      * ``NDOF_BUTTON_DOMINANT`` NDOF Dominant, NdofDom.
      * ``NDOF_BUTTON_PLUS`` NDOF Plus, Ndof+.
      * ``NDOF_BUTTON_MINUS`` NDOF Minus, Ndof-.
      * ``NDOF_BUTTON_ESC`` NDOF Esc, NdofEsc.
      * ``NDOF_BUTTON_ALT`` NDOF Alt, NdofAlt.
      * ``NDOF_BUTTON_SHIFT`` NDOF Shift, NdofShift.
      * ``NDOF_BUTTON_CTRL`` NDOF Ctrl, NdofCtrl.
      * ``NDOF_BUTTON_1`` NDOF Button 1, NdofB1.
      * ``NDOF_BUTTON_2`` NDOF Button 2, NdofB2.
      * ``NDOF_BUTTON_3`` NDOF Button 3, NdofB3.
      * ``NDOF_BUTTON_4`` NDOF Button 4, NdofB4.
      * ``NDOF_BUTTON_5`` NDOF Button 5, NdofB5.
      * ``NDOF_BUTTON_6`` NDOF Button 6, NdofB6.
      * ``NDOF_BUTTON_7`` NDOF Button 7, NdofB7.
      * ``NDOF_BUTTON_8`` NDOF Button 8, NdofB8.
      * ``NDOF_BUTTON_9`` NDOF Button 9, NdofB9.
      * ``NDOF_BUTTON_10`` NDOF Button 10, NdofB10.
      * ``NDOF_BUTTON_A`` NDOF Button A, NdofBA.
      * ``NDOF_BUTTON_B`` NDOF Button B, NdofBB.
      * ``NDOF_BUTTON_C`` NDOF Button C, NdofBC.

      :type: enum in ['NONE', 'LEFTMOUSE', 'MIDDLEMOUSE', 'RIGHTMOUSE', 'BUTTON4MOUSE', 'BUTTON5MOUSE', 'BUTTON6MOUSE', 'BUTTON7MOUSE', 'ACTIONMOUSE', 'SELECTMOUSE', 'PEN', 'ERASER', 'MOUSEMOVE', 'INBETWEEN_MOUSEMOVE', 'TRACKPADPAN', 'TRACKPADZOOM', 'MOUSEROTATE', 'WHEELUPMOUSE', 'WHEELDOWNMOUSE', 'WHEELINMOUSE', 'WHEELOUTMOUSE', 'EVT_TWEAK_L', 'EVT_TWEAK_M', 'EVT_TWEAK_R', 'EVT_TWEAK_A', 'EVT_TWEAK_S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'LEFT_CTRL', 'LEFT_ALT', 'LEFT_SHIFT', 'RIGHT_ALT', 'RIGHT_CTRL', 'RIGHT_SHIFT', 'OSKEY', 'GRLESS', 'ESC', 'TAB', 'RET', 'SPACE', 'LINE_FEED', 'BACK_SPACE', 'DEL', 'SEMI_COLON', 'PERIOD', 'COMMA', 'QUOTE', 'ACCENT_GRAVE', 'MINUS', 'PLUS', 'SLASH', 'BACK_SLASH', 'EQUAL', 'LEFT_BRACKET', 'RIGHT_BRACKET', 'LEFT_ARROW', 'DOWN_ARROW', 'RIGHT_ARROW', 'UP_ARROW', 'NUMPAD_2', 'NUMPAD_4', 'NUMPAD_6', 'NUMPAD_8', 'NUMPAD_1', 'NUMPAD_3', 'NUMPAD_5', 'NUMPAD_7', 'NUMPAD_9', 'NUMPAD_PERIOD', 'NUMPAD_SLASH', 'NUMPAD_ASTERIX', 'NUMPAD_0', 'NUMPAD_MINUS', 'NUMPAD_ENTER', 'NUMPAD_PLUS', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'PAUSE', 'INSERT', 'HOME', 'PAGE_UP', 'PAGE_DOWN', 'END', 'MEDIA_PLAY', 'MEDIA_STOP', 'MEDIA_FIRST', 'MEDIA_LAST', 'TEXTINPUT', 'WINDOW_DEACTIVATE', 'TIMER', 'TIMER0', 'TIMER1', 'TIMER2', 'TIMER_JOBS', 'TIMER_AUTOSAVE', 'TIMER_REPORT', 'TIMERREGION', 'NDOF_MOTION', 'NDOF_BUTTON_MENU', 'NDOF_BUTTON_FIT', 'NDOF_BUTTON_TOP', 'NDOF_BUTTON_BOTTOM', 'NDOF_BUTTON_LEFT', 'NDOF_BUTTON_RIGHT', 'NDOF_BUTTON_FRONT', 'NDOF_BUTTON_BACK', 'NDOF_BUTTON_ISO1', 'NDOF_BUTTON_ISO2', 'NDOF_BUTTON_ROLL_CW', 'NDOF_BUTTON_ROLL_CCW', 'NDOF_BUTTON_SPIN_CW', 'NDOF_BUTTON_SPIN_CCW', 'NDOF_BUTTON_TILT_CW', 'NDOF_BUTTON_TILT_CCW', 'NDOF_BUTTON_ROTATE', 'NDOF_BUTTON_PANZOOM', 'NDOF_BUTTON_DOMINANT', 'NDOF_BUTTON_PLUS', 'NDOF_BUTTON_MINUS', 'NDOF_BUTTON_ESC', 'NDOF_BUTTON_ALT', 'NDOF_BUTTON_SHIFT', 'NDOF_BUTTON_CTRL', 'NDOF_BUTTON_1', 'NDOF_BUTTON_2', 'NDOF_BUTTON_3', 'NDOF_BUTTON_4', 'NDOF_BUTTON_5', 'NDOF_BUTTON_6', 'NDOF_BUTTON_7', 'NDOF_BUTTON_8', 'NDOF_BUTTON_9', 'NDOF_BUTTON_10', 'NDOF_BUTTON_A', 'NDOF_BUTTON_B', 'NDOF_BUTTON_C'], default 'NONE'

   .. attribute:: map_type

      Type of event mapping

      :type: enum in ['KEYBOARD', 'TWEAK', 'MOUSE', 'NDOF', 'TEXTINPUT', 'TIMER'], default 'KEYBOARD'

   .. data:: name

      Name of operator (translated) to call on input event

      :type: string, default "", (readonly, never None)

   .. attribute:: oskey

      Operating system key pressed

      :type: boolean, default False

   .. data:: properties

      Properties to set when the operator is called

      :type: :class:`OperatorProperties`, (readonly)

   .. attribute:: propvalue

      The value this event translates to in a modal keymap

      :type: enum in ['NONE'], default 'NONE'

   .. attribute:: shift

      Shift key pressed

      :type: boolean, default False

   .. attribute:: show_expanded

      Show key map event and property details in the user interface

      :type: boolean, default False

   .. attribute:: type

      Type of event

      * ``NONE`` .
      * ``LEFTMOUSE`` Left Mouse, LMB.
      * ``MIDDLEMOUSE`` Middle Mouse, MMB.
      * ``RIGHTMOUSE`` Right Mouse, RMB.
      * ``BUTTON4MOUSE`` Button4 Mouse, MB4.
      * ``BUTTON5MOUSE`` Button5 Mouse, MB5.
      * ``BUTTON6MOUSE`` Button6 Mouse, MB6.
      * ``BUTTON7MOUSE`` Button7 Mouse, MB7.
      * ``ACTIONMOUSE`` Action Mouse, MBA.
      * ``SELECTMOUSE`` Select Mouse, MBS.
      * ``PEN`` Pen.
      * ``ERASER`` Eraser.
      * ``MOUSEMOVE`` Mouse Move, MsMov.
      * ``INBETWEEN_MOUSEMOVE`` In-between Move, MsSubMov.
      * ``TRACKPADPAN`` Mouse/Trackpad Pan, MsPan.
      * ``TRACKPADZOOM`` Mouse/Trackpad Zoom, MsZoom.
      * ``MOUSEROTATE`` Mouse/Trackpad Rotate, MsRot.
      * ``WHEELUPMOUSE`` Wheel Up, WhUp.
      * ``WHEELDOWNMOUSE`` Wheel Down, WhDown.
      * ``WHEELINMOUSE`` Wheel In, WhIn.
      * ``WHEELOUTMOUSE`` Wheel Out, WhOut.
      * ``EVT_TWEAK_L`` Tweak Left, TwkL.
      * ``EVT_TWEAK_M`` Tweak Middle, TwkM.
      * ``EVT_TWEAK_R`` Tweak Right, TwkR.
      * ``EVT_TWEAK_A`` Tweak Action, TwkA.
      * ``EVT_TWEAK_S`` Tweak Select, TwkS.
      * ``A`` A.
      * ``B`` B.
      * ``C`` C.
      * ``D`` D.
      * ``E`` E.
      * ``F`` F.
      * ``G`` G.
      * ``H`` H.
      * ``I`` I.
      * ``J`` J.
      * ``K`` K.
      * ``L`` L.
      * ``M`` M.
      * ``N`` N.
      * ``O`` O.
      * ``P`` P.
      * ``Q`` Q.
      * ``R`` R.
      * ``S`` S.
      * ``T`` T.
      * ``U`` U.
      * ``V`` V.
      * ``W`` W.
      * ``X`` X.
      * ``Y`` Y.
      * ``Z`` Z.
      * ``ZERO`` 0.
      * ``ONE`` 1.
      * ``TWO`` 2.
      * ``THREE`` 3.
      * ``FOUR`` 4.
      * ``FIVE`` 5.
      * ``SIX`` 6.
      * ``SEVEN`` 7.
      * ``EIGHT`` 8.
      * ``NINE`` 9.
      * ``LEFT_CTRL`` Left Ctrl, CtrlL.
      * ``LEFT_ALT`` Left Alt, AltL.
      * ``LEFT_SHIFT`` Left Shift, ShiftL.
      * ``RIGHT_ALT`` Right Alt, AltR.
      * ``RIGHT_CTRL`` Right Ctrl, CtrlR.
      * ``RIGHT_SHIFT`` Right Shift, ShiftR.
      * ``OSKEY`` OS Key, Cmd.
      * ``GRLESS`` Grless.
      * ``ESC`` Esc.
      * ``TAB`` Tab.
      * ``RET`` Return, Enter.
      * ``SPACE`` Spacebar, Space.
      * ``LINE_FEED`` Line Feed.
      * ``BACK_SPACE`` Back Space, BkSpace.
      * ``DEL`` Delete, Del.
      * ``SEMI_COLON`` ;.
      * ``PERIOD`` ..
      * ``COMMA`` ,.
      * ``QUOTE`` ".
      * ``ACCENT_GRAVE`` \`.
      * ``MINUS`` -.
      * ``PLUS`` +.
      * ``SLASH`` /.
      * ``BACK_SLASH`` \\.
      * ``EQUAL`` =.
      * ``LEFT_BRACKET`` [.
      * ``RIGHT_BRACKET`` ].
      * ``LEFT_ARROW`` Left Arrow, ←.
      * ``DOWN_ARROW`` Down Arrow, ↓.
      * ``RIGHT_ARROW`` Right Arrow, →.
      * ``UP_ARROW`` Up Arrow, ↑.
      * ``NUMPAD_2`` Numpad 2, Pad2.
      * ``NUMPAD_4`` Numpad 4, Pad4.
      * ``NUMPAD_6`` Numpad 6, Pad6.
      * ``NUMPAD_8`` Numpad 8, Pad8.
      * ``NUMPAD_1`` Numpad 1, Pad1.
      * ``NUMPAD_3`` Numpad 3, Pad3.
      * ``NUMPAD_5`` Numpad 5, Pad5.
      * ``NUMPAD_7`` Numpad 7, Pad7.
      * ``NUMPAD_9`` Numpad 9, Pad9.
      * ``NUMPAD_PERIOD`` Numpad ., Pad..
      * ``NUMPAD_SLASH`` Numpad /, Pad/.
      * ``NUMPAD_ASTERIX`` Numpad \*, Pad\*.
      * ``NUMPAD_0`` Numpad 0, Pad0.
      * ``NUMPAD_MINUS`` Numpad -, Pad-.
      * ``NUMPAD_ENTER`` Numpad Enter, PadEnter.
      * ``NUMPAD_PLUS`` Numpad +, Pad+.
      * ``F1`` F1.
      * ``F2`` F2.
      * ``F3`` F3.
      * ``F4`` F4.
      * ``F5`` F5.
      * ``F6`` F6.
      * ``F7`` F7.
      * ``F8`` F8.
      * ``F9`` F9.
      * ``F10`` F10.
      * ``F11`` F11.
      * ``F12`` F12.
      * ``F13`` F13.
      * ``F14`` F14.
      * ``F15`` F15.
      * ``F16`` F16.
      * ``F17`` F17.
      * ``F18`` F18.
      * ``F19`` F19.
      * ``PAUSE`` Pause.
      * ``INSERT`` Insert, Ins.
      * ``HOME`` Home.
      * ``PAGE_UP`` Page Up, PgUp.
      * ``PAGE_DOWN`` Page Down, PgDown.
      * ``END`` End.
      * ``MEDIA_PLAY`` Media Play/Pause, >/\|\|.
      * ``MEDIA_STOP`` Media Stop, Stop.
      * ``MEDIA_FIRST`` Media First, \|<<.
      * ``MEDIA_LAST`` Media Last, >>\|.
      * ``TEXTINPUT`` Text Input, TxtIn.
      * ``WINDOW_DEACTIVATE`` Window Deactivate.
      * ``TIMER`` Timer, Tmr.
      * ``TIMER0`` Timer 0, Tmr0.
      * ``TIMER1`` Timer 1, Tmr1.
      * ``TIMER2`` Timer 2, Tmr2.
      * ``TIMER_JOBS`` Timer Jobs, TmrJob.
      * ``TIMER_AUTOSAVE`` Timer Autosave, TmrSave.
      * ``TIMER_REPORT`` Timer Report, TmrReport.
      * ``TIMERREGION`` Timer Region, TmrReg.
      * ``NDOF_MOTION`` NDOF Motion, NdofMov.
      * ``NDOF_BUTTON_MENU`` NDOF Menu, NdofMenu.
      * ``NDOF_BUTTON_FIT`` NDOF Fit, NdofFit.
      * ``NDOF_BUTTON_TOP`` NDOF Top, Ndof↑.
      * ``NDOF_BUTTON_BOTTOM`` NDOF Bottom, Ndof↓.
      * ``NDOF_BUTTON_LEFT`` NDOF Left, Ndof←.
      * ``NDOF_BUTTON_RIGHT`` NDOF Right, Ndof→.
      * ``NDOF_BUTTON_FRONT`` NDOF Front, NdofFront.
      * ``NDOF_BUTTON_BACK`` NDOF Back, NdofBack.
      * ``NDOF_BUTTON_ISO1`` NDOF Isometric 1, NdofIso1.
      * ``NDOF_BUTTON_ISO2`` NDOF Isometric 2, NdofIso2.
      * ``NDOF_BUTTON_ROLL_CW`` NDOF Roll CW, NdofRCW.
      * ``NDOF_BUTTON_ROLL_CCW`` NDOF Roll CCW, NdofRCCW.
      * ``NDOF_BUTTON_SPIN_CW`` NDOF Spin CW, NdofSCW.
      * ``NDOF_BUTTON_SPIN_CCW`` NDOF Spin CCW, NdofSCCW.
      * ``NDOF_BUTTON_TILT_CW`` NDOF Tilt CW, NdofTCW.
      * ``NDOF_BUTTON_TILT_CCW`` NDOF Tilt CCW, NdofTCCW.
      * ``NDOF_BUTTON_ROTATE`` NDOF Rotate, NdofRot.
      * ``NDOF_BUTTON_PANZOOM`` NDOF Pan/Zoom, NdofPanZoom.
      * ``NDOF_BUTTON_DOMINANT`` NDOF Dominant, NdofDom.
      * ``NDOF_BUTTON_PLUS`` NDOF Plus, Ndof+.
      * ``NDOF_BUTTON_MINUS`` NDOF Minus, Ndof-.
      * ``NDOF_BUTTON_ESC`` NDOF Esc, NdofEsc.
      * ``NDOF_BUTTON_ALT`` NDOF Alt, NdofAlt.
      * ``NDOF_BUTTON_SHIFT`` NDOF Shift, NdofShift.
      * ``NDOF_BUTTON_CTRL`` NDOF Ctrl, NdofCtrl.
      * ``NDOF_BUTTON_1`` NDOF Button 1, NdofB1.
      * ``NDOF_BUTTON_2`` NDOF Button 2, NdofB2.
      * ``NDOF_BUTTON_3`` NDOF Button 3, NdofB3.
      * ``NDOF_BUTTON_4`` NDOF Button 4, NdofB4.
      * ``NDOF_BUTTON_5`` NDOF Button 5, NdofB5.
      * ``NDOF_BUTTON_6`` NDOF Button 6, NdofB6.
      * ``NDOF_BUTTON_7`` NDOF Button 7, NdofB7.
      * ``NDOF_BUTTON_8`` NDOF Button 8, NdofB8.
      * ``NDOF_BUTTON_9`` NDOF Button 9, NdofB9.
      * ``NDOF_BUTTON_10`` NDOF Button 10, NdofB10.
      * ``NDOF_BUTTON_A`` NDOF Button A, NdofBA.
      * ``NDOF_BUTTON_B`` NDOF Button B, NdofBB.
      * ``NDOF_BUTTON_C`` NDOF Button C, NdofBC.

      :type: enum in ['NONE', 'LEFTMOUSE', 'MIDDLEMOUSE', 'RIGHTMOUSE', 'BUTTON4MOUSE', 'BUTTON5MOUSE', 'BUTTON6MOUSE', 'BUTTON7MOUSE', 'ACTIONMOUSE', 'SELECTMOUSE', 'PEN', 'ERASER', 'MOUSEMOVE', 'INBETWEEN_MOUSEMOVE', 'TRACKPADPAN', 'TRACKPADZOOM', 'MOUSEROTATE', 'WHEELUPMOUSE', 'WHEELDOWNMOUSE', 'WHEELINMOUSE', 'WHEELOUTMOUSE', 'EVT_TWEAK_L', 'EVT_TWEAK_M', 'EVT_TWEAK_R', 'EVT_TWEAK_A', 'EVT_TWEAK_S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'LEFT_CTRL', 'LEFT_ALT', 'LEFT_SHIFT', 'RIGHT_ALT', 'RIGHT_CTRL', 'RIGHT_SHIFT', 'OSKEY', 'GRLESS', 'ESC', 'TAB', 'RET', 'SPACE', 'LINE_FEED', 'BACK_SPACE', 'DEL', 'SEMI_COLON', 'PERIOD', 'COMMA', 'QUOTE', 'ACCENT_GRAVE', 'MINUS', 'PLUS', 'SLASH', 'BACK_SLASH', 'EQUAL', 'LEFT_BRACKET', 'RIGHT_BRACKET', 'LEFT_ARROW', 'DOWN_ARROW', 'RIGHT_ARROW', 'UP_ARROW', 'NUMPAD_2', 'NUMPAD_4', 'NUMPAD_6', 'NUMPAD_8', 'NUMPAD_1', 'NUMPAD_3', 'NUMPAD_5', 'NUMPAD_7', 'NUMPAD_9', 'NUMPAD_PERIOD', 'NUMPAD_SLASH', 'NUMPAD_ASTERIX', 'NUMPAD_0', 'NUMPAD_MINUS', 'NUMPAD_ENTER', 'NUMPAD_PLUS', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'PAUSE', 'INSERT', 'HOME', 'PAGE_UP', 'PAGE_DOWN', 'END', 'MEDIA_PLAY', 'MEDIA_STOP', 'MEDIA_FIRST', 'MEDIA_LAST', 'TEXTINPUT', 'WINDOW_DEACTIVATE', 'TIMER', 'TIMER0', 'TIMER1', 'TIMER2', 'TIMER_JOBS', 'TIMER_AUTOSAVE', 'TIMER_REPORT', 'TIMERREGION', 'NDOF_MOTION', 'NDOF_BUTTON_MENU', 'NDOF_BUTTON_FIT', 'NDOF_BUTTON_TOP', 'NDOF_BUTTON_BOTTOM', 'NDOF_BUTTON_LEFT', 'NDOF_BUTTON_RIGHT', 'NDOF_BUTTON_FRONT', 'NDOF_BUTTON_BACK', 'NDOF_BUTTON_ISO1', 'NDOF_BUTTON_ISO2', 'NDOF_BUTTON_ROLL_CW', 'NDOF_BUTTON_ROLL_CCW', 'NDOF_BUTTON_SPIN_CW', 'NDOF_BUTTON_SPIN_CCW', 'NDOF_BUTTON_TILT_CW', 'NDOF_BUTTON_TILT_CCW', 'NDOF_BUTTON_ROTATE', 'NDOF_BUTTON_PANZOOM', 'NDOF_BUTTON_DOMINANT', 'NDOF_BUTTON_PLUS', 'NDOF_BUTTON_MINUS', 'NDOF_BUTTON_ESC', 'NDOF_BUTTON_ALT', 'NDOF_BUTTON_SHIFT', 'NDOF_BUTTON_CTRL', 'NDOF_BUTTON_1', 'NDOF_BUTTON_2', 'NDOF_BUTTON_3', 'NDOF_BUTTON_4', 'NDOF_BUTTON_5', 'NDOF_BUTTON_6', 'NDOF_BUTTON_7', 'NDOF_BUTTON_8', 'NDOF_BUTTON_9', 'NDOF_BUTTON_10', 'NDOF_BUTTON_A', 'NDOF_BUTTON_B', 'NDOF_BUTTON_C'], default 'NONE'

   .. attribute:: value

      :type: enum in ['ANY', 'NOTHING', 'PRESS', 'RELEASE', 'CLICK', 'DOUBLE_CLICK', 'NORTH', 'NORTH_EAST', 'EAST', 'SOUTH_EAST', 'SOUTH', 'SOUTH_WEST', 'WEST', 'NORTH_WEST'], default 'NOTHING'

   .. method:: compare(item)

      compare

      :arg item:

         Item

      :type item: :class:`KeyMapItem`
      :return:

         Comparison result

      :rtype: boolean

   .. classmethod:: bl_rna_get_subclass(id, default=None)
   
      :arg id: The RNA type identifier.
      :type id: string
      :return: The RNA type or default when not found.
      :rtype: :class:`bpy.types.Struct` subclass


   .. classmethod:: bl_rna_get_subclass_py(id, default=None)
   
      :arg id: The RNA type identifier.
      :type id: string
      :return: The class or default when not found.
      :rtype: type


.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`

.. rubric:: Inherited Functions

.. hlist::
   :columns: 2

   * :class:`bpy_struct.as_pointer`
   * :class:`bpy_struct.driver_add`
   * :class:`bpy_struct.driver_remove`
   * :class:`bpy_struct.get`
   * :class:`bpy_struct.is_property_hidden`
   * :class:`bpy_struct.is_property_readonly`
   * :class:`bpy_struct.is_property_set`
   * :class:`bpy_struct.items`
   * :class:`bpy_struct.keyframe_delete`
   * :class:`bpy_struct.keyframe_insert`
   * :class:`bpy_struct.keys`
   * :class:`bpy_struct.path_from_id`
   * :class:`bpy_struct.path_resolve`
   * :class:`bpy_struct.property_unset`
   * :class:`bpy_struct.type_recast`
   * :class:`bpy_struct.values`

.. rubric:: References

.. hlist::
   :columns: 2

   * :class:`KeyMap.keymap_items`
   * :class:`KeyMap.restore_item_to_default`
   * :class:`KeyMapItem.compare`
   * :class:`KeyMapItems.from_id`
   * :class:`KeyMapItems.new`
   * :class:`KeyMapItems.new_modal`
   * :class:`KeyMapItems.remove`
   * :class:`UILayout.template_keymap_item_properties`

