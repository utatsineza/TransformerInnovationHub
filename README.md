# Transformer Innovation Hub

Transformer Innovation Hub is a web application that allows users to shop for recycled materials and learn about the benefits of recycling through a dedicated blog section.

## Features

- **Shop**: Browse and purchase recycled materials.
- **Blog**: Read informative articles about recycling and sustainability.
- **User Authentication**: Sign up, log in, and manage user profiles.
- **Admin Panel**: Manage products, blog posts, and users through Django's admin interface.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS
- **Database**: SQLite (default for development)

## Prerequisites

Ensure you have the following installed on your system:

- Python (>= 3.8)
- Git
- Virtualenv (optional but recommended)

## Installation & Setup

Follow these steps to set up the project locally:

### 1. Clone the Repository

````sh
git clone https://github.com/utatsineza/TransformerInnovationHub.git
cd TransformerInnovationHub

### 2. Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
````

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

cd innovation_hub

### 4. Apply Migrations

```sh
python manage.py migrate
```

### 5. Create a Superuser (For Admin Panel)

```sh
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 6. Run the Development Server

```sh
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## API's

Google Font: https://developers.google.com/fonts/docs/getting_started

## Project Structure

```
TransformerInnovationHub/
|-- innovatin_hub
    │── manage.py           # Django management script
    │── webstore/           # web app
    │── cart/               # cart app
    |-- db.sqlite3
    |-- media               # storing media files
    |-- innovation_hub      # django project control center
|-- db.sqlite3
|-- README.md
|-- requirements.txt
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License.

## Contact

For inquiries, reach out via [aimablenkurikiyimana1@gmail.com or aimable0].


Thank you!