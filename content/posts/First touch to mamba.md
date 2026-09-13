---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626P3UNZL%2F20260913%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260913T125452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJFMEMCIG3WT972rDTxCaD1bg1PItqL2lI%2F3Ln0QgMHLKkHnQSsAh92HJOeuS9kCYTvBBSRHyE4%2BIvscqLL8Eq0DSLkFDNaKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy9hd%2BHTYLcwLzNEjMq3AMccBfl8Kb%2FHB07FmYf0yx7x1HmBrlhb%2B0f%2Fuyn4AdfW3Ps2xC1S9hEqvJQtsih8KxXYxWrXIxYpY9JFkRAETdhvNr%2Fx8uDSdnQnn119n7n7q71ApGMg6sqSmCniXhxvrll8phQgL1AeFHdtSkVFtHLDbGZvPOHtZFCfRyZp0bAhAhR1qJXuKE1fRpDIqQB3VYYA6Op17aNrmkKKHyNBy71vEikKPImdGQzq0YyJXeiKNoeO4WTLom%2F8YQglvLZ%2BH5GBwDlIytXk2S31urUL6YcIqxH%2BF8WmoAeIq0GldZ3ru7%2Bjz0faroBSvxKtgkAmNBlorzq3VKc8xM%2BnohvQzpTPK8jhMtsiHfurrNtF6iDbdcxuotWGW%2BjJuJqacqx45Dvy%2FlysvYO7VeAkeYABv13CXtSZex2pOmCyW5L0PZAGHfOwh1MCVmRBSu3Gf%2B%2F4XiNQDIpZVZv%2B16VVcHC%2BCkYUUIYlcGfmfB2qI%2BHrcnnYuxhbbNmWDIJDA4uHt%2FY2VfcWXisZ5KhWPKkTgB26QIiRK5l2zswPqILvtbgFcSt%2FnPL0ekdg865ZM47pm4jzlrvFLxdGz%2FIsJ7Os%2B7po%2BXCg3RBj2fFvF4EpB0a65FNM%2BrPBEUehlQ5v2fJtDDU9JnVBjqnAYwv%2B6zyLyTW%2B89HmoW8%2BJMc66R1ABpaRL0HiK01HEp81akTxw3U%2FYtWmVKWHlYnuWjIMPfgSBJUJHgXW2UsbYQCSBLDjieqDm8jXZby4kC6fbJkjcbpLq0QScPlV6e4Bo%2BrtBkd%2B6QLEj2Mndz3KTQygyj5JqFxxn5ehg98p9RVQC9%2Bjd0MQdIV1l7qxgXCuBgdc1BgMICwOA7ZP%2Fvm3Uk1X5sKBe9%2B&X-Amz-Signature=74de7fac772708bf431ab81aa671ba5efb3fbea572682beb3db16989eb4ff806&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
