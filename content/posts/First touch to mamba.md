---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFEFQDB5%2F20260825%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260825T025005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQC%2FZTHToXvW6Qe7eFPblfjtnikz4QtAY4HIecW9%2B9ZHMwIhAKfOJmhZ8dg81oC%2BJbH6UXT3ygPJeMgMsaT%2FZ9PUWNMTKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyApGxKB1KjQZ9S5L4q3AMs%2F39kY76s7D%2FXm1j8q%2FDdzwpFwi90RPnx%2BqJD66Lx2Cl33hYrTbT20u2BaqM6Bos8N5AMJdx9wCPsqbc4tH75AnWFkxujZFZLDjZe2wXlFZzsorVDam8COr%2BKlbA66UUQbp9ILFQxMwWqUmGzV6NoihrcXvXmG7HZzBr2QMOITL%2Fki9iBeFhEvErLSaYYVJW9j6oWPbokPB1cQys9IAJcXIZPXaaMK7FM6p6P4CM24Lk6x6FQUp%2FPQVR0aR%2B174YBkqgZg5Li8wqGw0tvbV81aXZK2Tx1M63idlU%2BBq5oDKSRkH7BJ4uZMqcerkofCLM%2F4lPByYxYOAI7Eb49%2Fqeus4%2BWwpg6oVlbf2sXwjG5jM6fvEoheY7kXh%2FZlct40mjUMY1r%2B5Uy9AulftpXPHZWN9Igwq3frLtFtYRu2D6BhvJ3hKuVK0OWhl1zON6UHdgQylX2411%2FxOnxqfY8WoHA6p6gsLDmjOwk3YNWNnpP%2Ba%2BgYRAaxWxM7H3yvI%2F13T8XNcmiAMFHnsaw29t%2F816%2BDcBpxJsTST93u9Ce2hSEQYt%2FaeOKzj2mNc3qqegCJnMoiMjHHZveQAHeOsMHxPKpFqzK0tSS1ss9bGoGj0tb5R%2BtVtflwCmU8KfAeDDc0rPUBjqkAZQIVHOeSRDnMfW8zHN7UPnGRxnznGw6XyyP3VL%2BYMxa%2BDVlCctFuKnPYAzq8JohtP%2BQVjpMKjYLds8ZYOq%2FxCZ6bhNrav7IT4JeX07GnJsc6GQtgdP8CyratiNwSTSIjVDNCH3nIxMpLUyxkz5bos7YNUQPAl72ZJ6Z8AcNrEdoqYA2w7bMMUImtsIIlAzyhWYz5CJCztZlp3hzQnQvZanymZ5j&X-Amz-Signature=9881627629afeaf502021c0d556115b4053d1efe10ae46c4834c09f03cfb337e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
