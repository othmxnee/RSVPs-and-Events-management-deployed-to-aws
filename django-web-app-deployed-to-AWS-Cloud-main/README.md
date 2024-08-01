# django-web-app-deployed-to-AWS-Cloud

# Events and RSVP Management Backend Web App

This is a backend web application for managing events and RSVPs, built with Django and Django REST Framework (DRF). The project is deployed to AWS using Zappa and leverages various AWS services such as S3, Lambda, API Gateway, SES, and CloudFront.

## Features

- Event management (CRUD operations)
- RSVP management
- User authentication with JWT
- Email notifications using AWS SES
- Static and media file storage with AWS S3
- Deployment with Zappa
- Logging




![Uploading Screenshot from 2024-07-31 21-26-15.png…]()







## Technologies Used

- Django
- Django REST Framework
- Zappa
- AWS Lambda
- AWS API Gateway
- AWS S3
- AWS SES
- AWS CloudFront
- PostgreSQL

## Setup and Installation

### Prerequisites

- Python 3.8 or later
- AWS account with IAM user credentials
- PostgreSQL database

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Configure environment variables:**

    Create a `.env` file in the project root and add the following variables:

    ```plaintext
    AWS_ACCESS_KEY_ID=your-aws-access-key-id
    AWS_SECRET_ACCESS_KEY=your-aws-secret-access-key
    AWS_SES_REGION_NAME=us-east-1
    AWS_SES_REGION_ENDPOINT=email.us-east-1.amazonaws.com
    DEFAULT_FROM_EMAIL=your-verified-email@example.com
    AWS_STORAGE_BUCKET_NAME=mydjangobucket007
    AWS_S3_REGION_NAME=us-east-1
    DATABASE_NAME=your_db_name
    DATABASE_USER=your_db_username
    DATABASE_PASSWORD=db_password
    DATABASE_HOST=db_host
    SECRET_KEY=your-secret-key
    ```

5. **Update `settings.py`**

















