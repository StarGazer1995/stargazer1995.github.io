---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD6O6QYG%2F20260612%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260612T230710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCICOLwPQBdfG96JW7WZrnu7YkydJfBw12AlHvjMebvGJlAiAc4ehnM6Wd6KS4%2BsHy0rODDUz0hgLiqOzI3frIZWijNir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMvgp1FtLdVuNJiGjNKtwD9YcMXfZrLl5WlIIi783wAVw5N%2FYE32m5ad7yGYTthdGc0DvezaQMEc0PDXsGPqAvlAouzBre6iSqRp1zQXtN76O6ukA%2F%2Brcwm%2FvA3%2FDHph5bWWqamiUL4dmb1o9KxIJiiclAwbnjeas1S%2FvghmWyGHUd0QBSRr7YVTF9fLrR3oH1yKYsAxH2swbc2Kj3Yki38z6ncxiYxUxtabcgsDy3Xwlg522Jp%2BdfOCZZ%2BSOxPdaPFM%2FDgmI5TsO3iKotv%2B9gkGE62FQ6HsjJTEbxMDqIKoyy3CndjXadzvYGxcpHJJovVuEUMpYflJpJAb%2Ff%2FUWdKemxBtZIZhDzyItcIhCu5jXL5AU3O2HIgc1H9XpPnoY1VwyP3L2VH2qlmkLYMBddSugJZHdceuLq%2Fj61FaUG8DdhigZSC2QLh65cnyK9VQ0vkAT%2BSfKw6EFGsRKbpmxNI3NZ9khdivWPT1aMFjrJZLOLJk4UdF0446awyfT2mfxmZAvE6d2A0tWVPJdGmlekCBNvDucTQiECZmZ%2BNeEIdECPAdhhvIL8xQBvVuCw5hTLMdmLKikkikYpiNwEbVazpkjSkCkC7v6AluoVkZvsXOmSziUGwf2J5OYcp8l6DbNx0kknTNXTO%2BXTYgIw2Zey0QY6pgE5uz%2FEXNzNXLtcNmP77Q1zQcjGfGOvgNFQmQXx8ubM4ufcGcwTdw3MMfArxuXLoXIb5VHss3ohCkViUNK2aDa3fzPWjCEVp21Q4ZfStV9PHZpiwM2BfOUHA0iD8K7nbKeQqOF4FbuzHLjpWdtNwgc0x9OnYbPf0O27z2Fnev4qAT2YI2ZzokveSA9Ht%2FVT6htvuyUvzPQXZqCdO1JKaEFZHanIsmvn&X-Amz-Signature=f33f0844fa133bbe824308c4034deff9d87ff879d91e157e52e4bdda685da884&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
