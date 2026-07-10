---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGDAHSBY%2F20260710%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260710T121904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0grdowUuSVQLJg1AWJDvTuwKI9himxBPvmc57MV9CcgIhAIVuazu5OhWyNMKHXLA6n2RonzeGFwJHvRNGcOKAe7CLKogECLT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzy5cMNYiBlY285jggq3AN3Y9pv593d64V0%2FivmLKgKmZERtzWhvsfhDF2mKf6yI4F59ScCtyZ4LtoMo6yaGda%2Bq6Y3rYYlV3lrYjNd2e71urExf%2F7PWxy1Za3LkqRicWZeiZbvepnlHpSXkS6fo50cE8beSI%2BdFz64Rji8BW6tf23x2crJE79pn5dfcNV03MaAAL%2Bgnbhj%2F4ll3N5LV4nxn3kRYFqj1rnjRvVZR6aTkUL7%2Fa7oCUdXK9n4SKZC62%2Fm8nedsYIYMtORlrQVHXWeT5nK9aEDtR%2BLUu92GlNar4LCYuUGn071RcmV74MRw8RDzGBiLlQo8G8GUe239W5%2BciI7wmEQIXdwbo1Bh5yx9t%2FdgjPySIhcNHFwZQ541NUCSlmhfGg%2BAzYx%2FS4%2FjogpUn3Z7q%2F4iDLpc6hiZaYLwEE7Q%2F1vawpWU4TDj5GLrARMy3QUSqrw42XSQcZ4d8mUd0tBFHtSIxJu%2BJm0Sgv%2BWMgJqvXF0KR33SOvSQOMcbDcdTSyfXYlLbbHyVqZd5iR3nMfDeRz23pGvLyCDglTQFdhe465XNRAaQsm98mLJ8Z5eCgwgCapmTvvhe82Ijhl8pzzM%2BZ5sv2ybIk8fqUHmhqZsbFQpDWtkbeN52aAtJHfyimMRExN%2BIoi%2BjCppsPSBjqkASnYnWb%2F9OyfdlbJBgm1er4pmZIQIPcjnnM32UNtZ6FuEFVC7FzCJFeNcOvWi5pAQYjvCwrkTZ%2FdNS6lTXVjSxMhj8Le5gibnARfnp0%2Fru0E5xq16sfuA9fgocf3iv9faRA8AOK2tfmc%2FnRM6%2FyJOcZmdyOmKWYlmEkuoAKvOxa3YtkvLATxSs7XJt4q6PSpxKJqeizo8dZ%2FsxF9YRd3mlRK1%2B9z&X-Amz-Signature=4e47c974b2bb4360350b65d446db52e3e866cb437c820177f1186199bb34f3d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
