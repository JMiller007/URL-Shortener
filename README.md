# URL Shortener

A simple URL shortener web application built using Flask and SQLAlchemy. The application allows users to shorten long URLs and redirect to the original URL using the shortened version.

## Features

- Shorten long URLs
- Redirect to original URLs using shortened versions
- Simple and intuitive web interface

## Technologies Used

- Python
- Flask
- SQLAlchemy
- SQLite
- HTML/CSS

## Prerequisites

- Python 3.x

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/JMiller007/URL-Shortener.git
cd URL-Shortener
```

### 2. Set Up a Virtual Environment

Create and activate a virtual environment to manage dependencies:

On macOS and Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages using pip:

```bash
pip install Flask Flask-SQLAlchemy
```

### 4. Set Up the Database

Run the following command to create the database:

```bash
python app.py
```

This command will initialize the SQLite database and create the necessary tables.

## Running the Application

Start the Flask development server:

```bash
python app.py
```

You should see output indicating that the server is running on `http://127.0.0.1:5000/`.

## Accessing the Application

1. Open your web browser and go to `http://127.0.0.1:5000/`.
2. Enter a long URL in the input field and click the "Shorten" button.
3. You will see the shortened URL displayed. Click on the short URL to be redirected to the original URL.

## Project Structure

```
URL-Shortener/
├── venv/                   # Virtual environment directory
├── app.py                  # Main Flask application
├── templates/
│   └── index.html          # HTML template for the web interface
├── urls.db                 # SQLite database file
└── README.md               # Project README file
```

## Code Explanation

### app.py

- **Imports:** Import necessary libraries and modules.
- **Flask App Configuration:** Set up the Flask application and configure the database.
- **Database Model:** Define the URL model with id, original_url, and short_url columns.
- **Database Creation:** Create the database tables.
- **URL Shortening:** Function to generate a random short URL.
- **Routes:** Define routes for the main page and URL redirection.
  - `/`: Handles URL shortening and displays the form.
  - `/<short_url>`: Redirects to the original URL using the short URL.

### templates/index.html

- **HTML Structure:** Basic HTML structure with a form to input the long URL and a section to display the shortened URL.
- **CSS Styling:** Inline CSS to enhance the appearance of the web page.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
