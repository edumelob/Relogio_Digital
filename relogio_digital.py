import time
import os

def clear_screen():
    """Limpa a tela do terminal (Windows/Linux)"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_clock():
    """Mostra o relógio digital em tempo real"""
    try:
        while True:
            clear_screen()
            current_time = time.strftime("%H:%M:%S")
            current_date = time.strftime("%d/%m/%Y")
            print("=== RELÓGIO DIGITAL ===")
            print(f"🕒 Hora atual: {current_time}")
            print(f"📅 Data: {current_date}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nEncerrando o relógio. ⏹️")

if __name__ == "__main__":
    show_clock()
