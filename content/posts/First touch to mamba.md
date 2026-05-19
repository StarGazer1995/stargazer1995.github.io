---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRBDN4W7%2F20260519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260519T194322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQDGe7sxoIO2vdYDcOiraXW8YU%2FVaM6o0dfBBwasPZU%2FoAIhAKgpexANvkF54Hugs6%2BzDASJguKBaXSq4syPwcS4QI%2BMKogECNz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzUcVlv%2BHEeAOvM%2Bm4q3AP5SU9JNO1ggKFFgz3Zm4X2MseRQ5hcQTNXIPBaoYTR%2BkOQJcZrltzCwUUVdt8yCqQtkynGYJirZRUuC9WiHanBTwo0tnnHo8yTm82yNgHfIyD8eOxFZIW36xJHmUAuFBVK%2BYGYH8VCKqV%2B5Dyo0YXyz5cWkupOQo3DgaW0Dbt27hbXhSNc0Pw6nvaMUQnAwiah6%2Bp25Bb4fkC7pNMotmRKWBNIWN3RvgPiYFrx247YU%2FaED4e5JQa4%2FnuyPIaCptYraQwwaFSzvuaob6NWjzvuQopwAiGUbumWzS%2FycO1II83zYWu5ZwnttKAFe7ZOS8VG2bizV2zY84UbIhgV%2FxhcoqmoR7VAMXCy4Zz2zwfGQymsyom7hieygcpclDaCEmfhF0jPnVIEmQU9u9VkFGbOPmz%2BrHXo0H6E7Mm%2BiGCT4UMLpprLxfkd5ckvMVUPqcTsyz4q8MtLiVDgnoYm3kpG%2BD6xaGpBcydylEI%2FU500C%2FBk%2FZo4SRVCErXumHdve4%2FzV4HImuO%2Bj8hMA6R7JzrpivR%2Bzcl%2Bm1S8BBsNOzUoZXQwYzX1ATo%2F45NiddDjdAKNY6QqwE9pLVWVJvrhlJj5ZSaMkmmlKdZf%2FDmLQwkeSoNQ3VKfchER82k2yjCQ27LQBjqkAZ0y8l0KNh%2FAoPNf4Vz3ENV3u%2BObNXCXTi7U2STjyR5yrnMRjNwqzkW%2BDqnjV9DB2XIbXOcTyzuJvtmfTGBk%2FxuLJKm5dGMThc29Ax5azGJpZzSIdq%2FIvgjMJ%2BKtROK4wSgzlHd9n3GYrZwDRC0bf9xTTyU3%2B%2BjZwQWhkJ6aABmjE8ckRnkxYkZ5%2BiL0kKpT%2F7%2BIGTLuHw57uFaChoYah%2FhwGBAA&X-Amz-Signature=f8301877f54d6514893522e9ed18e0fe5bbac102fc3f7123d7bbafe91c91d4e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
