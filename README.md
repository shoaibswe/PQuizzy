# PQuizzy

A clean, Python quiz application with object-oriented design. Test your knowledge across various topics with an intuitive command-line interface!

## 📝 Description

PQuizzy is a lightweight, well-structured quiz application built with modern Python practices. Features clean object-oriented code, comprehensive error handling, and professional development practices. Perfect for learning Python OOP concepts while having fun with quizzes!

## ✨ Features

- **Clean Object-Oriented Design**: Professional code structure with Question and Quiz classes
- **Smart Input Validation**: Retries invalid inputs (E, hello, 1) but moves on for wrong answers (A when C is correct)
- **Instant Feedback**: Immediate results with clear correct answer display
- **Professional Error Handling**: Graceful handling of interrupts and edge cases
- **Type Hints & Docstrings**: Modern Python practices with full documentation
- **Comprehensive Testing**: 16 unit tests covering all functionality
- **Easy to Extend**: Simple to add new questions or modify behavior

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/shoaibswe/PQuizzy.git
   cd PQuizzy
   ```

2. Create virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies (optional):
   ```bash
   pip install -r requirements.txt        # Main dependencies (none currently)
   pip install -r requirements-dev.txt    # Development dependencies
   ```

## 💻 Usage

### Run the Quiz
```bash
python main.py
```

### Example Session
```
🎯 Welcome to PQuizzy!
Answer each question once and move to the next.


========================================
Question 1: What is the capital of France?
Category: Geography
========================================
A. London
B. Berlin
C. Paris
D. Madrid

Your answer (A/B/C/D): A
❌ Wrong! Correct answer: C

========================================
Question 2: What is 2 + 2?
Category: Mathematics
========================================
A. 3
B. 4
C. 5
D. 6

Your answer (A/B/C/D): B
✅ Correct!

========================================
🏆 QUIZ COMPLETED!
========================================
Score: 1/2 (50%)
📚 Keep practicing!
========================================
```

### Run Tests
```bash
python tests.py
```

## 🧪 Testing

The application includes comprehensive unit tests:

- **16 test cases** covering all functionality
- **100% core feature coverage** 
- **Professional test structure** with mocking
- **Easy to run and understand**

```bash
# Run all tests
python tests.py

# Expected output:
🧪 Running PQuizzy Tests
========================================
...
✅ All tests passed!
📊 16 tests completed
```

## 🏗️ Architecture

### Code Structure
```
PQuizzy/
├── main.py             # Main application with Question & Quiz classes
├── tests.py            # Comprehensive unit tests (16 tests)
├── requirements.txt    # Production dependencies
├── requirements-dev.txt # Development dependencies
├── README.md          # Project documentation
└── venv/              # Virtual environment
```

### Key Classes
- **`Question`**: Represents a quiz question with validation
- **`Quiz`**: Main quiz logic with smart input handling
- **`QuizBuilder`**: Helper for creating default questions

### Design Principles
- **Single Responsibility**: Each class has one clear purpose
- **Error Handling**: Graceful handling of all edge cases
- **Type Safety**: Full type hints for better code quality
- **Testing**: Comprehensive test coverage for reliability

## 🎯 Key Behaviors

### Input Validation
- **Invalid inputs** (`E`, `hello`, `123`) → Retry until valid (A, B, C, D)
- **Wrong but valid answers** (`A` when correct is `C`) → Show correct answer, move to next question
- **Correct answers** → Celebrate and continue

### Scoring System
- **80%+ → "Excellent!"** 🎉
- **70-79% → "Good job!"** 👍  
- **50-69% → "Not bad, keep studying!"** 📚
- **<50% → "Keep practicing!"** 💪

## 🔧 Customization

### Adding New Questions
```python
new_question = Question(
    text="Your question here?",
    options={
        "A": "Option 1",
        "B": "Option 2", 
        "C": "Option 3",
        "D": "Option 4"
    },
    correct_answer="B",  # Must be A, B, C, or D
    category="Your Category"
)
```

### Creating Custom Quiz
```python
from main import Quiz, Question

questions = [new_question, another_question]
quiz = Quiz(questions)
quiz.run()
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/new-feature`)
3. **Make** your changes with tests
4. **Run** tests to ensure everything works (`python tests.py`)
5. **Commit** your changes (`git commit -m 'Add feature: description'`)
6. **Push** to the branch (`git push origin feature/new-feature`)
7. **Open** a Pull Request

### Development Guidelines
- Write tests for new features
- Follow existing code style
- Add type hints and docstrings
- Keep methods small and focused

## 🧰 Development Tools

Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

Available tools:
- **pytest**: Run tests with detailed output
- **black**: Code formatting
- **flake8**: Code linting  
- **mypy**: Type checking

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Shoaib Rahman** - [shoaibswe](https://github.com/shoaibswe)

## 🙏 Acknowledgments

- Built with modern Python best practices
- Inspired by the need for clean, educational code examples
- Thanks to the Python community for excellent testing tools

---

**Learn Python OOP concepts while having fun with quizzes! 🎉**
