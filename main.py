import os
from utils import get_groq_api_key, get_hf_token, pretty_print_result
from crewai import Agent, Task, Crew
import streamlit as st
from IPython.display import Markdown

os.environ['OPENAI_API_BASE'] = "https://api.groq.com/openai/v1"
os.environ['OPENAI_API_KEY'] = get_groq_api_key()
os.environ['OPENAI_MODEL_NAME'] = "gemma2-9b-it"

st.title("Content Planning and Review Tool")

topic = st.text_input("Enter the topic for content planning:")
if not topic:
    st.info("Please enter a topic to start.")
    st.stop()

planner = Agent(
    role="Content Planner",
    goal="Plan engaging and factually accurate content on {topic}",
    backstory="You're working on planning a blog article "
              "about the topic: {topic}.",
    allow_delegation=False,
    verbose=True,
)

writer = Agent(
    role="Content Writer",
    goal="Write insightful and factually accurate "
         "opinion piece about the topic: {topic}",
    backstory="You're working on writing "
              "a new opinion piece about the topic: {topic}.",
    allow_delegation=False,
    verbose=True,
)

editor = Agent(
    role="Editor",
    goal="Edit a given blog post to align with "
         "the writing style of the organization.",
    backstory="You are an editor who receives a blog post "
              "from the Content Writer.",
    allow_delegation=False,
    verbose=True,
)

# Define Tasks
plan = Task(
    description=(
        "1. Prioritize the latest trends, key players, "
        "and noteworthy news on {topic}.\n"
        "2. Identify the target audience, considering "
        "their interests and pain points.\n"
        "3. Develop a detailed content outline including "
        "an introduction, key points, and a call to action.\n"
        "4. Include SEO keywords and relevant data or sources."
    ),
    expected_output="simple words outline with sections "
                    "SEO keywords, and resources.",
    agent=planner,
)

write = Task(
    description=(
        "1. Use the content plan to craft a compelling "
        "blog post on {topic}.\n"
        "2. Incorporate SEO keywords naturally.\n"
        "3. Sections/Subtitles are properly named "
        "in an engaging manner.\n"
        "4. Ensure the post is structured with an "
        "engaging introduction, insightful body, "
        "and a summarizing conclusion.\n"
        "5. Proofread for grammatical errors and "
        "alignment with the brand's voice.\n"
    ),
    expected_output="A well-written blog post "
                    "in markdown format, ready for publication, "
                    "each section should have 2 or 3 paragraphs.",
    agent=writer,
)

edit = Task(
    description=("Proofread the given blog post for "
                 "grammatical errors and "
                 "alignment with the brand's voice."),
    expected_output="A well-written blog post in markdown format, "
                    "ready for publication, "
                    "each section should have 2 or 3 paragraphs.",
    agent=editor,
)

crew = Crew(
    agents=[planner, writer, editor],
    tasks=[plan, write, edit],
    verbose=2,
)

if st.button("Start Content Planning"):
    st.write("Processing... Please wait.")

    res = crew.kickoff(inputs={"topic": topic})

    if res:
        st.markdown("### Final Output")
        st.markdown(res)
    else:
        st.error("Failed to generate content. Please check your input or configurations.")
