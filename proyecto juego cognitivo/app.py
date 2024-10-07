import tkinter as tk
import random
import time

# Colores posibles para los patrones
COLORS = ["red", "blue", "green", "yellow", "purple", "orange"]

# Número de elementos en el patrón
PATTERN_LENGTH = 4

class PatternRecognitionGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Reconocimiento de Patrones")
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        self.start_button = tk.Button(root, text="Iniciar Juego", command=self.start_game)
        self.start_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def start_game(self):
        # Reiniciar el mensaje de resultado
        self.result_label.config(text="")

        # Generar el patrón aleatorio
        self.pattern = [random.choice(COLORS) for _ in range(PATTERN_LENGTH)]
        
        # Mostrar el patrón al jugador
        self.show_pattern()

    def show_pattern(self):
        self.canvas.delete("all")
        size = 50
        spacing = 20
        x_start = 100
        y = 150

        for i, color in enumerate(self.pattern):
            x = x_start + i * (size + spacing)
            self.canvas.create_rectangle(x, y, x + size, y + size, fill=color)

        # Después de mostrar el patrón durante unos segundos, mostrar las opciones
        self.root.after(3000, self.hide_pattern)

    def hide_pattern(self):
        # Limpiar el canvas
        self.canvas.delete("all")

        # Crear múltiples opciones con una opción correcta (el patrón original)
        options = [self.pattern]  # Primera opción es el patrón correcto

        # Crear algunas opciones incorrectas
        for _ in range(2):
            wrong_pattern = [random.choice(COLORS) for _ in range(PATTERN_LENGTH)]
            options.append(wrong_pattern)

        # Mezclar el orden de las opciones
        random.shuffle(options)

        # Mostrar las opciones en botones
        self.buttons = []
        for i, option in enumerate(options):
            button = tk.Button(self.root, text="Opción {}".format(i+1), command=lambda o=option: self.check_answer(o))
            button.pack(pady=5)
            self.buttons.append(button)

            # Dibujar el patrón en el canvas
            size = 50
            spacing = 20
            x_start = 100
            y = 50 + i * 100
            for j, color in enumerate(option):
                x = x_start + j * (size + spacing)
                self.canvas.create_rectangle(x, y, x + size, y + size, fill=color)

    def check_answer(self, selected_pattern):
        if selected_pattern == self.pattern:
            self.result_label.config(text="¡Correcto!", fg="green")
        else:
            self.result_label.config(text="Incorrecto, intenta nuevamente.", fg="red")

        # Eliminar botones después de seleccionar la respuesta
        for button in self.buttons:
            button.pack_forget()

# Crear la ventana principal de tkinter
root = tk.Tk()
game = PatternRecognitionGame(root)

# Iniciar el bucle principal de tkinter
root.mainloop()

