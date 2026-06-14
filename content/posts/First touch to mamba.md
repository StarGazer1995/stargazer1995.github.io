---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VJTHDVR%2F20260614%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260614T225911Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDGjjyVRFp8FgQYbYmp0cOIt7PJiCIB904fFat26tHBwIhAMZGgZ0uNEM8ZDS80whXVggkuOxiNj%2Btlq0ZK2F5rOa4Kv8DCE0QABoMNjM3NDIzMTgzODA1Igw%2BYNS14RBO8MMIF0oq3AN9RNW11VmoFtCUmrbQCnlHy2rXUlRUHUNY%2FxHTu2iidkptoDrMcr%2Fhr58cBu3pSUaR89JxxmybOuUsj1vwbupz%2BQAEpRDNFfSpxjdUWZyflagHPalbDemKbvBussxvX4sCzz8jU%2F2Xze5EzvwN5D9C%2BYPHDAK5r331iLwahJTCPArUEbCQ9tpQliLVvj6JSwfYqpej7VpkU1vSAVlHtibidJ70e5K2vmK%2ByH2V%2BBgCKhEr9dpqnTqSiUyFS8ea%2B41pJnIxq%2FKaeMQwt6kaUuqkCDqibdrbAeFNWTgF5x9KL2OK%2FKiphBu04zvEpmizw7e%2FsF2x2D66RiPuLA95eFN4yKpvYSJnCsgRH1kQ0XBVsFHubztknDTto%2B3j0kZZPGI63ETAirXE1CURvLBUBtDYHh8Qmbte7BUxPFitd%2BFJ7n6TWaIPQxWPJlE5H7m%2BNRK37EoZ9mgubGFWDEageio0VPYxgNwoQ%2BGuH9Wys9Fh5%2B9i%2BTFGhc8js5mUsnHMarnW9JGFwtBAlLYji%2Bp5u1ER8csiVW%2FrGXem08056VJvtodr5Lxvfz1zGmu4waS%2BExZ4yF2f5ysG8GQZ1VL6CnqNcv0lDtJ9VYIiSRlIiBnvVpSvxi12hBaOCwfluzDHlrzRBjqkAZzOsmPVT3NGg1%2Bv0gqrqEBIhAHeMzZCphaqMITginc4fx16bVwV0xzOte6Q%2BUBsedzD%2FNwDMJUTdPpahgrcKmXVyHz20NYj0nJRrGjjfCl2yHm2NFUfUfl%2FTo1SMjNJzSZ6RU2o6elJn0sC7LVjpJ8sooGzlHsaN9wo30YT%2FT3kZMS9YgXpJ2QIlMpLsUQGmQ4%2FyQQYuCn%2B3xgxTsZrd8hD41zA&X-Amz-Signature=ba8e7bf739e13dff95f093766b91245aeda9e51dd93bae397becd470f660c5b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
