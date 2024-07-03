---
created: 2023-09-07T12:03:00+00:00
categories:
  - notion2markdown
tags:
  - Notion
  - Hexo
  - Blog
  - GitHub
  - Action
updated: 2023-12-25T02:03:00+00:00
date: 2023-09-07T12:04:00+00:00
type: posts
slug: deploy-notion2hexo
title: Deploy Notion2Markdown-Action for Hexo Project Using GitHub Actions
id: bc5625b9-24cb-4265-999c-13ef4e95eb8b
---

In this post, we'll walk you through the process of deploying the Notion2Markdown-Action for your Hexo project using GitHub Actions. This workflow allows you to synchronize content from Notion to your Hexo blog automatically. We'll provide a detailed explanation of how to set up the necessary configurations and secrets for this GitHub Actions workflow.

## Prerequisites

Before you get started, make sure you have the following prerequisites in place:

### Notion Database

For Notion side, you have a prepare **a notion dataset** and **notion integration secret.**

For the former, we provide [a template here](/397943b2d0384e15ba69448900823984?v=06762d5d3e2140e399c03d84131ee682), feel free to duplicate it.

For the notion integration, [here](https://syncwith.com/gs/support/notion-api-key-qrsJHMnH5LuHUjDqvZnmWC#3dfedd0586ec402293add6e511478985) is a guide about how to get the integration secret and connect it to the dataset.

> DO NOT FORGET TO [CONNECT THE DATABASE](https://syncwith.com/gs/support/notion-api-key-qrsJHMnH5LuHUjDqvZnmWC#e4bb58f3025746b481eb65155be04e0e) TO YOUR NOTION INTEGRATION!!!

At this point, `NOTION_SECRET` and `NOTION_DATABASE_ID` should have been obtained.

### A configured image hosting service

If you want to upload all the images hosted by notion, a configured image hosting service shoud be prepared for this action.

Our picture bed service is based on [PicGo-Core](https://github.com/PicGo/PicGo-Core/blob/dev/README.md), so `smms/qiniu/upyun/tcyun/github/aliyun/imgur` are supported to be the backend service.

And a JSON configure file should be prepared as `PIC_BED_CONFIG`, according to the [docs](https://picgo.github.io/PicGo-Core-Doc/zh/guide/config.html#picbed). Here is an example:

```yaml
{
  "uploader": "aliyun",
  "aliyun":
    {
      "accessKeyId": "",
      "accessKeySecret": "",
      "bucket": "",
      "area": "",
      "path": "",
      "customUrl": "",
      "options": "",
    },
}
```

## GitHub Actions Workflow

Let's break down the GitHub Actions workflow step by step.

```yaml
name: Notion2Hexo

on:
  workflow_dispatch:
  schedule:
    - cron: "*/30 * * * *"

permissions:
  contents: write

jobs:
  notionSyncTask:
    name: Notion2hexo on ubuntu-latest
    runs-on: ubuntu-latest

    steps:
      - name: Checkout blog and theme
        uses: actions/checkout@v3
        with:
          submodules: "recursive"
          fetch-depth: 0

      - name: Check the NOTION_SYNC_DATETIME
        id: GetNotionSyncDatetime
        run: |
          NOTION_SYNC_DATETIME=$(git log -n 1 --grep="NotionSync" --format="%aI")
          echo "NOTION_SYNC_DATETIME=$NOTION_SYNC_DATETIME" >> "$GITHUB_OUTPUT"
          echo -e "Latest notion sync datetime:\\\\n$NOTION_SYNC_DATETIME"

      - name: Convert notion to markdown
        id: NotionSync
        uses: Doradx/notion2markdown-action@v1
        with:
          notion_secret: ${{ secrets.NOTION_SECRET }}
          database_id: ${{ secrets.NOTION_DATABASE_ID }}
          pic_migrate: true
          pic_bed_config: ${{ secrets.PICBED_CONFIG }}
          pic_compress: true
          output_page_dir: "source"
          output_post_dir: "source/_posts/notion"
          clean_unpublished_post: true
          metas_keeped: abbrlink
          metas_excluded: pstatus,ptype
          last_sync_datetime: ${{ steps.GetNotionSyncDatetime.outputs.NOTION_SYNC_DATETIME }}
      - name: Hexo deploy
        if: steps.NotionSync.outputs.updated_count != '0'
        run: |
          git pull
          npm install && npm run deploy

      - name: Commit & Push
        if: steps.NotionSync.outputs.updated_count != '0'
        uses: stefanzweifel/git-auto-commit-action@v4
        with:
          file_pattern: "source/"
          commit_message: Automatic NotionSync.
```

## Configuration Details

Now, let's explain each part of the workflow in detail.

1. **Schedule**: The workflow can be triggered manually or on a schedule using the `schedule` option. In this example, it runs every 30 minutes between 7 AM and 10 PM.
2. **Permissions**: This workflow requires write permissions to the repository content to update your Hexo blog.
3. **notionSyncTask**: This is the main job of the workflow.
   - **Checkout blog and theme**: It checks out your Hexo blog repository and its submodules.
   - **Check the NOTION_SYNC_DATETIME**: This step retrieves the latest sync datetime from the Git history for tracking changes.
   - **Convert notion to markdown**: This step uses the Notion2Markdown-Action to sync content from Notion to your Hexo blog. It requires several secrets and configurations:
     - `notion_secret`: Your Notion integration secret. [HOW TO GET IT?](https://syncwith.com/gs/support/notion-api-key-qrsJHMnH5LuHUjDqvZnmWC#3dfedd0586ec402293add6e511478985)
     - `database_id`: The ID of the Notion database you want to sync. [HOW TO GET IT?](https://syncwith.com/gs/support/notion-api-key-qrsJHMnH5LuHUjDqvZnmWC#3dfedd0586ec402293add6e511478985)
     - `pic_migrate`: Set to `true` to migrate images from Notion to your `pic_bed_config`.
     - `pic_bed_config`: Configuration for your image hosting service.
     - `pic_compress`: Set to `true` to compress images.
     - `output_page_dir` and `output_post_dir`: Directories where the converted content will be placed in your Hexo project.
     - `clean_unpublished_post`: Set to `true` to clean unpublished posts.
     - `metas_keeped` and `metas_excluded`: Metadata options.
     - `last_sync_datetime`: The datetime of the last sync, retrieved in the previous step.
   - **Hexo deploy**: This step runs when content has been updated. It pulls changes, installs dependencies, and deploys your Hexo blog.
   - **Commit & Push**: Also runs when content has been updated, it commits and pushes the changes to your repository with a specified commit message.

## Setting Up Secrets

To use this workflow, you need to set up the following secrets in your GitHub repository, with the location `Settings→Secrets and variables→Actions→Secrets→New repository secret`.

- `NOTION_SECRET`: Your Notion integration secret.
- `NOTION_DATABASE_ID`: The ID of the Notion database you want to sync.
- `PICBED_CONFIG`: Configuration for your image hosting service.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9724a895-d6d5-4e82-9739-74885ea5ba68/92e7d463-8e7f-453f-9fc2-70f9ba0a8908/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240425T061049Z&X-Amz-Expires=3600&X-Amz-Signature=8dc9728b4aac61918c52ab303d44db5967ac1875a9a94a4ffaefa71117c17f37&X-Amz-SignedHeaders=host&x-id=GetObject)

## Enjoying!

The workflow is usually triggered according to the schedule, but you can also trigger it manually to see whether it works fine. Tap `Actions→Notion2Hexo→Run workflow` to run it.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9724a895-d6d5-4e82-9739-74885ea5ba68/1b91b54d-01df-4754-af64-d2ab65da9b77/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240425T061049Z&X-Amz-Expires=3600&X-Amz-Signature=6b163cfaa483791c3085cc5fc697fe85fade6483637cb325d3d9e35c1b32f61b&X-Amz-SignedHeaders=host&x-id=GetObject)

## Conclusion

With this GitHub Actions workflow, you can automate the process of syncing content from Notion to your Hexo blog. Ensure that you have all the prerequisites and secrets set up correctly to make this workflow work seamlessly. Once configured, your Hexo blog will stay up-to-date with your Notion content automatically.
