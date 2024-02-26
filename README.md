# Web-Project

## Teams:
2024'spring
* Main/F1: Samadhi
* F2: Sora, Shun, John
* F3:Reeti, Rinko
* Back: Nour, Nghi

2023'fall
* Main/F1: Samadhi, Jalen, Diprekshya, Stevie 
* F2: Sora, Shun, John, Ryan
* F3: Nour, Reeti, Rinko, Karol
* Back: Cayden, Chadha

## HTML boilerplate:
Explaination for the boilerplate: [link](https://www.freecodecamp.org/news/basic-html5-template-boilerplate-code-example/)

## Image for example floor code:
[Dowload and save it in the folder you save your code file in](https://imgur.com/ZYsNEia)

## Git Commands

### Pushing Your Changes to Git

When you worked on some part of the project, say you edited <code>floor_2.html</code> and you want your team member to be able to access it, you can push your code and make it accessible to everyone. Here is a step-by-step guide for that:

#### Initial Set-up

Only one member of your group needs to do this:

1. While in the <code>Web-Project</code> repository from the terminal, run <code>git branch <branch_name></code> (in this example, <code>git branch floor2_group</code>).

   This creats a new branch in the repository for your group that makes things easier to navigate.

2. Then run <code>git checkout <branch_name></code> (the name of the branch you just created).

   This takes you to the branch you just created.

#### After Initial Set-up/ If you already have a branch:

1. Run <code>git branch -av</code> which would list all the remote branches that has been created. Find the name of the branch for your group and run <code>git checkout <branch_name></code> to go to your group's branch.
2. Navigate to the directory where the file you want to push is in. In this case, <code>floor_2.html</code> is in the folder/directory <code>floor2</code> in <code>Web-Project</code> and let's say you are currently in the main directory, <code>Web-Project</code>, you woud use the <code>cd</code> command to navigate to <code>floor2</code>. You use the command <code>cd floor2</code>, which leads you to the desired directory.
Note: use <code>cd ..</code> to go back a directory.

3. Now, you use the command `git add` and the name of the file/files (with spaces between multiple file names) to add the file you edited.  For example:
    
  ```ruby
  C:\Users\parsa\OneDrive\Desktop\GDSC\Web-Project\floor2> git add floor2.html
  ```
    
4. Then use <code>git commit -m “SOME COMMENT”</code> writing a comment on what you did with the file you are pushing in the “some comments” portion (remember the quotes). 
5. Finally, run the command <code>git push</code> to push the changes.

   NOTE: If this gives you an error, and says you need to <code>git pull</code> first, it means your group made some edits to your folder and pushed it before you. To be up-to-date with the changes, run         <code>git pull</code> before running the final <code>git push</code>  

Now, your friend or anyone else who cloned Web-Project can pull your changes using the command <code>git pull</code> after running <code>git checkout <name_of_your_branch></code>.

### Follow this [link](https://www.atlassian.com/git/glossary#commands) to learn about other necessary git commands you will be using

## VScode Extensions 

Here is a list of vscode extensions which would help you code for our project:

1. Live Server (which you already installed in a previous session)
2. CSS Peek
3. Auto Close Tag
4. Prettier - Code formatter
5. Auto Rename Tag
6. Path Intellisense

Click [here](https://blog.bitsrc.io/top-10-visual-studio-code-extensions-for-web-developers-5bd6a76bdf5f) to see the description of the extensions and [here](https://code.visualstudio.com/docs/editor/extension-marketplace#:~:text=Browse%20for%20extensions,-You%20can%20browse&text=Bring%20up%20the%20Extensions%20view,on%20the%20VS%20Code%20Marketplace.) to see how to get an extension if you forgot how to!

## Floor plan maker: [link](https://floorplancreator.net/)
