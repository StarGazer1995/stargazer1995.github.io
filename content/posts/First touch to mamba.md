---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JXZAGC7%2F20260907%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260907T013523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJIMEYCIQD8dONoLcJ3pK%2FGBHFmoXujT6jbRMprY5qijeF7w7irbAIhAMvnWf3L5v%2BQbyHHOT0%2B0a4JRuTSut5y1oaZkePBKaY4Kv8DCDIQABoMNjM3NDIzMTgzODA1IgxB%2BxNlv5JOfsyfB%2B4q3AN7iaUFIZTUxzPg8I7%2B6EpmP6fNCmQC7PgV%2Bi0RK1yZEakudnKIUzdBV8V3n5xh858nHzD%2FcmUwWQD5jtu648hPZ1NdKNk88iFFL8lZ1okZt06PwBrr2rWqh259355uhtrMm%2F3pS3XHWBLXPbKLH8cxgusWQL1O%2BNqZzATsg0wvlM2jnEd2OyI8QXpWL0lGeuuUQuCfGWPAHTWIFZdaScaWHSB0l9tJm1Y%2Be%2Bsn%2Bigui7RaQWqfPqxK2RHjU1idzs84AsktJxuVYPFZZWEibqkZjV6PvX%2BLkA%2B4%2BTGeg6aA1nvTJuAtBNXmneltYdigI1N0CQ3CcsahlgSkuIXA3h3gEXXjZoWtu9pRdT6xgf22dcJy3XJ3tXJTt3llrRLDXx5x7TE2V%2BoqbaIgZsSuDTiMWgtlt9HhEbZw4rT4Qgdfzls2SUS1mrdLRrd1Qy68wYbhIYBn6w5246li2VuJhTrha%2FODDAehmgviywgfNwZWoVNFkamuYlbiF0jtwhJXF%2FHH%2Bwgw30IWEUYGgLkuGfnMTLTM4nV7AWypvwSHl%2B9E6AdicjdQdqwlOHQXXJE7vMlL5vArKn28WGctV8nVGs5jQmZXjhsIySc4MKb8Bacb8T%2Br8XoI%2FDzAPcA85zCLjPjUBjqkAcR6SFShC7mzGxorMUz07vy4j4KPNSkTGYf0cA1mYsyzIgH80wJ9O2Stka2g2TwJSurmAM16VHT94pmPyqIQ%2B2PtT8c%2FclkE4eOOWdISRlrLa6MudluzSUfEfVnQD%2BJiTbp5JPJxxQNUGQGrzQjhZjIsGEGz2tqF%2Fh6MU45efHmvF7V%2F6D6SoAjYG1xvZlMZ2BJzIUrEGBybaiXrI8h2eiZRnOv9&X-Amz-Signature=958f5b64c4660bc70d07eded172141b5b4a7cc092adcc2584f482755422b88a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
