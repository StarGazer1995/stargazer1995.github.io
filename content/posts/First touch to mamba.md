---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7QSC4I4%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T005543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgk1ybAei4lL8GWTAJm0C9RrD%2FrQJipFYii7Vr0h1HjwIhALvZ8OxJC7VKuGRK%2FAh%2FKAuYx0HnlfHCwxPc84Q9lztOKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxs%2BLthErzhIkW3ObYq3AMVdPHhPyFJDP7pNe4b547pZjl%2BvC1G%2FDncdIZj8nYqsoa1dTA1rTP1zgs%2BmYj5WgelHRvY2bPEgsvlJtTgsmU5M4NPptwv%2BEvsWS1N0CMGkdTqxMGqsyhynOxA4lioda38rXDBiaJ2L577SWQKjAo3IgQS5MNExk7TU6SKCF%2ByR%2FhPkoo73lMODLgFN20wS%2BXrzwUNCPxaoX9%2FRzQwI7pOg4NuxcAwnyxtU7B38WWf5UKRVhXn2eWU1QZ5sRxY%2FdFnahGyaylCxA%2FH9tI7e0I9qLVCNkLRoIWUaLnuusQdPa22s4kMfgrCbASodcnffr%2BpYcBpfyecI7prO1sYPvVvfnHLoqGe0Pt%2FsY%2BWAUBIQmsHAV%2FWMK1aiJBw71WBeXYuoevpqzrGXRXKyLydwx3Xt%2BGpd33HzPJoY2cTvQ4Bm78jLSOpMmUokfQC%2FoBTd95SP2SkkLwHi7%2BBaj7NDTIeeEaVPCzyfnJxQGA%2BAANUbKmDYSOd730kJctn5SPhtQjyFb0bOc1xZwkucdmXyqTIBTPmCXprA4b9Rt9Wuwh5mvcxxdGchY7amY5CSEL3rX%2BP1n%2FGqj34kY8aPHRNHpzXUe95a9nTTeVLpVuUHN0ItrHXuAnWTN3GqBajqTDA6e7TBjqkATR821kkrcpI0PjRGV2e4A7sagHIabj%2FTM3ZcD37rpJLWlKvwB5%2FuWk0%2BXilpRBG2zRhSCTbKmnHtOBa2Y7HoAsaZT3zr7VT%2B6hhJfn3c6fUI6W5Y2rUIcKHMXyG0bQSGyYGZcJnJ8eTgK9vXbQNdn8aVcHOukGgMctp8TY1s91Q%2FhgVasGmcPUsOWouiD8alF5jv%2F%2F8%2BbHuPeQptie5Mer2%2Fekg&X-Amz-Signature=a5a2255db05f0cf67a7fa1b75055323a87b83ca82b4e3d5f1e5eef826754c229&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
