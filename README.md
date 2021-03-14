# ssciwr_sdc_team14
A repository for the course: [sustainable software development](https://github.com/ssciwr/sustainable_development_course) (team 14)

## Useful commands for working wit git
Create Repository:
1. cloning existing
    git clone <somue-URL>
1. initialising a local directory as git repo
    git init
    
Get newest stuff from remote
    git pull
    
Show local status of repository
    git status
    
Display local differences compared to last pull
    git diff
    then exit with 'q'

### Branches
Create branch
    git branch <some-branch-name>
Change to some branch for working on it
    git checkout <some-branch-name>
Push branch to remote
    git push -u origin <some-branch-name>
List local branches (those marked with * are checked out)
    git branch 
List remote branches
    git branch -r
Delete local branch
    git branch -d <some-branch-name>
Delete remote branch
    git push origin -delete <some-branch-name>
    
Move changes to another branch: https://stackoverflow.com/questions/7217894/moving-changed-files-to-another-branch-for-check-in
    
### Stage, commit and push
After changes are done add to staging
    git add <some-file-path>
Commit the staged change
    git commit -m 'a short meaningful message'
Push to remote
    git push