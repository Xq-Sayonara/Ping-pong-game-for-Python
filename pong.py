import turtle

# ==========================================
# Configuración de la ventana principal
# ==========================================
ventana = turtle.Screen()
ventana.title("Pong - Juego Clásico")
ventana.bgcolor("black")  # Fondo negro
ventana.setup(width=800, height=600)
ventana.tracer(0)  # Evita que la ventana se actualice automáticamente (mejora el rendimiento)

# ==========================================
# Variables de Puntuación
# ==========================================
puntos_a = 0
puntos_b = 0

# ==========================================
# Creación de Objetos (Paletas y Pelota)
# ==========================================

# Paleta Izquierda (Jugador 1)
paleta_a = turtle.Turtle()
paleta_a.speed(0)  # Máxima velocidad de animación
paleta_a.shape("square")  # Forma cuadrada por defecto (20x20 píxeles)
paleta_a.color("white")
paleta_a.shapesize(stretch_wid=5, stretch_len=1)  # Estiramos a 100x20 píxeles
paleta_a.penup()  # Evita que dibuje una línea al moverse
paleta_a.goto(-350, 0)  # Posición inicial (izquierda)

# Paleta Derecha (Jugador 2)
paleta_b = turtle.Turtle()
paleta_b.speed(0)
paleta_b.shape("square")
paleta_b.color("white")
paleta_b.shapesize(stretch_wid=5, stretch_len=1)
paleta_b.penup()
paleta_b.goto(350, 0)  # Posición inicial (derecha)

# Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)  # Comienza en el centro
# Velocidad de movimiento en los ejes X e Y (puedes ajustar estos valores para cambiar la dificultad)
pelota.dx = 0.15 
pelota.dy = 0.15

# ==========================================
# Marcador de Puntuación (Pen)
# ==========================================
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()  # Ocultamos el objeto, solo queremos el texto
marcador.goto(0, 260)
marcador.write("Jugador 1: 0  Jugador 2: 0", align="center", font=("Courier", 24, "normal"))

# ==========================================
# Funciones de Movimiento
# ==========================================
def paleta_a_arriba():
    y = paleta_a.ycor()
    if y < 250:  # Límite superior
        y += 20
        paleta_a.sety(y)

def paleta_a_abajo():
    y = paleta_a.ycor()
    if y > -240:  # Límite inferior
        y -= 20
        paleta_a.sety(y)

def paleta_b_arriba():
    y = paleta_b.ycor()
    if y < 250:
        y += 20
        paleta_b.sety(y)

def paleta_b_abajo():
    y = paleta_b.ycor()
    if y > -240:
        y -= 20
        paleta_b.sety(y)

# ==========================================
# Vinculación de Teclado
# ==========================================
ventana.listen()  # Le decimos a la ventana que escuche eventos de teclado
# Controles Jugador 1
ventana.onkeypress(paleta_a_arriba, "w")
ventana.onkeypress(paleta_a_arriba, "W")
ventana.onkeypress(paleta_a_abajo, "s")
ventana.onkeypress(paleta_a_abajo, "S")
# Controles Jugador 2
ventana.onkeypress(paleta_b_arriba, "Up")
ventana.onkeypress(paleta_b_abajo, "Down")

# ==========================================
# Bucle Principal del Juego
# ==========================================
try:
    while True:
        ventana.update()  # Actualiza la pantalla en cada iteración del bucle

        # Mover la pelota
        pelota.setx(pelota.xcor() + pelota.dx)
        pelota.sety(pelota.ycor() + pelota.dy)

        # Revisar bordes (Arriba y Abajo)
        if pelota.ycor() > 290:
            pelota.sety(290)
            pelota.dy *= -1  # Invierte la dirección vertical

        elif pelota.ycor() < -290:
            pelota.sety(-290)
            pelota.dy *= -1

        # Revisar bordes (Izquierda y Derecha - Puntos)
        if pelota.xcor() > 390:
            pelota.goto(0, 0)
            pelota.dx *= -1
            puntos_a += 1
            marcador.clear()  # Borra el marcador anterior antes de escribir el nuevo
            marcador.write(f"Jugador 1: {puntos_a}  Jugador 2: {puntos_b}", align="center", font=("Courier", 24, "normal"))

        elif pelota.xcor() < -390:
            pelota.goto(0, 0)
            pelota.dx *= -1
            puntos_b += 1
            marcador.clear()
            marcador.write(f"Jugador 1: {puntos_a}  Jugador 2: {puntos_b}", align="center", font=("Courier", 24, "normal"))

        # Colisiones de la pelota con las paletas
        # Lógica: Si la pelota está en el borde de la paleta en X, y su altura (Y) está dentro de la longitud de la paleta
        
        # Paleta Derecha
        if (pelota.xcor() > 340 and pelota.xcor() < 350) and (pelota.ycor() < paleta_b.ycor() + 50 and pelota.ycor() > paleta_b.ycor() - 50):
            pelota.setx(340)
            pelota.dx *= -1  # Invierte la dirección horizontal

        # Paleta Izquierda
        if (pelota.xcor() < -340 and pelota.xcor() > -350) and (pelota.ycor() < paleta_a.ycor() + 50 and pelota.ycor() > paleta_a.ycor() - 50):
            pelota.setx(-340)
            pelota.dx *= -1

except turtle.Terminator:
    # Maneja la excepción si el usuario cierra la ventana directamente
    pass