# Quiz Game

## Description
The Quiz Game is a console-based interactive program where players answer multiple-choice questions to test their knowledge. This project is designed for beginners to practice programming concepts while creating a fun and engaging game.

---

## How to Run the Project

### Prerequisites
To run the Quiz Game, ensure the following:
- Python 3.x is installed on your system.
- You have access to a terminal or command-line interface.

### Steps to Run
1. **Clone the Repository**  
   Use the following commands to clone the repository and navigate to the project folder:
   ```bash
   git clone <repository-url>
   cd quiz-game-{your-name}-{your-td-number}
   ```

2. **Run the Game**  
   Execute the game using Python:
   ```bash
   python quiz_game/main.py
   ```

3. **Follow the Instructions**
   - The game will display multiple-choice questions.
   - Enter the corresponding option number (e.g., `1` for the first option) to answer.
   - After each question, the game will notify you if your answer was correct or incorrect.
   - At the end, your total score will be displayed.

---

## Guide on How to Contribute

We welcome contributions to enhance the Quiz Game! Follow the steps below to get started:

### Steps to Contribute:
1. **Fork the Repository**  
   - Click the "Fork" button on the repository page to fork this repository to your GitHub account.

2. **Clone the Forked Repository**  
   Clone the repository to your local machine:
   ```bash
   git clone <your-forked-repository-url>
   cd quiz-game-{your-name}-{your-td-number}
   ```

3. **Create a New Branch**  
   Always create a branch before making changes:
   ```bash
   git checkout -b <branch-name>
   ```

4. **Make Your Changes**  
   - Implement the desired changes or fix any issues.
   - Test your changes thoroughly to ensure functionality.

5. **Commit Your Changes**  
   Use clear and descriptive commit messages:
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```

6. **Push Your Changes**  
   Push the branch to your forked repository:
   ```bash
   git push origin <branch-name>
   ```

7. **Submit a Pull Request**  
   - Go to the original repository on GitHub.
   - Click on **Pull Requests** > **New Pull Request**.
   - Write a detailed description of the changes and submit your pull request.

---

## How to Connect a Branch to an Issue

If you’ve created an issue and want to connect it to your branch, here’s how you can do it:

### Method 1: Reference in Commit Message
1. Switch to your branch:
   ```bash
   git checkout <your-branch-name>
   ```

2. Commit your changes and reference the issue number in the commit message:
   ```bash
   git commit -m "Fixes #<issue-number> - Description of the fix"
   ```

3. Push your changes:
   ```bash
   git push origin <your-branch-name>
   ```

This automatically links the branch to the issue. When the pull request is merged, the issue will be closed.

---

### Method 2: Mention in Pull Request
When creating a pull request:
1. In the pull request description, mention the issue:
   ```markdown
   Fixes #<issue-number>
   ```
2. Submit the pull request. The branch will now be linked to the issue.

---

### Method 3: Manually Link via GitHub Interface
1. Open the issue on GitHub.
2. Scroll to the **Development** section.
3. Click **Link a pull request or branch**.
4. Select your branch from the list to connect it to the issue.

---

## License
This project is licensed under the [MIT License](LICENSE).
