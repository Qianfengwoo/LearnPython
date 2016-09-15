Virtual environments start out as white-rooms with nothing but the standard library.

在学习matplotlib的时候，我用Python2.7虚拟了一个环境，在执行'plt.plot(x, y)'的时候，提示错误：
```Python
_tkinter.TclError: Can't find a usable init.tcl in the following directories: 
    /opt/anaconda1anaconda2anaconda3/lib/tcl8.5 /home/woo/microblog/matplotlib/env/lib/tcl8.5 /home/woo/microblog/matplotlib/lib/tcl8.5 /home/woo/microblog/matplotlib/env/library /home/woo/microblog/matplotlib/library /home/woo/microblog/matplotlib/tcl8.5.18/library /home/woo/microblog/tcl8.5.18/library
This probably means that Tcl wasn't installed properly.
```
通过google了解到，虚拟环境是个很“干净”的库，matplotlib依赖的Tcl并不在这个虚拟环境中，需要手动将tcl
添加到虚拟环境中，根据错误提示，在r'/home/woo/anacoda2/lib'下找到tcl8.5，将其粘贴到我的虚拟环境中的
lib下，在执行，提示错误：
```Python
_tkinter.TclError: Can't find a usable tk.tcl in the following directories: 
    /home/woo/microblog/matplotlib/env/lib/tcl8.5/tk8.5 /home/woo/microblog/matplotlib/env/lib/tk8.5 /opt/anaconda1anaconda2anaconda3/lib/tk8.5 /home/woo/microblog/matplotlib/lib/tk8.5 /home/woo/microblog/matplotlib/env/library



This probably means that tk wasn't installed properly.
```
依样画瓢，将tk8.5也粘贴到虚拟环境的lib下，再执行'plt.plot(x, y)'时，正常运行。

至此，这个问题得到妥善解决!
