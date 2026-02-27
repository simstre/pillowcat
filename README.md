# PillowCat

PillowCat is a geolocation-based classifieds web application for trading, selling, and buying used goods. Users can sign in, browse trending item listings, and view individual product pages -- all powered by a lightweight Flask backend with Redis as the data store.

## Tech Stack

| Layer        | Technology                     |
|--------------|--------------------------------|
| Language     | Python 2.7+                    |
| Framework    | Flask 0.10.1                   |
| Templating   | Jinja2 2.7.2                   |
| Data Store   | Redis (via Flask-And-Redis)    |
| Frontend     | Bootstrap 2.x, jQuery, custom CSS |
| WSGI Server  | Gunicorn 18.0                  |
| Deployment   | Heroku (Procfile-based)        |

## Features

- **User Authentication** -- Login/logout with session-based authentication backed by Redis. Includes a `login_required` decorator to protect authenticated routes.
- **Trending Items Dashboard** -- A main view that displays a ranked table of hot/trending items with listing counts.
- **Item Listings** -- Per-item listing pages accessible from the trending dashboard.
- **Sign Up** -- A registration page for new users.
- **Flash Messages** -- User-facing validation feedback on login errors.

## Project Structure

```
pillowcat/
├── run.py                  # Application entry point; registers blueprints and starts the server
├── base_config.py          # App configuration (debug, secret key, Redis connection)
├── requirements.txt        # Python dependencies
├── Procfile                # Heroku process definition (gunicorn)
├── __init__.py             # Top-level package marker
└── app/
    ├── __init__.py         # Flask app factory; initializes Flask and Redis
    ├── views.py            # Route definitions (front, signup, main, listings, settings)
    ├── decorators.py       # Custom decorators (login_required)
    ├── templates/
    │   ├── base.html       # Base layout (Bootstrap CSS/JS, jQuery)
    │   ├── front.html      # Login / landing page
    │   ├── main.html       # Authenticated dashboard with trending items table
    │   ├── listings.html   # Item listings page (stub)
    │   └── signup.html     # User registration page (stub)
    └── static/
        ├── css/
        │   ├── bootstrap.css / bootstrap.min.css
        │   ├── bootstrap-responsive.css / bootstrap-responsive.min.css
        │   └── main.css    # Custom application styles
        ├── js/
        │   ├── bootstrap.js / bootstrap.min.js
        └── img/
            ├── pillowcat_logo.png
            └── glyphicons-halflings*.png
```

## Prerequisites

- Python 2.7 (or a compatible Python version)
- pip
- A running Redis instance (the default configuration points to a hosted Redis service)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/simstre/pillowcat.git
   cd pillowcat
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m virtualenv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Redis:**

   Edit `base_config.py` and update the Redis connection parameters (`REDIS_HOST`, `REDIS_PORT`, `REDIS_PASSWORD`, `REDIS_DB`) to point to your Redis instance.

## Usage

### Development Server

Run the Flask development server directly:

```bash
python run.py
```

The application will be available at `http://127.0.0.1:5000/`.

### Production (Gunicorn)

Start the application with Gunicorn, as configured in the `Procfile`:

```bash
gunicorn run:app
```

## Routes

| Route         | Method(s)   | Auth Required | Description                         |
|---------------|-------------|---------------|-------------------------------------|
| `/`           | GET, POST   | No            | Landing page with login form        |
| `/signup`     | GET         | No            | User registration page              |
| `/main/`      | GET         | Yes           | Dashboard with trending items       |
| `/listings`   | GET         | Yes           | Item listings (accepts `?item=...`) |
| `/settings`   | GET         | Yes           | User settings (not yet implemented) |

## Configuration

All application configuration lives in `base_config.py`:

| Setting              | Description                              |
|----------------------|------------------------------------------|
| `DEBUG`              | Enable/disable Flask debug mode          |
| `SECRET_KEY`         | Secret key for session signing           |
| `SESSION_COOKIE_NAME`| Name of the session cookie (`pillowCat`) |
| `REDIS_HOST`         | Redis server hostname                    |
| `REDIS_PORT`         | Redis server port                        |
| `REDIS_PASSWORD`     | Redis authentication password            |
| `REDIS_DB`           | Redis database index                     |

## Deployment

The project includes a `Procfile` for Heroku deployment:

```
web: gunicorn run:app
```

To deploy to Heroku:

```bash
heroku create
git push heroku master
```

## License

No license file is currently included in the repository.
