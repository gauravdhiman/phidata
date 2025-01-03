"""
Gmail Agent that can read, draft and send emails using the Gmail.
"""
from phi.agent import Agent
from dotenv import load_dotenv
load_dotenv()

from phi.model.google import Gemini
from phi.tools.gmail_tools import GmailTools

agent = Agent(
    name="Gmail Agent",
    model=Gemini(id="gemini-2.0-flash-exp"),
    tools=[
        GmailTools()
    ],
    description="You are an expert Gmail Agent that can read, draft and send emails using the Gmail.",
    instructions=[
        "Based on user query, you can read, draft and send emails using the Gmail.",
        "While showing email contents, you can summarize the email contents, extract key details and dates.",
        "Show the email contents in a structured markdown format.",
    ],
    markdown=True,
    show_tool_calls=False,
    debug_mode=True,
)

agent.print_response(
    "summarize my last 5 emails with dates and key details, regarding ai agents",
    markdown=True,
    stream=True
)