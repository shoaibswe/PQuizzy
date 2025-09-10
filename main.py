#!/usr/bin/env python3
"""
PQuizzy -  Quiz Application

A clean, minimal, and well-structured quiz game.
Author: Shoaib Rahman
"""

from typing import Dict, List


class Question:
    """Represents a quiz question."""
    
    def __init__(self, text: str, options: Dict[str, str], correct_answer: str):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer.upper()
        
        if self.correct_answer not in options:
            raise ValueError(f"Correct answer '{correct_answer}' not in options")


class Quiz:
    """Main quiz class handling game logic."""
    
    def __init__(self, questions: List[Question]):
        if not questions:
            raise ValueError("Quiz must have at least one question")
        self.questions = questions
        self.score = 0
    
    def display_question(self, question: Question, number: int) -> None:
        """Display formatted question."""
        print(f"\n{'='*40}")
        print(f"Question {number}: {question.text}")
        print(f"{'='*40}")
        for key, value in question.options.items():
            print(f"{key}. {value}")
        print()
    
    def get_answer(self) -> str:
        """Get validated user input."""
        while True:
            answer = input("Your answer (A/B/C/D): ").upper().strip()
            if answer in ['A', 'B', 'C', 'D']:
                return answer
            print("⚠️  Please enter A, B, C, or D")
    
    def ask_question(self, question: Question, number: int) -> bool:
        """Ask question once and move on."""
        self.display_question(question, number)
        answer = self.get_answer()
        
        if answer == question.correct_answer:
            print("✅ Correct!")
            return True
        else:
            print(f"❌ Wrong! Correct answer: {question.correct_answer}")
            return False
    
    def display_results(self) -> None:
        """Display final results."""
        total = len(self.questions)
        percentage = (self.score / total) * 100
        
        print(f"\n{'='*40}")
        print("🏆 QUIZ COMPLETED!")
        print(f"{'='*40}")
        print(f"Score: {self.score}/{total} ({percentage:.0f}%)")

        if percentage >= 80:
            print("🎉 Excellent!")
        elif percentage >= 70:
            print("👍 Good job!")
        else:
            print("📚 Keep practicing!")
        print(f"{'='*40}")
    
    def run(self) -> None:
        """Run the complete quiz."""
        print("🎯 Welcome to PQuizzy!")
        print("Answer each question once and move to the next.\n")
        
        for i, question in enumerate(self.questions, 1):
            if self.ask_question(question, i):
                self.score += 1
        
        self.display_results()


def create_default_questions() -> List[Question]:
    """Create default quiz questions."""
    return [
        Question(
            "What is the capital of France?",
            {"A": "London", "B": "Berlin", "C": "Paris", "D": "Madrid"},
            "C"
        ),
        Question(
            "What is 2 + 2?",
            {"A": "3", "B": "4", "C": "5", "D": "6"},
            "B"
        ),
        Question(
            "What is the capital of Japan?",
            {"A": "Beijing", "B": "Tokyo", "C": "Seoul", "D": "Bangkok"},
            "B"
        ),
        Question(
            "What is the largest planet in our solar system?",
            {"A": "Earth", "B": "Jupiter", "C": "Saturn", "D": "Mars"},
            "B"
        )
    ]


def main():
    """Main entry point."""
    try:
        questions = create_default_questions()
        quiz = Quiz(questions)
        quiz.run()
    except KeyboardInterrupt:
        print("\n👋 Quiz interrupted. Goodbye!")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
