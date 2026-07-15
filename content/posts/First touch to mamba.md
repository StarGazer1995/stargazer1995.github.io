---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYGIJHBG%2F20260715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260715T204851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQCCLn%2FgoRqIOLLIaNIg8slQzn0b9UMOuLC79ggBIP4tdgIhAKdi4YLiC9mdTIQ6Cfsjoe99DTJnyRkZKlrjA8iLty2mKv8DCDUQABoMNjM3NDIzMTgzODA1IgynxvV%2BpxxDlqxuk68q3AOXceZSRXy3D1B3vGp%2FpzlMnshVYfjfd4WwqINxfQh9mj9CBROZF3trdMPwgEYuI2eqnWab81H4zgIoxKbPvbB8OkakHZNTg6e5I3vmQlkeK%2FfUQJzcplq1bVk0nZODKeVgxeLC0NyBR%2F283zokz3mV06J5H4eOGsexQDkmfKJzlxBaJrHz6C6ZCVWdlMIANUVRoyFuqB6iTKLSpowa5CqxF%2FkdfLojKqlVP6GIYic%2BdXGhZexknQ7eMiNq8ozJPvqdW5opLU9vMEv5N2kIkyT9BqdB7cA4Fxyp9noqZDbAC3TVNuvg90u%2BzY3kJIhPLmVK%2BI%2FLDbMkwBAoD4DcDll7J%2BjsCagRO1n0zHiXXuAFwoBTeWrxsgK118jbylHXGiGgtDIdTB%2BLFshgmsfgj1CuklzsrRWOg%2FQcfdXREjsTq%2FmnVGbifJgQ6pRGN950ZWepQCWBzl6ts8p7m5KvQe7i3JpRa1OGhS3pLO%2F2f9xMjtTiBmNNWsMeFtnZ5%2BgGJxlTwh9iU30HUzfxUixo%2BQUFxb8ApmrngOo40Cadb7B5fmdb5XDlWU%2BH5aV%2FfRtw%2BcEuw2LqyO%2B5iLS9JVHOIUa4D0y6mT%2BDS8qA%2Bn3bZnqN4qa6kJksPtDXqf0EXjC21d%2FSBjqkAS9CUJ7UpYyMHH%2BAH6H5um%2BDnr7%2F%2B%2FBDbrChZHyzbXqisALXrerQeXAYnJkbLQ9SuqfvbtXjfrv5Yd09n4tDjTR2oJxtIgk0HVLhBUzIsNFwvAO%2FDfqS4u4xhHk1QvI0ApClo%2BTsGowVPIwmGHWU0s5GY5Q49Jf5HPeSEe%2BvuqfVg%2FpoDqPOcrmLw0I8pjezOVh4tk6AIP%2FluY9yDA4YXhFap8Kg&X-Amz-Signature=715d16b7d05b719b01adbc229e2834e381e4837f25730a16ff73c0ba76059845&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
