# Pre-entrega 7 - Base inicial de Django

Proyecto base para comenzar el desarrollo de un blog web con Django.

El proyecto incluye la configuración inicial de Django y una aplicación llamada `posts`, que se utilizará en las próximas etapas para desarrollar las publicaciones del blog.

## Tecnologías

- Python 3
- Django 5.2.17
- SQLite

## Estructura principal

```text
Pre-entrega-7/
├── blog_project/
├── posts/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Clonar el repositorio

```powershell
git clone https://github.com/santimachuca/pre-entrega-7-python.git
cd pre-entrega-7-python
```

## Crear y activar el entorno virtual

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

## Instalar dependencias

```powershell
python -m pip install -r requirements.txt
```

## Ejecutar migraciones

```powershell
python manage.py migrate
```

## Levantar el servidor

```powershell
python manage.py runserver
```

Luego abrir `http://127.0.0.1:8000/`.

## Aplicación principal

La aplicación principal se llama `posts` y está registrada mediante `posts.apps.PostsConfig`.

## Configuración regional

- Idioma: español de Argentina (`es-ar`).
- Zona horaria: `America/Argentina/Buenos_Aires`.

## Autor

Santiago Machuca
