#!/usr/bin/env python3
"""
Unit Tests for PQuizzy Quiz Application
Run with: python tests.py
"""

import unittest
from unittest.mock import patch
from io import StringIO
import sys

from main import Question, Quiz, create_default_questions


class TestQuestion(unittest.TestCase):
    """Test Question class functionality."""
    
    def test_question_creation(self):
        """Test creating a valid question."""
        question = Question(
            text="What is 2 + 2?",
            options={"A": "3", "B": "4", "C": "5", "D": "6"},
            correct_answer="B"
        )
        self.assertEqual(question.text, "What is 2 + 2?")
        self.assertEqual(question.correct_answer, "B")
    
    def test_invalid_answer_error(self):
        """Test error when correct answer not in options."""
        with self.assertRaises(ValueError):
            Question("Test?", {"A": "1", "B": "2", "C": "3", "D": "4"}, "E")


class TestQuiz(unittest.TestCase):
    """Test Quiz class functionality."""
    
    def setUp(self):
        """Set up test questions."""
        self.questions = [
            Question("1+1?", {"A": "1", "B": "2", "C": "3", "D": "4"}, "B"),
            Question("2+2?", {"A": "3", "B": "4", "C": "5", "D": "6"}, "B")
        ]
    
    def test_quiz_initialization(self):
        """Test quiz creates correctly."""
        quiz = Quiz(self.questions)
        self.assertEqual(len(quiz.questions), 2)
        self.assertEqual(quiz.score, 0)
    
    def test_empty_quiz_error(self):
        """Test error with no questions."""
        with self.assertRaises(ValueError):
            Quiz([])
    
    @patch('builtins.input', return_value="A")
    def test_get_valid_answer(self, mock_input):
        """Test getting valid user input."""
        quiz = Quiz(self.questions)
        answer = quiz.get_answer()
        self.assertEqual(answer, "A")
    
    @patch('builtins.input', side_effect=["X", "invalid", "A"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_input_retry(self, mock_stdout, mock_input):
        """Test retry behavior for invalid inputs."""
        quiz = Quiz(self.questions)
        answer = quiz.get_answer()
        
        self.assertEqual(answer, "A")
        output = mock_stdout.getvalue()
        self.assertIn("Please enter A, B, C, or D", output)
    
    @patch('builtins.input', return_value="B")
    @patch('sys.stdout', new_callable=StringIO)
    def test_correct_answer(self, mock_stdout, mock_input):
        """Test asking question with correct answer."""
        quiz = Quiz(self.questions)
        result = quiz.ask_question(self.questions[0], 1)
        
        self.assertTrue(result)
        self.assertIn("Correct", mock_stdout.getvalue())
    
    @patch('builtins.input', return_value="A")
    @patch('sys.stdout', new_callable=StringIO)
    def test_wrong_answer_no_retry(self, mock_stdout, mock_input):
        """Test wrong answer moves on (no retry)."""
        quiz = Quiz(self.questions)
        result = quiz.ask_question(self.questions[0], 1)
        
        self.assertFalse(result)
        output = mock_stdout.getvalue()
        self.assertIn("Wrong", output)
        self.assertIn("Correct answer: B", output)
    
    @patch('builtins.input', side_effect=["B", "B"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_full_quiz_run(self, mock_stdout, mock_input):
        """Test complete quiz execution."""
        quiz = Quiz(self.questions)
        quiz.run()
        
        self.assertEqual(quiz.score, 2)
        output = mock_stdout.getvalue()
        self.assertIn("Welcome to PQuizzy", output)
        self.assertIn("QUIZ COMPLETED", output)
        self.assertIn("2/2 (100%)", output)


class TestDefaultQuestions(unittest.TestCase):
    """Test default question set."""
    
    def test_default_questions_count(self):
        """Test default questions are created correctly."""
        questions = create_default_questions()
        self.assertEqual(len(questions), 4)
        self.assertIsInstance(questions[0], Question)
    
    def test_specific_questions(self):
        """Test specific default questions."""
        questions = create_default_questions()
        
        # Test France question
        france_q = questions[0]
        self.assertIn("France", france_q.text)
        self.assertEqual(france_q.correct_answer, "C")
        
        # Test math question
        math_q = questions[1]
        self.assertIn("2 + 2", math_q.text)
        self.assertEqual(math_q.correct_answer, "B")


class TestIntegration(unittest.TestCase):
    """Integration tests for complete workflows."""
    
    @patch('builtins.input', side_effect=["C", "B", "B", "B"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_perfect_score_flow(self, mock_stdout, mock_input):
        """Test complete quiz with perfect score."""
        questions = create_default_questions()
        quiz = Quiz(questions)
        quiz.run()
        
        self.assertEqual(quiz.score, 4)
        output = mock_stdout.getvalue()
        self.assertIn("4/4 (100%)", output)
        self.assertIn("Excellent", mock_stdout.getvalue())
    
    @patch('builtins.input', side_effect=["A", "A", "A", "A"])
    @patch('sys.stdout', new_callable=StringIO)  
    def test_all_wrong_answers(self, mock_stdout, mock_input):
        """Test quiz with all wrong answers."""
        questions = create_default_questions()
        quiz = Quiz(questions)
        quiz.run()
        
        self.assertEqual(quiz.score, 0)
        output = mock_stdout.getvalue()
        self.assertIn("0/4 (0%)", output)
        self.assertIn("Keep practicing", mock_stdout.getvalue())
    
    @patch('builtins.input', side_effect=["invalid", "X", "C", "B", "B", "B"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_mixed_invalid_and_valid_inputs(self, mock_stdout, mock_input):
        """Test mix of invalid inputs and valid answers."""
        questions = create_default_questions()
        quiz = Quiz(questions)
        quiz.run()
        
        output = mock_stdout.getvalue()
        # Should retry invalid inputs
        self.assertIn("Please enter A, B, C, or D", output)
        # Should complete quiz
        self.assertIn("QUIZ COMPLETED", output)
        # Should get perfect score after retries
        self.assertEqual(quiz.score, 4)


class TestMainFunction(unittest.TestCase):
    """Test main application entry point."""
    
    @patch('builtins.input', side_effect=["C", "B", "B", "B"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_execution(self, mock_stdout, mock_input):
        """Test main function runs successfully."""
        from main import main
        main()
        
        output = mock_stdout.getvalue()
        self.assertIn("Welcome to PQuizzy", output)
        self.assertIn("QUIZ COMPLETED", output)
    
    @patch('builtins.input', side_effect=KeyboardInterrupt())
    @patch('sys.stdout', new_callable=StringIO)
    def test_keyboard_interrupt(self, mock_stdout, mock_input):
        """Test graceful handling of user interruption."""
        from main import main
        main()
        
        output = mock_stdout.getvalue()
        self.assertIn("interrupted", output)


def run_tests():
    """Run all tests with clean output."""
    print("🧪 Running PQuizzy Tests")
    print("=" * 40)
    
    # Run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Summary
    print("\n" + "=" * 40)
    if result.wasSuccessful():
        print("✅ All tests passed!")
    else:
        print(f"❌ {len(result.failures)} failures, {len(result.errors)} errors")
    
    print(f"📊 {result.testsRun} tests completed")
    return result.wasSuccessful()


if __name__ == "__main__":
    run_tests()


class TestDefaultQuestions(unittest.TestCase):
    """Test cases for default questions."""
    
    def test_create_default_questions(self):
        """Test creating default questions."""
        questions = create_default_questions()
        
        self.assertEqual(len(questions), 4)
        self.assertIsInstance(questions[0], Question)
        
        # Check specific questions
        france_question = questions[0]
        self.assertIn("France", france_question.text)
        self.assertEqual(france_question.correct_answer, "C")
        
        math_question = questions[1]
        self.assertIn("2 + 2", math_question.text)
        self.assertEqual(math_question.correct_answer, "B")


class TestIntegration(unittest.TestCase):
    """Integration tests for the complete quiz application."""
    
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_complete_quiz_flow_perfect_score(self, mock_stdout, mock_input):
        """Test complete quiz flow with perfect score."""
        # All correct answers for default questions
        mock_input.side_effect = ["C", "B", "B", "B"]
        
        questions = create_default_questions()
        quiz = Quiz(questions)
        quiz.run()
        
        self.assertEqual(quiz.score, 4)
        output = mock_stdout.getvalue()
        self.assertIn("Welcome to PQuizzy", output)
        self.assertIn("4/4 (100.0%)", output)
        self.assertIn("Excellent", output)
    
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_input_retry_behavior(self, mock_stdout, mock_input):
        """Test that invalid inputs cause retries but wrong answers don't."""
        # Invalid inputs followed by wrong answer (should not retry after wrong answer)
        mock_input.side_effect = ["hello", "E", "123", "", "A"]  # Invalid inputs then valid wrong answer
        
        result = self.quiz.ask_question(self.questions[0], 1)  # Correct answer is B, giving A
        
        self.assertFalse(result)  # Wrong answer should return False
        output = mock_stdout.getvalue()
        
        # Should see retry messages for invalid inputs
        self.assertEqual(output.count("Please enter A, B, C, or D"), 4)
        # Should see wrong answer message
        self.assertIn("Wrong! Correct answer: B", output)
        # Should NOT retry after wrong answer
        self.assertEqual(mock_input.call_count, 5)  # Exactly 5 calls, no more

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_complete_quiz_flow_with_wrong_answers(self, mock_stdout, mock_input):
        """Test complete quiz flow with some wrong answers (no retries)."""
        # Mix of wrong and correct answers - no retries for wrong answers
        mock_input.side_effect = [
            "A",  # Question 1: wrong (correct is C)
            "B",  # Question 2: correct
            "A",  # Question 3: wrong (correct is B)  
            "B"   # Question 4: correct
        ]
        
        questions = create_default_questions()
        quiz = Quiz(questions)
        quiz.run()
        
        self.assertEqual(quiz.score, 2)  # 2 correct out of 4
        output = mock_stdout.getvalue()
        # Should see "Wrong!" messages but no retries
        self.assertIn("Wrong!", output)
        self.assertIn("2/4 (50.0%)", output)
        # Should NOT contain retry messages since wrong answers don't retry
        self.assertNotIn("Try again", output)


class TestMainFunction(unittest.TestCase):
    """Test cases for the main function."""
    
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_function_normal_execution(self, mock_stdout, mock_input):
        """Test main function with normal execution (mix of right and wrong answers)."""
        mock_input.side_effect = ["A", "B", "B", "B"]  # Wrong first, correct rest
        
        from main import main
        main()
        
        output = mock_stdout.getvalue()
        self.assertIn("Welcome to PQuizzy", output)
        self.assertIn("QUIZ COMPLETED", output)
        self.assertIn("3/4", output)  # 3 correct out of 4
    
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_function_keyboard_interrupt(self, mock_stdout, mock_input):
        """Test main function with keyboard interrupt."""
        mock_input.side_effect = KeyboardInterrupt()
        
        from main import main
        main()
        
        output = mock_stdout.getvalue()
        self.assertIn("Quiz interrupted", output)
    
    @patch('main.create_default_questions')
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_function_exception_handling(self, mock_stdout, mock_create_questions):
        """Test main function with exception."""
        mock_create_questions.side_effect = Exception("Test error")
        
        from main import main
        main()
        
        output = mock_stdout.getvalue()
        self.assertIn("Error: Test error", output)


if __name__ == "__main__":
    # Run tests with detailed output
    print("🧪 Running PQuizzy Tests...")
    print("=" * 50)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 50)
    if result.wasSuccessful():
        print("✅ All tests passed!")
    else:
        print(f"❌ {len(result.failures)} test(s) failed, {len(result.errors)} error(s)")
        
    print(f"📊 Ran {result.testsRun} tests total")
    print("=" * 50)