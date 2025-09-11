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

**Tools Used:**
- Website search for real-time news and data
- File reading for local documents and reports
- Directory browsing for relevant materials

## 🔧 Customization

### Modifying Agent Personality
Edit the `backstory` parameter in `digital_twin_agent.py`:

```python
digital_twin_agent = Agent(
    role="Your Custom Role",
    goal="Your Custom Goal",
    backstory="""Your custom backstory that defines personality,
    experience, and approach to problem-solving""",
    # ... other parameters
)
```

### Adding New Tools
Create custom tools by extending `BaseTool`:

```python
class YourCustomTool(BaseTool):
    name: str = "your_tool_name"
    description: str = "Description of what your tool does"
    
    def _run(self, input_data: str) -> str:
        # Your tool implementation
        return "Tool output"
```

### Creating New Task Types
Add new task creation functions:

```python
def create_your_task_type(description: str) -> Task:
    return Task(
        description=f"Your task description: {description}",
        agent=digital_twin_agent,
        expected_output="Expected output description"
    )
```

## 📁 Project Structure

```
MIT AI Studio/
├── digital_twin_agent.py      # Main agent implementation
├── example_usage.py           # Usage examples and interactive mode
├── requirements.txt           # Python dependencies
├── env_example.txt           # Environment variables template
└── README.md                 # This documentation
```

## 🔑 Environment Variables

Required environment variables (set in `.env` file):

```bash
OPENAI_API_KEY=your_openai_api_key_here
CREWAI_VERBOSE=True
CREWAI_MEMORY=True
```

**Getting API Keys:**
- **OpenAI API Key**: Get from [OpenAI Platform](https://platform.openai.com/api-keys)

## 🎨 Example Scenarios

### Scenario 1: Self-Introduction
```python
result = run_digital_twin("introduce")
```

### Scenario 2: VC Pitch
```python
result = run_digital_twin(
    "pitch",
    idea_or_company="Fintech startup targeting small businesses"
)
```

### Scenario 3: Cold Email
```python
result = run_digital_twin(
    "cold_email",
    investor_name="John Smith from Sequoia Capital",
    context="Fintech startup seeking advice on scaling"
)
```

### Scenario 4: Acquisition Search
```python
result = run_digital_twin(
    "search_acquisitions",
    areas_of_interest="fintech, AI, and healthcare"
)
```

## 🚀 Advanced Usage

### Interactive Mode
Run the interactive mode for custom queries:

```bash
python example_usage.py
# Choose option 2 for interactive mode
```

### Custom Crews
Create multi-agent crews by combining your digital twin with other agents:

```python
from crewai import Crew, Process

crew = Crew(
    agents=[digital_twin_agent, other_agent],
    tasks=[task1, task2],
    process=Process.sequential,
    verbose=True
)
```

## 🔍 Troubleshooting

### Common Issues

1. **API Key Error**: Ensure your OpenAI API key is properly set in the `.env` file
2. **Import Errors**: Install all dependencies with `pip install -r requirements.txt`
3. **Memory Issues**: The agent uses memory by default; disable if needed

### Getting Help

- Check the CrewAI documentation: https://docs.crewai.com/
- Review the example usage in `example_usage.py`
- Modify agent parameters in `digital_twin_agent.py`

## 🎯 Future Enhancements

- Integration with real-time data sources
- Custom memory management
- Multi-language support
- Advanced visualization tools
- Integration with business intelligence platforms

## 📝 License

This project is for educational and personal use. Please ensure compliance with OpenAI's usage policies and any applicable licenses for the libraries used.

---

**Your Digital Twin Agent is ready to help you tackle complex business challenges with the analytical rigor and strategic thinking of an MBA graduate!** 🎓🤖
