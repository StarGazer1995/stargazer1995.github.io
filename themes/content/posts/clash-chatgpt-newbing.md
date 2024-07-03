---
created: 2023-12-25T01:57:00+00:00
categories:
  - 工具
  - Clash
description: 回来第一件事，是ChatGPT和NEW BING无法正常访问了，用VPN也经常被限制。由于用多了已经形成一定程度依赖，故折腾访问问题。
updated: 2023-12-25T02:01:00+00:00
date: 2023-12-25T01:57:00+00:00
type: posts
slug: clash-chatgpt-newbing
title: 折腾|Clash添加规则访问ChatGPT与NEW BING
id: 5979eb11-1ade-4c12-97e8-2b52fb183982
---

> 提醒：2023-11-05 近期 Clash 全系相继删库跑路（Clash-Core、Clash for Windows、Clash Verge、Clash for Android）！

# 起因

回来发现访问 ChatGPT 和 New Bing 还是非常困难的（在有账号的前提下）。

首先是要使用 VPN，不然 New Bing 经常给你重定向到`cn.bing.com`，非常烦。

此外，由于机场都是多人共享机器，所以一个 IP 的访问次数可能会很多，导致 IP 被封（主要是 ChatGPT）。

没想到用起来还不是很简单。

# 解决

首先我将 Bing 和 ChatGPT 的域名加入了 VPN 代理规则，由于 Clash 会自动更新订阅，所以我采用 Parsers 添加规则，避免每次更新订阅时规则被覆盖。

针对 ChatGPT, 将`openai.com`加入代理即可；针对 New Bing，将`bing.com`指定代理即可。

配置如下：

```yaml
parsers: # array
  - url: # 订阅链接
    yaml:
      prepend-rules:
        - DOMAIN-SUFFIX,openai.com,BWG-SS # 指定主机
        - DOMAIN-SUFFIX,bing.com,BWG-SS # 指定主机
        - DOMAIN-SUFFIX,github.com,♻️ 自动选择
        - DOMAIN-SUFFIX,vercel.app,♻️ 自动选择
        - DOMAIN-SUFFIX,githubusercontent.com,♻️ 自动选择
        - DOMAIN-SUFFIX,doi.org,♻️ 自动选择
      append-proxies: # 加上自己的主机
        - name: BWG-SS # 主机名称
          type: ss # 类型
          server: 1.1.1.1 # IP
          port: 444 # 端口
          cipher: chacha20-ietf-poly1305 # 加密方式
          password: 12345678 # 密码
```

一开始我指定的机场的美国机器，但发现被 ChatGPT 封 IP 了，Bing 也经常不能用。

后来换成香港的，发现也经常无法使用。

遂将自己此前买了一直没咋用的搬瓦工主机用上，独享 IP，才解决了该问题。

目前已能顺畅访问。

巴适~

# 参考

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://docs.cfw.lbyczf.com/contents/parser.html"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">docs.cfw.lbyczf.com</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;"></div><div style="display: flex; margin-top: 6px; height: 16px;"><img src=""style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://docs.cfw.lbyczf.com/contents/parser.html</div></div></div></a></div></div>

<div style="width: 100%; margin-top: 4px; margin-bottom: 4px;"><div style="display: flex; background:white;border-radius:5px"><a href="https://github.com/iczrac/Parsers-for-clash/tree/main"target="_blank"rel="noopener noreferrer"style="display: flex; color: inherit; text-decoration: none; user-select: none; transition: background 20ms ease-in 0s; cursor: pointer; flex-grow: 1; min-width: 0px; flex-wrap: wrap-reverse; align-items: stretch; text-align: left; overflow: hidden; border: 1px solid rgba(55, 53, 47, 0.16); border-radius: 5px; position: relative; fill: inherit;"><div style="flex: 4 1 180px; padding: 12px 14px 14px; overflow: hidden; text-align: left;"><div style="font-size: 14px; line-height: 20px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-height: 24px; margin-bottom: 2px;">GitHub - iczrac/Parsers-for-clash: 自用Clash的预处理配置文件（parsers）</div><div style="font-size: 12px; line-height: 16px; color: rgba(55, 53, 47, 0.65); height: 32px; overflow: hidden;">自用Clash的预处理配置文件（parsers）. Contribute to iczrac/Parsers-for-clash development by creating an account on GitHub.</div><div style="display: flex; margin-top: 6px; height: 16px;"><img src="https://github.githubassets.com/favicons/favicon.svg"style="width: 16px; height: 16px; min-width: 16px; margin-right: 6px;"><div style="font-size: 12px; line-height: 16px; color: rgb(55, 53, 47); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">https://github.com/iczrac/Parsers-for-clash/tree/main</div></div></div><div style="flex: 1 1 180px; display: block; position: relative;"><div style="position: absolute; inset: 0px;"><div style="width: 100%; height: 100%;"><img src="https://opengraph.githubassets.com/5911b014a0efd06c0c816495700b6dd49fee7ae68f0dddc0df73579aa42788c4/iczrac/Parsers-for-clash" referrerpolicy="no-referrer" style="display: block; object-fit: cover; border-radius: 3px; width: 100%; height: 100%;"></div></div></div></a></div></div>
