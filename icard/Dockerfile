# Utiliza la imagen base de Python 3.9
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos de requerimientos (requirements.txt) al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Copia el resto del proyecto al directorio de trabajo
COPY . .

# Ejecuta el archivo build.sh para instalar dependencias, recopilar archivos estáticos y realizar migraciones
RUN ./build.sh

# Expone el puerto en el que se ejecuta tu aplicación Django (por defecto, 8000)
EXPOSE 8000

# Define el comando de inicio de tu aplicación Django
CMD ["gunicorn", "icard.wsgi", "--bind", "0.0.0.0:$PORT"]
    