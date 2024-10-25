# StudyBuddyAI

This is a web application that generates and grades quizzes based on selected chapters/topics from a course curriculum.

## Technologies Used

- **Front End:**

  - React
  - React Router DOM
  - Material-UI

- **Back End:**
  - Flask
  - Python
  - HTML Parsing (for quiz generation)

## Prerequisites

Before running this application locally, make sure that you have the following installed:

- Node.js and npm (Node Package Manager)
- Python 3
- Flask (Python web framework)

## Getting Started

To get a local copy of this project up and running, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/arushib2007/Course-Curriculum-Generator.git
cd Course-Curriculum-Generator
```

### 2. Setup the Back End (Flask)

Create and activate a Python virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

Install Flask and other dependencies:

```bash
pipenv install
```

IMPORTANT: Create a `.env` file at the root level of the Flask application with the following content:

```bash
OPENAI_API_KEY=your_api_key_here
```

Run Flask:

```bash
flask run
```

This will start the Flask development server at http://localhost:5000.

### 3. Setup the Front End (React)

In a separate Terminal shell, navigate to the front end directory:

```bash
cd front-end
```

Install dependencies:

```bash
npm install
```

Start the React development server:

```bash
npm start
```

This will start the React development server at http://localhost:3000.

### 4. Accessing the Application

Open your web browser and go to http://localhost:3000 to access the Course Curriculum Generator application.

Feel free to fork this repository, make changes, and submit pull requests. Contributions are welcome!

This project is licensed under the MIT License.
