# PRESENTATION_IT_navigator

This is my 5th program on Python. At the time of its creation,
I still had not read a single book, article or tutorial on the language,
but already learned how to break the code into several files and learned a couple of new tricks

The program is designed to view many items in a chain of stores.
Each store has computers, cameras and other commercial equipment.
Each equipment has its own IP address, subnet mask, its type and other displayed information.

Screenshots are attached to the source code, in which all the confidential information
was cut out (including the contents of the table) so as not to harm the company.

The program is an unfinished product, at the moment it can only display information in a convenient form,
as well as copy it from cells, but it is not able to change or add new data.

Despite this, I have something to be proud of:
the entire GUI is completely made on the tkinter module manually.
Since this module has very limited functionality, I had to apply many tricks to get the desired behavior
from it. The biggest congestion of these tricks is the table module.

The file with the table is located on the path: RU/Source/gui/kat_gui/kat_table.py

A feature of this table is that it is assembled from the simplest elements.
Headings are buttons with specific text, when clicked, sorting by one or another column is processed,
the table is rearranged in a new order and the button text changes.

To implement scrolling the table with the mouse wheel,
I also had to resort to a trick: when scrolling the mouse wheel, either the top line (s) is deleted
or vice versa (if there is something to add).
Thus, scrolling of the table is implemented

Hovering a mouse over a specific cell also highlights in a different color both the row or column (depending on the settings).
And yes, I also had to try here: hovering over the cell (and the cells, by the way, are ordinary text labels)
launches a function that calculates which cells in which colors you want to color. Similar actions occur when the mouse
leaves the cell zone, or when left-clicking on it occurs.

In addition, this table has a huge number of settings, thanks to which it can be completely customized to your style.
This, probably, will not be useful to me anymore, since I have already discovered the PyQT module for myself, however, maybe someone will be interested.

Although without configuring the RU/Source/functions/shoplist_fncs.py file to receive the correct data, the program will not work normally,
source code can come in handy

Used modules:

  import time,
  sys,
  os,
  pyodbc,
  win32api,
  win32net,
  tkinter,
