---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663ENL7PW%2F20260617%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260617T133644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2VZghCgcHlhYEXHplLtG5oJjaPfmTUiq8DW4Zrqf4hgIgFFd1H9fV%2FT18r7MuI0xxago0IUiQtKKcgJeAxTeVDroqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDClffc1x7OtG%2FFRSXSrcA27o5NV%2BBzvwLUW4Klrw86sZOPzveIQqXQeJ8M4kMpTocmc%2B9wwG%2F7udWwv1CR9DUa2pobd8OQnF9KHltMpINhSblN%2BYaFm2hfcyJRHx4xSNzVkvLLSfdICY8Ypy7cwnOZKycRf8Uh%2B3jEBi1CPcE9AmDZOVtDAIAtmwtmy8kJctOqARvPqtUtkZT33MuGUiAAPYJo8%2BeoVG7oG08DwOCZjsQxHCzzVDE9Uc1NMv6%2BCwZBXcOmBhwHL9WKw0u%2F6fR441uC27SEgj5Z18x3qzm0F6qQSluXtlL8eq4iJkHm1M0pRqRdTchsuEvtzi5JvkVqoPQr1ETnekGtttA4T9ZRHmS5hXgKpT34t7RxDBGTNn7AR1%2BwstK%2Ffur4Oz3WZLWCNbFZUAZeJpfMYPMzaFCJyZIWJjZjhcm3fUnCcPnUbsoDYXQlp0sSwx4viWYobC2rlWRTblCh%2Bj1B8MQYbqJ1aDmrwUHdRqsFffYCn9b0e68K0DmM5m4u3k6ityA5SSD7Ui%2BkWYNKSCoiZWqW37Bc4Rz2bGUKjFAYiwstarK1wbZ0pujtnPM81836TQv6NSBFjvIXZATctJEEQpqZNw4S17mcU7dzDVqS6lDfLBk%2B2F7G9oozjih%2BOT7mUcMO2sytEGOqUBwJaSjFurTeLbPjtmClvp2DvuK67Rr1C6G7gbj%2BzdqnuCkMYRlxTi%2FK1LcflrfLJ60qjtokZ%2Fviw7ueCscvqbP4z2b8ZhPSA3%2Fosze4BwW5ykWcLPqS8rsH8iYLThBP3ok32FXdCEO5eCcgghqHGvSx2rst8MLITEA1eBjN4MBHR7ZmXCITC%2Fr3tU%2Fc7Ib528wdqCZN2fi6REYdHrdweThbUVOBK6&X-Amz-Signature=db3d3664ad2c5bcbd7286dd872863f60c6af54ca698fad0555501dcf6982237e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
