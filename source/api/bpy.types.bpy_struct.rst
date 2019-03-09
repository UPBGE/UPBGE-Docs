bpy_struct
==========

.. module:: bpy.types

subclasses --- 
:class:`ActionFCurves`, :class:`ActionGroup`, :class:`ActionGroups`, :class:`ActionPoseMarkers`, :class:`Actuator`, :class:`Addon`, :class:`AddonPreferences`, :class:`Addons`, :class:`AlembicObjectPath`, :class:`AlembicObjectPaths`, :class:`AnimData`, :class:`AnimDataDrivers`, :class:`AnimViz`, :class:`AnimVizMotionPaths`, :class:`AnimVizOnionSkinning`, :class:`AnyType`, :class:`Area`, :class:`AreaSpaces`, :class:`ArmatureBones`, :class:`ArmatureEditBones`, :class:`BackgroundImage`, :class:`BackgroundImages`, :class:`BakePixel`, :class:`BakeSettings`, :class:`BezierSplinePoint`, :class:`BlendData`, :class:`BlendDataActions`, :class:`BlendDataArmatures`, :class:`BlendDataBrushes`, :class:`BlendDataCacheFiles`, :class:`BlendDataCameras`, :class:`BlendDataCurves`, :class:`BlendDataFonts`, :class:`BlendDataGreasePencils`, :class:`BlendDataGroups`, :class:`BlendDataImages`, :class:`BlendDataLamps`, :class:`BlendDataLattices`, :class:`BlendDataLibraries`, :class:`BlendDataLineStyles`, :class:`BlendDataMasks`, :class:`BlendDataMaterials`, :class:`BlendDataMeshes`, :class:`BlendDataMetaBalls`, :class:`BlendDataMovieClips`, :class:`BlendDataNodeTrees`, :class:`BlendDataObjects`, :class:`BlendDataPaintCurves`, :class:`BlendDataPalettes`, :class:`BlendDataParticles`, :class:`BlendDataScenes`, :class:`BlendDataScreens`, :class:`BlendDataSounds`, :class:`BlendDataSpeakers`, :class:`BlendDataTexts`, :class:`BlendDataTextures`, :class:`BlendDataWindowManagers`, :class:`BlendDataWorlds`, :class:`BlenderRNA`, :class:`BoidRule`, :class:`BoidSettings`, :class:`BoidState`, :class:`Bone`, :class:`BoneGroup`, :class:`BoneGroups`, :class:`BrushCapabilities`, :class:`CameraStereoData`, :class:`ChannelDriverVariables`, :class:`ChildParticle`, :class:`ClothCollisionSettings`, :class:`ClothSettings`, :class:`ClothSolverResult`, :class:`CollisionSettings`, :class:`ColorManagedDisplaySettings`, :class:`ColorManagedInputColorspaceSettings`, :class:`ColorManagedSequencerColorspaceSettings`, :class:`ColorManagedViewSettings`, :class:`ColorMapping`, :class:`ColorRamp`, :class:`ColorRampElement`, :class:`ColorRampElements`, :class:`CompositorNodeOutputFileFileSlots`, :class:`CompositorNodeOutputFileLayerSlots`, :class:`ConsoleLine`, :class:`Constraint`, :class:`ConstraintTarget`, :class:`Context`, :class:`Controller`, :class:`CurveMap`, :class:`CurveMapPoint`, :class:`CurveMapPoints`, :class:`CurveMapping`, :class:`CurvePaintSettings`, :class:`CurveSplines`, :class:`CyclesCameraSettings`, :class:`CyclesCurveRenderSettings`, :class:`CyclesCurveSettings`, :class:`CyclesLampSettings`, :class:`CyclesMaterialSettings`, :class:`CyclesMeshSettings`, :class:`CyclesObjectSettings`, :class:`CyclesRenderLayerSettings`, :class:`CyclesRenderSettings`, :class:`CyclesVisibilitySettings`, :class:`CyclesWorldSettings`, :class:`Depsgraph`, :class:`DisplaySafeAreas`, :class:`DopeSheet`, :class:`Driver`, :class:`DriverTarget`, :class:`DriverVariable`, :class:`DupliObject`, :class:`DynamicPaintBrushSettings`, :class:`DynamicPaintCanvasSettings`, :class:`DynamicPaintSurface`, :class:`DynamicPaintSurfaces`, :class:`EditBone`, :class:`EffectorWeights`, :class:`EnumPropertyItem`, :class:`EnvironmentMap`, :class:`Event`, :class:`FCurve`, :class:`FCurveKeyframePoints`, :class:`FCurveModifiers`, :class:`FCurveSample`, :class:`FFmpegSettings`, :class:`FModifier`, :class:`FModifierEnvelopeControlPoint`, :class:`FModifierEnvelopeControlPoints`, :class:`FieldSettings`, :class:`FileBrowserFSMenuEntry`, :class:`FileSelectParams`, :class:`FluidSettings`, :class:`FluidVertexVelocity`, :class:`FreestyleLineSet`, :class:`FreestyleModuleSettings`, :class:`FreestyleModules`, :class:`FreestyleSettings`, :class:`Function`, :class:`GPUDOFSettings`, :class:`GPUFXSettings`, :class:`GPUSSAOSettings`, :class:`GPencilBrush`, :class:`GPencilFrame`, :class:`GPencilFrames`, :class:`GPencilInterpolateSettings`, :class:`GPencilLayer`, :class:`GPencilPalette`, :class:`GPencilPaletteColor`, :class:`GPencilPaletteColors`, :class:`GPencilSculptBrush`, :class:`GPencilSculptSettings`, :class:`GPencilStroke`, :class:`GPencilStrokePoint`, :class:`GPencilStrokePoints`, :class:`GPencilStrokes`, :class:`GPencilTriangle`, :class:`GameCameraViewportData`, :class:`GameObjectSettings`, :class:`GameProperty`, :class:`GameSoftBodySettings`, :class:`GreasePencilBrushes`, :class:`GreasePencilLayers`, :class:`GreasePencilPalettes`, :class:`GroupObjects`, :class:`Header`, :class:`Histogram`, :class:`ID`, :class:`IDMaterials`, :class:`IKParam`, :class:`ImageFormatSettings`, :class:`ImagePackedFile`, :class:`ImagePreview`, :class:`ImageUser`, :class:`ImapaintToolCapabilities`, :class:`KeyConfig`, :class:`KeyConfigurations`, :class:`KeyMap`, :class:`KeyMapItem`, :class:`KeyMapItems`, :class:`KeyMaps`, :class:`Keyframe`, :class:`KeyingSet`, :class:`KeyingSetInfo`, :class:`KeyingSetPath`, :class:`KeyingSetPaths`, :class:`KeyingSets`, :class:`KeyingSetsAll`, :class:`LampSkySettings`, :class:`LampTextureSlots`, :class:`LatticePoint`, :class:`LineStyleAlphaModifiers`, :class:`LineStyleColorModifiers`, :class:`LineStyleGeometryModifiers`, :class:`LineStyleModifier`, :class:`LineStyleTextureSlots`, :class:`LineStyleThicknessModifiers`, :class:`Linesets`, :class:`LodLevel`, :class:`LoopColors`, :class:`Macro`, :class:`MaskLayer`, :class:`MaskLayers`, :class:`MaskParent`, :class:`MaskSpline`, :class:`MaskSplinePoint`, :class:`MaskSplinePointUW`, :class:`MaskSplinePoints`, :class:`MaskSplines`, :class:`MaterialGameSettings`, :class:`MaterialHalo`, :class:`MaterialRaytraceMirror`, :class:`MaterialRaytraceTransparency`, :class:`MaterialSlot`, :class:`MaterialStrand`, :class:`MaterialSubsurfaceScattering`, :class:`MaterialTextureSlots`, :class:`MaterialVolume`, :class:`Menu`, :class:`MeshColor`, :class:`MeshColorLayer`, :class:`MeshEdge`, :class:`MeshEdges`, :class:`MeshLoop`, :class:`MeshLoopColor`, :class:`MeshLoopColorLayer`, :class:`MeshLoops`, :class:`MeshPaintMaskLayer`, :class:`MeshPaintMaskProperty`, :class:`MeshPolygon`, :class:`MeshPolygonFloatProperty`, :class:`MeshPolygonFloatPropertyLayer`, :class:`MeshPolygonIntProperty`, :class:`MeshPolygonIntPropertyLayer`, :class:`MeshPolygonStringProperty`, :class:`MeshPolygonStringPropertyLayer`, :class:`MeshPolygons`, :class:`MeshSkinVertex`, :class:`MeshSkinVertexLayer`, :class:`MeshStatVis`, :class:`MeshTessFace`, :class:`MeshTessFaces`, :class:`MeshTextureFace`, :class:`MeshTextureFaceLayer`, :class:`MeshTexturePoly`, :class:`MeshTexturePolyLayer`, :class:`MeshUVLoop`, :class:`MeshUVLoopLayer`, :class:`MeshVertex`, :class:`MeshVertexFloatProperty`, :class:`MeshVertexFloatPropertyLayer`, :class:`MeshVertexIntProperty`, :class:`MeshVertexIntPropertyLayer`, :class:`MeshVertexStringProperty`, :class:`MeshVertexStringPropertyLayer`, :class:`MeshVertices`, :class:`MetaBallElements`, :class:`MetaElement`, :class:`Modifier`, :class:`MotionPath`, :class:`MotionPathVert`, :class:`MovieClipProxy`, :class:`MovieClipScopes`, :class:`MovieClipUser`, :class:`MovieReconstructedCamera`, :class:`MovieTracking`, :class:`MovieTrackingCamera`, :class:`MovieTrackingDopesheet`, :class:`MovieTrackingMarker`, :class:`MovieTrackingMarkers`, :class:`MovieTrackingObject`, :class:`MovieTrackingObjectPlaneTracks`, :class:`MovieTrackingObjectTracks`, :class:`MovieTrackingObjects`, :class:`MovieTrackingPlaneMarker`, :class:`MovieTrackingPlaneMarkers`, :class:`MovieTrackingPlaneTrack`, :class:`MovieTrackingPlaneTracks`, :class:`MovieTrackingReconstructedCameras`, :class:`MovieTrackingReconstruction`, :class:`MovieTrackingSettings`, :class:`MovieTrackingStabilization`, :class:`MovieTrackingTrack`, :class:`MovieTrackingTracks`, :class:`NlaStrip`, :class:`NlaStripFCurves`, :class:`NlaStrips`, :class:`NlaTrack`, :class:`NlaTracks`, :class:`Node`, :class:`NodeInputs`, :class:`NodeInstanceHash`, :class:`NodeInternalSocketTemplate`, :class:`NodeLink`, :class:`NodeLinks`, :class:`NodeOutputFileSlotFile`, :class:`NodeOutputFileSlotLayer`, :class:`NodeOutputs`, :class:`NodeSetting`, :class:`NodeSocket`, :class:`NodeSocketInterface`, :class:`NodeTreeInputs`, :class:`NodeTreeOutputs`, :class:`NodeTreePath`, :class:`Nodes`, :class:`ObjectActivityCulling`, :class:`ObjectBase`, :class:`ObjectConstraints`, :class:`ObjectModifiers`, :class:`OceanTexData`, :class:`Operator`, :class:`OperatorMacro`, :class:`OperatorOptions`, :class:`OperatorProperties`, :class:`PackedFile`, :class:`Paint`, :class:`PaletteColor`, :class:`PaletteColors`, :class:`Panel`, :class:`Particle`, :class:`ParticleBrush`, :class:`ParticleDupliWeight`, :class:`ParticleEdit`, :class:`ParticleHairKey`, :class:`ParticleKey`, :class:`ParticleSettingsTextureSlots`, :class:`ParticleSystem`, :class:`ParticleSystems`, :class:`ParticleTarget`, :class:`PathCompare`, :class:`PathCompareCollection`, :class:`PointCache`, :class:`PointCaches`, :class:`PointDensity`, :class:`PolygonFloatProperties`, :class:`PolygonIntProperties`, :class:`PolygonStringProperties`, :class:`Pose`, :class:`PoseBone`, :class:`PoseBoneConstraints`, :class:`Property`, :class:`PropertyGroup`, :class:`PropertyGroupItem`, :class:`PythonComponent`, :class:`PythonComponentProperty`, :class:`Region`, :class:`RegionView3D`, :class:`RenderEngine`, :class:`RenderLayer`, :class:`RenderLayers`, :class:`RenderPass`, :class:`RenderPasses`, :class:`RenderResult`, :class:`RenderSettings`, :class:`RenderSlot`, :class:`RenderSlots`, :class:`RenderView`, :class:`RenderViews`, :class:`RigidBodyConstraint`, :class:`RigidBodyObject`, :class:`RigidBodyWorld`, :class:`SPHFluidSettings`, :class:`SceneBases`, :class:`SceneGameData`, :class:`SceneGameRecastData`, :class:`SceneObjects`, :class:`SceneRenderLayer`, :class:`SceneRenderView`, :class:`Scopes`, :class:`SculptToolCapabilities`, :class:`Sensor`, :class:`Sequence`, :class:`SequenceColorBalanceData`, :class:`SequenceCrop`, :class:`SequenceEditor`, :class:`SequenceElement`, :class:`SequenceElements`, :class:`SequenceModifier`, :class:`SequenceModifiers`, :class:`SequenceProxy`, :class:`SequenceTransform`, :class:`Sequences`, :class:`ShapeKey`, :class:`ShapeKeyBezierPoint`, :class:`ShapeKeyCurvePoint`, :class:`ShapeKeyPoint`, :class:`SmokeCollSettings`, :class:`SmokeDomainSettings`, :class:`SmokeFlowSettings`, :class:`SoftBodySettings`, :class:`Space`, :class:`SpaceNodeEditorPath`, :class:`SpaceUVEditor`, :class:`Spline`, :class:`SplineBezierPoints`, :class:`SplinePoint`, :class:`SplinePoints`, :class:`Stereo3dDisplay`, :class:`Stereo3dFormat`, :class:`Struct`, :class:`TessfaceUVTextures`, :class:`TexMapping`, :class:`TexPaintSlot`, :class:`TextBox`, :class:`TextCharacterFormat`, :class:`TextLine`, :class:`TextureSlot`, :class:`Theme`, :class:`ThemeBoneColorSet`, :class:`ThemeClipEditor`, :class:`ThemeConsole`, :class:`ThemeDopeSheet`, :class:`ThemeFileBrowser`, :class:`ThemeFontStyle`, :class:`ThemeGradientColors`, :class:`ThemeGraphEditor`, :class:`ThemeImageEditor`, :class:`ThemeInfo`, :class:`ThemeLogicEditor`, :class:`ThemeNLAEditor`, :class:`ThemeNodeEditor`, :class:`ThemeOutliner`, :class:`ThemePanelColors`, :class:`ThemeProperties`, :class:`ThemeSequenceEditor`, :class:`ThemeSpaceGeneric`, :class:`ThemeSpaceGradient`, :class:`ThemeSpaceListGeneric`, :class:`ThemeStyle`, :class:`ThemeTextEditor`, :class:`ThemeTimeline`, :class:`ThemeUserInterface`, :class:`ThemeUserPreferences`, :class:`ThemeView3D`, :class:`ThemeWidgetColors`, :class:`ThemeWidgetStateColors`, :class:`TimelineMarker`, :class:`TimelineMarkers`, :class:`Timer`, :class:`ToolSettings`, :class:`TransformOrientation`, :class:`UILayout`, :class:`UIList`, :class:`UIPieMenu`, :class:`UIPopupMenu`, :class:`UVLoopLayers`, :class:`UVProjector`, :class:`UVTextures`, :class:`UnifiedPaintSettings`, :class:`UnitSettings`, :class:`UnknownType`, :class:`UserPreferences`, :class:`UserPreferencesEdit`, :class:`UserPreferencesFilePaths`, :class:`UserPreferencesInput`, :class:`UserPreferencesSystem`, :class:`UserPreferencesView`, :class:`UserSolidLight`, :class:`VertexColors`, :class:`VertexFloatProperties`, :class:`VertexGroup`, :class:`VertexGroupElement`, :class:`VertexGroups`, :class:`VertexIntProperties`, :class:`VertexStringProperties`, :class:`View2D`, :class:`VoxelData`, :class:`WalkNavigation`, :class:`Window`, :class:`WorldLighting`, :class:`WorldMistSettings`, :class:`WorldTextureSlots`

.. class:: bpy_struct

   built-in base class for all classes in bpy.types.

   .. note::

      Note that bpy.types.bpy_struct is not actually available from within Blender,
      it only exists for the purpose of documentation.

   .. method:: as_pointer()
   
      Returns the memory address which holds a pointer to blenders internal data
   
      :return: int (memory address).
      :rtype: int
   
      .. note:: This is intended only for advanced script writers who need to
         pass blender data to their own C/Python modules.


   .. method:: driver_add(path, index=-1)
   
      Adds driver(s) to the given property
   
      :arg path: path to the property to drive, analogous to the fcurve's data path.
      :type path: string
      :arg index: array index of the property drive. Defaults to -1 for all indices or a single channel if the property is not an array.
      :type index: int
      :return: The driver(s) added.
      :rtype: :class:`bpy.types.FCurve` or list if index is -1 with an array property.


   .. method:: driver_remove(path, index=-1)
   
      Remove driver(s) from the given property
   
      :arg path: path to the property to drive, analogous to the fcurve's data path.
      :type path: string
      :arg index: array index of the property drive. Defaults to -1 for all indices or a single channel if the property is not an array.
      :type index: int
      :return: Success of driver removal.
      :rtype: boolean


   .. method:: get(key, default=None)
   
      Returns the value of the custom property assigned to key or default
      when not found (matches pythons dictionary function of the same name).
   
      :arg key: The key associated with the custom property.
      :type key: string
      :arg default: Optional argument for the value to return if
         *key* is not found.
      :type default: Undefined
   
      .. note::
   
         Only :class:`bpy.types.ID`, :class:`bpy.types.Bone` and 
         :class:`bpy.types.PoseBone` classes support custom properties.


   .. method:: is_property_hidden(property)
   
      Check if a property is hidden.
   
      :return: True when the property is hidden.
      :rtype: boolean


   .. method:: is_property_readonly(property)
   
      Check if a property is readonly.
   
      :return: True when the property is readonly (not writable).
      :rtype: boolean


   .. method:: is_property_set(property)
   
      Check if a property is set, use for testing operator properties.
   
      :return: True when the property has been set.
      :rtype: boolean


   .. method:: items()
   
      Returns the items of this objects custom properties (matches pythons
      dictionary function of the same name).
   
      :return: custom property key, value pairs.
      :rtype: list of key, value tuples
   
      .. note::
   
         Only :class:`bpy.types.ID`, :class:`bpy.types.Bone` and 
         :class:`bpy.types.PoseBone` classes support custom properties.


   .. method:: keyframe_delete(data_path, index=-1, frame=bpy.context.scene.frame_current, group="")
   
      Remove a keyframe from this properties fcurve.
   
      :arg data_path: path to the property to remove a key, analogous to the fcurve's data path.
      :type data_path: string
      :arg index: array index of the property to remove a key. Defaults to -1 removing all indices or a single channel if the property is not an array.
      :type index: int
      :arg frame: The frame on which the keyframe is deleted, defaulting to the current frame.
      :type frame: float
      :arg group: The name of the group the F-Curve should be added to if it doesn't exist yet.
      :type group: str
      :return: Success of keyframe deleation.
      :rtype: boolean


   .. method:: keyframe_insert(data_path, index=-1, frame=bpy.context.scene.frame_current, group="")
   
      Insert a keyframe on the property given, adding fcurves and animation data when necessary.
   
      :arg data_path: path to the property to key, analogous to the fcurve's data path.
      :type data_path: string
      :arg index: array index of the property to key.
         Defaults to -1 which will key all indices or a single channel if the property is not an array.
      :type index: int
      :arg frame: The frame on which the keyframe is inserted, defaulting to the current frame.
      :type frame: float
      :arg group: The name of the group the F-Curve should be added to if it doesn't exist yet.
      :type group: str
      :arg options: Optional flags:
   
         - ``INSERTKEY_NEEDED`` Only insert keyframes where they're needed in the relevant F-Curves.
         - ``INSERTKEY_VISUAL`` Insert keyframes based on 'visual transforms'.
         - ``INSERTKEY_XYZ_TO_RGB`` Color for newly added transformation F-Curves (Location, Rotation, Scale)
            and also Color is based on the transform axis.
      :type flag: set
      :return: Success of keyframe insertion.
      :rtype: boolean

      This is the most simple example of inserting a keyframe from python.

      .. literalinclude:: ..\examples\bpy.types.bpy_struct.keyframe_insert.py
         :lines: 4-

      Note that when keying data paths which contain nested properties this must be
      done from the :class:`ID` subclass, in this case the :class:`Armature` rather
      than the bone.

      .. literalinclude:: ..\examples\bpy.types.bpy_struct.keyframe_insert.1.py
         :lines: 6-


   .. method:: keys()
   
      Returns the keys of this objects custom properties (matches pythons
      dictionary function of the same name).
   
      :return: custom property keys.
      :rtype: list of strings
   
      .. note::
   
         Only :class:`bpy.types.ID`, :class:`bpy.types.Bone` and 
         :class:`bpy.types.PoseBone` classes support custom properties.


   .. method:: path_from_id(property="")
   
      Returns the data path from the ID to this object (string).
   
      :arg property: Optional property name which can be used if the path is
         to a property of this object.
      :type property: string
      :return: The path from :class:`bpy.types.bpy_struct.id_data`
         to this struct and property (when given).
      :rtype: str


   .. method:: path_resolve(path, coerce=True)
   
      Returns the property from the path, raise an exception when not found.
   
      :arg path: path which this property resolves.
      :type path: string
      :arg coerce: optional argument, when True, the property will be converted
         into its python representation.
      :type coerce: boolean


   .. method:: property_unset(property)
   
      Unset a property, will use default value afterward.


   .. method:: type_recast()
   
      Return a new instance, this is needed because types
      such as textures can be changed at runtime.
   
      :return: a new instance of this object with the type initialized again.
      :rtype: subclass of :class:`bpy.types.bpy_struct`


   .. method:: values()
   
      Returns the values of this objects custom properties (matches pythons
      dictionary function of the same name).
   
      :return: custom property values.
      :rtype: list
   
      .. note::
   
         Only :class:`bpy.types.ID`, :class:`bpy.types.Bone` and 
         :class:`bpy.types.PoseBone` classes support custom properties.


   .. attribute:: id_data

      The :class:`bpy.types.ID` object this datablock is from or None, (not available for all data types)


