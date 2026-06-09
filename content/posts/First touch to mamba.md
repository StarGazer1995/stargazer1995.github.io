---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGTC64QO%2F20260609%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260609T123243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCICcuxi74NizMw4dP286NVbVCaaZxfemU0KvAHRvy0iMrAiEA8lRmpyInvL4XiB%2F13zUyh557ZazV0zLrG%2F8iBQeFft8qiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGzSfq%2BZHJ2O9%2FzfECrcA1E4YZuog60jewPu5XPkwplQybYtCjZ36AcHtSEGjiqJC8NcOHgfHAdxub%2F1ST2%2BuR94qOvTSZYZb3OVnOHZiqP1U9iRhshm5Q8RdSEJxxd4YB4Jbp2f3G%2BDlRLOfAcU5qU4zFAgCXffFuq0TAg8HGApVDRUMG%2F1hXr7mpkd9QcGT%2FFMZn9YM9lu5mez3OKBkdb99We9mp6y0EZ%2BCx2nDo6j4eOedBykMwr7oGfbhisohtL%2BRXZcIhMHsfJjYn4rnZC1JtS7dtrPbLY11D3cjnyTWOjYGZ%2FZYh5l%2BB2VBpGO5j%2BRm%2Fk%2Fty%2F7h7anwuobIxMUT26Zw6EpnhRv7OGLwo3RwjjGb4sFeetW%2FZajpL4wDl5TmlL9h0JMCRSNPMSGD5Dpjf8IWNA%2BVbs89rKkxbRePEkWwrQq1U6QiWcpNhNmzzlwo4Xl%2FKeFzPnw5bm5GPYGpO1bFdDbcrmUCJ1Aq6qsLmk15JnStCgSscyW7%2BTAAP2X7LuC%2FX4sefmW46bTPPONj2gUK3kZtJB9DBaqxVtfqgYAhjHwspOY7dDqJD%2BPXssBcNFN3oDab2gAd8KG5dGffiqMx6%2Bz4Xsi8iKZKL5a4ynl2cZNSJ783mT9WunedoYnsTekIbN%2FLq%2BLMKeOoNEGOqUBT3Yg%2Bxj8nUdyQW2dgzCFep8belJJmhsKYMmXrpdCq%2B%2BP3BeQ0MjDjtQAfXWtx5hqb9k7dzOxRru0ODfc85rKsBM5hK0KgaIcJ9lEEKWm2MwzUHlZfdg%2FHcEQbO7thNhSRslz1OId1E98OHpPZZEBkucBXbCGKE4R394K4X7C2%2BzUEYeo4uImSxG0lIB7ixmsBrKv75GpBcAbR1MNy9IFgLpbIYrO&X-Amz-Signature=af82543638288ab7eddcb9c0fd8df2d322556367a551a038e31c36d0798607b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
