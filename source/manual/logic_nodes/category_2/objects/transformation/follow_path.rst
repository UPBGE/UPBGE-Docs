*************
Follow Path
*************

Description
===========

Define posições por onde seu objeto irá se locomover através de objetos vazios com parentesco.

See also `Parenting Objects<https://docs.blender.org/manual/en/2.79/editors/3dview/object/properties/relations/parents.html>`_


Input
=====

Condition
    The condition for this node start

Moving Object
    Objeto que será movimentado

Rotating Object
    Se houver rotação: objeto que irá rotacionar na mudança de direção

Path (Parent of a set of Empties)
    Uma série de Objetos Vazios com parentesco.
    
    O pai não define a posição do objeto.
    
    Os filhos marcam quais posições o objeto irá passar durante o deslocamento
    
    A ordem que o objeto seguirá é de acordo com a ordem alfabética e numérica dos filhos

Loop
    Se selecionado: após a chegada na posição do último filho o objeto retornará para o início do deslocamento
    
    Não selecionado: o objeto irá finalizar o deslocamento no último objeto vazio da família.

Optional Navmesh
    Se houver uma delimitação na área onde o objeto percorre, selecionar a `Navigation Mesh<https://upbge.org/manual/manual/logic_nodes/category_2/objects/transformation/move_to_with_navmesh.html>`_
    
Move as Dynamic
    ??????

Lin Speed
    The linear speed of the object, basically the travelling speed

Reach Threshold
    The distance to the target it needs to count as "arrived"

Look At
    If selected, the front of the object will observe the direction of displacement.

Root Speed
    The speed at which the object will move sideways when making a change of direction

Rot Axis
    When the object makes a change of direction, which axis will rotate

Front
    Which axis is the front of the object

Output
======

**Done** 
    **True** if the node performed successfully.
