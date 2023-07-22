# Devvit App Upload GitHub Action

The Devvit App Upload GitHub Action is a custom GitHub Action designed to streamline the process of uploading apps to the [Devvit](https://developers.reddit.com/) platform. 


## Inputs
- `refresh_token`: The refresh token associated with your Devvit account. You have to extract the refresh token manually. For Linux, the refresh token is saved in file `~/.devvit/token`. Copy the whole thing and insert it as Github Secret in your repository. 

[Using encrypted secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets)

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
      - name: Devvit Upload Github Action
        uses: neobrains/space-deployment-github-action@v0.5
        with:
            refresh_token: ${{ secrets.REFRESH_TOKEN }}
```

In this example, the workflow will be triggered whenever there is a push event in your repository. 