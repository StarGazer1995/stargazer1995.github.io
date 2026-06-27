---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVR4JV7A%2F20260627%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260627T165459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyC2fJpedJaLrRIW0o0xh4SvAoXvFsJRTFXG06YSvl3gIhAL3T8u9dt6Y2DkrG0t%2FOcFzegzSP1se3pFjEMjxrMZkjKogECIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGbxjmTYoaDFhEPuwq3AMTmQ0fEL70smYVQhwlUo2lDzgDYeX6I9CQVu1wmgpw7wyNHJoPZc%2FWZo23q8r6su5sCSYxpiqEa4kXiZeAPj8D0Y0o2CVPacChCOZCoT5CQIND92NaksQArTQzvUdpzhW%2Bit7Q%2B8rCUFiHrc5jAQBjzVlfv5SN0RZvRukiwGffqcMCRr%2F057cHsdBL8NbV4HGbf9i9bcJBYqX8fdHufLtZR4hoejjOESIdbziayBJe5aY7v8vjZl7fSucqsewDtSnNn2idzLozfHYV90krrFYfPmp6jHJK5BTl1ybWnjZOp9WyjJCEwTPuvLR%2BvC3bcrBtjPPDDHmF5cpeLWJx1Ou%2BBAJh6zDNd94QM92%2FDc3cBGvQbFwiNLJe8HvTPKNqUrjGpjVotY0BPlg0tHImNE2jOFbBdBnyB8J%2FrWizpX9D1h0SgJW9qP%2Bk%2FBMd3WfNNF2%2BRZfCCXKlAmOSWHLyRcw4u5RUTiyz%2FwEcJbYh0xzxw4SZcxYQmH42Z1dN0L2kl62wW4F6OFFdfkpDdgbuyanFzAMBOwWG7xZvuYImgsO4EIoZa954fcGb7GX7Io5dbYQ52xuT5lUI6kAjraL4wrSx2l3T7NnnSFWKYGyLfwvCSh%2BgZdeZURkhuDPfrTCn8%2F%2FRBjqkASdXYCeyGcYltudvDIBSywurfdKMEaTPbaXRwsFHuryeBjcb3g2JcjZLBHbt%2FOzyLdf12Cep4F9i7TcBS3JKM9p2Avg7tfbALrOalKaWpi%2FSkHL%2FQ9E6HGWeRW7GWpt3U%2F1dG22mAL9pwhw7h0y%2FFFw9TMw%2F5Jm7MlAjygJHRB%2F3QnODQvPq62BQEzrQm4MIxRelzWxkZpPiR2e2FxtvcovBDFlr&X-Amz-Signature=91ab103cb972612777153da08b2da12c40d90ef261135126e37d6cb5c393487c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
