import sqlite3
import os

# Contraseña almacenada directamente en el código.
# Vulnerabilidad: Hardcoded Credentials.
PASSWORD = "admin123"

# Token expuesto en el código fuente.
# Vulnerabilidad: Secret Exposure.
GITHUB_TOKEN = "ghp_123456789abcdef123456789abcdef"

# Solicita el nombre de usuario.
usuario = input("Usuario: ")

# Conexión a la base de datos SQLite.
conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

# Consulta construida con datos del usuario.
# Vulnerabilidad: SQL Injection.
consulta = "SELECT * FROM usuarios WHERE nombre='" + usuario + "'"

cursor.execute(consulta)

# Ejecuta una expresión ingresada por el usuario.
# Vulnerabilidad: Unsafe Eval / Code Injection.
expresion = input("Ingrese operación: ")
resultado = eval(expresion)

# Ejecuta un comando del sistema operativo.
# Vulnerabilidad: Command Injection.
archivo = input("Nombre del archivo: ")
os.system("cat " + archivo)

# Muestra el resultado obtenido.
print(resultado)    
