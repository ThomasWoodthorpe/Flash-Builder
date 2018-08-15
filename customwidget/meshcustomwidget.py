from pyqtgraph.opengl import GLMeshItem
from OpenGL.GL import *
import pyqtgraph.functions as fn
from pyqtgraph.Qt import QtGui
from pyqtgraph.opengl import *
import numpy as np

class CustomBox(GLMeshItem):

    def __init__(self, **kwds):
        #super(CustomFrame, self,).__init__(size, color, glOptions)
        GLMeshItem.__init__(self, **kwds)

    def paint(self):
        self.setupGLState()

        self.parseMeshData()

        if self.opts['drawFaces']:
            with self.shader():
                verts = self.vertexes
                norms = self.normals
                color = self.colors
                faces = self.faces
                if verts is None:
                    return
                glEnableClientState(GL_VERTEX_ARRAY)
                try:
                    glVertexPointerf(verts)

                    if self.colors is None:
                        color = self.opts['color']
                        if isinstance(color, QtGui.QColor):
                            glColor4f(*fn.glColor(color))
                        else:
                            glColor4f(*color)
                    else:
                        glEnableClientState(GL_COLOR_ARRAY)
                        glColorPointerf(color)


                    if norms is not None:
                        glEnableClientState(GL_NORMAL_ARRAY)
                        glNormalPointerf(norms)

                    if faces is None:
                        glDrawArrays(GL_TRIANGLES, 0, np.product(verts.shape[:-1]))
                    else:
                        faces = faces.astype(np.uint).flatten()
                        glDrawElements(GL_TRIANGLES, faces.shape[0], GL_UNSIGNED_INT, faces)
                finally:
                    glDisableClientState(GL_NORMAL_ARRAY)
                    glDisableClientState(GL_VERTEX_ARRAY)
                    glDisableClientState(GL_COLOR_ARRAY)

        if self.opts['drawEdges']:
            verts = self.edgeVerts
            edges = self.edges
            glEnableClientState(GL_VERTEX_ARRAY)
            try:
                glVertexPointerf(verts)

                if self.edgeColors is None:
                    color = self.opts['edgeColor']
                    if isinstance(color, QtGui.QColor):
                        glColor4f(*fn.glColor(color))
                    else:
                        glColor4f(*color)
                else:
                    glEnableClientState(GL_COLOR_ARRAY)
                    glColorPointerf(color)
                edges = edges.flatten()
                glDrawElements(GL_LINES, edges.shape[0], GL_UNSIGNED_INT, edges)
            finally:
                glDisableClientState(GL_VERTEX_ARRAY)
                glDisableClientState(GL_COLOR_ARRAY)

