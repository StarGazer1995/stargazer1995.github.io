---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664THWJ3YR%2F20260512%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260512T225325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIQCG5y9Kj1cySLg7fbiXCHHiz2RaBvK4oiDLqnoPo%2FV97QIgaGqlPBlMBPzaeL%2F3s4DthTULtc0d0NzyEuZMpB1OuHQq%2FwMIOBAAGgw2Mzc0MjMxODM4MDUiDH8jkq9h9X40Xou4nSrcA4S7AsEXD1XvWMp3eXN%2BQa98gl2K%2Bkhwl%2FAeYACIWATdVUIK60B3kANB83Gd%2B1UkMbK%2FwTH0dRJe62XrUktt1YRQv7f5v8Q9ioWymj7h3rGXKINP2q3z3B36dX%2FGXkcRK0u1oEI5HHsTxPlLYqmbTaILqXsEJDzN1kJSPpsy%2Btsq1Oa8TZua50znIoV83fKJh0d9z1uIIqUp5t%2FjYT9i7xqPqx8yLvQScPcdd3wTAvonnEHFWpBg9ezL59jJhbZb9YEbBhigFPg3Epnu74%2BFTgbWJrR95aLS33VToU7RTAQ%2FUwO7GLfK5TWS4Smf%2FszYsCA%2FgXajz1OOZq%2F9ZJVNRpiKvTIdnr5JWdcNh%2FZByH5Ny1OJLFlBICu3YKMjMW%2FFdIu5aHOL2FzeEUHXx1KpYv7zzChDVo9LqYq0RCr8C1%2B2bafg%2Byfa6ZL20qxV6n%2FZ%2F%2FqXGJTSDoX%2FNiZ2pYHvsazGA67nSoaVmAltG0t5RjyarMpWHzSG18ALerOuU6KzR9UhjyXg4VUi%2BDcgaPCd2nchme2asvwx8ssOOgWv78zA7Zx2EVI6%2BAn3yLTGNNoYdt4gdyR2KVnvz%2BEd12CoD2NSFzCisr9gfdKryigNmn0%2F43NJb1gu%2Fk0m1uvrMIrTjtAGOqUB64Dfp%2FdEEXQO1IbCmS%2FcbvEYsRGwRt%2BGSOcSgCyOjhLnKtBUi2ONf8kyOcJYGQkJrT3fH5i3tVmNFUDMv0KRRO%2Bkga4HspqfagbupXhuomvF5dGniztjnrbKmWWHI3ML%2FoqZi85TkZfDqGF%2FebsT%2Fa%2B9ZI2OTNRfJD2APie%2Ba70u%2FJ0ySk2YoKdQA5aYnYJ0eSVCUfaw5dNznMZ9sa%2BXJrpuH%2Fy%2B&X-Amz-Signature=0e64ee82997a99d34d98816807af28b837d404d820e9b3fa6ca91d24bcb73314&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
