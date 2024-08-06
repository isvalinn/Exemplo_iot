import os
import tkinter as tk
from PIL import Image, ImageTk
#instalar o pillow
class TemperatureApp:
    def __init__(self, root):
        script_dir = os.path.dirname(__file__)
        relative_path = "alerta.png"
        abs_flie_path = os.path.join(script_dir,relative_path)
        self.root = root
        self.root.title("Controle de Temperatura")

        # Configurações da temperatura
        self.max_temperature = 30  # Temperatura máxima para exibir o aviso
        self.current_temperature = 20  # Temperatura inicial
        self.min_temperature = 0
        # Carregar a imagem de aviso
        try:
            self.alert_img = Image.open(abs_flie_path)
            self.tk_alert_img = ImageTk.PhotoImage(self.alert_img)
        except IOError:
            print("Erro ao abrir a imagem de alerta. Verifique se o arquivo 'alert.png' está no diretório.")
            self.root.destroy()
            return

        # Configurar o slider (barra deslizante)
        self.temperature_slider = tk.Scale(root, from_=40, to=0, orient=tk.VERTICAL, command=self.update_temperature)
        self.temperature_slider.set(self.current_temperature)
        self.temperature_slider.pack(side=tk.LEFT, padx=20)

        # Label para exibir a temperatura
        self.temp_label = tk.Label(root, text=f"Temperatura: {self.current_temperature}°C", font=("Arial", 16))
        self.temp_label.pack(side=tk.LEFT, padx=20)

        # Label para exibir a imagem de alerta
        self.alert_label = tk.Label(root)
        self.alert_label.pack(pady=20)
        self.alert_label.config(image='')

    def update_temperature(self, value):
        self.current_temperature = int(value)
        self.temp_label.config(text=f"Temperatura: {self.current_temperature}°C")

        # Verificar se a temperatura está acima do máximo
        if self.current_temperature >= self.max_temperature:
            self.alert_label.config(image=self.tk_alert_img)
        elif self.current_temperature <= self.min_temperature:
            self.alert_label.config(image=self.tk_alert_img)
        else:
            self.alert_label.config(image='')

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("900x500")
    app = TemperatureApp(root)
    root.mainloop()
