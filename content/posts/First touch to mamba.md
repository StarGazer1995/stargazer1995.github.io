---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWMFR5Z6%2F20260923%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260923T143101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF7z4QNFSflK54w4WVNWC3ZhAPS2w4uGtOFiqMu%2FfnJ9AiEArjnF8W7U3umFSFm6oB8EJxm7qzVA7oxuzY4eCytsOJcqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG422VKKyvLXVSx6circA0FFr5wODgfmZu91e%2Bu73A9f1Y15SLO4BKyxCKLHonA8%2F4OwRtDjVx3KWQ2WV3crYyVx1h5Pm9PkP0SQ4i3qlZYg3vn3WX8LezRo93cd2tzCuueupoIZa0oPc%2FqN5QIV%2Fi4axbqaM9TQx5NTNI9A0jsOiBrc27FhvyfcJPm0jKH16M72QIgNE32sk9oWoJmeIJdFv5QEjXPTtT9piISAGEI3Dr7XG%2Fwmc%2BYXe85iilM2QhWXm%2FBEPz8etRVKWHleB%2BQ4fgUqLH9YxmXvUGjI2iZK9wKy2K8OFxUww%2FBj9OG3fjS%2BT5SE1EbQ8KpGscfMRqb4KV6%2Br8I6pYGOs04eSaeO6HJ%2FEwLqMApNvhHYAhOZPmmiVN2%2FPV324WLPhIhc9w9WOAXw%2BL%2FLuyYzBUuJvRQA%2BgD%2BsKNpiulgXdNLvzt0cUZeOc84icYUtRFmkANh4nZKH%2Bb5gfQokPhpD79WCuuOhjI12sYm%2FlCYWqItSrxBJHfuVOPu1Ke7WvxsYqF4m9iiwPAbfQQmDjDh18k3%2BQpvLgptCpES1AxY5RGsjEgcMXPv5wpkZQvJWj2iYZPci3dcbiiMBKmNw7vqk0sqJsZPdC6DMaGTJBifD46NEXEyEbZnxtqjK8%2Fmr%2BinMOCEz9UGOqUBHW3o3lSEAii8dIjZcnk9BZiwoZt%2FP820AyNNWOP9obolt9glWkAbf1%2BhwuE1yPBD9dhlT%2FhHm2luowMLe21gRFtY54v1LBJnuOyrGp1F2xhNjcBdaQ4vddHMXsK2HJJ1X%2BhNf9NQSvAPy%2BpQY7Jm%2F4VHzW9cSzcfwuv6QL87QvSn26rl8DBiotHjI6%2B0WSKZkIaqma7rkGFsV0AVL3gsaz10%2FKzx&X-Amz-Signature=303bbb1ecfbc08fe0e9bb5144a4aab998008ad608c637a0259b231f51ead2335&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
