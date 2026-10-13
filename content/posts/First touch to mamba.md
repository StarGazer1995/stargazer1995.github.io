---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QW4B7GST%2F20261013%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261013T083854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEYGwo4mjzLq5GJ4SitQ3Sa%2BPgFC1WnVRgYPS81cufjJAiB31H7EU7sZxw4nujvuei2S7F5Pp41M6NVYSqlJWH5AyCqIBAiZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8gxYfUenJUmZvpGmKtwD8uM5AJGc5e6mA5kRSJSm1qBkkka2dBPm0cnfPRsVEV2rIorAFyKsaFz0q92nWbucWl6b6iv1nz3yzyj4xBp2lrrMchh0iu%2Fb%2BtJZSdNDJaVoFMxiBXCDwB1FDHLwIgTF8Fnl6arVnaJ2qiM0kaMmoqQcMpr6FGlig6M%2F6b0HYVlxt7vlqTCvT8wGsHA94pjJFSX9QLILZkPQGfg0QQlh2QNd2laOGFX%2FUIF8eD8DMlOeeE6kFKbeLB7PPyF8SdIrUlavRdCgRJCd55xWd157g17SHfugSLwPM4n%2BQHT4cevX9Ym6bRLmnRoS19NjWTpuJP18KJb%2BAZ0ldEuOCLmULEJZeJDijrVBNQUmEgFwHe0dAYuReYJNPI2kSVmhcQT5AzUoNbFnJ7EruRNIUohAUURPYMvEvjmwH%2BrWPiPj1Ve5Xwur5pZRHQbnxzIe313OiOtUCc4C3tne0ASdSoeHPy5Xtm2NVY8m2vFC5XM8STP1AXrYd0DSj%2BnkzdUXLoWOzWbZdjX7sMHzozk7s415WwYNm3nwIt1WtPPRwmACE%2FDDBne604rc%2BcYa6IlU09MVUhC%2Bqa1MLsR%2Ftc0fHSE4ogYFvMTooIrN%2BJxE6nLGRQSonYPPd4Apr3P%2F0Rcw2ci31gY6pgGn0TW%2FXkH2Z4lMN701Q8Uu9qvcLEOEoFNWSY9IUpGjlf3eU7KMujeXJ1BA5mg21q93AYiO1PD%2BGtEbqQ3gf%2FfVV2sujQanshZQ3JBAslCkeyVqKWAuKxsVyWQfL24j%2BP0Ee92bQc5Rb6DkIr30aplAoAmUsFmNbeiE4ktWVlQR5y1P7jTVh%2F80PJSM9yn7ww9uoh72v6RhfqDOSe60damh9Jw9zxIo&X-Amz-Signature=77e00070a1c30bd4e6868071f72cd1cccf8b4faa1a7a5375d9f33d92f8eeecc9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
