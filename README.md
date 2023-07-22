# Devvit App Upload GitHub Action

The Devvit App Upload GitHub Action is a custom GitHub Action designed to streamline the process of uploading apps to the [Devvit](https://developers.reddit.com/) platform. 


## Inputs
- `refresh_token`: The refresh token associated with your Devvit account. You have to extract the refresh token manually. For Linux, the refresh token is saved in file `~/.devvit/token`. Copy the whole thing and insert it as Github Secret in your repository. 

- `GITHUB_TOKEN`: This is automaticaly created for you provided by GitHub to authenticate and authorize actions within a GitHub Actions workflow. This token is used to updated the `devvit.yaml` after devvit upload.

See the [Using encrypted secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets) for more detail on adding secrets to your repository.

## Usage

To use the Devvit App Upload GitHub Action in your repository, you need to create or update a GitHub Actions workflow file (e.g., .github/workflows/devvit-upload.yml) and add the following content:

```yaml
name: Push to Devvit
on: push

jobs:
  push-to-devvit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          persist-credentials: false

      - name: Devvit Upload Github Action
        uses: isFakeAccount/devvit-upload-github-action@v0.0.1
        with:
            refresh_token: ${{ secrets.REFRESH_TOKEN }}
      
      - name: Commit & Push changes
        uses: actions-js/push@master
        with:
          branch: main
          github_token: ${{ secrets.GITHUB_TOKEN }}
          message: Bumping the app version number

```

In this example, the workflow will be triggered whenever there is a push event in your repository. 