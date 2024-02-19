.. _introduction-briefing:

==============================
Briefing
==============================

An Origin Story
++++++++++++++++++++++++++++++

It was the mid-1990s, and the personal computer was taking off faster than anyone had anticipated. With it, there arose the advent of animated graphics and 3D games.

Blender Begins
------------------------------

It was at this ripe time that Blender came into being. Blender started off as an in-house 3D animation software created by a small Dutch animation studio called NeoGeo. Perhaps it was because of the lack of a cheap and capable substitute; perhaps it was due to sheer ambition, NeoGeo decided to create its own animation software from scratch rather than using what was available. 

The chief programmer of Blender was *Ton Roosendaal*, who was responsible for writing a large part of the core Blender functionalities.

For the next few years, Blender remained the internal tool of a very successful animation studio. The software became so good that in 1998, Blender was made available to the public. A new company, Not a Number (NaN), was formed to oversee the development and distribution of Blender. Largely via the Internet, Blender was distributed as two separate versions: a free version with limited functionality and a version that was not free (called Blender Publisher) that had a few additional features. Being the only complete 3D animation and game creation package available for free at a time when computer graphics was still in its infancy, Blender started gaining popularity, and many online communities developed that allowed artists to share knowledge and their work.

.. figure:: /images/introduction/01-blender16.jpg
   
   Blender 1.6 and Blender 2.5

The Dark Nights
------------------------------

Alas, with the collapse of the Internet bubble and some other unfortunate circumstances, Not a Number (NaN) filed for bankruptcy in 2002. Since Blender was the intellectual property of the company at the time, dissolving the company meant an uncertain future for Blender. The Blender community did not want to see their favorite software go down with NaN. So a deal was struck in which NaN would release the source code of Blender to the public for a payment of €100,000. A "Free the Blender" fundraising campaign was started. The online community responded very generously. A few months later, enough money was collected to convince NaN to re-release Blender as an open source software to the newly established Blender Foundation. The foundation was created specifically to manage the now open source Blender. Ton Roosendaal, the original creator of Blender, heads the foundation.

Blender Rises
------------------------------

Located in beautiful Amsterdam, the Blender Foundation now oversees the development, distribution, and marketing of Blender. But because of the open source nature of the software, its development has been driven largely by volunteer contributors from across the world.

The Blender Foundation also created the Blender Institute, an animation and game studio that focuses on movie and game development using Blender. The Institute produced the movies **Elephants Dream**, **Big Buck Bunny**, **Sintel**, **Tears of Steel**, **Cosmos Laundromat** and the game **Yo, Frankie!**. These projects serve two main goals: The production process is an opportunity to improve Blender in a real studio environment, and the end result also serves as an advertisement for the software itself.

.. figure:: /images/introduction/02-blender_reel.jpg

   Blender reel
   
Then came Blender 2.5, which changed much of how Blender looked and behaved. This refactoring, as it was called, took years of planning and coding. Blender 2.5 marks a significant milestone in the history of Blender. For users coming from the Blender 2.4x series, the entire interface looks radically different: menus items are rearranged, keyboard shortcuts are altered, even the default color scheme has changed from a boring gray to a slightly less boring shade of gray.  Blender 2.5 is designed to be more intuitive, faster to use, and easier to learn than its predecessor.

Blender uses the Python programming language for scripting. With Python, you can customize the behavior of Blender, extend its functionality, and, more importantly, control the game engine. Knowing how to program is not a requirement for using Blender, but knowing Python will make you a far more capable game-maker.

.. figure:: /images/introduction/03-blender_commits.png
   :width: 70%

   Monthly commits

The year 2012 marked the tenth anniversary of Blender going open source. During these 10 years of open source development, more than 150 people have contributed something to the source code, totaling 50,000 contributions ("commits," in GIT techno-jargon), averaging nearly 30 commits every day over the past year. Needless to say, the program has improved much over the years, and it shows no sign of slowing down when it reaches almost to the thirtieth anniversary. The image below shows the Blender development statistics gathered from the official GIT repository including Blender trunk all its branches.

Blender vs UPBGE
------------------------------

You already know that Blender is an open source 3D software that is capable of modeling, animation, rendering, compositing, and producing a game all in one package. Let's analyze the term "open source 3D software": "Open source 3D software" means that Blender's source code is available for anyone to access and modify. The most obvious advantage to open source software is that as an artist, you can use Blender for free, for non-commercial as well as commercial work. As a developer, you are allowed to modify Blender in any way you want to suit your specific needs. But open source does not mean that anyone can make changes to the Blender code without approval. Blender is licensed under the GNU Public License v2 (GPL2). In a nutshell, it means that Blender can be copied, modified, and if re-shared, the changes in the source code have to be available and licensed in an equivalent license.

The **Uchronia Project Blender Game Engine** (UPBGE) is a `Blender <https://www.blender.org/>`__'s builtin tool derived from Blender Foundation's `Blender Game Engine <https://en.wikipedia.org/wiki/Blender_Game_Engine/>`__ for real-time projects, from architectural visualizations and simulations to games.

Originally created by Tristan Porteries as a fork from the Blender Game Engine with the purpose to develop the Blender Game Engine in a faster way, became indepent with the Blender Foundation's announcement of BGE's removal when it reached to Blender 2.80. With this independency, the UPBGE's developers (former BGE developers) have freedom to change and add features that could not be changed before (because the possibility of an official Blender merge, now discarded).

Basically, due to its periodic synchronization with Blender source code (almost daily), UPBGE, as its acronym suggests, has become a Blender from a parallel universe in which the game engine was never removed.

In any case, UPBGE is kriptonian for "hope". Who knows if in the future that parallel universe merges with our universe and we may add another line entitled "Justice League" to this beautiful story :-).

Until that time comes, UPBGE has adopted the new physically based and state-of-the-art real-time render engine, Eevee. This way all you can do in Blender/UPBGE editor you can translate it to the Game Engine. A truly WYSIWYG (What You See Is What You Get) Game Engine, the strongest UPBGE feature.

Of course, software exists to serve the users - that's you. Every time a Blender and/or UPBGE user creates a piece of artwork, it justifies, even if just a little, the enormous amount of time that went into creating the software. We hope that by picking up this manual, you are on your way to creating something amazing to share with the world.

Features
------------------------------

Compared to some of the commercial game engines available today, the Uchronia Project Blender Game Engine (UPBGE or BGE or GE for short) is relatively simple. Is that a bad thing? Not necessarily. A simple platform like UPBGE is very easy to learn, and yet it's flexible enough to do a lot.

UPBGE have lots of `new features <https://github.com/UPBGE/upbge/wiki/Release-notes>`__, improvements and bugs fixed. Some features that UPBGE supports are:

- Realtime advanced physics powered by `Bullet <https://github.com/bulletphysics/bullet3>`__, including rigid bodies, obstacle simulation and path finding.
  
- Fully integrated audio engine powered by `OpenAL <https://www.openal.org/>`__ and `Audaspace <https://github.com/neXyon/audaspace/>`__,supporting 3D sound and sound effects.

- Two easy and straightforward visual logic systems, Logic Bricks and Logic Nodes.

- Powerful `Python <https://www.python.org/>`__ language bindings, allowing support to even more libraries through the use of `PyPI <https://pypi.org/>`__.

- Development process entirely inside Blender, without needing to import/export assets, although most used formats are supported through import/export addons (FBX, Collada, glTF, obj, stl, etc).

- Execution of game in Blender's viewport (for fast previewing) or on an standalone executable.

- Rendering powered by state of art Blender's EEVEE engine including PBR shading, SSR reflections, GTAO ambient occlusion, Bloom, Soft and contact shadows, Light probes for global ilumination, Volumetrics, etc.

- Blender's `Linked Libraries <https://docs.blender.org/manual/en/dev/data_system/linked_libraries.html>`__ feature, allowing to organize projects in multiple blend files.

- GLSL custom shaders for visual effects and post processing.

Development
------------------------------

UPBGE is maintained by a group of developers in their spare time and its community. You can contribute to UPBGE if you code in C++ or Python: just `open a pull request <https://github.com/UPBGE/upbge/pulls>`__, submit your changes and wait for the reviewers. Also, even if you don't code, you can contribute by submitting bug reports, feature requests and participating discussions `on issues <https://github.com/UPBGE/upbge/issues>`__.
