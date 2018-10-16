from pyqtgraph.opengl import GLBoxItem
from OpenGL.GL import *


class CustomFrame(GLBoxItem):

    def __init__(self, size=None, color=None, glOptions='translucent', linewidth=5):
        #super(CustomFrame, self,).__init__(size, color, glOptions)
        GLBoxItem.__init__(self, size, color, glOptions)
        self.linewidth = linewidth

    def paint(self):
        #glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        #glEnable( GL_BLEND )
        #glEnable( GL_ALPHA_TEST )
        ##glAlphaFunc( GL_ALWAYS,0.5 )
        #glEnable(GL_POINT_SMOOTH)
        #glDisable( GL_DEPTH_TEST )
        glEnable(GL_LINE_SMOOTH)
        self.setupGLState()
        glLineWidth(self.linewidth)
        glBegin(GL_LINES)

        glColor4f(*self.color().glColor())
        x, y, z = self.size()
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, z)
        glVertex3f(x, 0, 0)
        glVertex3f(x, 0, z)
        glVertex3f(0, y, 0)
        glVertex3f(0, y, z)
        glVertex3f(x, y, 0)
        glVertex3f(x, y, z)

        glVertex3f(0, 0, 0)
        glVertex3f(0, y, 0)
        glVertex3f(x, 0, 0)
        glVertex3f(x, y, 0)
        glVertex3f(0, 0, z)
        glVertex3f(0, y, z)
        glVertex3f(x, 0, z)
        glVertex3f(x, y, z)

        glVertex3f(0, 0, 0)
        glVertex3f(x, 0, 0)
        glVertex3f(0, y, 0)
        glVertex3f(x, y, 0)
        glVertex3f(0, 0, z)
        glVertex3f(x, 0, z)
        glVertex3f(0, y, z)
        glVertex3f(x, y, z)

        glEnd()
        glLineWidth(1)
