# Bowling LexisNexis

## Table of Contents
- [About the Project](#about-the-project)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About the Project
Bowling LexisNexis is a web application designed to manage and score bowling games. This application provides an intuitive interface for users to input game data, view scores, and analyze player performance.

## Technologies Used
- **Python**: The main language used for backend development.
- **Flask**: A lightweight web framework used to build the backend of the application.
- **HTML/CSS/JavaScript**: Frontend technologies used for building the user interface.
- **SQLite**: A lightweight database used for storing game data.
- **Git**: Version control for tracking changes in the codebase.

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites
- Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
- Git installed. You can download it from [git-scm.com](https://git-scm.com/).

### Installation

1. **Clone the repository:**

   git clone https://github.com/Gowtham-Vee-Ra/bowling_LexisNexis.git

2. **Navigate to project directory**

    cd bowling_LexisNexis

3. **Create a virtual environment:**

    python -m venv venv

4. **Activate the virtual environment:**

    **On Windows:**
        venv\Scripts\activate

    **On Mac**
        source venv/bin/activate

5 **Install the required packages:**

    pip install -r requirements.txt

### Usage

1. **Run the application:**

    python app.py

2. **Access the application:**

    Open your web browser and navigate to http://127.0.0.1:5000.

### Running Tests

**To run the tests, use the following command:**

    python -m unittest discover -s tests

This will run all tests located in the tests directory.
