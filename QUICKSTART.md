# Quick Start Guide

Get up and running with AI Agents Examples in 5 minutes!

## Prerequisites

- Python 3.10 or higher installed
- Basic command line knowledge
- OpenAI API account (free tier works for testing)

## 5-Minute Setup

### Step 1: Get OpenAI API Key (2 minutes)

1. Go to https://platform.openai.com/
2. Sign up or log in
3. Navigate to API Keys section
4. Create new secret key
5. Copy and save it securely

### Step 2: Clone and Setup (1 minute)

```bash
# Clone the repository
git clone https://github.com/thomascherickal/ai-agents-examples.git
cd ai-agents-examples

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### Step 3: Configure Environment (1 minute)

```bash
# Copy environment template
cp .env.example .env

# Edit .env file and add your API key
# OPENAI_API_KEY=sk-your-actual-key-here
```

Or set it directly:
```bash
# Windows
set OPENAI_API_KEY=sk-your-actual-key-here

# Mac/Linux
export OPENAI_API_KEY=sk-your-actual-key-here
```

### Step 4: Install and Run (1 minute)

Choose ONE example to start with:

#### Option A: Document Summarization (Easiest)
```bash
pip install langchain openai
echo "This is a test meeting transcript." > meeting_transcript.txt
python 01_langchain_document_extractor.py
```

#### Option B: Financial Analysis (Most Visual)
```bash
pip install phidata yfinance pandas openai
python 06_phidata_financial_assistant.py
```

#### Option C: Email Assistant (Most Practical)
```bash
pip install semantic-kernel
python 10_semantic_kernel_email_assistant.py
```

## What to Try First

### For Beginners
Start with **Example 06 (Phidata)** - it's simple and gives immediate, visual results.

### For Developers
Try **Example 04 (AutoGen)** - demonstrates AI pair programming.

### For Business Users
Try **Example 07 (OpenAI Assistants)** - practical scheduling automation.

## Common First-Time Issues

### "Module not found"
```bash
# Solution: Install the required package
pip install <package-name>
```

### "API key not found"
```bash
# Solution: Set environment variable
export OPENAI_API_KEY=your-key-here  # Mac/Linux
set OPENAI_API_KEY=your-key-here     # Windows
```

### "Rate limit exceeded"
```bash
# Solution: Add a small delay or check your API quota
# Most examples work fine on free tier with small datasets
```

## Cost Expectations

Approximate costs for testing (as of January 2025):

- **GPT-3.5-turbo**: ~$0.01 per example run
- **GPT-4**: ~$0.10 per example run
- **Free tier**: Usually sufficient for testing all examples

💡 **Tip**: Start with GPT-3.5-turbo to minimize costs while learning.

## Next Steps

1. ✅ Run one example successfully
2. 📖 Read the detailed README.md
3. 🔧 Customize the example for your use case
4. 🚀 Try other frameworks
5. 🤝 Contribute your own examples!

## Getting Help

- 📚 Check the [full README](README.md)
- 🐛 Report issues on [GitHub Issues](https://github.com/yourusername/ai-agents-examples/issues)
- 💬 Ask questions in [Discussions](https://github.com/yourusername/ai-agents-examples/discussions)

## Success Checklist

- [ ] Python 3.10+ installed and working
- [ ] OpenAI API key obtained and set
- [ ] Virtual environment created
- [ ] At least one example running successfully
- [ ] Ready to explore more frameworks!

---

For detailed documentation, see [README.md](README.md)
