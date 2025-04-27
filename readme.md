# Multi-Agent Article Researcher and Writer

This is a Python application that demonstrates the power of multi-agent systems using CrewAI. The application consists of two specialized agents working together to research a topic and create a well-written article.

## Overview

The application uses two AI agents:
1. **Researcher Agent**: Responsible for gathering and analyzing information about a given topic
2. **Writer Agent**: Takes the research findings and crafts them into a well-structured article

## Features

- Multi-agent collaboration using CrewAI
- Automated research and content generation
- Topic-based research capabilities
- Structured article writing
- Easy-to-use interface

## Requirements

- Python 3.8+
- CrewAI
- Additional dependencies (to be added as development progresses)

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/multiagent-article-researcher-writer.git

# Navigate to the project directory
cd multiagent-article-researcher-writer

# Install dependencies
pip install -r requirements.txt
```

## Configuration

Before running the application, you need to set up your API keys:

1. Copy the template config file:
   ```bash
   cp config.json.template config.json
   ```

2. Edit the `config.json` file and add your API keys:
   - `openai_api_key`: Your OpenAI API key
   - `serper_api_key`: Your Serper API key for web search
   - `model`: The OpenAI model to use (default: gpt-4-turbo-preview)
   - `temperature`: The temperature setting for the model (default: 0.7)

The `config.json` file is ignored by git to protect your API keys.

## Usage

Instructions for using the application will be added as development progresses.

## Project Structure

The project structure will be documented here as we develop the application.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
