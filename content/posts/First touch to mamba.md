---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VW5Y3AP%2F20260722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260722T045653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQC1ghGheDVuZbRda8KN%2B0gjneiCqRk63Qigvm%2Bl7hNMKgIhAKt13VEfGwlO6X8M4I00VDCqAn%2FXOuCcsWU3RvdGpfOYKogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzoHrTrLg53ceKCMsAq3ANq5dvyuB7ItBZQcPYkXI8pc1Kz%2FDpmLY2U8b1A44W3UWO0r%2Bk9auAf6MYjB5aA3AHGEQo0%2FYPKW%2Fpfga6F8646vrLHYpLEAkPFAYr%2FCl9IFLanz8S1EWijwCKnPq%2BMp0UHCZ%2FVbTvBjOZBJXMa2YYaQC3Zq9rszaPdI%2B51fNfpTWESq156YtXTr1Jnl0UuHo66UlhWiFjiO8bMeyrRP4e8OF5JCJD9zm37XKLQQRZKdR9u2enZ5zpYI%2B33SIHSgKqfC9CGspSyLgFd15oUZZh5Y4ykkgMKhTOfVy1gdLPhR9PwhBbgyoI%2BlvqaR%2Bzj%2Bd9eBGJuDvSreA%2Ba7BLCOr7Tmwe%2FEmbzG1Sj0K5wlE3eSi7xNxRBL7zaVm14yIUPmz08XWII4gtPCEEdZBdRqNKfP00V5DnMSacbQXTfAqBoCp94pny71m0XCEYOVmkG7sVmC%2BEkj8%2BhMote%2FpypAYLNmNWx9Kd8Le23zAaqqTj70DD0GI6tK%2BN4rynMBeyeym3T1CxXAkMMZnJY%2BrvgmDWsxpd7NiVIkSd5s8AUEPEJshybPhRNWa1ZplPaiaRdeavB9f7EnmydBlm8BbkckE2Om8s%2FshjU0M8I2bM34TpvzbPMxI7VoOj53MgN4DD0%2BoDTBjqkARfIjSIHjsf%2Fu2R8yxfXys%2BP6iA%2BKI5953MzL4S42UBj41V%2B32IO00BtYWMaFR5ZnrytNwvM4hfmOM4BvpCIpvtrASsBqmtqsO0wckdAsiiyOi9RHALe7mk7%2Fjuk0PB2QeCvh0EzqaMTY5FNlT60ufcPlBqrPgnXBYCWBcqoYWnG8atGMMUFZ7QdcGeprPTuEU23NQAvQAszjg%2B%2BCFrI8nrv01Cm&X-Amz-Signature=0c36303565f54699d6c33c68cc38c60e3aca8fad0b09cb70d1bf570bc48eb12d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
