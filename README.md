# Digital Twin Agent - CrewAI Implementation

A sophisticated CrewAI agent designed to embody your skills, personality, and interests as an MBA/MS graduate. This "digital twin lite" combines analytical rigor with business acumen to provide comprehensive business analysis, academic research, and strategic planning.

## 🎯 Features

### Core Capabilities
- **Self-Introduction**: Create compelling personal introductions that represent you professionally
- **VC Pitch**: Draft investor-ready pitches for your business ideas or companies
- **Cold Email**: Write professional cold emails to potential investors seeking advice
- **Acquisition Search**: Research latest M&A activity and market trends in your areas of interest

### Custom Tools
- **DirectoryReadTool**: Read and analyze files in directories
- **FileReadTool**: Read and process individual files
- **WebsiteSearchTool**: Search websites for real-time information

## 🚀 Quick Start

### 1. Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp env_example.txt .env
# Edit .env and add your OpenAI API key
```

### 2. Basic Usage

```python
from digital_twin_agent import run_digital_twin

# Self-Introduction
result = run_digital_twin("introduce")

# VC Pitch
result = run_digital_twin(
    "pitch", 
    idea_or_company="AI healthcare startup"
)

# Cold Email
result = run_digital_twin(
    "cold_email",
    investor_name="Sarah Johnson",
    context="AI startup seeking advice"
)

# Search Acquisitions
result = run_digital_twin(
    "search_acquisitions",
    areas_of_interest="AI, healthcare, fintech"
)
```

### 3. Run Examples

```bash
python example_usage.py
```

## 🛠️ Agent Personality & Skills

### Role
Your Digital Twin - Personal AI Assistant

### Key Characteristics
- **Authentic**: Represents you authentically in all communications
- **Professional**: Maintains high standards in all business interactions
- **Strategic**: Big-picture thinking with practical implementation focus
- **Network-Focused**: Builds meaningful business relationships

### Expertise Areas
- Personal Branding & Professional Communication
- VC Pitching & Investor Relations
- Business Development & Networking
- Market Research & Trend Analysis
- Strategic Thinking & Problem Solving

## 📊 Task Types

### 1. Self-Introduction
Create compelling personal introductions that highlight:
- Professional background and expertise
- Key achievements and experiences
- Current focus areas and interests
- Unique value proposition
- What makes you stand out

### 2. VC Pitch
Draft investor-ready pitches including:
- Problem statement and market opportunity
- Solution and unique value proposition
- Business model and revenue streams
- Market size and traction
- Competitive advantage and moats
- Team and execution capability
- Financial projections and funding ask
- Use of funds and next milestones

### 3. Cold Email
Write professional cold emails including:
- Compelling subject line
- Personalized hook
- Brief self-introduction
- Specific reason for reaching out
- Clear advice request
- Meeting proposal
- Clear call to action

### 4. Acquisition Search
Research latest market activity including:
- Recent M&A activity and deal values
- Key players making acquisitions
- Emerging trends and patterns
- Investment themes and valuations
- Market opportunities and gaps
- Strategic insights and implications

### 5. Interactive Mode
In Interactive Mode, you can directly instruct your Digital Twin Agent to perform any custom task. Simply type your task description and specify the desired output format or instructions. The agent will process your request and return a tailored result.

**How to use Interactive Mode:**
1. Run the script in "Interactive" mode.
2. When prompted, enter your task description (e.g., "Draft a LinkedIn summary for a product manager").
3. Specify what kind of output you want (e.g., "A concise, professional summary under 150 words").
4. The agent will generate and display the result.
5. Type "exit" at any time to leave Interactive Mode.

This mode is ideal for experimenting, brainstorming, or handling unique requests beyond the predefined task types.

**Tools Used:**
- Website search for real-time news and data
- File reading for local documents and reports
- Directory browsing for relevant materials