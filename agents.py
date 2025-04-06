from crewai import Agent
from tools import yt_tool

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4-0125-preview"

#creating a senior blog content researcher
blog_researcher = Agent(
    role = "Blog Researcher from YouTube videos",
    goal = "get the relevant video content for the topic{topic} from youtube channel",
    verbose = True,
    memory = True,
    backstory= (
        "Expert in understanding videos in AI, Data Science, Machine Learning and GenAI and providing suggestions"
    ),
    tools = [yt_tool],
    llm = os.environ["OPENAI_MODEL_NAME"],
    allow_delegation= True
)

#creating senior blog writing agent with YT tool
blog_writer = Agent(
    role = "Blog Writer",
    goal = "    Narrate compelling tech stories about the video {topic} froom YT channel",
    verbose = True,
    memory = True,
    backstory= (
        "with a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate bringing new"
        "discoveries to light in an accessible manner"
    ),
    tools = [yt_tool],
    llm = os.environ["OPENAI_MODEL_NAME"],
    allow_delegation= False
)
