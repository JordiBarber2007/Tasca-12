# Importa la biblioteca pygame para crear juegos y sys para las funciones del sistema.
import pygame
import sys
# Importa la biblioteca random para generar números aleatorios.
import random



def main():
    # Inicializa todas las funciones de pygame.
    pygame.init()

    # Define el ancho y alto de la pantalla del juego.
    SW, SH = 800, 800

    # Define el tamaño del bloque de la serpiente y la manzana.
    BLOCK_SIZE = 50
    # Carga la fuente para el texto del puntaje, ajustando el tamaño de la fuente al doble del tamaño del bloque.
    FONT = pygame.font.Font("font.ttf", BLOCK_SIZE*2)

    # Crea una ventana de juego con las dimensiones especificadas.
    screen = pygame.display.set_mode((800, 800))
    # Establece el título de la ventana del juego.
    pygame.display.set_caption("Snake!")
    # Inicializa el reloj para controlar la velocidad del juego.
    clock = pygame.time.Clock()

   # Define la clase Apple (Manzana).
    class Apple:
        def __init__(self):
            # Genera una posición aleatoria para la manzana dentro de la cuadrícula.
            self.x = int(random.randint(0, SW)/BLOCK_SIZE) * BLOCK_SIZE
            self.y = int(random.randint(0, SH)/BLOCK_SIZE) * BLOCK_SIZE
            # Crea un rectángulo que representa la manzana.
            self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        
        def update(self):
            # Dibuja la manzana en la pantalla.
            pygame.draw.rect(screen, "orange", self.rect)

    # Define la clase Snake (Serpiente).
    class Snake:
        def __init__(self):
            # Inicializa la posición y dirección de la cabeza de la serpiente.
            self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
            self.xdir = 1
            self.ydir = 0
            # Crea un rectángulo que representa la cabeza de la serpiente.
            self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
            # Crea el cuerpo de la serpiente como una lista de rectángulos.
            self.body = [pygame.Rect(self.x-BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
            self.dead = False
        
        def update(self, apple):
            
            # Verifica colisiones con el cuerpo de la serpiente y los bordes de la pantalla.
            for square in self.body:
                if self.head.x == square.x and self.head.y == square.y:
                    self.dead = True
                if self.head.x not in range(0, SW) or self.head.y not in range(0, SH):
                    self.dead = True
            
            # Si la serpiente está muerta, reinicia su posición y dirección.
            if self.dead:
                self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
                self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
                self.body = [pygame.Rect(self.x-BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
                self.xdir = 1
                self.ydir = 0
                self.dead = False
                apple = Apple()
            
            # Actualiza la posición del cuerpo de la serpiente.
            self.body.append(self.head)
            for i in range(len(self.body)-1):
                self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
            # Mueve la cabeza en la dirección actual.
            self.head.x += self.xdir * BLOCK_SIZE
            self.head.y += self.ydir * BLOCK_SIZE
            self.body.remove(self.head)

 

    # Función para dibujar la cuadrícula en la pantalla.
    def drawGrid():
        for x in range(0, SW, BLOCK_SIZE):
            for y in range(0, SH, BLOCK_SIZE):
                rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(screen, "#3c3c3b", rect, 1)

    # Renderiza el texto del puntaje inicial.
    score = FONT.render("1", True, "white")
    score_rect = score.get_rect(center=(SW/2, SH/20))

    # Dibuja la cuadrícula en la pantalla.
    drawGrid()

    # Crea una instancia de la serpiente.
    snake = Snake()

    # Crea una instancia de la manzana.
    apple = Apple()

    # Bucle principal del juego.
    while True:
        for event in pygame.event.get():
            # Maneja los eventos de cierre de ventana.
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Maneja los eventos de teclado para cambiar la dirección de la serpiente.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    snake.ydir = 1
                    snake.xdir = 0
                elif event.key == pygame.K_UP:
                    snake.ydir = -1
                    snake.xdir = 0
                elif event.key == pygame.K_RIGHT:
                    snake.ydir = 0
                    snake.xdir = 1
                elif event.key == pygame.K_LEFT:
                    snake.ydir = 0
                    snake.xdir = -1

        # Actualiza la posición y estado de la serpiente.
        snake.update(apple)
        
        # Llena la pantalla de negro para borrar los gráficos anteriores.
        screen.fill('black')
        # Dibuja la cuadrícula en la pantalla.
        drawGrid()

        # Actualiza y dibuja la manzana en la pantalla.
        apple.update()

        # Renderiza el puntaje actual.
        score = FONT.render(f"{len(snake.body) + 1}", True, "white")

        # Dibuja la cabeza de la serpiente en la pantalla.
        pygame.draw.rect(screen, "green", snake.head)

        # Dibuja cada segmento del cuerpo de la serpiente en la pantalla.
        for square in snake.body:
            pygame.draw.rect(screen, "green", square)

        # Dibuja el puntaje en la pantalla.
        screen.blit(score, score_rect)

        # Verifica si la cabeza de la serpiente ha colisionado con la manzana.
        if snake.head.x == apple.x and snake.head.y == apple.y:
            snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
            apple = Apple()

        # Actualiza la pantalla con los nuevos gráficos.
        pygame.display.update()
        # Controla la velocidad del juego.
        clock.tick(5)

def pex3():
    main()
