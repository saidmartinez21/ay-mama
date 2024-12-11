import tkinter as tk
from tkinter import ttk, messagebox

def CalcularMontoPagar():
    lecturaAnterior=0.0
    lecturaActual=0.0
    tarifa=0
    montoPagar=0.0

class CalculadoraAgua:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora de Consumo de Agua")
        
        # Variables
        self.lectura_anterior = tk.DoubleVar(value=0.0)
        self.lectura_actual = tk.DoubleVar(value=0.0)
        self.tarifa = tk.DoubleVar(value=0.0)
        self.monto_pagar = tk.DoubleVar(value=0.0)
        
        self.crear_widgets()
    
    def crear_widgets(self):
        # Frame principal
        frame = ttk.Frame(self.master, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Etiquetas y entradas
        ttk.Label(frame, text="Lectura Anterior (m³):").grid(row=0, column=0, pady=5)
        self.entrada_anterior = ttk.Entry(frame, textvariable=self.lectura_anterior)
        self.entrada_anterior.grid(row=0, column=1, pady=5)
        
        ttk.Label(frame, text="Lectura Actual (m³):").grid(row=1, column=0, pady=5)
        self.entrada_actual = ttk.Entry(frame, textvariable=self.lectura_actual)
        self.entrada_actual.grid(row=1, column=1, pady=5)
        
        ttk.Label(frame, text="Tarifa por m³:").grid(row=2, column=0, pady=5)
        self.entrada_tarifa = ttk.Entry(frame, textvariable=self.tarifa)
        self.entrada_tarifa.grid(row=2, column=1, pady=5)
        
        # Botón calcular
        ttk.Button(frame, text="Calcular", command=self.calcular_monto_pagar).grid(row=3, column=0, columnspan=2, pady=10)
        
        # Etiqueta resultado
        self.etiqueta_resultado = ttk.Label(frame, text="Monto a pagar: $0.00")
        self.etiqueta_resultado.grid(row=4, column=0, columnspan=2, pady=5)
        
    def calcular_monto_pagar(self):
        try:
            consumo = self.lectura_actual.get() - self.lectura_anterior.get()
            if consumo < 0:
                messagebox.showerror("Error", "La lectura actual no puede ser menor que la anterior")
                return
                
            monto = consumo * self.tarifa.get()
            self.monto_pagar.set(monto)
            self.etiqueta_resultado.config(text=f"Monto a pagar: ${monto:.2f}")
            
        except tk.TclError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraAgua(root)
    root.mainloop()