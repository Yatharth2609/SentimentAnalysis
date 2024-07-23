# Sentiment Analysis Project

This project is a web application that performs sentiment analysis on text input using a machine learning model trained on Amazon reviews.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Dataset](#dataset)
4. [Project Structure](#project-structure)
5. [Running the Application](#running-the-application)
6. [Deployment](#deployment)
7. [Contributing](#contributing)
8. [License](#license)

## Prerequisites

- Python 3.7+
- pip (Python package installer)
- Git

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/sentiment-analysis-project.git
   cd sentiment-analysis-project
   ```

2. Create a virtual environment:
   ```
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     .venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source .venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Dataset

This project uses the Amazon Reviews dataset for training the sentiment analysis model. Follow these steps to download and prepare the dataset:

1. Download the dataset:
   - Visit [Amazon Reviews dataset]([https://www.kaggle.com/datasets/bittlingmayer/amazonreviews](https://data.world/datafiniti/consumer-reviews-of-amazon-products)) (you may need to create a Data World account if you don't have one)
   - Click on the "Download" button to get the dataset

2. Extract the downloaded file:
   - The dataset is typically compressed. Extract it using your preferred method (e.g., 7-Zip, WinRAR, or the `unzip` command on Unix-based systems)

3. Preprocess the dataset:
   - Run the preprocessing script:
     ```
     python preprocess_data.py
     ```
   - This script will create a cleaned and formatted version of the dataset named `amazon_reviews.csv` in the project root directory

Note: The original dataset is quite large. If you're facing issues with memory or processing time, consider using a subset of the data for initial development and testing.

## Project Structure

```
sentiment-analysis-project/
│
├── .venv/                  # Virtual environment (not tracked by Git)
├── static/                 # Static files (CSS, JavaScript)
├── templates/              # HTML templates
├── .gitignore              # Specifies intentionally untracked files to ignore
├── app.py                  # Main Flask application
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## Running the Application

1. Ensure your virtual environment is activated

2. Run the Flask application:
   ```
   python app.py
   ```

3. Open a web browser and navigate to `http://localhost:5000`

## Deployment

### PythonAnywhere

1. Sign up for a free account at PythonAnywhere.com

2. Upload your project files using PythonAnywhere's "Files" tab or via Git

3. Create a new web app:
   - Go to the "Web" tab and click "Add a new web app"
   - Choose "Manual configuration" and select Python 3.7+

4. Set up your virtual environment:
   ```
   mkvirtualenv --python=/usr/bin/python3.7 mysite-virtualenv
   pip install -r requirements.txt
   ```

5. Configure your WSGI file:
   - Modify the WSGI configuration file to import your Flask app

6. Upload your dataset or configure database access as needed

7. Reload your web app

For more detailed instructions, refer to the PythonAnywhere deployment guide in our project documentation.

### Render

1. Sign up for a free account at render.com

2. Connect your GitHub repository

3. Create a new Web Service:
   - Choose your repository
   - Select the branch you want to deploy
   - Set the environment to Python 3
   - Set the build command to `pip install -r requirements.txt`
   - Set the start command to `gunicorn app:app`

4. Configure environment variables if necessary

5. Deploy your application

For more detailed instructions, refer to the Render deployment guide in our project documentation.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
