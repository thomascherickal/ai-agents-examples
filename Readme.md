**Use Case**: Automatically categorize and route customer support tickets.

**Run**:
```bash
python 08_haystack_ticket_classifier.py
```

---

### 9. BabyAGI - Project Management

**File**: `09_babyagi_project_manager.py`

Task-driven autonomous agent that generates, prioritizes, and executes sub-tasks.

**Key Features**:
- Automatic sub-task generation
- Dynamic task prioritization
- Iterative execution with context awareness

**Use Case**: Break down complex projects into manageable tasks and execute them autonomously.

**Run**:
```bash
python 09_babyagi_project_manager.py
```

---

### 10. Semantic Kernel - Email Assistant

**File**: `10_semantic_kernel_email_assistant.py`

Professional email composition and tone adjustment using Microsoft's Semantic Kernel.

**Key Features**:
- Multiple tone options (professional, friendly, urgent, apologetic, congratulatory)
- Key points integration
- Tone transformation capabilities

**Use Case**: Generate professional emails quickly and adjust tone for different audiences.

**Run**:
```bash
python 10_semantic_kernel_email_assistant.py
```

---

## Project Structure

```
ai-agents-examples/
│
├── 01_langchain_document_extractor.py    # LangChain document processing
├── 02_autogpt_researcher.py              # AutoGPT autonomous research
├── 03_crewai_marketing_campaign.py       # CrewAI multi-agent collaboration
├── 04_autogen_pair_programming.py        # Microsoft AutoGen coding
├── 05_llamaindex_hr_assistant.py         # LlamaIndex RAG system
├── 06_phidata_financial_assistant.py     # Phidata financial analysis
├── 07_openai_scheduling_assistant.py     # OpenAI Assistants API
├── 08_haystack_ticket_classifier.py      # Haystack NLP pipeline
├── 09_babyagi_project_manager.py         # BabyAGI task management
├── 10_semantic_kernel_email_assistant.py # Semantic Kernel email tools
│
├── README.md                              # This file
├── LICENSE                                # MIT License
├── requirements.txt                       # All dependencies
│
├── data/                                  # Sample data files
│   ├── meeting_transcript.txt
│   └── handbook_docs/
│
└── research_output/                       # Generated reports
```

## Usage

### General Workflow

1. **Choose an Example**: Select the framework that best matches your use case
2. **Install Dependencies**: Install the specific requirements for that example
3. **Configure API Keys**: Set your OpenAI API key in environment variables
4. **Prepare Data**: Create any required input files or directories
5. **Run the Script**: Execute the Python file
6. **Review Output**: Check console output or generated files

### Best Practices

- **API Key Security**: Never commit API keys to version control
- **Cost Management**: Monitor your OpenAI API usage to control costs
- **Error Handling**: Each example includes basic error handling; extend as needed
- **Customization**: Modify prompts and parameters to fit your specific needs
- **Testing**: Start with small datasets before processing large volumes

### Common Customizations

**Changing the Model**:
```python
# Instead of GPT-4
llm = ChatOpenAI(model="gpt-4", temperature=0)

# Use GPT-3.5-turbo for cost savings
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
```

**Adjusting Temperature**:
```python
# More creative (0.7-1.0)
llm = ChatOpenAI(model="gpt-4", temperature=0.9)

# More deterministic (0.0-0.3)
llm = ChatOpenAI(model="gpt-4", temperature=0.1)
```

**Modifying Chunk Sizes**:
```python
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=2000,  # Increase for more context
    chunk_overlap=400  # Increase overlap for better continuity
)
```

## Framework Comparison

| Framework | Best For | Complexity | Multi-Agent | Memory | Learning Curve |
|-----------|----------|------------|-------------|---------|----------------|
| **LangChain** | General purpose, chains | Medium | No | External | Medium |
| **AutoGPT** | Autonomous research | High | No | Built-in | High |
| **CrewAI** | Team collaboration | Medium | Yes | Shared | Medium |
| **AutoGen** | Conversational agents | Medium | Yes | Thread-based | Medium |
| **LlamaIndex** | Document Q&A, RAG | Low | No | Vector DB | Low |
| **Phidata** | Domain-specific tasks | Low | No | Context | Low |
| **OpenAI API** | Production apps | Low | No | Thread-based | Low |
| **Haystack** | Search & NLP pipelines | Medium | No | Document Store | Medium |
| **BabyAGI** | Task automation | High | No | Vector-based | High |
| **Semantic Kernel** | Enterprise integration | Medium | No | Plugin-based | Medium |

## Troubleshooting

### Common Issues

**API Key Not Found**:
```
Error: OpenAI API key not found
Solution: Set OPENAI_API_KEY environment variable
```

**Module Not Found**:
```
Error: ModuleNotFoundError: No module named 'langchain'
Solution: pip install langchain
```

**Rate Limiting**:
```
Error: Rate limit exceeded
Solution: Add delays between requests or upgrade API plan
```

**Memory Issues**:
```
Error: Out of memory when processing large documents
Solution: Reduce chunk_size or process in smaller batches
```

### Debug Mode

Enable verbose output in most frameworks:

```python
# LangChain
agent = initialize_agent(verbose=True)

# CrewAI
crew = Crew(verbose=True)

# AutoGen
agent = AssistantAgent(verbose=True)
```

## Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the Repository**
2. **Create a Feature Branch**: `git checkout -b feature/new-example`
3. **Add Your Example**: Follow the existing code structure
4. **Test Thoroughly**: Ensure your example runs without errors
5. **Update Documentation**: Add your example to this README
6. **Submit a Pull Request**: Describe your changes clearly

### Contribution Guidelines

- Follow PEP 8 style guidelines
- Include clear docstrings and comments
- Add error handling and input validation
- Provide sample data files if needed
- Update requirements.txt with new dependencies
- Test with both GPT-3.5 and GPT-4 if possible

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### MIT License Summary

```
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the software, subject to the following conditions:

- The above copyright notice shall be included in all copies
- The software is provided "as is" without warranty
```

## References

### Official Documentation

- **LangChain**: https://python.langchain.com/docs/get_started/introduction
- **AutoGPT**: https://docs.agpt.co/
- **CrewAI**: https://docs.crewai.com/
- **Microsoft AutoGen**: https://microsoft.github.io/autogen/
- **LlamaIndex**: https://docs.llamaindex.ai/en/stable/
- **Phidata**: https://docs.phidata.com/
- **OpenAI Assistants API**: https://platform.openai.com/docs/assistants/overview
- **Haystack**: https://docs.haystack.deepset.ai/
- **BabyAGI**: https://github.com/yoheinakajima/babyagi
- **Semantic Kernel**: https://learn.microsoft.com/en-us/semantic-kernel/

### Research Papers

1. **ReAct: Synergizing Reasoning and Acting in Language Models** (Yao et al., 2022)
   - https://arxiv.org/abs/2210.03629

2. **Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks** (Lewis et al., 2020)
   - https://arxiv.org/abs/2005.11401

3. **Constitutional AI: Harmlessness from AI Feedback** (Bai et al., 2022)
   - https://arxiv.org/abs/2212.08073

4. **Toolformer: Language Models Can Teach Themselves to Use Tools** (Schick et al., 2023)
   - https://arxiv.org/abs/2302.04761

### Useful Resources

- **OpenAI API Pricing**: https://openai.com/pricing
- **Prompt Engineering Guide**: https://www.promptingguide.ai/
- **LangChain Templates**: https://github.com/langchain-ai/langchain/tree/master/templates
- **Agent Patterns**: https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/

### Community & Support

- **LangChain Discord**: https://discord.gg/langchain
- **OpenAI Community Forum**: https://community.openai.com/
- **AI Agents Reddit**: https://www.reddit.com/r/LangChain/
- **Stack Overflow**: Tag with `langchain`, `openai`, `ai-agents`

### Related Projects

- **LangGraph**: https://github.com/langchain-ai/langgraph - For building stateful agents
- **AutoGen Studio**: https://github.com/microsoft/autogen/tree/main/samples/apps/autogen-studio
- **Chainlit**: https://github.com/Chainlit/chainlit - UI for LangChain applications
- **Flowise**: https://github.com/FlowiseAI/Flowise - Drag & drop LLM flows

### Video Tutorials

- **LangChain Crash Course**: https://www.youtube.com/watch?v=LbT1yp6quS8
- **Building AI Agents**: https://www.youtube.com/watch?v=F8NKVhkZZWI
- **CrewAI Tutorial**: https://www.youtube.com/watch?v=tnejrr-0a94
- **RAG from Scratch**: https://www.youtube.com/watch?v=sVcwVQRHIc8

### Books

1. **"Building LLM Powered Applications"** by Valentina Alto (2024)
2. **"Generative AI with LangChain"** by Ben Auffarth (2023)
3. **"Hands-On Large Language Models"** by Jay Alammar & Maarten Grootendorst (2024)

## Acknowledgments

- OpenAI for the GPT models and API
- Framework developers and maintainers
- The open-source AI community
- Contributors to this repository

## Changelog

### Version 1.0.0 (January 2025)
- Initial release with 10 framework examples
- Comprehensive documentation
- Sample data and use cases

---

## Support

If you encounter issues or have questions:

1. Check the [Troubleshooting](#troubleshooting) section
2. Review the framework's official documentation
3. Search existing GitHub issues
4. Create a new issue with detailed information

## Disclaimer

These examples are for educational purposes. When deploying to production:

- Implement proper error handling and logging
- Add authentication and authorization
- Monitor API usage and costs
- Follow security best practices
- Comply with data privacy regulations
- Test thoroughly before deployment

---

**⭐ If you find this repository helpful, please consider giving it a star!**

**📧 Questions or suggestions? Open an issue or submit a pull request.**

---

*Last Updated: January 2025*
*Author: AI Agents Article Examples*
*Repository: https://github.com/yourusername/ai-agents-examples*
