NodeInternalSocketTemplate(bpy_struct)
======================================

.. module:: bpy.types

base class --- :class:`bpy_struct`

.. class:: NodeInternalSocketTemplate(bpy_struct)

   Type and default value of a node socket

   .. data:: identifier

      Identifier of the socket

      :type: string, default "", (readonly, never None)

   .. data:: name

      Name of the socket

      :type: string, default "", (readonly, never None)

   .. data:: type

      Data type of the socket

      :type: enum in ['CUSTOM', 'VALUE', 'INT', 'BOOLEAN', 'VECTOR', 'STRING', 'RGBA', 'SHADER'], default 'VALUE', (readonly)

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

   * :class:`CompositorNodeAlphaOver.input_template`
   * :class:`CompositorNodeAlphaOver.output_template`
   * :class:`CompositorNodeBilateralblur.input_template`
   * :class:`CompositorNodeBilateralblur.output_template`
   * :class:`CompositorNodeBlur.input_template`
   * :class:`CompositorNodeBlur.output_template`
   * :class:`CompositorNodeBokehBlur.input_template`
   * :class:`CompositorNodeBokehBlur.output_template`
   * :class:`CompositorNodeBokehImage.input_template`
   * :class:`CompositorNodeBokehImage.output_template`
   * :class:`CompositorNodeBoxMask.input_template`
   * :class:`CompositorNodeBoxMask.output_template`
   * :class:`CompositorNodeBrightContrast.input_template`
   * :class:`CompositorNodeBrightContrast.output_template`
   * :class:`CompositorNodeChannelMatte.input_template`
   * :class:`CompositorNodeChannelMatte.output_template`
   * :class:`CompositorNodeChromaMatte.input_template`
   * :class:`CompositorNodeChromaMatte.output_template`
   * :class:`CompositorNodeColorBalance.input_template`
   * :class:`CompositorNodeColorBalance.output_template`
   * :class:`CompositorNodeColorCorrection.input_template`
   * :class:`CompositorNodeColorCorrection.output_template`
   * :class:`CompositorNodeColorMatte.input_template`
   * :class:`CompositorNodeColorMatte.output_template`
   * :class:`CompositorNodeColorSpill.input_template`
   * :class:`CompositorNodeColorSpill.output_template`
   * :class:`CompositorNodeCombHSVA.input_template`
   * :class:`CompositorNodeCombHSVA.output_template`
   * :class:`CompositorNodeCombRGBA.input_template`
   * :class:`CompositorNodeCombRGBA.output_template`
   * :class:`CompositorNodeCombYCCA.input_template`
   * :class:`CompositorNodeCombYCCA.output_template`
   * :class:`CompositorNodeCombYUVA.input_template`
   * :class:`CompositorNodeCombYUVA.output_template`
   * :class:`CompositorNodeComposite.input_template`
   * :class:`CompositorNodeComposite.output_template`
   * :class:`CompositorNodeCornerPin.input_template`
   * :class:`CompositorNodeCornerPin.output_template`
   * :class:`CompositorNodeCrop.input_template`
   * :class:`CompositorNodeCrop.output_template`
   * :class:`CompositorNodeCurveRGB.input_template`
   * :class:`CompositorNodeCurveRGB.output_template`
   * :class:`CompositorNodeCurveVec.input_template`
   * :class:`CompositorNodeCurveVec.output_template`
   * :class:`CompositorNodeDBlur.input_template`
   * :class:`CompositorNodeDBlur.output_template`
   * :class:`CompositorNodeDefocus.input_template`
   * :class:`CompositorNodeDefocus.output_template`
   * :class:`CompositorNodeDespeckle.input_template`
   * :class:`CompositorNodeDespeckle.output_template`
   * :class:`CompositorNodeDiffMatte.input_template`
   * :class:`CompositorNodeDiffMatte.output_template`
   * :class:`CompositorNodeDilateErode.input_template`
   * :class:`CompositorNodeDilateErode.output_template`
   * :class:`CompositorNodeDisplace.input_template`
   * :class:`CompositorNodeDisplace.output_template`
   * :class:`CompositorNodeDistanceMatte.input_template`
   * :class:`CompositorNodeDistanceMatte.output_template`
   * :class:`CompositorNodeDoubleEdgeMask.input_template`
   * :class:`CompositorNodeDoubleEdgeMask.output_template`
   * :class:`CompositorNodeEllipseMask.input_template`
   * :class:`CompositorNodeEllipseMask.output_template`
   * :class:`CompositorNodeFilter.input_template`
   * :class:`CompositorNodeFilter.output_template`
   * :class:`CompositorNodeFlip.input_template`
   * :class:`CompositorNodeFlip.output_template`
   * :class:`CompositorNodeGamma.input_template`
   * :class:`CompositorNodeGamma.output_template`
   * :class:`CompositorNodeGlare.input_template`
   * :class:`CompositorNodeGlare.output_template`
   * :class:`CompositorNodeGroup.input_template`
   * :class:`CompositorNodeGroup.output_template`
   * :class:`CompositorNodeHueCorrect.input_template`
   * :class:`CompositorNodeHueCorrect.output_template`
   * :class:`CompositorNodeHueSat.input_template`
   * :class:`CompositorNodeHueSat.output_template`
   * :class:`CompositorNodeIDMask.input_template`
   * :class:`CompositorNodeIDMask.output_template`
   * :class:`CompositorNodeImage.input_template`
   * :class:`CompositorNodeImage.output_template`
   * :class:`CompositorNodeInpaint.input_template`
   * :class:`CompositorNodeInpaint.output_template`
   * :class:`CompositorNodeInvert.input_template`
   * :class:`CompositorNodeInvert.output_template`
   * :class:`CompositorNodeKeying.input_template`
   * :class:`CompositorNodeKeying.output_template`
   * :class:`CompositorNodeKeyingScreen.input_template`
   * :class:`CompositorNodeKeyingScreen.output_template`
   * :class:`CompositorNodeLensdist.input_template`
   * :class:`CompositorNodeLensdist.output_template`
   * :class:`CompositorNodeLevels.input_template`
   * :class:`CompositorNodeLevels.output_template`
   * :class:`CompositorNodeLumaMatte.input_template`
   * :class:`CompositorNodeLumaMatte.output_template`
   * :class:`CompositorNodeMapRange.input_template`
   * :class:`CompositorNodeMapRange.output_template`
   * :class:`CompositorNodeMapUV.input_template`
   * :class:`CompositorNodeMapUV.output_template`
   * :class:`CompositorNodeMapValue.input_template`
   * :class:`CompositorNodeMapValue.output_template`
   * :class:`CompositorNodeMask.input_template`
   * :class:`CompositorNodeMask.output_template`
   * :class:`CompositorNodeMath.input_template`
   * :class:`CompositorNodeMath.output_template`
   * :class:`CompositorNodeMixRGB.input_template`
   * :class:`CompositorNodeMixRGB.output_template`
   * :class:`CompositorNodeMovieClip.input_template`
   * :class:`CompositorNodeMovieClip.output_template`
   * :class:`CompositorNodeMovieDistortion.input_template`
   * :class:`CompositorNodeMovieDistortion.output_template`
   * :class:`CompositorNodeNormal.input_template`
   * :class:`CompositorNodeNormal.output_template`
   * :class:`CompositorNodeNormalize.input_template`
   * :class:`CompositorNodeNormalize.output_template`
   * :class:`CompositorNodeOutputFile.input_template`
   * :class:`CompositorNodeOutputFile.output_template`
   * :class:`CompositorNodePixelate.input_template`
   * :class:`CompositorNodePixelate.output_template`
   * :class:`CompositorNodePlaneTrackDeform.input_template`
   * :class:`CompositorNodePlaneTrackDeform.output_template`
   * :class:`CompositorNodePremulKey.input_template`
   * :class:`CompositorNodePremulKey.output_template`
   * :class:`CompositorNodeRGB.input_template`
   * :class:`CompositorNodeRGB.output_template`
   * :class:`CompositorNodeRGBToBW.input_template`
   * :class:`CompositorNodeRGBToBW.output_template`
   * :class:`CompositorNodeRLayers.input_template`
   * :class:`CompositorNodeRLayers.output_template`
   * :class:`CompositorNodeRotate.input_template`
   * :class:`CompositorNodeRotate.output_template`
   * :class:`CompositorNodeScale.input_template`
   * :class:`CompositorNodeScale.output_template`
   * :class:`CompositorNodeSepHSVA.input_template`
   * :class:`CompositorNodeSepHSVA.output_template`
   * :class:`CompositorNodeSepRGBA.input_template`
   * :class:`CompositorNodeSepRGBA.output_template`
   * :class:`CompositorNodeSepYCCA.input_template`
   * :class:`CompositorNodeSepYCCA.output_template`
   * :class:`CompositorNodeSepYUVA.input_template`
   * :class:`CompositorNodeSepYUVA.output_template`
   * :class:`CompositorNodeSetAlpha.input_template`
   * :class:`CompositorNodeSetAlpha.output_template`
   * :class:`CompositorNodeSplitViewer.input_template`
   * :class:`CompositorNodeSplitViewer.output_template`
   * :class:`CompositorNodeStabilize.input_template`
   * :class:`CompositorNodeStabilize.output_template`
   * :class:`CompositorNodeSunBeams.input_template`
   * :class:`CompositorNodeSunBeams.output_template`
   * :class:`CompositorNodeSwitch.input_template`
   * :class:`CompositorNodeSwitch.output_template`
   * :class:`CompositorNodeSwitchView.input_template`
   * :class:`CompositorNodeSwitchView.output_template`
   * :class:`CompositorNodeTexture.input_template`
   * :class:`CompositorNodeTexture.output_template`
   * :class:`CompositorNodeTime.input_template`
   * :class:`CompositorNodeTime.output_template`
   * :class:`CompositorNodeTonemap.input_template`
   * :class:`CompositorNodeTonemap.output_template`
   * :class:`CompositorNodeTrackPos.input_template`
   * :class:`CompositorNodeTrackPos.output_template`
   * :class:`CompositorNodeTransform.input_template`
   * :class:`CompositorNodeTransform.output_template`
   * :class:`CompositorNodeTranslate.input_template`
   * :class:`CompositorNodeTranslate.output_template`
   * :class:`CompositorNodeValToRGB.input_template`
   * :class:`CompositorNodeValToRGB.output_template`
   * :class:`CompositorNodeValue.input_template`
   * :class:`CompositorNodeValue.output_template`
   * :class:`CompositorNodeVecBlur.input_template`
   * :class:`CompositorNodeVecBlur.output_template`
   * :class:`CompositorNodeViewer.input_template`
   * :class:`CompositorNodeViewer.output_template`
   * :class:`CompositorNodeZcombine.input_template`
   * :class:`CompositorNodeZcombine.output_template`
   * :class:`NodeFrame.input_template`
   * :class:`NodeFrame.output_template`
   * :class:`NodeGroup.input_template`
   * :class:`NodeGroup.output_template`
   * :class:`NodeGroupInput.input_template`
   * :class:`NodeGroupInput.output_template`
   * :class:`NodeGroupOutput.input_template`
   * :class:`NodeGroupOutput.output_template`
   * :class:`NodeReroute.input_template`
   * :class:`NodeReroute.output_template`
   * :class:`ShaderNodeAddShader.input_template`
   * :class:`ShaderNodeAddShader.output_template`
   * :class:`ShaderNodeAmbientOcclusion.input_template`
   * :class:`ShaderNodeAmbientOcclusion.output_template`
   * :class:`ShaderNodeAttribute.input_template`
   * :class:`ShaderNodeAttribute.output_template`
   * :class:`ShaderNodeBackground.input_template`
   * :class:`ShaderNodeBackground.output_template`
   * :class:`ShaderNodeBevel.input_template`
   * :class:`ShaderNodeBevel.output_template`
   * :class:`ShaderNodeBlackbody.input_template`
   * :class:`ShaderNodeBlackbody.output_template`
   * :class:`ShaderNodeBrightContrast.input_template`
   * :class:`ShaderNodeBrightContrast.output_template`
   * :class:`ShaderNodeBsdfAnisotropic.input_template`
   * :class:`ShaderNodeBsdfAnisotropic.output_template`
   * :class:`ShaderNodeBsdfDiffuse.input_template`
   * :class:`ShaderNodeBsdfDiffuse.output_template`
   * :class:`ShaderNodeBsdfGlass.input_template`
   * :class:`ShaderNodeBsdfGlass.output_template`
   * :class:`ShaderNodeBsdfGlossy.input_template`
   * :class:`ShaderNodeBsdfGlossy.output_template`
   * :class:`ShaderNodeBsdfHair.input_template`
   * :class:`ShaderNodeBsdfHair.output_template`
   * :class:`ShaderNodeBsdfPrincipled.input_template`
   * :class:`ShaderNodeBsdfPrincipled.output_template`
   * :class:`ShaderNodeBsdfRefraction.input_template`
   * :class:`ShaderNodeBsdfRefraction.output_template`
   * :class:`ShaderNodeBsdfToon.input_template`
   * :class:`ShaderNodeBsdfToon.output_template`
   * :class:`ShaderNodeBsdfTranslucent.input_template`
   * :class:`ShaderNodeBsdfTranslucent.output_template`
   * :class:`ShaderNodeBsdfTransparent.input_template`
   * :class:`ShaderNodeBsdfTransparent.output_template`
   * :class:`ShaderNodeBsdfVelvet.input_template`
   * :class:`ShaderNodeBsdfVelvet.output_template`
   * :class:`ShaderNodeBump.input_template`
   * :class:`ShaderNodeBump.output_template`
   * :class:`ShaderNodeCameraData.input_template`
   * :class:`ShaderNodeCameraData.output_template`
   * :class:`ShaderNodeCombineHSV.input_template`
   * :class:`ShaderNodeCombineHSV.output_template`
   * :class:`ShaderNodeCombineRGB.input_template`
   * :class:`ShaderNodeCombineRGB.output_template`
   * :class:`ShaderNodeCombineXYZ.input_template`
   * :class:`ShaderNodeCombineXYZ.output_template`
   * :class:`ShaderNodeEmission.input_template`
   * :class:`ShaderNodeEmission.output_template`
   * :class:`ShaderNodeExtendedMaterial.input_template`
   * :class:`ShaderNodeExtendedMaterial.output_template`
   * :class:`ShaderNodeFresnel.input_template`
   * :class:`ShaderNodeFresnel.output_template`
   * :class:`ShaderNodeGamma.input_template`
   * :class:`ShaderNodeGamma.output_template`
   * :class:`ShaderNodeGeometry.input_template`
   * :class:`ShaderNodeGeometry.output_template`
   * :class:`ShaderNodeGroup.input_template`
   * :class:`ShaderNodeGroup.output_template`
   * :class:`ShaderNodeHairInfo.input_template`
   * :class:`ShaderNodeHairInfo.output_template`
   * :class:`ShaderNodeHoldout.input_template`
   * :class:`ShaderNodeHoldout.output_template`
   * :class:`ShaderNodeHueSaturation.input_template`
   * :class:`ShaderNodeHueSaturation.output_template`
   * :class:`ShaderNodeInvert.input_template`
   * :class:`ShaderNodeInvert.output_template`
   * :class:`ShaderNodeLampData.input_template`
   * :class:`ShaderNodeLampData.output_template`
   * :class:`ShaderNodeLayerWeight.input_template`
   * :class:`ShaderNodeLayerWeight.output_template`
   * :class:`ShaderNodeLightFalloff.input_template`
   * :class:`ShaderNodeLightFalloff.output_template`
   * :class:`ShaderNodeLightPath.input_template`
   * :class:`ShaderNodeLightPath.output_template`
   * :class:`ShaderNodeMapping.input_template`
   * :class:`ShaderNodeMapping.output_template`
   * :class:`ShaderNodeMaterial.input_template`
   * :class:`ShaderNodeMaterial.output_template`
   * :class:`ShaderNodeMath.input_template`
   * :class:`ShaderNodeMath.output_template`
   * :class:`ShaderNodeMixRGB.input_template`
   * :class:`ShaderNodeMixRGB.output_template`
   * :class:`ShaderNodeMixShader.input_template`
   * :class:`ShaderNodeMixShader.output_template`
   * :class:`ShaderNodeNewGeometry.input_template`
   * :class:`ShaderNodeNewGeometry.output_template`
   * :class:`ShaderNodeNormal.input_template`
   * :class:`ShaderNodeNormal.output_template`
   * :class:`ShaderNodeNormalMap.input_template`
   * :class:`ShaderNodeNormalMap.output_template`
   * :class:`ShaderNodeObjectData.input_template`
   * :class:`ShaderNodeObjectData.output_template`
   * :class:`ShaderNodeObjectInfo.input_template`
   * :class:`ShaderNodeObjectInfo.output_template`
   * :class:`ShaderNodeOutput.input_template`
   * :class:`ShaderNodeOutput.output_template`
   * :class:`ShaderNodeOutputLamp.input_template`
   * :class:`ShaderNodeOutputLamp.output_template`
   * :class:`ShaderNodeOutputLineStyle.input_template`
   * :class:`ShaderNodeOutputLineStyle.output_template`
   * :class:`ShaderNodeOutputMaterial.input_template`
   * :class:`ShaderNodeOutputMaterial.output_template`
   * :class:`ShaderNodeOutputWorld.input_template`
   * :class:`ShaderNodeOutputWorld.output_template`
   * :class:`ShaderNodeParallax.input_template`
   * :class:`ShaderNodeParallax.output_template`
   * :class:`ShaderNodeParticleInfo.input_template`
   * :class:`ShaderNodeParticleInfo.output_template`
   * :class:`ShaderNodeRGB.input_template`
   * :class:`ShaderNodeRGB.output_template`
   * :class:`ShaderNodeRGBCurve.input_template`
   * :class:`ShaderNodeRGBCurve.output_template`
   * :class:`ShaderNodeRGBToBW.input_template`
   * :class:`ShaderNodeRGBToBW.output_template`
   * :class:`ShaderNodeScript.input_template`
   * :class:`ShaderNodeScript.output_template`
   * :class:`ShaderNodeSeparateHSV.input_template`
   * :class:`ShaderNodeSeparateHSV.output_template`
   * :class:`ShaderNodeSeparateRGB.input_template`
   * :class:`ShaderNodeSeparateRGB.output_template`
   * :class:`ShaderNodeSeparateXYZ.input_template`
   * :class:`ShaderNodeSeparateXYZ.output_template`
   * :class:`ShaderNodeSqueeze.input_template`
   * :class:`ShaderNodeSqueeze.output_template`
   * :class:`ShaderNodeSubsurfaceScattering.input_template`
   * :class:`ShaderNodeSubsurfaceScattering.output_template`
   * :class:`ShaderNodeTangent.input_template`
   * :class:`ShaderNodeTangent.output_template`
   * :class:`ShaderNodeTexBrick.input_template`
   * :class:`ShaderNodeTexBrick.output_template`
   * :class:`ShaderNodeTexChecker.input_template`
   * :class:`ShaderNodeTexChecker.output_template`
   * :class:`ShaderNodeTexCoord.input_template`
   * :class:`ShaderNodeTexCoord.output_template`
   * :class:`ShaderNodeTexEnvironment.input_template`
   * :class:`ShaderNodeTexEnvironment.output_template`
   * :class:`ShaderNodeTexGradient.input_template`
   * :class:`ShaderNodeTexGradient.output_template`
   * :class:`ShaderNodeTexImage.input_template`
   * :class:`ShaderNodeTexImage.output_template`
   * :class:`ShaderNodeTexMagic.input_template`
   * :class:`ShaderNodeTexMagic.output_template`
   * :class:`ShaderNodeTexMusgrave.input_template`
   * :class:`ShaderNodeTexMusgrave.output_template`
   * :class:`ShaderNodeTexNoise.input_template`
   * :class:`ShaderNodeTexNoise.output_template`
   * :class:`ShaderNodeTexPointDensity.input_template`
   * :class:`ShaderNodeTexPointDensity.output_template`
   * :class:`ShaderNodeTexSky.input_template`
   * :class:`ShaderNodeTexSky.output_template`
   * :class:`ShaderNodeTexVoronoi.input_template`
   * :class:`ShaderNodeTexVoronoi.output_template`
   * :class:`ShaderNodeTexWave.input_template`
   * :class:`ShaderNodeTexWave.output_template`
   * :class:`ShaderNodeTexture.input_template`
   * :class:`ShaderNodeTexture.output_template`
   * :class:`ShaderNodeTime.input_template`
   * :class:`ShaderNodeTime.output_template`
   * :class:`ShaderNodeUVAlongStroke.input_template`
   * :class:`ShaderNodeUVAlongStroke.output_template`
   * :class:`ShaderNodeUVMap.input_template`
   * :class:`ShaderNodeUVMap.output_template`
   * :class:`ShaderNodeValToRGB.input_template`
   * :class:`ShaderNodeValToRGB.output_template`
   * :class:`ShaderNodeValue.input_template`
   * :class:`ShaderNodeValue.output_template`
   * :class:`ShaderNodeVectorCurve.input_template`
   * :class:`ShaderNodeVectorCurve.output_template`
   * :class:`ShaderNodeVectorMath.input_template`
   * :class:`ShaderNodeVectorMath.output_template`
   * :class:`ShaderNodeVectorTransform.input_template`
   * :class:`ShaderNodeVectorTransform.output_template`
   * :class:`ShaderNodeVolumeAbsorption.input_template`
   * :class:`ShaderNodeVolumeAbsorption.output_template`
   * :class:`ShaderNodeVolumeScatter.input_template`
   * :class:`ShaderNodeVolumeScatter.output_template`
   * :class:`ShaderNodeWavelength.input_template`
   * :class:`ShaderNodeWavelength.output_template`
   * :class:`ShaderNodeWireframe.input_template`
   * :class:`ShaderNodeWireframe.output_template`
   * :class:`TextureNodeAt.input_template`
   * :class:`TextureNodeAt.output_template`
   * :class:`TextureNodeBricks.input_template`
   * :class:`TextureNodeBricks.output_template`
   * :class:`TextureNodeChecker.input_template`
   * :class:`TextureNodeChecker.output_template`
   * :class:`TextureNodeCompose.input_template`
   * :class:`TextureNodeCompose.output_template`
   * :class:`TextureNodeCoordinates.input_template`
   * :class:`TextureNodeCoordinates.output_template`
   * :class:`TextureNodeCurveRGB.input_template`
   * :class:`TextureNodeCurveRGB.output_template`
   * :class:`TextureNodeCurveTime.input_template`
   * :class:`TextureNodeCurveTime.output_template`
   * :class:`TextureNodeDecompose.input_template`
   * :class:`TextureNodeDecompose.output_template`
   * :class:`TextureNodeDistance.input_template`
   * :class:`TextureNodeDistance.output_template`
   * :class:`TextureNodeGroup.input_template`
   * :class:`TextureNodeGroup.output_template`
   * :class:`TextureNodeHueSaturation.input_template`
   * :class:`TextureNodeHueSaturation.output_template`
   * :class:`TextureNodeImage.input_template`
   * :class:`TextureNodeImage.output_template`
   * :class:`TextureNodeInvert.input_template`
   * :class:`TextureNodeInvert.output_template`
   * :class:`TextureNodeMath.input_template`
   * :class:`TextureNodeMath.output_template`
   * :class:`TextureNodeMixRGB.input_template`
   * :class:`TextureNodeMixRGB.output_template`
   * :class:`TextureNodeOutput.input_template`
   * :class:`TextureNodeOutput.output_template`
   * :class:`TextureNodeRGBToBW.input_template`
   * :class:`TextureNodeRGBToBW.output_template`
   * :class:`TextureNodeRotate.input_template`
   * :class:`TextureNodeRotate.output_template`
   * :class:`TextureNodeScale.input_template`
   * :class:`TextureNodeScale.output_template`
   * :class:`TextureNodeTexBlend.input_template`
   * :class:`TextureNodeTexBlend.output_template`
   * :class:`TextureNodeTexClouds.input_template`
   * :class:`TextureNodeTexClouds.output_template`
   * :class:`TextureNodeTexDistNoise.input_template`
   * :class:`TextureNodeTexDistNoise.output_template`
   * :class:`TextureNodeTexMagic.input_template`
   * :class:`TextureNodeTexMagic.output_template`
   * :class:`TextureNodeTexMarble.input_template`
   * :class:`TextureNodeTexMarble.output_template`
   * :class:`TextureNodeTexMusgrave.input_template`
   * :class:`TextureNodeTexMusgrave.output_template`
   * :class:`TextureNodeTexNoise.input_template`
   * :class:`TextureNodeTexNoise.output_template`
   * :class:`TextureNodeTexStucci.input_template`
   * :class:`TextureNodeTexStucci.output_template`
   * :class:`TextureNodeTexVoronoi.input_template`
   * :class:`TextureNodeTexVoronoi.output_template`
   * :class:`TextureNodeTexWood.input_template`
   * :class:`TextureNodeTexWood.output_template`
   * :class:`TextureNodeTexture.input_template`
   * :class:`TextureNodeTexture.output_template`
   * :class:`TextureNodeTranslate.input_template`
   * :class:`TextureNodeTranslate.output_template`
   * :class:`TextureNodeValToNor.input_template`
   * :class:`TextureNodeValToNor.output_template`
   * :class:`TextureNodeValToRGB.input_template`
   * :class:`TextureNodeValToRGB.output_template`
   * :class:`TextureNodeViewer.input_template`
   * :class:`TextureNodeViewer.output_template`

