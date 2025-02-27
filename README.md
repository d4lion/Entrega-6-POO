# 🐍 Entrega 6: POO App

Aplicación desarrollada con **Flet** para crear una interfaz gráfica interactiva, utilizando una base de datos **SQLite3** para la gestión de usuarios. Implementa un diseño moderno inspirado en **Material UI**.

## 🚀 Características principales

- 🧱 **Interfaz gráfica**: Basada en Material UI con Flet.
- 📊 **Gestión de usuarios**: CRUD completo con SQLite3.
- 🔌 **Compatibilidad multiplataforma**: Ejecuta en escritorio, web, Android, iOS, Windows, macOS y Linux.
- 📂 **Modularidad**: Código organizado con Programación Orientada a Objetos (POO).

## 🖼️ Vista previa de la app
https://github-production-user-asset-6210df.s3.amazonaws.com/111100025/417406367-7a089d05-564e-4416-9eeb-7d72f71c4467.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20250227%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250227T025930Z&X-Amz-Expires=300&X-Amz-Signature=c3b20891b8a1a8458a482da7e194dcdc3d13af1357adc79c57f0749b711d2941&X-Amz-SignedHeaders=host


## 📦 Instalación y ejecución

### Con `uv`

Ejecutar como aplicación de escritorio:

```bash
uv run flet run
```

Ejecutar como aplicación web:

```bash
uv run flet run --web
```

### Con `poetry`

Instalar dependencias desde `pyproject.toml`:

```bash
poetry install
```

Ejecutar como aplicación de escritorio:

```bash
poetry run flet run
```

Ejecutar como aplicación web:

```bash
poetry run flet run --web
```

📘 Para más detalles, consulta la [Guía de inicio rápido](https://flet.dev/docs/getting-started/).

## 🛠️ Construir la aplicación

### 📱 Android

```bash
flet build apk -v
```

📘 Más detalles en la [Guía de empaquetado para Android](https://flet.dev/docs/publish/android/).

### 🍎 iOS

```bash
flet build ipa -v
```

📘 Más detalles en la [Guía de empaquetado para iOS](https://flet.dev/docs/publish/ios/).

### 💻 macOS

```bash
flet build macos -v
```

📘 Más detalles en la [Guía de empaquetado para macOS](https://flet.dev/docs/publish/macos/).

### 🐧 Linux

```bash
flet build linux -v
```

📘 Más detalles en la [Guía de empaquetado para Linux](https://flet.dev/docs/publish/linux/).

### 🪟 Windows

```bash
flet build windows -v
```

📘 Más detalles en la [Guía de empaquetado para Windows](https://flet.dev/docs/publish/windows/).

## 📊 Base de datos (SQLite3)

Estructura de la tabla `users`:

```sql
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone INTEGER NOT NULL
);
```

Insertar registros de ejemplo:

```sql
INSERT INTO users (id, name, last_name, email, phone) VALUES
    (100000044, 'Daniel', 'Martinez', 'dmartinez@unal.edu.co', 3190000000),
    (100000045, 'Ana', 'Lopez', 'alopez@unal.edu.co', 3124567890),
    (100000046, 'Carlos', 'Ramirez', 'cramirez@unal.edu.co', 3009876543);
```

📌 **Nota**: Puedes ampliar la tabla para añadir más usuarios y gestionar el CRUD completo.


## 📜 Licencia
Este proyecto está bajo la licencia **MIT**. ¡Siéntete libre de usar y mejorar este código! 😊

