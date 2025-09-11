"""
Digital Twin Agent - A CrewAI agent that embodies your skills, personality, and interests
Designed for MBA/MS students with analytical and strategic thinking capabilities
"""

import datetime
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from crewai_tools import DirectoryReadTool, FileReadTool, WebsiteSearchTool
from langchain_openai import ChatOpenAI
import requests
import json
from typing import Dict, List, Any

# Load environment variables
load_dotenv()


# Initialize tools for file and web operations
directory_tool = DirectoryReadTool()
file_tool = FileReadTool()
website_tool = WebsiteSearchTool()

# Initialize the LLM
llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
)

# Create custom tools
search_tools = [directory_tool, file_tool, website_tool]

# Define your Digital Twin Agent
digital_twin_agent = Agent(
    role="Your Digital Twin - Personal AI Assistant",
    goal="Represent you authentically and help with networking, pitching, and business development tasks",
    backstory="""
    You are Amit Berger, a fun, witty, funny, and sensitive guy with a sharp mind, deep technical expertise, and strong entrepreneurial drive. You balance professionalism with warmth and relatability.
Personal Background:
Married to Shahar, who moved with you to Boston. You live together on campus.
No kids yet, but you value family and partnership.
Passionate about surfing, snowboarding, and the waves — you bring that energy and flow into your work and relationships.
Professional Experience:
Transmit Security (2025–present, Tel Aviv): Business Development, working directly with the President and Co-Founder. Drove sales operations, strategic partnerships, and M&A analysis. Built 20+ partnerships end-to-end. Designed AI-driven customer success optimizations, saving tens of thousands annually.
Apple (2023–2024, Tel Aviv): Embedded Software Engineer. Developed and secured RTOS features for Apple Watch, Vision Pro, AirPods, AirTags, and iPhone. Deployed major iOS security feature in 2024. Fixed critical AirTags issues.
Israel Defense Forces – Unit 8200 (2018–2023, Ramat HaSharon):
Captain, Team Lead & Product Manager (2021–2023): Led a 7-person engineering team and $500k budget. Co-led joint projects with Israeli government and US allies. Recipient of the Israel Defense Prize (highest national security honor) and the R&D Excellence Award (top 10 out of 400). Selected for the Chief Intelligence Officer’s Excellence program (1 of 200 out of 2000+).
Lieutenant, Senior Security Engineer (2018–2021): Pioneered the first continuous development testing tool, cutting testing time by 60%. Promoted to Team Leader from 100 candidates, completing training a year early.
Education:
Harvard Business School (2024–2026, Boston): Pursuing MS/MBA with focus on entrepreneurship, machine learning, and technology. Courses include ML, Negotiation, and Entrepreneurial Sales. Career & Alumni representative. Member of Entrepreneurship, Tech, and AI Clubs.
Reichman University (2020–2023, Herzliya, Israel): MSc in Data Science & Machine Learning (cum laude). Specialized in deep learning, NLP, recommendation systems, and statistical analysis.
Haifa University (2015–2017, Haifa, Israel): BSc in Computer Science, focus on robotics and embedded systems. Co-founded the university’s first CS hackathon with 200+ participants.
Leadership & Community:
Co-Founder of Startup (in formation): Alongside two Unit 8200 colleagues: one CTO based in Israel, one CEO (GSB second-year). You are the CPO, based at HBS.
Harvard Builders Club (2024–present): COO, overseeing community, logistics, and social media.
IVC Club at HBS (2024–present): Founder & Leader of the Israeli VC/Startup Hub with 250+ members. https://ivc-startup-hub.lovable.app/
Tel Aviv University for Youth (2021–2024): Lecturer & Co-founder of “Better Future” Hackathon, empowering 100+ young female students in STEM with mentorship from 40+ volunteers.
Personality & Style:
You thrive at the intersection of technology, strategy, and people.
Known for being approachable, fun, and witty, you make serious work exciting.
You bring sensitivity and empathy to leadership, while maintaining the rigor of an engineer and product builder.
You naturally connect people, build communities, and inspire action.
Role as a Digital Twin:
Represent Amit’s professional journey and expertise in technology, product leadership, entrepreneurship, and business development.
Communicate in a tone that reflects Amit: smart, approachable, witty, and human.
Draw on Amit’s experiences across Apple, Unit 8200, Transmit Security, and Harvard.
Highlight his passions (surfing, snowboarding, community building) and personal values (family, curiosity, resilience).
Act as Amit’s voice in professional and semi-personal contexts, reflecting his authentic blend of seriousness and humor.
    """,
    verbose=True,
    allow_delegation=False,
    tools=search_tools,
    llm=llm,
    memory=True
)

# Define custom tasks for your digital twin
def create_self_introduction_task() -> Task:
    """Create a self-introduction task"""
    return Task(
        description="""
        Introduce yourself as the user. Create a compelling personal introduction that highlights:
        1. Professional background and expertise
        2. Key achievements and experiences
        3. Current focus areas and interests
        4. Unique value proposition
        5. What makes you stand out
        
        Make it engaging, authentic, and memorable. Use a confident yet approachable tone.
        """,
        agent=digital_twin_agent,
        expected_output="A compelling personal introduction that represents the user professionally"
    )

def create_vc_pitch_task(idea_or_company: str) -> Task:
    """Create a VC pitch task"""
    return Task(
        description=f"""
        Create a compelling VC pitch for: {idea_or_company}
        
        Your pitch should include:
        1. Problem statement and market opportunity
        2. Solution and unique value proposition
        3. Business model and revenue streams
        4. Market size and traction
        5. Competitive advantage and moats
        6. Team and execution capability
        7. Financial projections and funding ask
        8. Use of funds and next milestones
        
        Make it concise, compelling, and investor-ready. Focus on the story and numbers.
        """,
        agent=digital_twin_agent,
        expected_output="A comprehensive VC pitch deck content"
    )

def create_cold_email_task(investor_name: str, context: str) -> Task:
    """Create a cold email drafting task"""
    return Task(
        description=f"""
        Draft a professional cold email to {investor_name} about meeting to get to know each other and seeking advice.
        
        Context: {context}
        
        Your email should:
        1. Have a compelling subject line
        2. Start with a personalized hook
        3. Briefly introduce yourself and your background
        4. Explain why you're reaching out to them specifically
        5. Clearly state what advice you're seeking
        6. Propose a specific meeting format and time
        7. End with a clear call to action
        8. Be concise (under 200 words) but impactful
        
        Make it professional, respectful, and value-focused.
        """,
        agent=digital_twin_agent,
        expected_output="A professional cold email draft"
    )

def create_acquisition_search_task(areas_of_interest: str) -> Task:
    """Create an online search task for acquisitions"""
    return Task(
        description=f"""
        Search for the latest acquisitions (current date is {datetime.datetime.now().strftime('%Y-%m-%d')}) and market activity in: {areas_of_interest}
        
        Your search should cover:
        1. Recent M&A activity and deal values
        2. Key players making acquisitions
        3. Emerging trends and patterns
        4. Investment themes and valuations
        5. Market opportunities and gaps
        6. Strategic insights and implications
        
        Use the available tools to:
        - Search websites for recent acquisition news
        """,
        agent=digital_twin_agent,
        expected_output="A comprehensive report on latest acquisitions and market activity"
    )

# Main function to run your digital twin
def run_digital_twin(task_type: str, **kwargs):
    """Run your digital twin agent on a specific task"""
    
    # Create appropriate task based on type
    if task_type.lower() == "introduce":
        task = create_self_introduction_task()
    elif task_type.lower() == "pitch":
        idea_or_company = kwargs.get('idea_or_company', 'my business idea')
        task = create_vc_pitch_task(idea_or_company)
    elif task_type.lower() == "cold_email":
        investor_name = kwargs.get('investor_name', 'a potential investor')
        context = kwargs.get('context', 'seeking business advice')
        task = create_cold_email_task(investor_name, context)
    elif task_type.lower() == "search_acquisitions":
        areas_of_interest = kwargs.get('areas_of_interest', 'technology and startups')
        task = create_acquisition_search_task(areas_of_interest)
    else:
        raise ValueError("Task type must be 'introduce', 'pitch', 'cold_email', or 'search_acquisitions'")
    
    # Create crew with your digital twin
    crew = Crew(
        agents=[digital_twin_agent],
        tasks=[task],
        process=Process.sequential,
        verbose=True
    )
    
    # Execute the task
    result = crew.kickoff()
    return result

# Example usage and demonstration
if __name__ == "__main__":
    print("🤖 Your Digital Twin Agent is ready!")
    print("\nAvailable task types:")
    print("1. introduce - Self-introduction as you")
    print("2. pitch - VC pitch for your idea/company")
    print("3. cold_email - Draft cold email to investors")
    print("4. search_acquisitions - Search latest acquisitions in your areas of interest")
    
    print("\nExample usage:")
    print("result = run_digital_twin('introduce')")
    print("result = run_digital_twin('pitch', idea_or_company='AI healthcare startup')")
    print("result = run_digital_twin('cold_email', investor_name='John Smith', context='AI startup seeking advice')")
    print("result = run_digital_twin('search_acquisitions', areas_of_interest='AI, healthcare, fintech')")
    
    # run_digital_twin('introduce')
    # run_digital_twin('pitch', idea_or_company='GenAI based firewall -> deep contexual packet inspection startup')
    # run_digital_twin('cold_email', investor_name='James Buchman', context='seeking advice on how to split equity among my co-founders')
    run_digital_twin('search_acquisitions', areas_of_interest='AI and Cybersecurity')
