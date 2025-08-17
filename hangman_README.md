# 🎮 Hangman Game

A modern Python implementation of the classic Hangman word guessing game with API integration, hints system, and scoring mechanics.

## ✨ Features

- **Word Guessing**: Classic hangman gameplay with letter-by-letter or complete word guessing
- **API Integration**: Fetches additional hints from Wordnik API
- **Scoring System**: Points-based gameplay with bonuses and penalties
- **Multiple Hints**: Local word definitions plus API-powered hints
- **Game Statistics**: Track total points, games played, and average score
- **Portuguese Interface**: User-friendly Portuguese language interface

## 🚀 How to Play

1. **Start the Game**: Run the script to begin
2. **View Hints**: Each word comes with multiple helpful hints
3. **Make Guesses**: 
   - Enter single letters to guess letter-by-letter
   - Enter complete words to guess the entire answer
4. **Scoring**: Earn points based on word length, mistakes, and completion method
5. **Continue Playing**: Play multiple rounds to build your total score

## 🎯 Scoring System

- **Base Points**: Word length × 2
- **Penalty**: -2 points per wrong guess
- **Complete Word Bonus**: +10 points for guessing entire word
- **Perfect Game Bonus**: +5 points for no mistakes
- **Game Over Penalty**: -5 points for losing

## 🛠️ Technologies Used

- **Python 3.x**: Core programming language
- **Requests Library**: API integration for additional hints
- **Wordnik API**: External word definitions and hints

## 📋 Requirements

```bash
pip install requests
```

## 🎮 Usage

```bash
python hangman_game.py
```

## 🔧 Configuration

The game includes:
- 10 predefined Portuguese words
- 6 maximum wrong guesses allowed
- Automatic API hint fetching with fallback to local hints
- Real-time statistics tracking

## 📊 Game Statistics

The game tracks:
- Total points earned
- Number of games played
- Average points per game
- Performance feedback based on average score

## 🌐 API Integration

Uses Wordnik API for enhanced hints:
- Fetches random words for additional context
- Provides English definitions as hints
- Graceful fallback to local hints if API is unavailable

---

*Part of the Daily Coding Projects Portfolio*