---
created: 2023-12-25T01:57:00+00:00
categories:
  - notion2markdown
description: 这里是快速使用notion2markdown-action的方法，帮助大家快速部署！
tags:
  - Notion
  - Hexo
  - Blog
  - GitHub
updated: 2023-12-25T02:05:00+00:00
date: 2023-12-25T01:57:00+00:00
type: posts
slug: tutorial-notion2markdown-action
title: notion2markdown-action简要使用教程
cover: https://images.unsplash.com/photo-1471107340929-a87cd0f5b5f3?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb
id: c5ebb4ea-b2c6-4a81-8d3b-f85933075306
---

# 前言

此前开发了[notion2markdown-action](https://github.com/Doradx/notion2markdown-action)插件，可在`GitHub Actions`中将 Notion 中的页面同步导出到博客中，旧教程[在此](https://blog.cuger.cn/p/634642fd/)。

由于近期更新（更新至`v0.7.0`），配置方案已与原教程不大相符，故在此写简约版的最新教程。

该插件已发布与[marketplace](https://github.com/marketplace/actions/notion2markdown-action)，公开供大家使用。

# 功能概述

目前主要特点如下：

- 能从`Notion`中快速导出文章，生成`Markdown`文件，供静态博客使用。

# 工作流

部署成功后，日常工作流大概如下：

- 文章撰写：在 Notion 中，创建草稿进行文章撰写
- 文章发布：在 Notion 中，将文章状态改为<u>[已发布]</u>
- 文章更新：在 Notion 中，直接修改<u>[已发布]</u>的文章即可，定时任务会自动更新
- 文章删除/撤回：在 Notion 中，将文章的<u>[已发布]</u>状态改为任何其它状态

> `GitHub Actions`采用定时任务在后台执行，每**20 分钟**查询`Notion`是否有**页面更新**，所以在`Noiton`上无需进行任何操作，所有已发布的文章会自动同步到博客上。

# 快速开始

> 本教程最后更新于 2023.09.05, 基于`v0.7.3`版本

本方案基于`Notion Integration`读取`Notion`的页面数据，使用 GitHub Actions 进行自动化部署。

## Notion 配置

> 主要是为了获取`NOTION_TOKEN`和`NOTION_DATABASE_ID` 两项关键参数；前者用于`Notion`认证，后者决定同步哪一个数据库。

1.  从[Untitled](https://www.notion.so/397943b2d0384e15ba69448900823984) 复制`Dataset`模板，复制`数据库ID`，作为`NOTION_DATABASE_ID` 保存；简单获取方法：复制数据库页面链接，例如：https://www.notion.so/{username}/{database_id}?v={view_id}，其中database_id部分即为`数据库ID`。
2.  参考`Notion`官方教程[Create an integration (notion.com)](https://developers.notion.com/docs/create-a-notion-integration)，创建**Notion integration**
    应用，并获取**`Secrets`**，保存该数据，会用作`NOTION_TOKEN`。直达链接：[My integrations | Notion Developers](https://www.notion.so/my-integrations)

        ![Secrets存储位置](https://prod-files-secure.s3.us-west-2.amazonaws.com/9724a895-d6d5-4e82-9739-74885ea5ba68/1b1883ea-24ce-4e2e-bcc9-c0d0d6be62a3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240425T061049Z&X-Amz-Expires=3600&X-Amz-Signature=466d17cfb63db04ce1df15abc5555d5d961d5a5a44993ed3187a8868ae8218b1&X-Amz-SignedHeaders=host&x-id=GetObject)

3.  将创建的`Dataset`数据库授权给刚创建的`Integration`应用，如下图：

![在Notion给Integration应用授权](https://prod-files-secure.s3.us-west-2.amazonaws.com/9724a895-d6d5-4e82-9739-74885ea5ba68/6d2f3047-beae-41a2-984e-be64b9ddc508/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240425T061049Z&X-Amz-Expires=3600&X-Amz-Signature=320fefc50c9b67f4e4f0e22b4f498231a7ac0c7758d1023c421fb150cc770a73&X-Amz-SignedHeaders=host&x-id=GetObject)

就此，Notion 授权部分配置完成，得到`NOTION_TOKEN`和`NOTION_DATABASE_ID` 两项关键参数。

## GitHub Actions 配置

下面开展 GitHub Action 配置，分为两个部分：

- `Workflow`配置：配置`Actions`的工作逻辑，复制粘贴后，根据需要修改
- `Action Secrets`配置：配置`Actions`的各类参数，例如`Notion`和`picgo`图床参数

### Workflows 配置

这里介绍 notion2markdown-action 的 workflow，用于将 Notion 页面同步到 GitHub。

1. 切换到自己在`GitHub`上托管的仓库目录，`Actions→New workflow→set up a workflow yourself`，在`.github/workflows`目录下，创建`notion_sync.yml`配置文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9724a895-d6d5-4e82-9739-74885ea5ba68/b48514df-cd08-4734-b3bc-0fbb9220f659/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240425T061049Z&X-Amz-Expires=3600&X-Amz-Signature=83f367604951b1fb79cd79e8bd99e171cc4044e106d0226a2455ed587fba54f5&X-Amz-SignedHeaders=host&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9724a895-d6d5-4e82-9739-74885ea5ba68/3d83d3ac-75f2-4a52-b72e-1de3dce56cf5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240425T061049Z&X-Amz-Expires=3600&X-Amz-Signature=f87b8ca35f850119ff7b6eac232125f837c1f3c1b337cd8bf4824fda79309389&X-Amz-SignedHeaders=host&x-id=GetObject)

1. 根据需要，复制下面的配置文档，粘贴到`notion_sync.yml`，并保存。此配置文件为基础版，不包含图床、图片压缩和博客部署等功能。

```yaml
name: Notion Sync

on:
  workflow_dispatch:
  schedule:
   - cron: '*/20 1-17/1 * * *'
  repository_dispatch:
    types:
      - notion_sync

concurrency:
  group: notion-sync-${{ github.ref }}

permissions:
  contents: write

jobs:
  notionSyncTask:
    name: ${{ matrix.os }}
    runs-on: ubuntu-latest
    strategy:
      matrix:
        os: [ubuntu-latest]
    outputs:
      HAS_CHANGES: ${{ steps.NotionSync.outputs.updated_count != '0' }}
    steps:
      - name: Checkout blog and theme
        uses: actions/checkout@v3
        with:
          submodules: 'recursive'
          fetch-depth: 0
      - name: Check the NOTION_SYNC_DATETIME
        id: GetNotionSyncDatetime
        run: |
          echo -e "Latest commit id: $(git rev-parse HEAD)"
          echo -e "Latest notion sync commit:\n$(git log -n 1 --grep="NotionSync")"
          NOTION_SYNC_DATETIME=$(git log -n 1 --grep="NotionSync" --format="%aI")
          echo "NOTION_SYNC_DATETIME: $NOTION_SYNC_DATETIME"
          echo "NOTION_SYNC_DATETIME=$NOTION_SYNC_DATETIME" >> "$GITHUB_OUTPUT"
      - name: Convert notion to markdown
        id: NotionSync
        uses: Doradx/notion2markdown-action@latest
        with:
					last_sync_datetime: ${{ steps.GetNotionSyncDatetime.outputs.NOTION_SYNC_DATETIME }}
          notion_secret: ${{ secrets.NOTION_TOKEN }}
          database_id: ${{ secrets.NOTION_DATABASE_ID }}
					page_output_dir: 'source'
          post_output_dir: 'source/_posts/notion'
					keys_to_keep: ${{ secrets.KEYS_TO_KEEP}}
          clean_unpublished_post: true

      - name: Sync git
        if: steps.NotionSync.outputs.updated_count != '0'
        run: |
          git pull
      - name: Commit & Push
        if: steps.NotionSync.outputs.updated_count != '0'
        uses: stefanzweifel/git-auto-commit-action@v4
        with:
          file_pattern: 'source/'
          commit_message: Automatic NotionSync.
```
