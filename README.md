# Bowling LexisNexis

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Summary of Endpoint](#summary-of-endpoints)
- [Continuous Integration](#continuous-integration)
- [Future Enhancements](#future-enhancements)

## Project Description

The Bowling Game API is a RESTful web service that allows users to:

* Create and manage players.
* Start and track bowling games.
* Record rolls and calculate scores according to standard * bowling rules.
* Generate natural language summaries of games using OpenAI's language model.
* Retrieve player statistics.

This application can serve as a backend for bowling game applications or integrate into other services requiring bowling score calculations.

## Features

* Player Management: Create and retrieve player information.
* Game Management: Start new games and track game progress.
* Roll Recording: Record individual rolls for each game.
* Score Calculation: Calculate and retrieve the current score of a game.
* Game Summaries: Generate natural language summaries of games.
* Player Statistics: Retrieve statistics for individual players.
* Continuous Integration: Automated testing using GitHub Actions.

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Virtual Environment (optional but recommended)
- OpenAI API Key (for generating game summaries)

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

6 **Set Up Environment Variables**

- Create a .env file in the project root directory
- Add your OpenAI API key:

    OPENAI_API_KEY=your-openai-api-key

### Usage

1. **Run the application:**

    python app.py

2. **Access the application:**

    Open your web browser and navigate to http://127.0.0.1:5000.

### Running Tests

**To run the tests, use the following command:**

    python -m unittest discover -s tests

This will run all tests located in the tests directory.


### Summary of Endpoints

**Games**

* POST /games: Create a new game.
* POST /games/{game_id}/rolls: Record a roll.
* GET /games/{game_id}/score: Get the current score.
* GET /games/{game_id}/summary: Get a game summary.


**Players**

* POST /players: Create a new player.
* GET /players/{player_id}/statistics: Get player statistics.

### Continuous Integration

- The project uses GitHub Actions for continuous integration.
- Workflows are defined in .github/workflows/ci.yml.
- Tests are automatically run on each push and pull request to the main branch.


### Future Enhancements

- Integrate a persistent database for data storage.
- Implement authentication and authorization mechanisms.
- Extend the API to support multi-player games.
- Deploy the application to a live server for public access.
- Add detailed API documentation using Swagger or similar tools.

# API Reference

### Base URL

Local Development: http://127.0.0.1:5000

### Endpoints

1. Create a New Player:

        - URL: /players
        - Method: POST
        - Description: Create a new player.

    * Request Body:

            {
                "name": "string"
            }

            - name (string, required): The name of the player.

    * Response:

     - Success (201 Created):

            {
                "player_id": "string"
            }

     - Error Responses:

            400 Bad Request: Invalid input data.
            500 Internal Server Error: Server error.

2. Get Player Statistics

        - URL: /players/{player_id}/statistics
        - Method: GET
        - Description: Retrieve statistics for a specific player.

    Path Parameters:

        - player_id (string, required): The ID of the player.

    Response:

        Success (200 OK):
        {
            "player_id": "string",
            "name": "string",
            "games_played": "integer",
            "average_score": "float"
        }

    Error Responses:

        - 404 Not Found: Player not found.
        - 500 Internal Server Error: Server error.

3. Create a New Game

        - URL: /games
        - Method: POST
        - Description: Start a new game for a player
    
    Request Body:

        {
            "player_id": "string"
        }

        player_id (string, required): The ID of the player starting the game.

    Response:

        Success (201 Created):
            
            {
                "game_id": "string"
            }

        Error Response:

            - 400 Bad Request: Invalid input data.
            - 404 Not Found: Player not found.
            - 500 Internal Server Error: Server error.

4. Record a Roll

        - URL: /games/{game_id}/rolls
        - Method: POST
        - Description: Record a roll in a game.

    Path Parameters:
    
        game_id (string, required): The ID of the game

    Request Body:

        {
            "pins": "integer"
        }

        pins (integer, required): Number of pins knocked down in the roll (0-10).

    Response:

        Success (200 OK):

        {
            "message": "Roll recorded"
        }

        Error Responses:

        - 400 Bad Request: Invalid input data.
        - 404 Not Found: Game not found.
        - 500 Internal Server Error: Server error.

5. Get Current Score

        URL: /games/{game_id}/score
        Method: GET
        Description: Retrieve the current score of a game.

    Path Parameters:

        game_id (string, required): The ID of the game

    Response:

        Success (200 OK):

        {
            "score": "integer"
        }

        Error Responses:

        - 404 Not Found: Game not found.
        - 500 Internal Server Error: Server error.

6. Get Game Summary

        URL: /games/{game_id}/summary
        Method: GET
        Description: Generate a natural language summary of the game.

    Path Parameters:

        game_id (string, required): The ID of the game

    Response:

        Success (200 OK):

        {
            "summary": "string"
        }

        Error Response:

        - 404 Not Found: Game not found.
        - 500 Internal Server Error: Failed to generate summary.

Error Codes:

    - 200 OK: The request was successful.
    - 201 Created: A new resource was successfully created.
    - 400 Bad Request: The request was invalid or cannot be served.
    - 404 Not Found: The requested resource could not be found.
    - 500 Internal Server Error: An error occurred on the server.


### Authentication

* Current Status: No authentication is implemented.
* Future Considerations:
        * Implementing API keys or token-based authentication to secure endpoints..

