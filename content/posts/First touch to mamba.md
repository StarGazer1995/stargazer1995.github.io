---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664W3EGHJQ%2F20260614%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260614T021646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIEkCaUGvS8i8YfEb2GY6lgqFsU6Cqo4LrlffbVnFH7OvAiA%2BpFlkIe7YNDHafhcrj1Ctr9DTkYF%2BwmjpXfq%2BHt5Hnir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMnJKI44WAOCV%2Bd42EKtwDe2VF%2B6au%2FgxRyk62NbJjb3QHLJqDiMGXi3Du4wPfe3EAKaIVcYvLi4AzKbf3NV5rNJ8ahgWNbkSIwMcliSZzonBeiM6TYzZjGIAH1cLYYCwMmYiBhBD%2F2n5v6GRymSI0Q7UJxh5Y40Yo6ZTEvHVwkhCIOJe38%2FsPcUMEvALpD5kbkyo8odd%2FNaqkleLYS3KtzjIbpGgFiSTOFmCng%2BzVnECAN5EGwLzFAT24RjTd7RuFHXEHqUUYSDupWqYNaUWOlfM9IVsG44uOZG6ZBOcarSqRxpZERVYoaGROy6iCMzk%2FGwSoDCH8P9FlCL%2B01Pp0%2Fp%2Fm3W7XQWyDV8pNt5KkaRC%2FD1CyWY1oGijFpRMqKrKB6tiX38RFSBXcLfSj30h7jB9twMEN%2F30Wt3EOUSS%2FW15VO%2Fpsqf7shMeIl6zFmSneaqEkBvXsrlfbFwl95A7h6SnUMSl%2Fqtj%2Fv%2Bu1FBYSLh1x8GcGkKG5j6BWfHXkfqPvynDO8kdI0d0GPpWPVb1NE4XAsMQ8TBcrzFYFSxD4yaxWQfGSGkY7RkZ3xh7KxeX2T6xR08WTkJlhWJIQI6f7Ii11pwuQGm7dMa3k9tdIP4Ik%2F37oXHxrS4ZRDAhSeIwt6Jpy1JHyd%2FpuOLowidq30QY6pgHRncUl%2BfzcfmpDzF0MXXfDeaxDyET4VpHoRf1ehszgNIpm%2FwJ%2BC%2BvdVPosc4g8VOFjH6%2BBo%2BXde4g4RdVGCGOvDCnspQSGDJqS9zgXMxfd15QimYPO3jYxQK%2Fu%2Fhm0BOID7tQuixwQrVGtPFFHkRjve4d2iGcxEIuton%2Bt6EVVKgHsROJ23%2F6hDYX3iky4zLN20CZL5HkSTrd1LdtH1%2F%2BoUTVFnPO8&X-Amz-Signature=706b311ca776384a8b9222c1d30cdcac7c63ac7a18d33609ff725ed325d9a095&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
