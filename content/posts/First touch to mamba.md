---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLQP6XCY%2F20260911%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260911T064544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCQbXPs7SPiRETOpYpLaqbtwFLP7f8iFXBGwuHK91rClwIhAKg7jgfe4XLVLSEYhiErFpEMwQBZzsW1cf%2FbBgZA2vKPKogECJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzMMle2LZgNwCVE0sUq3AM%2Fjyk7SjLaMey7QT4B%2B%2Fx16fSaa73bcTy0sCblR31AhDYabAu2OQYV3F48MEPZRzkls4tw7mW5Q5btn9ZPmls8OpC3CYiZaggCW6Ec%2Bc4mX5gtWtEHt9KmwGYsIIj3RDM7TZaWY307OhVRpuqVByfAy%2BIC3B5FUhhirgE%2FQgZ1ku3duenPqDtlAVRuM9h0zeAfeOSJ%2BUBCwmXQC04bkndxAgmKXERQHZKqH%2F5dGazghNEDmEHTDiOuwT5C81OpWpHfAO69%2FG3xU%2FyetBxZNMc%2Fj0PnuL4OXUnIr7QjSjW%2FZvWw%2FLJWkvfI%2FghasLivv3r%2Fl4msk3W9ofqAA5Jk307QFtbegOhd1ltniFiKy2oX5f6%2FWRMX5BSkXGbYtKHtGFlT0b6ROa8xBI8%2BAu2zAWZTP%2Ffjap6j7upRrIoC%2BlyLlcJiJesgCFNJH%2FdBYkJ6awevWpXyE27o0I8C5%2F2uIakB%2F6Vn8ZzL765JSdRhmGLNby7Pb1oPhtea5%2F3cUE1LOPGfSl8ja2ePwJWbS7WKtvgzrztU2I53bX6Y7bR8%2FvxfXsoh7fLFsAQSmSeRjG9%2FJtsERvm2dBBm48PyIGnN9QHL9GnLHYRLQhaPApglcABaZkaqnTHtA6Ks7rO4dTC0mI7VBjqkASczE8HJi%2BjvObGyjUuyq46AYkid3W2fQhbEvMA8SJhevf%2B0E3q7s1Cw5OoJ3j74TnOAAx6rVhu2cFqtoCrFvr2AsxahEhi3YjwPZIymsG43GyDAfcR5W2DBdig4aykH8tk1fhUUWjvtbkzOloL47Nz3P4E1dNb5fumFSoKI1qfhhQhtdueI1StTnfOkDFjL7m%2BltHr%2FhCT2Z04Ag2kWQsP1vo5K&X-Amz-Signature=5414471f4a09032a32322954171bf47ea1f79b89c2b8f861a91679184d0440b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
