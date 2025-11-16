from services.admin.admin_reserva_service import *
import os 

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def listar_reservas():
    listar_reservas_service()
