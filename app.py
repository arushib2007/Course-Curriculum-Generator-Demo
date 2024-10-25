from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

# import pdfkit

# path_wkhtmltopdf = 'C:\\Program Files\\wkhtmltopdf'
# config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

app = Flask(__name__)
CORS(app)

from langchain.agents import initialize_agent
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import AgentType
from langchain_community.chat_models import ChatOpenAI

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

import os
from dotenv import load_dotenv

load_dotenv()

# Sensitive Information
API_KEY = os.getenv('OPENAI_API_KEY')

llm=ChatOpenAI(model="gpt-4-turbo-preview", temperature=0, frequency_penalty=0, presence_penalty=0, 
               streaming=False, callbacks=[StreamingStdOutCallbackHandler()])

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(memory_key = "chat_history")

tools = tools = load_tools([], llm=llm)

agent_chain = initialize_agent(llm=llm, tools = [], agent = AgentType.CONVERSATIONAL_REACT_DESCRIPTION, verbose = False, handle_parsing_errors = True, memory = memory)

def prompt_template(course_topic, num_weeks, num_chapters, num_tests, final_format):
    prompt = f"""You are a professor at a college, expert at desgning and creating a course in the field of {course_topic}. This course will take {num_weeks} weeks to complete.
    {num_chapters} chapters should be covered in the course duration. Students will have {num_tests} tests and the finals 
    format will be a {final_format}. You are an expert at writing contents for each specific week and each chapter.
    """
    
    return prompt

def quiz_prompt_template(results):
    prompt = f"Please pull a simple bullet list of the main conceps in {results}. Each item in the list should only contain one short sentence and be separated by an asterisk (*)."

    return prompt

def quiz_generate_template(topic):

    prompt = f"""You are an experienced quiz generator chatbot. Provided the course material, generate Advanced Placement (AP) style multiple choice quiz questions for a student and ask them. 
    Once the user provides you with the answers in the same order, grade their quiz. Remember, this quiz MUST HAVE 5 questions. 
    At the end of the quiz, provide meaningful feedback to the student along with their grade.
    [TOPIC]
    {topic}
    [END OF TOPIC]
    """
    
    return prompt

def submit_quiz_template(quiz_content, first_answer, second_answer, third_answer, fourth_answer, fifth_answer):
    
    print(quiz_content)
    
    prompt = f"Here is my quiz: {quiz_content}. Here are my answers: {first_answer, second_answer, third_answer, fourth_answer, fifth_answer}. Please provide me with my results."

    return prompt

@app.route("/")
def home():
    return "Welcome to My App"

@app.route("/about")
def about():
    return 'About My Application'

@app.route("/handle_submit", methods = ['POST'])
def handle_submit():
    data = request.get_json()

    subject = data['subject']
    weeks = data['weeks']
    chapters = data['chapters']
    tests = data['tests']
    final_exam_or_project = data['finalExamOrProject']

    prompt = prompt_template(
        course_topic = subject, 
        num_weeks = weeks, 
        num_chapters = chapters, 
        num_tests = tests, 
        final_format = final_exam_or_project)  

    agent_response = agent_chain.run(prompt)
    return render_template('results.html', agent_response=agent_response)

    # prompt_template(subject, difficulty, weeks, chapters, midterms, final_exam_or_project)

# # To Do: Handle Conversion of JSON Response to PDF
# @app.route("/handle_pdf", methods = ['POST'])
# @cross_origin()
# def handle_pdf():
#     html = '<h1>Testing</h1>'
#     return pdfkit.from_string(html, 'response.pdf', configuration=config)

@app.route('/generate_quiz', methods= ['POST'])
def generate_quiz():
    data = request.get_json()
    chapters = data['chapters']

    prompt = quiz_prompt_template(chapters)

    agent_response = agent_chain.run(prompt)

    return render_template('results.html', agent_response=agent_response)

@app.route('/render_quiz', methods = ['POST'])
def render_quiz():
    data = request.get_json()
    topic = data['topic']

    prompt = quiz_generate_template(topic)

    agent_response = agent_chain.run(prompt)

    return render_template("results.html", agent_response=agent_response)

@app.route('/submit_quiz', methods = ['POST'])
def submit_quiz():
    data = request.get_json()

    quiz_content = data['quizContent']
    first_answer = data['firstAnswer']
    second_answer = data['secondAnswer']
    third_answer = data['thirdAnswer']
    fourth_answer = data['fourthAnswer']
    fifth_answer = data['fifthAnswer']

    prompt = submit_quiz_template(
            quiz_content=quiz_content, 
            first_answer=first_answer, 
            second_answer=second_answer, 
            third_answer=third_answer, 
            fourth_answer=fourth_answer, 
            fifth_answer=fifth_answer
        )
    
    agent_response = agent_chain.run(prompt)

    return render_template("results.html", agent_response=agent_response)

if __name__ == '__main__':
    app.run(debug=True)