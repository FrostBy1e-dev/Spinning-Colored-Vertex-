import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
def draw_cube():
    vertices = [
        [1, 1, -1],
        [1, 1, 1],
        [1, -1, 1],
        [1, -1, -1],
        [-1, 1, -1],
        [-1, -1, -1],
        [-1, -1, 1],
        [-1, 1, 1]
    ]

    triangle_pairs = [
        [0, 1, 2, 3],
        [3, 2, 6, 5],
        [5, 6, 7, 4],
        [4, 7, 1, 0],
        [1, 7, 6, 2],
        [4, 0, 3, 5]
    ]

    colors = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1]
    ]

    glBegin(GL_TRIANGLES)
    for color, faces in zip(colors, triangle_pairs):
        glColor3fv(color)
        for vertex in faces:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("04 Lab 1, Dela Pena_Jay Daniel_701")
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glEnable(GL_DEPTH_TEST)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    glTranslatef(-1, 0, 0)
                if event.key == pygame.K_d:
                    glTranslatef(1, 0, 0)
                if event.key == pygame.K_w:
                    glTranslatef(0, 1, 0)
                if event.key == pygame.K_s:
                    glTranslatef(0, -1, 0)

        glRotatef(1, 3, 1, 1)  # rotating the cube for demonstration purposes
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube()
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
