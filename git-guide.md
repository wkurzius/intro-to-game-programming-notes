# Brief guide to Git and Github

**Git** is version control software. As you commit changes to your work, Git keeps track of what changes and allows you to revert back to previous versions. There are other features, but we'll be using this for the most part.

**GitHub** is a hosting service for Git repositories (you can think of repositories as projects). We'll be using GitHub as a kind of backup service. A copy of your project will be stored online and can be accessed anywhere. So, it will act as a replacement for your storage folder.

## Getting started

1. Create a repository.

2. Once the Quick Setup page appears, minimize (don't close) GitHub and open your project folder on your computer.

3. Right click in the folder and select 'Git Bash here'.

4. We need to initialize Git for your project, so enter

    ``` bash
    git init
    ```

5. Now, we need to tell Git to keep track of all files in the folder.

    ``` bash
    git add .
    ```

6. Next we need to commit those changes. Git requires a message when you commit. Use it to note what changed, or what you worked on. Since this is the first one, there's not much to say.

    ``` bash
    git commit -m "first commit"
    ```

7. Now we need to link to your repository on GitHub. Head back to the Quick Setup page and copy and paste the line that looks like the one below

    ``` bash
    git remote add origin https://github.com/username/repository-name.git
    ```

8. Last step. This will push your local repository to the remote one.

    ``` bash
    git push -u origin master
    ```

## Downloading your project

For getting your project from GitHub to your machine so you can work on it.

1. Right click on the Desktop and open Git Bash.

2. Download your project with

    ``` bash
    git clone https://github.com/username/repository-name.git
    ```

3. The project folder will appear on your Desktop.

## Committing changes

For the end of the period after you save your work.

1. Open your project folder and Git Bash.

2. Add all new/changed files with

    ``` bash
    git add .
    ```

3. Commit those change and don't forget the message.
    ``` bash
    git commit -m "a meaningful message about what you did that day"
    ```

4. Push to the remote repository

    ``` bash
    git push -u origin master
    ```
