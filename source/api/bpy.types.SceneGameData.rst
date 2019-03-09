SceneGameData(bpy_struct)
=========================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: SceneGameData(bpy_struct)

   Game data for a Scene data-block

   .. attribute:: deactivation_angular_threshold

      Angular velocity that an object must be below before the deactivation timer can start

      :type: float in [0.001, 10000], default 1.0

   .. attribute:: deactivation_linear_threshold

      Linear velocity that an object must be below before the deactivation timer can start

      :type: float in [0.001, 10000], default 0.8

   .. attribute:: deactivation_time

      Amount of time (in seconds) after which objects with a velocity less than the given threshold will deactivate (0.0 means no deactivation)

      :type: float in [0, 60], default 0.0

   .. attribute:: depth

      Display bit depth of full screen display

      :type: int in [8, 32], default 32

   .. attribute:: exit_key

      The key that exits the Game Engine

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

      :type: enum in ['NONE', 'LEFTMOUSE', 'MIDDLEMOUSE', 'RIGHTMOUSE', 'BUTTON4MOUSE', 'BUTTON5MOUSE', 'BUTTON6MOUSE', 'BUTTON7MOUSE', 'ACTIONMOUSE', 'SELECTMOUSE', 'PEN', 'ERASER', 'MOUSEMOVE', 'INBETWEEN_MOUSEMOVE', 'TRACKPADPAN', 'TRACKPADZOOM', 'MOUSEROTATE', 'WHEELUPMOUSE', 'WHEELDOWNMOUSE', 'WHEELINMOUSE', 'WHEELOUTMOUSE', 'EVT_TWEAK_L', 'EVT_TWEAK_M', 'EVT_TWEAK_R', 'EVT_TWEAK_A', 'EVT_TWEAK_S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'LEFT_CTRL', 'LEFT_ALT', 'LEFT_SHIFT', 'RIGHT_ALT', 'RIGHT_CTRL', 'RIGHT_SHIFT', 'OSKEY', 'GRLESS', 'ESC', 'TAB', 'RET', 'SPACE', 'LINE_FEED', 'BACK_SPACE', 'DEL', 'SEMI_COLON', 'PERIOD', 'COMMA', 'QUOTE', 'ACCENT_GRAVE', 'MINUS', 'PLUS', 'SLASH', 'BACK_SLASH', 'EQUAL', 'LEFT_BRACKET', 'RIGHT_BRACKET', 'LEFT_ARROW', 'DOWN_ARROW', 'RIGHT_ARROW', 'UP_ARROW', 'NUMPAD_2', 'NUMPAD_4', 'NUMPAD_6', 'NUMPAD_8', 'NUMPAD_1', 'NUMPAD_3', 'NUMPAD_5', 'NUMPAD_7', 'NUMPAD_9', 'NUMPAD_PERIOD', 'NUMPAD_SLASH', 'NUMPAD_ASTERIX', 'NUMPAD_0', 'NUMPAD_MINUS', 'NUMPAD_ENTER', 'NUMPAD_PLUS', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'PAUSE', 'INSERT', 'HOME', 'PAGE_UP', 'PAGE_DOWN', 'END', 'MEDIA_PLAY', 'MEDIA_STOP', 'MEDIA_FIRST', 'MEDIA_LAST', 'TEXTINPUT', 'WINDOW_DEACTIVATE', 'TIMER', 'TIMER0', 'TIMER1', 'TIMER2', 'TIMER_JOBS', 'TIMER_AUTOSAVE', 'TIMER_REPORT', 'TIMERREGION', 'NDOF_MOTION', 'NDOF_BUTTON_MENU', 'NDOF_BUTTON_FIT', 'NDOF_BUTTON_TOP', 'NDOF_BUTTON_BOTTOM', 'NDOF_BUTTON_LEFT', 'NDOF_BUTTON_RIGHT', 'NDOF_BUTTON_FRONT', 'NDOF_BUTTON_BACK', 'NDOF_BUTTON_ISO1', 'NDOF_BUTTON_ISO2', 'NDOF_BUTTON_ROLL_CW', 'NDOF_BUTTON_ROLL_CCW', 'NDOF_BUTTON_SPIN_CW', 'NDOF_BUTTON_SPIN_CCW', 'NDOF_BUTTON_TILT_CW', 'NDOF_BUTTON_TILT_CCW', 'NDOF_BUTTON_ROTATE', 'NDOF_BUTTON_PANZOOM', 'NDOF_BUTTON_DOMINANT', 'NDOF_BUTTON_PLUS', 'NDOF_BUTTON_MINUS', 'NDOF_BUTTON_ESC', 'NDOF_BUTTON_ALT', 'NDOF_BUTTON_SHIFT', 'NDOF_BUTTON_CTRL', 'NDOF_BUTTON_1', 'NDOF_BUTTON_2', 'NDOF_BUTTON_3', 'NDOF_BUTTON_4', 'NDOF_BUTTON_5', 'NDOF_BUTTON_6', 'NDOF_BUTTON_7', 'NDOF_BUTTON_8', 'NDOF_BUTTON_9', 'NDOF_BUTTON_10', 'NDOF_BUTTON_A', 'NDOF_BUTTON_B', 'NDOF_BUTTON_C'], default 'ESC'

   .. attribute:: fps

      Nominal number of game frames per second (physics fixed timestep = 1/fps, independently of actual frame rate)

      :type: int in [1, 10000], default 60

   .. attribute:: frame_color

      Set color of the bars

      :type: float array of 3 items in [0, 1], default (0.0, 0.0, 0.0)

   .. attribute:: frame_type

      Select the type of Framing you want

      * ``LETTERBOX`` Letterbox, Show the entire viewport in the display window, using bar horizontally or vertically.
      * ``EXTEND`` Extend, Show the entire viewport in the display window, viewing more horizontally or vertically.
      * ``SCALE`` Scale, Stretch or squeeze the viewport to fill the display window.

      :type: enum in ['LETTERBOX', 'EXTEND', 'SCALE'], default 'LETTERBOX'

   .. attribute:: frequency

      Display clock frequency of fullscreen display

      :type: int in [4, 2000], default 60

   .. attribute:: hdr

      The precision of screen display

      * ``HDR_NONE`` None, 8 bits per channel.
      * ``HDR_HALF_FLOAT`` Half, 16 bits per channel.
      * ``HDR_FULL_FLOAT`` Full, 32 bits per channel.

      :type: enum in ['HDR_NONE', 'HDR_HALF_FLOAT', 'HDR_FULL_FLOAT'], default 'HDR_NONE'

   .. attribute:: level_height

      Max difference in heights of obstacles to enable their interaction

      :type: float in [0, 200], default 2.0

   .. attribute:: logic_step_max

      Maximum number of logic frame per game frame if graphics slows down the game, higher value allows better synchronization with physics

      :type: int in [1, 10000], default 5

   .. attribute:: obstacle_simulation

      Simulation used for obstacle avoidance in the game engine

      :type: enum in ['NONE', 'RVO_RAYS', 'RVO_CELLS'], default 'NONE'

   .. attribute:: occlusion_culling_resolution

      Size of the occlusion buffer, use higher value for better precision (slower)

      :type: int in [128, 1024], default 128

   .. attribute:: physics_engine

      Physics engine used for physics simulation in the game engine

      * ``NONE`` None, Don't use a physics engine.
      * ``BULLET`` Bullet, Use the Bullet physics engine.

      :type: enum in ['NONE', 'BULLET'], default 'BULLET'

   .. attribute:: physics_gravity

      Gravitational constant used for physics simulation in the game engine

      :type: float in [0, 10000], default 9.8

   .. attribute:: physics_solver

      Physics constraint solver

      * ``SOLVER_SEQUENTIAL`` Sequential, Sequential physics solver, default solver.
      * ``SOLVER_NNGC`` NNGC, NNGC physics solver.
      * ``SOLVER_MLCP_DANTZIG`` MLCP Dantzig, MLCP Dantzig physics solver.
      * ``SOLVER_MLCP_LEMKE`` MLCP Lemke, MLCP Lemke physics solver.

      :type: enum in ['SOLVER_SEQUENTIAL', 'SOLVER_NNGC', 'SOLVER_MLCP_DANTZIG', 'SOLVER_MLCP_LEMKE'], default 'SOLVER_SEQUENTIAL'

   .. attribute:: physics_step_max

      Maximum number of physics step per game frame if graphics slows down the game, higher value allows physics to keep up with realtime

      :type: int in [1, 10000], default 5

   .. attribute:: physics_step_sub

      Number of simulation substep per physic timestep, higher value give better physics precision

      :type: int in [1, 50], default 1

   .. attribute:: python_console_key1

      First python console shortcut key

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

      :type: enum in ['NONE', 'LEFTMOUSE', 'MIDDLEMOUSE', 'RIGHTMOUSE', 'BUTTON4MOUSE', 'BUTTON5MOUSE', 'BUTTON6MOUSE', 'BUTTON7MOUSE', 'ACTIONMOUSE', 'SELECTMOUSE', 'PEN', 'ERASER', 'MOUSEMOVE', 'INBETWEEN_MOUSEMOVE', 'TRACKPADPAN', 'TRACKPADZOOM', 'MOUSEROTATE', 'WHEELUPMOUSE', 'WHEELDOWNMOUSE', 'WHEELINMOUSE', 'WHEELOUTMOUSE', 'EVT_TWEAK_L', 'EVT_TWEAK_M', 'EVT_TWEAK_R', 'EVT_TWEAK_A', 'EVT_TWEAK_S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'LEFT_CTRL', 'LEFT_ALT', 'LEFT_SHIFT', 'RIGHT_ALT', 'RIGHT_CTRL', 'RIGHT_SHIFT', 'OSKEY', 'GRLESS', 'ESC', 'TAB', 'RET', 'SPACE', 'LINE_FEED', 'BACK_SPACE', 'DEL', 'SEMI_COLON', 'PERIOD', 'COMMA', 'QUOTE', 'ACCENT_GRAVE', 'MINUS', 'PLUS', 'SLASH', 'BACK_SLASH', 'EQUAL', 'LEFT_BRACKET', 'RIGHT_BRACKET', 'LEFT_ARROW', 'DOWN_ARROW', 'RIGHT_ARROW', 'UP_ARROW', 'NUMPAD_2', 'NUMPAD_4', 'NUMPAD_6', 'NUMPAD_8', 'NUMPAD_1', 'NUMPAD_3', 'NUMPAD_5', 'NUMPAD_7', 'NUMPAD_9', 'NUMPAD_PERIOD', 'NUMPAD_SLASH', 'NUMPAD_ASTERIX', 'NUMPAD_0', 'NUMPAD_MINUS', 'NUMPAD_ENTER', 'NUMPAD_PLUS', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'PAUSE', 'INSERT', 'HOME', 'PAGE_UP', 'PAGE_DOWN', 'END', 'MEDIA_PLAY', 'MEDIA_STOP', 'MEDIA_FIRST', 'MEDIA_LAST', 'TEXTINPUT', 'WINDOW_DEACTIVATE', 'TIMER', 'TIMER0', 'TIMER1', 'TIMER2', 'TIMER_JOBS', 'TIMER_AUTOSAVE', 'TIMER_REPORT', 'TIMERREGION', 'NDOF_MOTION', 'NDOF_BUTTON_MENU', 'NDOF_BUTTON_FIT', 'NDOF_BUTTON_TOP', 'NDOF_BUTTON_BOTTOM', 'NDOF_BUTTON_LEFT', 'NDOF_BUTTON_RIGHT', 'NDOF_BUTTON_FRONT', 'NDOF_BUTTON_BACK', 'NDOF_BUTTON_ISO1', 'NDOF_BUTTON_ISO2', 'NDOF_BUTTON_ROLL_CW', 'NDOF_BUTTON_ROLL_CCW', 'NDOF_BUTTON_SPIN_CW', 'NDOF_BUTTON_SPIN_CCW', 'NDOF_BUTTON_TILT_CW', 'NDOF_BUTTON_TILT_CCW', 'NDOF_BUTTON_ROTATE', 'NDOF_BUTTON_PANZOOM', 'NDOF_BUTTON_DOMINANT', 'NDOF_BUTTON_PLUS', 'NDOF_BUTTON_MINUS', 'NDOF_BUTTON_ESC', 'NDOF_BUTTON_ALT', 'NDOF_BUTTON_SHIFT', 'NDOF_BUTTON_CTRL', 'NDOF_BUTTON_1', 'NDOF_BUTTON_2', 'NDOF_BUTTON_3', 'NDOF_BUTTON_4', 'NDOF_BUTTON_5', 'NDOF_BUTTON_6', 'NDOF_BUTTON_7', 'NDOF_BUTTON_8', 'NDOF_BUTTON_9', 'NDOF_BUTTON_10', 'NDOF_BUTTON_A', 'NDOF_BUTTON_B', 'NDOF_BUTTON_C'], default 'LEFT_CTRL'

   .. attribute:: python_console_key2

      Second python console shortcut key

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

      :type: enum in ['NONE', 'LEFTMOUSE', 'MIDDLEMOUSE', 'RIGHTMOUSE', 'BUTTON4MOUSE', 'BUTTON5MOUSE', 'BUTTON6MOUSE', 'BUTTON7MOUSE', 'ACTIONMOUSE', 'SELECTMOUSE', 'PEN', 'ERASER', 'MOUSEMOVE', 'INBETWEEN_MOUSEMOVE', 'TRACKPADPAN', 'TRACKPADZOOM', 'MOUSEROTATE', 'WHEELUPMOUSE', 'WHEELDOWNMOUSE', 'WHEELINMOUSE', 'WHEELOUTMOUSE', 'EVT_TWEAK_L', 'EVT_TWEAK_M', 'EVT_TWEAK_R', 'EVT_TWEAK_A', 'EVT_TWEAK_S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'LEFT_CTRL', 'LEFT_ALT', 'LEFT_SHIFT', 'RIGHT_ALT', 'RIGHT_CTRL', 'RIGHT_SHIFT', 'OSKEY', 'GRLESS', 'ESC', 'TAB', 'RET', 'SPACE', 'LINE_FEED', 'BACK_SPACE', 'DEL', 'SEMI_COLON', 'PERIOD', 'COMMA', 'QUOTE', 'ACCENT_GRAVE', 'MINUS', 'PLUS', 'SLASH', 'BACK_SLASH', 'EQUAL', 'LEFT_BRACKET', 'RIGHT_BRACKET', 'LEFT_ARROW', 'DOWN_ARROW', 'RIGHT_ARROW', 'UP_ARROW', 'NUMPAD_2', 'NUMPAD_4', 'NUMPAD_6', 'NUMPAD_8', 'NUMPAD_1', 'NUMPAD_3', 'NUMPAD_5', 'NUMPAD_7', 'NUMPAD_9', 'NUMPAD_PERIOD', 'NUMPAD_SLASH', 'NUMPAD_ASTERIX', 'NUMPAD_0', 'NUMPAD_MINUS', 'NUMPAD_ENTER', 'NUMPAD_PLUS', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'PAUSE', 'INSERT', 'HOME', 'PAGE_UP', 'PAGE_DOWN', 'END', 'MEDIA_PLAY', 'MEDIA_STOP', 'MEDIA_FIRST', 'MEDIA_LAST', 'TEXTINPUT', 'WINDOW_DEACTIVATE', 'TIMER', 'TIMER0', 'TIMER1', 'TIMER2', 'TIMER_JOBS', 'TIMER_AUTOSAVE', 'TIMER_REPORT', 'TIMERREGION', 'NDOF_MOTION', 'NDOF_BUTTON_MENU', 'NDOF_BUTTON_FIT', 'NDOF_BUTTON_TOP', 'NDOF_BUTTON_BOTTOM', 'NDOF_BUTTON_LEFT', 'NDOF_BUTTON_RIGHT', 'NDOF_BUTTON_FRONT', 'NDOF_BUTTON_BACK', 'NDOF_BUTTON_ISO1', 'NDOF_BUTTON_ISO2', 'NDOF_BUTTON_ROLL_CW', 'NDOF_BUTTON_ROLL_CCW', 'NDOF_BUTTON_SPIN_CW', 'NDOF_BUTTON_SPIN_CCW', 'NDOF_BUTTON_TILT_CW', 'NDOF_BUTTON_TILT_CCW', 'NDOF_BUTTON_ROTATE', 'NDOF_BUTTON_PANZOOM', 'NDOF_BUTTON_DOMINANT', 'NDOF_BUTTON_PLUS', 'NDOF_BUTTON_MINUS', 'NDOF_BUTTON_ESC', 'NDOF_BUTTON_ALT', 'NDOF_BUTTON_SHIFT', 'NDOF_BUTTON_CTRL', 'NDOF_BUTTON_1', 'NDOF_BUTTON_2', 'NDOF_BUTTON_3', 'NDOF_BUTTON_4', 'NDOF_BUTTON_5', 'NDOF_BUTTON_6', 'NDOF_BUTTON_7', 'NDOF_BUTTON_8', 'NDOF_BUTTON_9', 'NDOF_BUTTON_10', 'NDOF_BUTTON_A', 'NDOF_BUTTON_B', 'NDOF_BUTTON_C'], default 'LEFT_SHIFT'

   .. attribute:: python_console_key3

      Third python console shortcut key

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

      :type: enum in ['NONE', 'LEFTMOUSE', 'MIDDLEMOUSE', 'RIGHTMOUSE', 'BUTTON4MOUSE', 'BUTTON5MOUSE', 'BUTTON6MOUSE', 'BUTTON7MOUSE', 'ACTIONMOUSE', 'SELECTMOUSE', 'PEN', 'ERASER', 'MOUSEMOVE', 'INBETWEEN_MOUSEMOVE', 'TRACKPADPAN', 'TRACKPADZOOM', 'MOUSEROTATE', 'WHEELUPMOUSE', 'WHEELDOWNMOUSE', 'WHEELINMOUSE', 'WHEELOUTMOUSE', 'EVT_TWEAK_L', 'EVT_TWEAK_M', 'EVT_TWEAK_R', 'EVT_TWEAK_A', 'EVT_TWEAK_S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'LEFT_CTRL', 'LEFT_ALT', 'LEFT_SHIFT', 'RIGHT_ALT', 'RIGHT_CTRL', 'RIGHT_SHIFT', 'OSKEY', 'GRLESS', 'ESC', 'TAB', 'RET', 'SPACE', 'LINE_FEED', 'BACK_SPACE', 'DEL', 'SEMI_COLON', 'PERIOD', 'COMMA', 'QUOTE', 'ACCENT_GRAVE', 'MINUS', 'PLUS', 'SLASH', 'BACK_SLASH', 'EQUAL', 'LEFT_BRACKET', 'RIGHT_BRACKET', 'LEFT_ARROW', 'DOWN_ARROW', 'RIGHT_ARROW', 'UP_ARROW', 'NUMPAD_2', 'NUMPAD_4', 'NUMPAD_6', 'NUMPAD_8', 'NUMPAD_1', 'NUMPAD_3', 'NUMPAD_5', 'NUMPAD_7', 'NUMPAD_9', 'NUMPAD_PERIOD', 'NUMPAD_SLASH', 'NUMPAD_ASTERIX', 'NUMPAD_0', 'NUMPAD_MINUS', 'NUMPAD_ENTER', 'NUMPAD_PLUS', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'PAUSE', 'INSERT', 'HOME', 'PAGE_UP', 'PAGE_DOWN', 'END', 'MEDIA_PLAY', 'MEDIA_STOP', 'MEDIA_FIRST', 'MEDIA_LAST', 'TEXTINPUT', 'WINDOW_DEACTIVATE', 'TIMER', 'TIMER0', 'TIMER1', 'TIMER2', 'TIMER_JOBS', 'TIMER_AUTOSAVE', 'TIMER_REPORT', 'TIMERREGION', 'NDOF_MOTION', 'NDOF_BUTTON_MENU', 'NDOF_BUTTON_FIT', 'NDOF_BUTTON_TOP', 'NDOF_BUTTON_BOTTOM', 'NDOF_BUTTON_LEFT', 'NDOF_BUTTON_RIGHT', 'NDOF_BUTTON_FRONT', 'NDOF_BUTTON_BACK', 'NDOF_BUTTON_ISO1', 'NDOF_BUTTON_ISO2', 'NDOF_BUTTON_ROLL_CW', 'NDOF_BUTTON_ROLL_CCW', 'NDOF_BUTTON_SPIN_CW', 'NDOF_BUTTON_SPIN_CCW', 'NDOF_BUTTON_TILT_CW', 'NDOF_BUTTON_TILT_CCW', 'NDOF_BUTTON_ROTATE', 'NDOF_BUTTON_PANZOOM', 'NDOF_BUTTON_DOMINANT', 'NDOF_BUTTON_PLUS', 'NDOF_BUTTON_MINUS', 'NDOF_BUTTON_ESC', 'NDOF_BUTTON_ALT', 'NDOF_BUTTON_SHIFT', 'NDOF_BUTTON_CTRL', 'NDOF_BUTTON_1', 'NDOF_BUTTON_2', 'NDOF_BUTTON_3', 'NDOF_BUTTON_4', 'NDOF_BUTTON_5', 'NDOF_BUTTON_6', 'NDOF_BUTTON_7', 'NDOF_BUTTON_8', 'NDOF_BUTTON_9', 'NDOF_BUTTON_10', 'NDOF_BUTTON_A', 'NDOF_BUTTON_B', 'NDOF_BUTTON_C'], default 'LEFT_ALT'

   .. attribute:: python_console_key4

      Fourth python console shortcut key

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

      :type: enum in ['NONE', 'LEFTMOUSE', 'MIDDLEMOUSE', 'RIGHTMOUSE', 'BUTTON4MOUSE', 'BUTTON5MOUSE', 'BUTTON6MOUSE', 'BUTTON7MOUSE', 'ACTIONMOUSE', 'SELECTMOUSE', 'PEN', 'ERASER', 'MOUSEMOVE', 'INBETWEEN_MOUSEMOVE', 'TRACKPADPAN', 'TRACKPADZOOM', 'MOUSEROTATE', 'WHEELUPMOUSE', 'WHEELDOWNMOUSE', 'WHEELINMOUSE', 'WHEELOUTMOUSE', 'EVT_TWEAK_L', 'EVT_TWEAK_M', 'EVT_TWEAK_R', 'EVT_TWEAK_A', 'EVT_TWEAK_S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'LEFT_CTRL', 'LEFT_ALT', 'LEFT_SHIFT', 'RIGHT_ALT', 'RIGHT_CTRL', 'RIGHT_SHIFT', 'OSKEY', 'GRLESS', 'ESC', 'TAB', 'RET', 'SPACE', 'LINE_FEED', 'BACK_SPACE', 'DEL', 'SEMI_COLON', 'PERIOD', 'COMMA', 'QUOTE', 'ACCENT_GRAVE', 'MINUS', 'PLUS', 'SLASH', 'BACK_SLASH', 'EQUAL', 'LEFT_BRACKET', 'RIGHT_BRACKET', 'LEFT_ARROW', 'DOWN_ARROW', 'RIGHT_ARROW', 'UP_ARROW', 'NUMPAD_2', 'NUMPAD_4', 'NUMPAD_6', 'NUMPAD_8', 'NUMPAD_1', 'NUMPAD_3', 'NUMPAD_5', 'NUMPAD_7', 'NUMPAD_9', 'NUMPAD_PERIOD', 'NUMPAD_SLASH', 'NUMPAD_ASTERIX', 'NUMPAD_0', 'NUMPAD_MINUS', 'NUMPAD_ENTER', 'NUMPAD_PLUS', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'PAUSE', 'INSERT', 'HOME', 'PAGE_UP', 'PAGE_DOWN', 'END', 'MEDIA_PLAY', 'MEDIA_STOP', 'MEDIA_FIRST', 'MEDIA_LAST', 'TEXTINPUT', 'WINDOW_DEACTIVATE', 'TIMER', 'TIMER0', 'TIMER1', 'TIMER2', 'TIMER_JOBS', 'TIMER_AUTOSAVE', 'TIMER_REPORT', 'TIMERREGION', 'NDOF_MOTION', 'NDOF_BUTTON_MENU', 'NDOF_BUTTON_FIT', 'NDOF_BUTTON_TOP', 'NDOF_BUTTON_BOTTOM', 'NDOF_BUTTON_LEFT', 'NDOF_BUTTON_RIGHT', 'NDOF_BUTTON_FRONT', 'NDOF_BUTTON_BACK', 'NDOF_BUTTON_ISO1', 'NDOF_BUTTON_ISO2', 'NDOF_BUTTON_ROLL_CW', 'NDOF_BUTTON_ROLL_CCW', 'NDOF_BUTTON_SPIN_CW', 'NDOF_BUTTON_SPIN_CCW', 'NDOF_BUTTON_TILT_CW', 'NDOF_BUTTON_TILT_CCW', 'NDOF_BUTTON_ROTATE', 'NDOF_BUTTON_PANZOOM', 'NDOF_BUTTON_DOMINANT', 'NDOF_BUTTON_PLUS', 'NDOF_BUTTON_MINUS', 'NDOF_BUTTON_ESC', 'NDOF_BUTTON_ALT', 'NDOF_BUTTON_SHIFT', 'NDOF_BUTTON_CTRL', 'NDOF_BUTTON_1', 'NDOF_BUTTON_2', 'NDOF_BUTTON_3', 'NDOF_BUTTON_4', 'NDOF_BUTTON_5', 'NDOF_BUTTON_6', 'NDOF_BUTTON_7', 'NDOF_BUTTON_8', 'NDOF_BUTTON_9', 'NDOF_BUTTON_10', 'NDOF_BUTTON_A', 'NDOF_BUTTON_B', 'NDOF_BUTTON_C'], default 'T'

   .. data:: recast_data

      :type: :class:`SceneGameRecastData`, (readonly, never None)

   .. attribute:: resolution_x

      Number of horizontal pixels in the screen

      :type: int in [4, 10000], default 640

   .. attribute:: resolution_y

      Number of vertical pixels in the screen

      :type: int in [4, 10000], default 480

   .. attribute:: samples

      The number of AA Samples to use for MSAA

      :type: enum in ['SAMPLES_0', 'SAMPLES_2', 'SAMPLES_4', 'SAMPLES_8', 'SAMPLES_16'], default 'SAMPLES_0'

   .. attribute:: scene_hysteresis_percentage

      Minimum distance change required to transition to the previous level of detail

      :type: int in [0, 100], default 10

   .. attribute:: show_armatures

      Show a visualization of armatures

      * ``DISABLE`` Disable, Disable debugging.
      * ``FORCE`` Force, Force debugging.
      * ``ALLOW`` Allow, Allow debugging from individual settings.

      :type: enum in ['DISABLE', 'FORCE', 'ALLOW'], default 'DISABLE'

   .. attribute:: show_bounding_box

      Show a visualization of bounding volume box

      * ``DISABLE`` Disable, Disable debugging.
      * ``FORCE`` Force, Force debugging.
      * ``ALLOW`` Allow, Allow debugging from individual settings.

      :type: enum in ['DISABLE', 'FORCE', 'ALLOW'], default 'DISABLE'

   .. attribute:: show_camera_frustum

      Show a visualization of the camera frustum according to the current viewport dimensions

      * ``DISABLE`` Disable, Disable debugging.
      * ``FORCE`` Force, Force debugging.
      * ``ALLOW`` Allow, Allow debugging from individual settings.

      :type: enum in ['DISABLE', 'FORCE', 'ALLOW'], default 'DISABLE'

   .. attribute:: show_debug_properties

      Show properties marked for debugging while the game runs

      :type: boolean, default False

   .. attribute:: show_framerate_profile

      Show framerate and profiling information while the game runs

      :type: boolean, default False

   .. attribute:: show_fullscreen

      Start player in a new fullscreen display

      :type: boolean, default False

   .. attribute:: show_mouse

      Start player with a visible mouse cursor

      :type: boolean, default False

   .. attribute:: show_obstacle_simulation

      Enable debug visualization for obstacle simulation

      :type: boolean, default False

   .. attribute:: show_physics_visualization

      Show a visualization of physics bounds and interactions

      :type: boolean, default False

   .. attribute:: show_render_queries

      Show render queries information while the game runs

      :type: boolean, default False

   .. attribute:: show_shadow_frustum

      Show a visualization of the light shadow frustum

      * ``DISABLE`` Disable, Disable debugging.
      * ``FORCE`` Force, Force debugging.
      * ``ALLOW`` Allow, Allow debugging from individual settings.

      :type: enum in ['DISABLE', 'FORCE', 'ALLOW'], default 'DISABLE'

   .. attribute:: stereo

      * ``NONE`` None, Disable Stereo and Dome environments.
      * ``STEREO`` Stereo, Enable Stereo environment.

      :type: enum in ['NONE', 'STEREO'], default 'NONE'

   .. attribute:: stereo_eye_separation

      Set the distance between the eyes - the camera focal distance/30 should be fine

      :type: float in [0.01, 5], default 0.1

   .. attribute:: stereo_mode

      Stereographic techniques

      :type: enum in ['QUADBUFFERED', 'ABOVEBELOW', 'INTERLACED', 'ANAGLYPH', 'SIDEBYSIDE', 'VINTERLACE', '3DTVTOPBOTTOM'], default 'ANAGLYPH'

   .. attribute:: time_scale

      Time scale to slow down or speed up animations and physics in game

      :type: float in [0.001, 10000], default 1.0

   .. attribute:: use_activity_culling

      Enable object activity culling in this scene

      :type: boolean, default False

   .. attribute:: use_auto_start

      Automatically start game at load time

      :type: boolean, default False

   .. attribute:: use_deprecation_warnings

      Print warnings when using deprecated features in the python API

      :type: boolean, default False

   .. attribute:: use_desktop

      Use the current desktop resolution in fullscreen mode

      :type: boolean, default False

   .. attribute:: use_frame_rate

      Respect the frame rate from the Physics panel in the world properties rather than rendering as many frames as possible

      :type: boolean, default False

   .. attribute:: use_glsl_color_management

      Use color management for GLSL rendering

      :type: boolean, default False

   .. attribute:: use_glsl_environment_lighting

      Use environment lighting for GLSL rendering

      :type: boolean, default False

   .. attribute:: use_glsl_extra_textures

      Use extra textures like normal or specular maps for GLSL rendering

      :type: boolean, default False

   .. attribute:: use_glsl_lights

      Use lights for GLSL rendering

      :type: boolean, default False

   .. attribute:: use_glsl_nodes

      Use nodes for GLSL rendering

      :type: boolean, default False

   .. attribute:: use_glsl_ramps

      Use ramps for GLSL rendering

      :type: boolean, default False

   .. attribute:: use_glsl_shaders

      Use shaders for GLSL rendering

      :type: boolean, default False

   .. attribute:: use_glsl_shadows

      Use shadows for GLSL rendering

      :type: boolean, default False

   .. attribute:: use_occlusion_culling

      Use optimized Bullet DBVT tree for view frustum and occlusion culling (more efficient, but it can waste unnecessary CPU if the scene doesn't have occluder objects)

      :type: boolean, default False

   .. attribute:: use_python_console

      Create a python interpreter console in game

      :type: boolean, default False

   .. attribute:: use_restrict_animation_updates

      Restrict the number of animation updates to the animation FPS (this is better for performance, but can cause issues with smooth playback)

      :type: boolean, default False

   .. attribute:: use_scene_hysteresis

      Use LoD Hysteresis setting for the scene

      :type: boolean, default False

   .. attribute:: vsync

      Change vsync settings

      * ``OFF`` Off, Disable vsync.
      * ``ON`` On, Enable vsync.
      * ``ADAPTIVE`` Adaptive, Enable adaptive vsync (if supported).

      :type: enum in ['OFF', 'ON', 'ADAPTIVE'], default 'ON'

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

   * :class:`Scene.game_settings`

