---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZACCA47%2F20260612%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260612T021318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJHMEUCIQCb2OV17i%2F15uQyz4vjeymKkNqEOn1xdVwHHNRvMsYOowIgBewd%2FrR%2Bxevj8HR%2Fh97mdFzMlMkxkjLBicn6BjKNL94q%2FwMICxAAGgw2Mzc0MjMxODM4MDUiDMYJMGO6R%2FdoY94WdircA5TznMceexLGZDJ%2Ft%2Bxwnw1YGsms3Lt8MBwHeXsgHb8SAu8p4OgM1TGIXd6H%2FAHG%2F0AImvaBqZIfeuTYLF7j49otqHCKoybNXiTgXuhjB0bRZw%2BXpBSKErBNFaCNSQmBBmU8o3vntvMVKB3%2FlOTccfnZvPUsQQ1r4qDgtdfI2uiOdj%2ByjStaqWWgttrWEsMPkQzc2ELSOU44pPHX504xlURO3IV0CBB%2FKdkpqxw5DKw8zPafVoEoFV7xFOLNOF4jGOf98ejURct22qRezE8A5FQ9%2Bs4hsSQGCVI7H5LAKSy0vLeM7o1cuY%2Fx2DcJXy4E8uhyiPGz5Qg1As7a9Ls%2FlBk4MBDtdO7ANQBno9wogAbRHiEB8MWYF4TNCTkHRNwMX7sYfdD9lv5THlVNB8CI%2B0Yn5yntHWkpQwnoResLc3z2E4jMo50W60pmMYTZqFzZad0nOAL1d8LMHnBGTr0wZql2NNmYLP50QC3Wo%2Fa2rP9MEgXejp7Fi2l%2Bqyv77gYZ2xZObgsF2%2B1NSl4VUUhHjTbVO50QQcxa5sB52MB8THJ3uV6GefJsoxfl%2FxJIz4mpsARZN5qVmIIbkNvbSte6sIXAf0T5zdGgp%2F2WmzwGbnyYyl73m2wqGjolJnTkMOnNrdEGOqUBhYi93hAcxntX7%2F2cUH4Wiag%2BMjn%2F%2Fh6v7lVmsHFR6rM8gbHcz64HHbc09fNJ8t4Wk91%2FVBA0uVvJFKiveL62BqhzmutJBs4iG3jM9%2FMe%2F0WedlbTjAIgH0RzfuxFPS0aPKUwJxTCj9TUIhy8xNJrWjRjzDwoqCxRUKCAcd6PDVyVJlHb%2B2XSUqWn1PoSs%2BQmaHzPqYdpR9ATc%2B%2BtKWrcGqt5qpX7&X-Amz-Signature=2d0419d5c2a0affa6311c51ee2b41fc4cb39a1467b36f4ff9d1e1afc3f9436d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
