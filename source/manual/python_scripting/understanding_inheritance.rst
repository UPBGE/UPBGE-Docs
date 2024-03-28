.. _understanding-inheritance-and-composition-in-game-scripting:

==============================
Inheritance And Composition
==============================

Introduction
++++++++++++++++++++++++++++++

Let us imagine we are making a video game in which characters can attack each other and receive damage. You will likely want to add a few properties like health or max_health to each object and write simple scripts to calculate them when the character gets hit or drinks a potion. Pretty simple, isn't it?

In many cases, writing game scripts doesn't require much more knowledge than that. A game engine is supposed to handle most of the heavy lifting for you, and all you need to do is declaring a few such variables, or writing a few conditional statements, loops, or functions to stitch them together. There is a reason why writing game logic is called 'scripting' even when it's done with a compiled language like C#, after all.

But what if you want to try something more complex, like creating an RPG where you can bash a door or a chest until it breaks open? Do you see the resemblance between hitting an enemy with a sword and doing the same to a crate?

Of course, you can simply add the same variables to the crate and copy and paste the same code you used to calculate a character's health. But what if there are many similar cases and you have to paste the same code to hundreds of them? Wouldn't it make your project challenging to understand or modify?

Although software engineering is not a popular topic among most game developers, some of its principles like DRY or SOLID can offer a helpful guide in such a situation.

And with slight exaggeration, we can say that the entire idea of software design revolves around the concept of generalisation and abstraction, which is a tool invented to solve precisely such a kind of problem. In other words, how can we generalise the idea of something that can be damaged into a reusable code so that we don't have to repeatedly copy and paste the same code over and over?

Object-Oriented Programming or OOP is a software paradigm that provides powerful tools we can utilise to solve such a problem. Even though it has seen increasing challenges over the years, it remains one of the most widely used software paradigms, well supported by popular languages like Python or C#. So, let's look into the concept briefly in the next chapter.

Type and Inheritance
--------------------

To put it simply, a type in an OOP language determines an object's nature (i.e. properties and behaviours). It also applies to a dynamically typed language like Python, which allows you to write code without caring too much about types. You know that you can change the value of a variable from abc to ABC by invoking its 'upper()' API because it has the type of str which declares upper() as its method.

But the real benefit of having a type system goes further than allowing you to figure out what functions an existing object provides. It can also serve as a tool to express a set of common characteristics that things can share, like the fact that they can be damaged, for example.

A character can be attacked and receives damage, and so can a crate. In other words, they are both something capable of being damaged and probably also destroyed after getting hit repeatedly. Let's generalise this idea as Damageable type as follows:

.. code-block:: python

   class Damageable:
     def __init__(self, init_health: int = 100):
       self.health = init_health

     def damage(self, amount: int) -> None:
       self.health = max(0, self.health - amount)

     @property
     def destroyed(self) -> bool:
       return self.health == 0

But how can you use (or 'reuse') it to eliminate the repetition? And that is where the concept of 'inheritance' comes in.

If you want to make your character or a crate class damageable, you can simply make them 'inherit' or derive from 'Damageable' type like this:

.. code-block:: python

   class Character(Damageable):
     pass

   class Crate(Damageable):
     pass

   character = Character()

   character.damage(40)
   crate.damage(120)

   print(character.health) # Prints "60"
   print(character.destroyed) # Prints "False"

   print(crate.health) # Prints "0"
   print(crate.destroyed) # Prints "True"

As you can see, inheritance is a powerful tool to generalise ideas and promote code reuse. But it is not without problems which we will discuss in the following chapter.

Problems of Inheritance
-----------------------

We just made a crate damageable by deriving it from Damageable type. But what if we also want to add some other features, like being able to be opened? Maybe we could define another class Openable to describe the concept of something which can be opened. But can an object inherit from both of those types?

This can pose a serious issue in a language that does not allow multiple inheritance like C#. And even with languages that do, deriving from multiple parents may bring more headaches than benefits sometimes, causing issues like the infamous Diamond Problem.

Furthermore, it can also introduce additional challenges in the context of game development. Typically a game engine handles all performance-critical operations in its native layer while exposing a small set of features as a scripting API in a higher-level language like C# or Python to offer better productivity and ease of use for its users.

Because of this, some game engines (e.g. a famous private one that keeps them "united" :-)) do not allow instantiating such game-related classes directly in the scripting layer, making it difficult or even impossible to extend them by subtyping, as we discussed in the previous chapter.

And even those that do (e.g. Godot), the typical workflow they provide involves providing initial parameters from the editor, which the engine uses to instantiate objects for the user. So, if you create game objects directly in code, you'll lose all the conveniences the editor provides. (This, however, is not the case in UPBGE as it has a unique feature that allows you to combine both approaches. We will discuss this feature later.)

Due to such limitations, it is often desirable to take a different approach to promote code reuse when working on a game project. Fortunately, a design principle can be used to overcome this particular problem called Composition Over Inheritance, which also works well when writing game scripts.

Composition Over Inheritance
----------------------------

The basic idea of composition is implementing each feature of an object as a modular 'component'. By doing so, we can compose such elements to describe the behaviours and properties of the whole.

For example, instead of making the Crate class inherit from Damageable type, we can rename the latter to HitBox and make it a property of the enclosing class:

.. code-block:: python

   class HitBox:
     def __init__(self, init_health: int = 100):
       self.health = init_health

     def damage(self, amount: int) -> None:
       self.health = max(0, self.health - amount)

     @property
     def destroyed(self) -> bool:
       return self.health == 0

   class Crate:
     def __init__(self):
       self.hit_box = HitBox()

   crate = Crate()

   crate.hit_box.damage(80)

   print(crate.hit_box.health) # Prints "20"
   print(crate.hit_box.destroyed) # Prints "False"

   crate.hit_box.damage(50)

   print(crate.hit_box.health) # Prints "0"
   print(crate.hit_box.destroyed) # Prints "True"

Similarly, we can also make the crate 'openable' by creating a Door component and assign an instance of it as a property of Crate:

.. code-block:: python

   class Door:
     def __init__(self, opened: bool = True):
       self.opened = opened

     def open(self) -> None:
       self.opened = True

     def close(self) -> None:
       self.opened = False

   class Crate:
     def __init__(self):
       self.hit_box = HitBox()
       self.door = Door()

   crate = Crate()

   crate.door.open()
   print(crate.door.opened) # Prints "True"

   crate.door.close()
   print(crate.door.opened) # Prints "False"

In this way, you can add as many features to an object as you like without the concern of introducing potential conflict in the type hierarchy.

Dynamic Component Model
-----------------------

Let's take the idea one step further and generalise the concept of components itself. What if we replace individual properties like door or hit_box with a generic list?

.. code-block:: python

   class Crate:
     def __init__(self):
       self.components = dict()

   crate = Crate()

   crate.components["hit_box"] = HitBox() # Now the crate can be damaged.
   crate.components["door"] = Door() # And it becomes openable.

As you see, now we can attach an arbitrary behaviour to an existing object without modifying the class definition. And what if we make the Character class damageable in the same manner? Wouldn't it make Character look almost identical with Crate?

.. code-block:: python

   class Character:
     def __init__(self):
       self.components = dict()

   character = Character()

   character.components["hit_box"] = HitBox()

They look similar indeed! Then why not replace them both with something more generic, like GameObject?

.. code-block:: python

   class GameObject:
     def __init__(self, name: str):
       self.name = name
       self.components = dict()

   character = GameObject("Character")
   character.components["hit_box"] = HitBox()

   crate = GameObject("Crate")
   crate.components["hit_box"] = HitBox()
   crate.components["door"] = Door()

If you want to make it a bit more precise, you can define a common base type to represent a component, like Component and derive both HitBox and Door from it. Using Python's typing support for clarity, the code would look like the following example:

.. code-block:: python

   from abc import ABC
   from typing import Dict

   class Component(ABC): # Indicates that this is an abstract base class
     pass

   class GameObject:
     def __init__(self, name: str):
       self.name = name
       self.components: Dict[str, Component] = dict()

   class Door(Component):
     ...

   class HitBox(Component):
     ...

In fact, this is what objects and components in game engines are all about. They may be named differently or have slightly different APIs, depending on the game engine you choose. But be it GameObject/MonoBehaviour in other game engine or KX_GameObject/KX_PythonComponent in UPBGE, the core idea behind it remains the same nonetheless.

The dynamic nature - namely, the ability to define arbitrary behaviour as a component and attach it to an object without modifying its source - of the compositional pattern fits game development so well that many game engines enforce it as the only viable method to write game scripts.

But could it be a 'silver bullet' of software design pattern? If composition is so good for everything, why almost all major OOP languages still support inheritance?

Why Inheritance Still Matters?
------------------------------

One prominent case where using inheritance over composition would make sense is when the concepts you want to represent as types have an is-a relationship with each other.

Suppose you want to make an inventory system that can store things like food or weapons. Both an apple and a dagger may take up some space if you put them in your inventory, and they may also have other common traits like having specific weight and so on.

In other words, we can say that any item has a specific inventory slot size and weight. As long as Potion or Weapon is an Item, it inherits common properties like inventory_size or weight from its parent type. Bearing that in mind, it shouldn't be difficult to see how saying that "a dagger is an item" is much more intuitive than saying that "it contains a component with item-specific properties and behaviours".

Another disadvantage of using the compositional pattern could be its dynamic nature itself. As with most things in software development, there is a trade-off relationship between dynamically attaching properties or behaviours of an object and statically defining them.

Remember our first version of Character class that directly extends Damageable?

.. code-block:: python

   character = Character()
   character.damage(50)

Now, compare that with a componentised version:

.. code-block:: python

   character = GameObject("Character")

   # Let's assume that the engine added HitBox component automatically.
   character.components["hit_box"].damage(50)

Can you see the difference? Aside from being slightly more verbose, the latter version is also much more prone to errors. With the former example, a decent Python IDE with a proper setup will autocomplete methods like damage and warn you if you accidentally make a typo, like when you type character.destroeyd instead of character.destroyed, for example.

And in case you want to rename a method or property, like changing damage to hit, for instance, you rely on refactoring support that most IDEs provide to perform the task without an error.

However, you will lose all such conveniences with the dynamic approach as your IDE won't be able to infer proper types in that case, which could become a significant issue if your project grows larger and more complex.

Now, examine this method signature:

.. code-block:: python

   def heal(target, amount)

Can you guess the proper usage of that API or how to implement its body if you are a developer? If you are not sure, how about this version?

.. code-block:: python

   def heal(target: GameObject, amount: float) -> None

Now you know that you are expected to pass a GameObject instance as the first parameter and specify the amount you want to heal as a float value. But what is a GameObject really?

As we learned from the previous chapter, it's just something that contains components. It may mean anything - anything from a character to a house. You may make a good guess from the method name and assume it would expect a GameObject with a Hitbox attached to it, but nobody will stop you if you pass an actual house as long as it's also a GameObject.

Also, others may not be as smart as you and may have difficulty guessing the proper type of object to pass as the first parameter without having good documentation.

But what if we haven't adopted the component approach but just used the plain inheritance model instead?

.. code-block:: python

   def heal(target: Damageable, amount: float) -> None:

Now it became immediately apparent what the function expects as its first parameter. If you use an IDE, it will also let you know that the target argument supports damage method, which you can use to implement the function body as target.damage(-amount). Furthermore, it will also warn you if you attempt to pass a non-Damageable type object like a House, all of which can help you maintain your codebase as it grows in size.

However, there was a good reason why we considered adopting the more dynamic approach before, and we may still want to keep some of its benefits.

Suppose you want to derive your Crate class directly from Openable type instead of attaching a Door component to it as we did before. Wouldn't it be still nice if you can assign different kinds of doors - like one with an animation, or another with a locking mechanism, and so on - without having to rewrite the Crate class every time?

A language feature or a design pattern called mixin can provide an answer to this question.

Mixins And Traits
-----------------

According to a relevant Wikipedia article, a mixin is "a class that contains methods for use by other classes without having to be the parent class of those other classes".

Such a class is sometimes called a trait and often named as an adjective like Damageable or Openable to describe a specific aspect or characteristic of the target object.

The idea is, you can define various aspects of an object as "traits" and "mix them in" as needed. It is a powerful tool that provides a way to add behaviours to an existing class in a compositional manner without erasing the type information as the component pattern does.

Let's make our Crate class again using the technique:

.. code-block:: python

   # The same class we saw at the beginning, now acting as a 'trait'.
   class Damageable:
     def __init__(self):
       self.health = 100

     def damage(self, amount: int) -> None:
       self.health = max(0, self.health - amount)

     @property
     def destroyed(self) -> bool:
       return self.health == 0

   # Tha same Door class, now renamed as appropriate for a trait
   class Openable:
     def __init__(self):
       self.opened = True

     def open(self) -> None:
       self.opened = True

     def close(self) -> None:
       self.opened = False

   # Let's assume there is a base class for all items, named as `Item`.
   # Now you can "mix" useful traits into Item as follows:
   class Crate(Damageable, Openable, Item):
     pass

   crate = Crate()

   print(isinstance(crate, Damageable)) # Returns "True"

   crate.damage(50) # Much better than crate.components["hit_box"].damage(50)
   crate.open()

You may have noticed how intuitive the class definition reads now. Even without any comment or having to read the source code, you can immediately see the purpose of the Crate class as it's a "damageable and openable item", indeed.

Also, because the class is a proper subtype of both Damageable and Openable, an IDE will be able to autocomplete such methods like damage(amount) or open() for you. It also enables you to tighten the type signature when you write an API like def heal(damageable: Damageable, amount: Float) -> None so that an IDE can warn you if you attempt to pass an object with a wrong type by mistake.

But how can we preserve the dynamic nature of the component model? What if I want to add crates in the game editor and make some of them have a unique animation when they open?

Of course, you can still benefit from the dynamic nature of using components, well, by using components! In fact, mixins and components are not mutually exclusive concepts since you can write a trait that relies on a component to implement a behaviour.

.. code-block:: python

   class Door(Component):
     def __init__(self):
       self.opened = True

   class Openable:

     @property
     def door(self) -> Door:
       return next(filter(lambda o: isinstance(o, Door), self.components))

     @property
     def opened(self)-> bool:
       return self.door.opened

     def open(self) -> None:
       self.door.opened = True

     def close(self) -> None:
       self.door.opened = False

   class Crate(Openable, GameObject):
     pass

As the trait is now mixed into a GameObject, it can reference its components property from which it can find a suitable component to work with, in this case, a Door. And the fact that the Door class is a component means that you can dynamically assign a specific implementation of it from the game editor without modifying the source code of either Crate or Openable.

If you want to add an animation to some of the crates, for example, you can write a special subtype of Door like class AnimatedDoor(Door) and attach it to a game object with the Openable trait. As long as the target object has the trait, it wouldn't matter if it's a crate or a gate. And as long as the component derives from Door, it will work perfectly fine with any Openable object, be it an animated door or one that requires a key to open it, for instance.

Mixins and Components in UPBGE
------------------------------

As shown in the previous chapters, the component model and mixins are powerful tools to design your software while maintaining a clean separation of concern between classes responsible for different functionalities.

To reap the full benefits of these design patterns, however, it is necessary to have a proper programming environment that supports such concepts.

An older version of C# (before 8.0), for example, didn't allow providing a default implementation of a method defined in an interface, thus severely limiting its usefulness when used as a trait.

And while most of the game engines enforced either the component model (e.g. private one that keeps them united) or the inheritance model (e.g. Godot) on their users, few, if any, support both of them like UPBGE now does.

With its recent introduction of the custom game object feature, you can define either static or dynamic (i.e. component-based) traits and mix them into any game object in UPBGE. It provides programmers with a powerful tool to design and organise game-related classes without sacrificing the ability to configure them graphically within UPBGE.

The example code shown above will work almost verbatim on UPBGE if you simply replace GameObject with KX_GameObject and Component with KX_PythonComponent like this:

.. code-block:: python

   class Door(KX_PythonComponent):
     args = OrderedDict((
       ("Open", True),
     ))

     def start(self, args) -> None:
       self.opened = args["Open"]

   # A dynamic trait based on component
   class Openable:

     @property
     def door(self) -> Door:
       return next(filter(lambda o: isinstance(o, Door), self.components))

     @property
     def opened(self)-> bool:
       return self.door.opened

     def open(self) -> None:
       self.door.opened = True

     def close(self) -> None:
       self.door.opened = False

   # An example of a static trait
   class Damageable:
     health: float

     def damage(self, amount: int) -> None:
       self.health = max(0, self.health - amount)

     @property
     def destroyed(self) -> bool:
       return self.health == 0

   class Crate(Openable, Damageable, KX_GameObject):
     args = OrderedDict((
       ("Health", 100),
     ))

     def start(self, args) -> None:
       self.health = args["Health"]

Now you can assign different initial health values to each crate in UPBGE or add an animated door to some of them without writing a new class for such cases. Also, when you write scripts, you can directly invoke any API they define without having to look up nested components or losing the valuable type information.

Those are some of the few unique advantages that UPBGE has over its competitors.
