---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AIBXUUT%2F20260915%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260915T065341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJHMEUCIQCdS3sV2UabxOYGfVXs%2FsqGH65JIWsaZTDrcFcWWf5yTwIgBf31OjRE5BnhNaBHHIxq05FTxZ8xyzcjpLdX7Swk%2BZcqiAQI9v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIEYum8mUTK0tuhhrircA1%2BbU0ynB1Ul3BbGd%2Bn4ojsj9o7iDIfTxq%2BXQ9OgDgm%2BfXkeIqbgXjLvtvVig1TNV0mBDRAvjDN0nHnPg9t6QJ5it4oZ98bXNOc%2FZUxjaWXN5LrMzOf5yOwdIKaJIgrBj1EeVAvcFZBUqSnQp3JpIUvPMbPDrykZIVMnSDHdHOowzHcOFD6N4HlhYYid3XauEU3v1bH1GOU73XKnmzmPNMtVmx08gdZmav%2FQBp93cged5n4WhChoO%2FI%2BzPJ5YeCpJKd8EjssBZbbXy2MQgTDoXDxUberO%2FiCP0XBPoj1hFxkAI6hnB2G7rD6pNP4gUS8wv%2FUR0f2xbsMJ3FC6G7bRynDnpUB99oPmqLTIT7ubfOSCpXmG3qJTtgtRinf4wVq%2F7N51WTGs7BW0ds4vS90kWdh6WnPl4FPFldMjVIQNCxzpYMCSKq7%2BXV5uN24jG9%2BUSIv%2F2Gs8KhVIF1RQcqQZSqxnksz6z%2FBMDqsjF1eQmOHhc3Wv55WEflYcXdXzTq54agO4XI66dbIj%2FOci98lpkY82w4H3mwkpN7YXVtlVTHCn1Qa%2FoiI8qxheazOJoHicNDjDSXL%2FjxehmuHcxjYcVNkNkYSLThUIypepGTnUKEOazqfot6iJc5V%2Bd%2F5MKmvo9UGOqUBFkYs0acj2CgRoYBZyYeBT4Tiw%2FWIj0EJAG6EEpadqa5SNj5WxgfYjakz2IeHUh9izKVxVseDeu9BZU%2FtjmAqwBByhGbojRneSaBzr6j9Pob4SGPoVEix3A7GI2UoYWOuFFof5tPi6K462r7RwgXMOMRPMKP4YJxPWnT1MyC4eLmaDpWhJsU6nPZxwy5roFNT1jroCD4HO%2BPiXc2PFg%2FveMhzO7CN&X-Amz-Signature=2b2fdfed7ca6fe29d1c884a7a7cf9ccf955766c3b73df62305decfbfc781a6b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

From the perceptive of the structure of mamba, this is a discrete selective space machine that runs in linear time using linear space.

lets say, matrix A is a state space matrix for the last system status h(t). we then can calculate the next h(t+1) based on the following equation:

$$
\begin{equation}h(t) = A*h(t-1) + B*x(t)\end{equation}
$$

$$
y = C*h(t)
$$

Where B is a weight for input x(t) and C is the weight for output y.

We define A matrix in a HiPPO matrix manner.

$$
A = \begin{cases} \sqrt{(2n+1)(2k+1)} && everything-below -diagonal \\
n+1 && on-diagonal \\
0 && everything-beyond-diagonal \end{cases}
$$

By doing this, we can use SVD partition for reducing the computing demand.

$$
A=V\Lambda V^* - PQ^T = V(\Lambda - (V^*P)(V^*Q)^*)V
$$

This can be done
