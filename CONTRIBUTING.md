# Contributing to AI Agents Article Examples

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## Code of Conduct

Be respectful, inclusive, and professional in all interactions.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/yourusername/ai-agents-examples/issues)
2. If not, create a new issue with:
   - Clear, descriptive title
   - Steps to reproduce
   - Expected vs actual behavior
   - Python version and dependencies
   - Error messages or logs

### Suggesting Features

1. Check existing feature requests
2. Create an issue describing:
   - The problem you're trying to solve
   - Your proposed solution
   - Alternative solutions considered
   - Examples from other projects

### Submitting Code

1. **Fork the repository**
2. **Create a branch**: `git checkout -b feature/your-feature-name`
3. **Make your changes**:
   - Follow PEP 8 style guidelines
   - Add docstrings and comments
   - Include error handling
   - Update documentation
4. **Test your changes**: Ensure code runs without errors
5. **Commit**: Use clear, descriptive commit messages
6. **Push**: `git push origin feature/your-feature-name`
7. **Submit a Pull Request**

## Code Style

### Python Style Guide

- Follow [PEP 8](https://pep8.org/)
- Use 4 spaces for indentation
- Maximum line length: 88 characters (Black formatter default)
- Use descriptive variable names
- Add type hints where appropriate

### Documentation Style

- Use Google-style docstrings
- Include parameter descriptions
- Provide usage examples
- Explain complex logic with comments

Example:
```python
def process_document(file_path: str, chunk_size: int = 1000) -> list:
    """Process a document and split it into chunks.
    
    Args:
        file_path: Path to the document file
        chunk_size: Size of each chunk in characters
        
    Returns:
        List of document chunks
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If chunk_size is invalid
        
    Example:
        >>> chunks = process_document("doc.txt", chunk_size=500)
        >>> len(chunks)
        10
    """
    pass
```

## Adding New Examples

When adding a new AI agent framework example:

1. **Create a new Python file**: `NN_framework_usecase.py`
2. **Follow the template structure**:
   ```python
   """
   Framework Name - Use Case Title
   ================================
   Brief description of what this example demonstrates.
   
   Requirements:
   - dependency1
   - dependency2
   
   Author: Your Name
   """
   
   # Imports
   # Configuration
   # Main functionality
   # Example usage
   
   if __name__ == "__main__":
       # Instructions for running
       pass
   ```

3. **Update README.md**:
   - Add to table of contents
   - Add detailed section with description
   - Include run instructions

4. **Update requirements.txt**: Add new dependencies

5. **Provide sample data**: If needed, include example files

6. **Test thoroughly**: Run with both GPT-3.5 and GPT-4

## Testing

Before submitting:

```bash
# Run the example
python your_example.py

# Check code style
black your_example.py
flake8 your_example.py

# Type checking (optional)
mypy your_example.py
```

## Pull Request Process

1. Update documentation for any new features
2. Add yourself to contributors list
3. Link related issues in PR description
4. Ensure all checks pass
5. Request review from maintainers

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring

## Testing
How was this tested?

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Examples run successfully
- [ ] No API keys in code
```

## Review Process

1. Maintainers will review within 1-2 weeks
2. Address any requested changes
3. Once approved, PR will be merged

## Questions?

- Open an issue for questions
- Join community discussions
- Reach out to maintainers

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Recognition

Contributors will be acknowledged in:
- README.md contributors section
- GitHub contributors page
- Release notes

Thank you for contributing!
