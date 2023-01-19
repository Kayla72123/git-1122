# Chapter 4 Git and GitHub
This assignment will guide you through using git and GitHub. You will clone and modify an incomplete implementation of rock paper scissors, performing git operations where necessary.

For the following code snippets, Dollar signs (`$`) indicate shell commands. For example
```txt
$ python3 foo.py
Hello, World!
$ git push
```

## 1 Downloading Code
1. Clone the code
```txt
$ git clone https://GitHub.com/jepst/git-1122.git
```
2. Run the code. Type "Q" or "q" to stop execution.
```txt
$ cd git-1122
$ python3 rps.py
Please enter your choice:
```
3. Explore the git history
```txt
$ git log
```

## 2 Fixing the Bug
By running the code and playing the game, you should have realised that there is a scoring bug that does not grant points to the computer player. Your job is to fix it. 
1. Browse the function `computer_won()` on line 16.
2. Ensure that the computer is awarded a point if it wins; change the "0" to a "1".
3. Run the code and ensure it works.
4. Stage the changes
```txt
$ git add rps.py
```
5. Commit the changes. Make sure to add a good commit message.
**Remember:** Be concise. Computer scientists enjoy brevity.
```txt
$ git commit -m "<your message>"
```

## 3 Adding a New feature
You will add a new feature to the program: a goodbye message. Once the user enters "Q" or "q", the final score should be displayed along with a goodbye message. You will add this feature on a new branch.
### 3.1 Branching
1. Create a new branch named "dev"
```txt
$ git branch dev
```
2. Switch to the new branch
```txt
$ git switch dev
```
### 3.2 Adding the Feature
1. Modify the if-block on line 36 by adding the goodbye message before the `break`:
```py
print(f"Final score is {user_score}-{computer_score}")
```
2. Stage and commit your changes

## 4 Merging New Changes
Finally, you will merge your changes to the `dev` branch by merging it into the `main` branch.
1. Switch to the main branch
```txt
$ git switch main
```
2. Merge branch `dev` with branch `main`
```txt
$ git merge dev
```
3. Optionally, delete the `dev` branch
```txt
$ git branch -d dev
```

## 5 *Optional* More GitHub
If you desire, you can host this repository on GitHub.
1. Make a private repository on GitHub
2. Connect remote
```txt
$ git remote add origin <https URL>
```
3. Push upstream
```txt
$ git push -u origin main
```
