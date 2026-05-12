---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WQTMLAW%2F20260512%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260512T015157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQDSQ5TG2UR7mZwa%2FQNkOzzwBpyBTf4oRjA1llNFCC7RFwIhAPegKKeaS%2F5gjfnymC0uFrxcl2tb2lVD3aw0Tv3uu538Kv8DCCAQABoMNjM3NDIzMTgzODA1IgyFvgM0xX20HZBE5Ycq3ANZ4Gz8JdjEifNZt7SZ4JilGRfCkngxzU6PMJ%2Bt26%2BJk6UgbEb1bh%2BnBrX596k2I4rZNacTPMYj4jhVodDBTjnBfD%2B%2BVIb%2F7s3EqptQkHqgslTntQuMpZ2LEQ7He43zlxOUDnjev0b9pZBuDsla7Td6t0Z6tPDEpaC47RKAk6U4gw9mMmBuR3yn6%2B0WKD%2B5FDNhBuYaqmyqPfmcsTZqbWdX2bUQqN8dmmELCnqwXZubwDpVFqXi0ebsVKh4wsD7nVb%2BUyM7H%2Fl9xW2%2FveKePglhEMaw11STJJJ5CwK%2FnjXBSHIQz%2BOAvjozmey2mdTMQYE4gwoUB2u3PhD93ksT%2BGQ27dxsEJH0DTXUo%2BbV91Zzya9y1AbCcpec1jhy4BzUQMXSPY%2FpjFFknG%2Ff5fM8l9njmMNHaBRlE3cFkkpj71Hl0SP01uvTJcTNaQdSBaFKV%2By5wwmdiJJYd1ZTWddi7nxoqUbMdTNqwbKGxf8T73eengqm%2B%2FNQUixghkN3XHJylp1jABEsmX9vnPQTAdACX16kApNfB6RW8%2BZHyGfJlQKefkn6fvMcagqm7nFRtD2Dy1wCPs3UgroradnkH0c1PtMDc%2FbMb1yOXrEorce2%2Bi%2FECDBUP966jw%2FUjIM9KDChzInQBjqkAXVlXIyVbZOecJpqZ1Zg8kjPa9tUx6uwwnuCFkq79pWUrxHVf68ofBi6uSctLp8dqC5jil12vhprmqjLB9UuIK6iqtWflOYuipZaJBuWGBzhWAPrN37AVxiOjh99pSJ7ehLGsXibPOnZM7CDKJ24A8MUgltmSLpn8W85ueV0OUVwzW9ug1fnUqNN4YbODicR5dL79mg8%2FtLbsEt89lU1jr0lWsag&X-Amz-Signature=efbcf5cc7f823ecee6ce2d3fc3b3744b0ae4b06d094ad5a3ef4938567b20d0dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
