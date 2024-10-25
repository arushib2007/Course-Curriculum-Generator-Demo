# from langchain.agents import initialize_agent
# from langchain_community.agent_toolkits.load_tools import load_tools
# from langchain.agents import AgentType
# from langchain_community.chat_models import ChatOpenAI

# from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# import os
# from dotenv import load_dotenv

# load_dotenv()

# # Sensitive Information
# API_KEY = os.getenv('OPENAI_API_KEY')

# llm=ChatOpenAI(model="gpt-4-turbo-preview", temperature=0, frequency_penalty=0, presence_penalty=0, 
#                streaming=True, callbacks=[StreamingStdOutCallbackHandler()])

# from langchain.chat_models import ChatOpenAI
# from langchain.chains import ConversationChain
# from langchain.memory import ConversationBufferMemory

# memory = ConversationBufferMemory(memory_key = "chat_history")

# tools = tools = load_tools([], llm=llm)

# agent_chain = initialize_agent(llm=llm, tools = [], agent = AgentType.CONVERSATIONAL_REACT_DESCRIPTION, verbose = False, handle_parsing_errors = True, memory = memory)

# def prompt_template(course_topic, num_weeks, num_chapters, num_tests, final_format):
#     prompt = f"""You are a professor at a college, expert at desgning and creating a course in the field of {course_topic}. This course will take {num_weeks} to complete.
#     {num_chapters} chapters should be covered in the course duration. There will be {num_tests} tests in this course. The finals format will be a {final_format}.
#     You are an expert at writing contents for each week and each specific chapter assigned to that week.
#     """
    
#     return prompt

# human_input = ""

# while human_input.lower() != "end":
#     len_memory = memory.load_memory_variables({})["chat_history"]
    
    
#     if len_memory == "":
#         beginning= True
#     else:
#         beginning = False

#     if beginning:
#         course_topic = input("Please enter the course topic: ")
#         num_weeks = input("Please enter the number of weeks: ")
#         num_chapters = input("Please enter the number of chapters: ")
#         num_tests = input("Please enter the number of tests: ")
#         final_format = input("Please enter the finals format (Final exam or project): ")

#         prompt = prompt_template(course_topic = course_topic, num_weeks = num_weeks, num_chapters = num_chapters, num_tests = num_tests, final_format = final_format)  

#         agent_response = agent_chain.run(prompt)
#         print(agent_response)
#         continue

#     else:
#         human_input = input("Human: \n\n[To end chat, simply type 'end']")
#         if human_input.lower() != "end":
#             agent_reponse = agent_chain.run(human_input)
#             print(agent_response)
