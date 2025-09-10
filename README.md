# PQuizzy

A simple and interactive Python quiz game that tests your knowledge across various topics. Challenge yourself with multiple-choice questions and track your progress!

## 📝 Description

PQuizzy is a lightweight, command-line quiz application built with Python. It offers an engaging way to test your knowledge through customizable quizzes with immediate feedback and scoring. Perfect for students, educators, or anyone looking to learn while having fun!

## ✨ Features

- **Interactive Quiz Interface**: Clean, user-friendly command-line interface
- **Multiple Categories**: Support for various quiz topics and categories
- **Instant Feedback**: Get immediate results after each question
- **Score Tracking**: Keep track of your performance and progress
- **Customizable Questions**: Easy to add new questions and categories
- **Randomized Questions**: Questions are shuffled for a fresh experience each time

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/shoaibswe/PQuizzy.git
   cd PQuizzy
   ```

2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

Run the quiz game:
```bash
python quiz.py
```

Follow the on-screen prompts to:
1. Select a quiz category
2. Answer multiple-choice questions
3. View your final score and performance

## 🎯 Example

```
Welcome to PQuizzy!

Select a category:
1. General Knowledge
2. Science
3. History

Enter your choice (1-3): 1

Question 1/10:
What is the capital of France?
A) London
B) Berlin
C) Paris
D) Madrid

Your answer: C
Correct! ✓

Score: 1/1
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/new-feature`)
3. **Commit** your changes (`git commit -m 'Add some feature'`)
4. **Push** to the branch (`git push origin feature/new-feature`)
5. **Open** a Pull Request

### Adding New Questions
To add new questions, edit the question files in the appropriate category or create new category files following the existing format.

## 📁 Project Structure

```
PQuizzy/
├── quiz.py          # Main quiz application
├── questions/       # Quiz questions by category
├── utils/          # Utility functions
├── README.md       # Project documentation
└── requirements.txt # Python dependencies
```

## 🔧 Customization

- **Add Categories**: Create new question files in the `questions/` directory
- **Modify Scoring**: Adjust scoring logic in the main quiz module
- **Customize Interface**: Modify the display and interaction functions

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Shoaib** - [shoaibswe](https://github.com/shoaibswe)

## 🙏 Acknowledgments

- Thanks to all contributors who help improve PQuizzy
- Inspired by the need for simple, educational quiz applications

---

**Enjoy learning with PQuizzy! 🎉**
