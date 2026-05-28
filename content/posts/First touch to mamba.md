---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGL754BV%2F20260528%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260528T150254Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICxVFbkwzF9aEoTrvGvN4JAzOM37OgdOW7S%2FPJE3tM3vAiB4Er%2FjpVHgBdZHOIlud2uD5pl8BBSbrNdFspjVwGEPByqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5qw0Yb5CuI2r%2F7qsKtwDarNW2IMJK27qFJvn4v9IR89rGiyYuqEDOX5qKGvuhT9oVrsXxu%2FFHQsCNxXagmuovSz8qi%2FJAyHeaS3PZnMn9sk%2FM77nFOuZwRbj6LHfCPVdCKWeqFHyN6ZGITC6%2FT5wPZ2l2VNOdntLVhnnm5FsuTw4LtMZhc%2FiCE2A78Q3s64xmFEfS7Ussyj8LGj0okBL0kdDiqpVpXTUSwaKhuGH0XoAARF9pprlw54Z0LkjBAk8VbIKILa%2FuqoJR6QP75wEP3O5YrXze2mNqP5dWFZWxm4%2FwKqRtRWBEjJNaqv2ghkNmxZmOiKsBX3Llhc8pMsykFR2Lfq4JOek%2BwbAnG5AJl7riHtDoryraEp2EOPUKIPTOAnpRe0kxKh%2Ff9YI5OKHgPSco4MOHi%2BS0IBgzCZmQMwUxGd2srFvPHBOxGslO52aS4TVRMsTDv%2Bgk2aYL2nQCk3%2FdlDq4Q13lo4xlfmqD94gn6XweKS94HLg8rj8L1aL%2F5HdHzvg%2FIPxp1Z8rMHLjqnXBjWHYhAGM%2F51ztKbmivxf9QAsn5PwYl2ltNgq2swAVNu81C0WcbesizPTBE2hAya1R0wXCyq2%2B%2FfvhSW2ptzT5%2FkbBcLqtrF6UIa11ffr%2BBJE70guB%2BJwLwwga%2Fh0AY6pgGxhj9xuOdg1qcalUBfAJ%2B%2Bs4ll%2BlV%2BOz6S3J8Azgg0qjx6tKNQa4YfUpJSDiIzL0Wn7YmATVhCmokXkG%2BqwvjLGFlLjZ%2B44KDF%2F5VxsTPwSq7PQTnKewMqMxCbtLrBJxZB8dpb9hbQQO5hJYGfAyTcakb2bWHLoctYJVxDaCm94O5Qe3Jkb9o1AV2fnMBdEcJkruHjaugCV7orLd3Y9%2FJIS82SVauT&X-Amz-Signature=43a7e6b99b2336df544bb62a8289ee46d9558ecdaf685902e7fc0e39f2bafd2c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
