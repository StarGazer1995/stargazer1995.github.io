---
created: 2023-12-25T01:57:00+00:00
categories:
  - notion2markdown
description: 封面描述
updated: 2023-12-25T02:05:00+00:00
date: 2023-12-25T01:57:00+00:00
type: posts
title: notion2markdown-action介绍
id: b3df50d1-ea45-4515-a320-3d737dd16b89
---

此前开发了[notion2markdown-action](https://github.com/Doradx/notion2markdown-action)插件，可在`GitHub Actions`中将 Notion 中的页面同步导出到博客中，旧教程[在此](https://blog.cuger.cn/p/634642fd/)。

# 功能

如名称所言，在`GitHub Actions`中调用此插件，能将 Notion 中的页面同步到`GitHub`仓库中，一般用于静态博客发布。

包含特性：

- `Notion`转`Markdown`功能完备：在[notion-to-md](https://github.com/souvikinator/notion-to-md)项目的基础上，适配了多种类型的`Block`
- YAML 元信息：支持`Notion`页面属性转为`Markdown`的 YAML 元信息
- PicGo 图床：支持将`Notion`中的图片上传到 PicGo 所支持的多类图床中，包含：`smms/qiniu/upyun/tcyun/github/aliyun/imgur`

# 使用

直接在 GitHub Actions 中的 workflow 使用本插件即可。极简代码段如下：

```yaml
- name: Convert notion to markdown
  uses: Doradx/notion2markdown-action@v1
  with:
    notion_secret: ${{ secrets.NOTION_TOKEN }}
    database_id: ${{ secrets.NOTION_DATABASE_ID }}
```

使用该`Action`即可将`Notion`页面转为 Markdown 文件。

## 参数

参数信息在[action.yml](https://github.com/Doradx/notion2markdown-action/blob/main/action.yml)配置文件中已经写明，故搬运。

各项参数的具体解释，以及用法如下。

### 基础参数

| 名称                   | 必要 | 默认值                | 说明                                                                                                                                                                                             | 示例                              |
| ---------------------- | ---- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------- |
| notion_secret          | 是   | 无                    | `Notion Secret`, 建议最好放到 `Action Secret` 中。获取方法见：[Create integrations with the Notion API – Notion Help Center](https://www.notion.so/help/create-integrations-with-the-notion-api) | ${{ secrets.NOTION_SECRET }}      |
| database_id            | 是   | 无                    | `Notion`数据库 ID，假设你的数据库页面链接是`https://www.notion.so/username/0f3d856498ca4db3b457c5b4eeaxxxx?v=xxxx`，那么`0f3d856498ca4db3b457c5b4eeaxxxx`就是你的数据库 ID                       | ${{ secrets.NOTION_DATABASE_ID }} |
| status_name            | 否   | status                | `Notion`数据库中，用于区分页面状态的字段名, 支持自定义                                                                                                                                           | status                            |
| status_published       | 否   | 已发布                | `Notion`数据库中，文章已发布状态的字段值                                                                                                                                                         | 已发布                            |
| page_output_dir        | 否   | source/               | 将`Notion`页面 type 字段为 page 的页面，保存到 GitHub 中的 page_output_dir 路径下                                                                                                                | source/                           |
| post_output_dir        | 否   | source/\_posts/notion | 将`Notion`页面 type 字段为 page 的页面，保存到 GitHub 中的 post_output_dir 路径下                                                                                                                | source/\_posts/notion             |
| clean_unpublished_post | 否   | false                 | 是否开启文章删除功能，也就是`Notion`中状态从[已发布]改为其它的文章，是否在`GitHub`中移除？建议开启，但要确保`post_output_dir`下仅有`Notion`同步的文章！！！否则可能删除原已存在的文章            | true                              |
| metas_keeped           | 否   | abbrlink              | 在文章同步时，`Markdown`元数据中需要保留，并同步到`Notion`页面属性的字段，多个值请用逗号隔开，例如：`abbrlink,date`                                                                              | abbrlink,date                     |
| metas_excluded         | 否   | ptype, pstatus        | 在文章同步时，需要从 Markdown 中移除的 Notion 页面属性                                                                                                                                           | ptype, pstatus                    |
| last_sync_datetime     | 否   | 无                    | 上次同步`Notion`数据库的时间, 用于增量同步, 务必采用`moment.js`能够解析的格式。建议采用 git 中最新一次`Notion`同步的`commit`时间, 例如: `git log -n 1 --grep="NotionSync" --format="%aI"`        | `2023-09-04T17:21:33+00:00`       |
| timezone               | 否   | Asia/Shanghai         | 时区。`Notion`页面属性中，ISO 时间转为本地时间，本地时区。                                                                                                                                       | Asia/Shanghai                     |

基础参数中，需要保密的参数有`notion_secret`和`database_id`，建议保存在`GitHub Actions Secret`中，设置方法见[Using secrets in GitHub Actions - GitHub 文档](https://docs.github.com/zh/actions/security-guides/using-secrets-in-github-actions)

其它项根据描述进行配置即可。

### 图床参数

| 名称           | 必要 | 默认值 | 描述                                                                                                                                                                                                                                          | 示例     |
| -------------- | ---- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| pic_migrate    | 否   | false  | 是否迁移图片到图床。注意: 如果不迁移图片默认导出图片链接是 notion 的自带链接, 访问时效仅一小时。                                                                                                                                              | true     |
| pic_bed_config | 否   | {}     | 当开启图床时，PicGo-Core 中 picBed 部分的配置, 支持多类型图床。详见: [https://picgo.github.io/PicGo-Core-Doc/zh/guide/config.html#手动生成](https://picgo.github.io/PicGo-Core-Doc/zh/guide/config.html#%E6%89%8B%E5%8A%A8%E7%94%9F%E6%88%90) | 详见后文 |
| pic_compress   | 否   | false  | 图片上传图床前，是否进行图片压缩                                                                                                                                                                                                              | true     |

图床参数中，`pic_bed_config`和`pic_base_url`的配置较为关键。

- `pic_bed_config`是 JSON 格式的文本，保存 PicGo-Core 中 picBed 部分的配置，用于 PicGo 的初始化。建议保存在`GitHub Actions Secret`中，设置方法见[Using secrets in GitHub Actions - GitHub 文档](https://docs.github.com/zh/actions/security-guides/using-secrets-in-github-actions)

以腾讯云、阿里云和 GitHub 为图床，`pic_bed_config`的配置案例如下：

```yaml
{
    "uploader": "tcyun", // 代表当前的默认上传图床为,
    "tcyun":
    {
        "secretId": "",
        "secretKey": "",
        "bucket": "", // 存储桶名，v4 和 v5 版本不一样
        "appId": "",
        "area": "", // 存储区域，例如 ap-beijing-1
        "path": "", // 自定义存储路径，比如 img/
        "customUrl": "", // 自定义域名，注意要加 http://或者 https://
        "version": "v5" | "v4" // COS 版本，v4 或者 v5
    }
}
```

```yaml
{
    "uploader": "aliyun", // 代表当前的默认上传图床,
    "aliyun":
    {
        "accessKeyId": "",
        "accessKeySecret": "",
        "bucket": "", // 存储空间名
        "area": "", // 存储区域代号
        "path": "", // 自定义存储路径
        "customUrl": "", // 自定义域名，注意要加 http://或者 https://
        "options": "" // 针对图片的一些后缀处理参数 PicGo 2.2.0+ PicGo-Core 1.4.0+
    }
}
```

```yaml
{
    "uploader": "github", // 代表当前的默认上传图床,
    "github":
    {
        "repo": "", // 仓库名，格式是 username/reponame
        "token": "", // github token
        "path": "", // 自定义存储路径，比如 img/
        "customUrl": "", // 自定义域名，注意要加 http://或者 https://
        "branch": "" // 分支名，默认是 main
    }
}
```

## 输出

`Actions`执行结束，会给一个输出，报告更新的页面数量。

| 字段          | 类型 | 描述           |
| ------------- | ---- | -------------- |
| updated_count | 文本 | 更新的页面数量 |

使用时，可以调用`steps.{step_id}.outputs.updated_count`，以获取页面更新数量，包含添加、更新和删除的页面数总和。

# 案例

以下提供几种案例（模板），以供快速部署。

首先需要在 GitHub 的仓库中配置 GitHub Actions Secrets，位置为`Settings→Secrets and variables→Actions→New repository secret`，添加以下三个关键配置参数：

- `NOTION_SECRET`: Notion integration 的授权 SECRET，获取方法见：[Create integrations with the Notion API – Notion Help Center](https://www.notion.so/help/create-integrations-with-the-notion-api)
- `NOTION_DATABASE_ID`: Notion 数据库 ID，复制你 Database 链接，如 `https://www.notion.so/username/{database_id}?v={view_id}`，那么`database_id`就是数据库 ID
- `PICBED_CONFIG`: 如果想将图片上传到图床，请配置该项；格式为 JSON 字符串，详见上文。

## [案例 1]Notion2hexo

介绍`Notion`部署到`hexo`的`workflow`模板，直接复制粘贴到仓库的`.github/workflows/notion2hexo.yml`中即可。

> 记得预先配置 GitHub Actions 的 Secrets

```yaml
name: Notion2Hexo
on:
  workflow_dispatch:
  schedule:
    - cron: "*/30 1-17/1 * * *"
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
          echo -e "Latest notion sync datetime:\n$NOTION_SYNC_DATETIME"
      - name: Convert notion to markdown
        id: NotionSync
        uses: Doradx/notion2markdown-action@v1
        with:
          notion_secret: ${{ secrets.NOTION_TOKEN }}
          database_id: ${{ secrets.NOTION_DATABASE_ID }}
          pic_migrate: true
          pic_bed_config: ${{ secrets.PICBED_CONFIG }}
          pic_compress: true
          output_page_dir: "source"
          output_post_dir: "source/_posts/notion"
          clean_unpublished_post: true
          keys_to_keep: abbrlink
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

## [案例 2]Notion2hugo

这里给出`Notion2hugo`的模板：

```yaml
name: Notion2Hugo
on:
  workflow_dispatch:
  schedule:
    - cron: "*/30 1-17/1 * * *"

permissions:
  contents: write
  pages: write
  id-token: write

jobs:
  notionSyncTask:
    name: Notion2Hugo on ubuntu-latest
    runs-on: ubuntu-latest
    outputs:
      HAS_CHANGES: ${{ steps.NotionSync.outputs.updated_count !='0' }}
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
          echo -e "Latest notion sync datetime:\n$NOTION_SYNC_DATETIME"
      - name: Convert notion to markdown
        id: NotionSync
        uses: Doradx/notion2markdown-action@v1
        with:
          notion_secret: ${{ secrets.NOTION_SECRET }}
          database_id: ${{ secrets.NOTION_DATABASE_ID }}
          pic_migrate: true
          pic_bed_config: ${{ secrets.PICBED_CONFIG }}
          pic_compress: true
          output_page_dir: "content/pages"
          output_post_dir: "content/posts"
          clean_unpublished_post: true
          metas_keeped: slug
          metas_excluded: pstatus, ptype
          last_sync_datetime: ${{ steps.GetNotionSyncDatetime.outputs.NOTION_SYNC_DATETIME }}
      - name: Commit & Push
        if: steps.NotionSync.outputs.updated_count != '0'
        uses: stefanzweifel/git-auto-commit-action@v4
        with:
          file_pattern: "content/"
          commit_message: Automatic NotionSync.

  # Build job
  build:
    runs-on: ubuntu-latest
    env:
      HUGO_VERSION: 0.114.0
    needs: notionSyncTask
    if: needs.notionSyncTask.outputs.HAS_CHANGES
    steps:
      - name: Install Hugo CLI
        run: |
          wget -O ${{ runner.temp }}/hugo.deb https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.deb \
          && sudo dpkg -i ${{ runner.temp }}/hugo.deb
      - name: Install Dart Sass
        run: sudo snap install dart-sass
      - name: Checkout
        uses: actions/checkout@v3
        with:
          submodules: recursive
      - name: Setup Pages
        id: pages
        uses: actions/configure-pages@v3
      - name: Install Node.js dependencies
        run: "[[ -f package-lock.json || -f npm-shrinkwrap.json ]] && npm ci || true"
      - name: Build with Hugo
        env:
          # For maximum backward compatibility with Hugo modules
          HUGO_ENVIRONMENT: production
          HUGO_ENV: production
        run: |
          hugo \
            --minify \
            --baseURL "${{ steps.pages.outputs.base_url }}/"
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v2
        with:
          path: ./public

  # Deployment job
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v2
```

其中定时任务`schedule`可以根据自己的需要修改，建议间隔不小于 20 分钟。
