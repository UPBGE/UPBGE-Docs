.. _contribute-contribute:

==========
Contribute
==========

The UPBGE Manual is a community driven effort to which anyone can contribute. If you found a typo or you want to improve the general quality of the documentation, there are several options for helping out. You can:

#. Fix problems, improve the documentation and write new sections. Make a Pull Request (PR) with the proposed changes in `UPBGE Docs <https://github.com/UPBGE/UPBGE-Docs>`__ project. Detailed instructions are in following pages.

#. `Report errors <https://github.com/UPBGE/UPBGE-Docs/issues>`__ in the documentation.

#. Join UPBGE `Discord channel <https://discord.gg/DqXJn75aD3>`__ for help and chat.

UPBGE source-code repository can be found on `github <https://github.com/UPBGE/upbge>`__.

If you want to contribute several things directly, ask for commit rights.

--------------------
Install Dependencies
--------------------
To build the documentation we need:

   * `Python 3 <https://www.python.org/>`__ to run Sphinx;
   * `Sphinx <https://pypi.org/project/Sphinx/>`__ to build html pages;
   * `ReadTheDocs Theme for Sphinx <https://pypi.org/project/sphinx_rtd_theme/>`__ as default theme;
   * `git <https://github.com/git-guides/install-git>`__ to clone the documentation and commit changes. 

Linux
+++++

For the appropriate system, run the command in a terminal:

Debian/Ubuntu:

``$ sudo apt-get install python3 python3-pip git``

``$ pip3 install sphinx sphinx-rtd-theme``

Redhat/Fedora:

``$ sudo yum install python3 python3-pip git``

``$ pip3 install sphinx sphinx-rtd-theme``

Arch Linux:

``$ sudo pacman -S python3 python3-pip git``

``$ pip3 install sphinx sphinx-rtd-theme``

..
   Once a change is committed, a build is automatically generated and the new changes pushed to the upbge-docs repository directly.

macOs
+++++

.. note:

   This guide relies heavily on command-line tools. It assumes you are the least familiar with the macOS Terminal application.


If using `Homebrew <https://brew.sh/>`__, run the following commands in the terminal:

``python3 -m ensurepip``

``brew install git``

..
   someone check if macOS instructions are complete

Windows
+++++++

Download the `Python installation <https://www.python.org/downloads/>`__ package for Windows, and install Python with the installation wizard.
    
.. note::
   Please **make sure** that you enable the **Add Python to PATH** option.
   The option must be enabled so you can build the manual with the *make* script.
   All other settings can remain as set by default.

.. figure:: /images/contribute/add_python_to_path.png

-----------------------
Download the Repository
-----------------------

Navigate into desired folder, where *UPBGE-Docs* will be installed:

``cd ~/path-to-folder``

Clone the *UPBGE Manual* repository:

``git clone https://github.com/UPBGE/UPBGE-Docs.git``

The repository will be downloaded, which may take a few minutes, depending on your internet connection.

---------------------------
Setup the Build Environment
---------------------------

.. note::
   Below command will install *sphinx* and *sphinx_rtd_theme*. If you already installed them, following the above instructions, there is no need to install them again. This is for Windows users.
   
Navigate into *UPBGE-Docs* folder, which was just created by ``git clone``:

``cd UPBGE-Docs``

Inside that folder is a file called *requirements.txt*, which contains a list of all the dependencies we need. To install these dependencies, we use the ``pip`` command:

``pip install -r requirements.txt``

.. tip::
   Every now and then you may want to make sure your dependencies are up to date using:

``pip install -r requirements.txt --upgrade``

-----------------
Build the Manual
-----------------

Once all dependencies are installed, navigate into *UPBGE-Docs* folder and run the *make* command:

``make html``

This command will build the documentation files into the *build* directory.

Navigate into ``build/html`` folder, and run *index.html* file, either from terminal, or *file explorer*, by double-clicking the file. Documentation will be opened with OS default web browser. 

.. tip::
   On MS Windows you can double-click *make.bat* file, to easily run the command, without having to open the Command Prompt and typing commands.

---------------
Troubleshooting
---------------

#. If for some reason the build fails, check if the *C-compiler* or *build-essential* (or *build-essentials*) are installed on your operating system. Search the web or post a question in online forums for more information.

#. If after build the structure of the Manual, i.e. *navigation/toc* side panel does not work as expected, deleting whole *build* directory, and runing ``make html`` command again might help solve the issue.

#. If *rst* formatting is not displayed as expected, try adding::
   
   .. highlight:: rst
   
directive to the top of the ``.rst`` file.

------------------
Editing the Manual
------------------

.. tip::
   Before editing the Manual, it is advised to copy the *UPBGE-Docs* folder, and rename this copy, i.e. *UPBGE-Docs-edit*. Make the changes in this copy, and when satisfied with changes you want to commit, copy-paste the relevant files into original *UPBGE-Docs* folder.

   As a good developer practice, it is also advisable to have your personal document file, where notes are kept: copy-paste info from web, what works and what not, fixes that were applied and solved issues etc.
    
With your favorite text/code editor, make some changes, fix typos, add images, and commit the changes back to *github* repository. Guidelines about ``.rst`` files, *Writing Style* and *Markup Style* are in the following pages.

------------------------
UPBGE Documentation Team
------------------------

   * Antônio Froz (uayten)
   * Denis Nicolas (denicolas)
   * Guilherme Teres Nunes (UnidayStudio)
   * Joel Gomes da Silva (joelgomes1994)
   * Jorge Bernal (lordloki)
   * Leopold A-C (IzaZed)
   * marechal-p (wkk)
   * NaincyKumariKnoldus
   * RPaladin
   * ShaunKulesa
   * Tristan Porteries (panzergame)
   * Ulysse Martin (youle31)
   * Xavier Cho (mysticfall)
   * You!

