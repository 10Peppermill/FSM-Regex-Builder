# FSM-Regex-Builder
Through a GUI allow a user to create a finite state machine and convert it to a regular expression.

Requirments
------------

This package runs under Python 3.7+, use pip_ to install:

.. code:: bash

    $ pip install graphviz
    $ pip install tkinter

To render the generated DOT source code, you also need to install Graphviz_
(`download page <upstream-download_>`_,
`archived versions <upstream-archived_>`_,
`installation procedure for Windows <upstream-windows_>`_).

Make sure that the directory containing the ``dot`` executable is on your
systems' ``PATH``
(sometimes done by the installer;
setting ``PATH``
on `Linux <set-path-linux_>`_,
`Mac <set-path-darwin_>`_,
and `Windows <set-path-windows_>`_).